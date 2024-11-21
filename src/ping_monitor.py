import os
import json
import time
import platform
import subprocess
import socket
from datetime import datetime
from logger import Logger
from telegram_handler import TelegramHandler
from colorama import init, Fore, Style

# Initialize colorama for Windows
init()

class PingMonitor:
    def __init__(self):
        self.load_config()
        self.logger = Logger(self.config['log']['file'])
        self.telegram = TelegramHandler(
            self.config['telegram']['bot_token'],
            self.config['telegram']['chat_id']
        )
        self.hosts_status = {}

    def load_config(self):
        with open('config/config.json', 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        with open('config/hosts.json', 'r', encoding='utf-8') as f:
            self.hosts_data = json.load(f)
            self.hosts = self.hosts_data['hosts']
            self.groups = self.hosts_data['groups']

    def resolve_domain(self, domain):
        try:
            return socket.gethostbyname(domain)
        except socket.gaierror:
            return None

    def ping(self, host):
        ip = host['ip']
        
        # Nếu là domain, resolve IP trước
        if host['type'] == 'DOMAIN':
            resolved_ip = self.resolve_domain(ip)
            if not resolved_ip:
                return False
            ip = resolved_ip

        ping_count = '-n' if platform.system().lower() == 'windows' else '-c'
        ping_timeout = '-w' if platform.system().lower() == 'windows' else '-W'
        
        try:
            cmd = ['ping', ping_count, '1', ping_timeout, '1000', ip]
            result = subprocess.run(cmd, 
                                 stdout=subprocess.PIPE, 
                                 stderr=subprocess.PIPE,
                                 text=True)
            return result.returncode == 0
        except Exception as e:
            self.logger.error(f"Error pinging {ip}: {str(e)}")
            return False

    def get_status_color(self, status):
        return {
            'UP': Fore.GREEN,
            'DOWN': Fore.RED,
            'UNKNOWN': Fore.YELLOW
        }.get(status, Fore.WHITE)

    def check_host(self, host):
        current_status = "UP" if self.ping(host) else "DOWN"
        previous_status = self.hosts_status.get(host['ip'], "UNKNOWN")

        if current_status != previous_status:
            self.hosts_status[host['ip']] = current_status
            self.logger.info(
                f"Status change - Host: {host['name']} ({host['ip']}) "
                f"Type: {host['type']} Status: {current_status}"
            )
            
            # Chỉ gửi thông báo trong 2 trường hợp:
            # 1. Khi trạng thái chuyển sang DOWN
            # 2. Khi trạng thái từ DOWN chuyển sang UP
            if current_status == "DOWN" or (current_status == "UP" and previous_status == "DOWN"):
                self.telegram.send_alert(host, current_status, previous_status)

        return current_status

    def print_status_header(self):
        print("\n" + "="*80)
        print(f"{'Name':<20} {'IP':<20} {'Type':<10} {'Status':<10} {'Description'}")
        print("="*80)

    def monitor(self):
        self.logger.info("Starting ping monitor...")
        
        try:
            while True:
                self.print_status_header()
                
                for host in self.hosts:
                    status = self.check_host(host)
                    color = self.get_status_color(status)
                    
                    print(
                        f"{host['name']:<20} "
                        f"{host['ip']:<20} "
                        f"{host['type']:<10} "
                        f"{color}{status:<10}{Style.RESET_ALL} "
                        f"{host['description']}"
                    )
                
                print(f"\nLast update: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                time.sleep(self.config['ping']['interval'])
                
                # Clear screen for better visibility
                os.system('cls' if platform.system().lower() == 'windows' else 'clear')
        
        except KeyboardInterrupt:
            self.logger.info("Stopping ping monitor...")
        except Exception as e:
            self.logger.error(f"Error in monitor loop: {str(e)}")
            raise

def main():
    monitor = PingMonitor()
    monitor.monitor()

if __name__ == "__main__":
    main()