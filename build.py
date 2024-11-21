import os
import shutil
import PyInstaller.__main__
from datetime import datetime

def clean_dist():
    """Xóa thư mục dist và build cũ nếu tồn tại"""
    dirs_to_clean = ['dist', 'build']
    for dir_name in dirs_to_clean:
        if os.path.exists(dir_name):
            shutil.rmtree(dir_name)
            print(f"Đã xóa thư mục {dir_name}")
    
    # Xóa file spec nếu tồn tại
    spec_file = "PingMonitor.spec"
    if os.path.exists(spec_file):
        os.remove(spec_file)
        print(f"Đã xóa file {spec_file}")

def create_version_file():
    """Tạo file version.txt"""
    version = datetime.now().strftime("%Y.%m.%d")
    version_file = os.path.join(os.getcwd(), "version.txt")
    with open(version_file, "w") as f:
        f.write(version)
    return version

def copy_configs():
    """Copy thư mục config vào dist"""
    if not os.path.exists("dist/config"):
        os.makedirs("dist/config")
    
    config_files = [
        "config/config.json",
        "config/hosts.json"
    ]
    
    for file in config_files:
        if os.path.exists(file):
            shutil.copy2(file, "dist/config/")
            print(f"Đã copy {file} vào dist/config/")
        else:
            print(f"Không tìm thấy file {file}")

def build_exe():
    """Build file exe using PyInstaller"""
    version = create_version_file()
    
    # Đường dẫn tới các file nguồn
    main_file = os.path.join(os.getcwd(), 'src', 'ping_monitor.py')
    version_file = os.path.join(os.getcwd(), 'version.txt')
    
    PyInstaller.__main__.run([
        main_file,                            # File chính
        '--name=PingMonitor',                 # Tên file exe
        '--onefile',                          # Đóng gói thành 1 file
        '--console',                          # Hiển thị console để debug
        '--clean',                            # Xóa cache trước khi build
        '--distpath=dist',                    # Thư mục output
        '--workpath=build',                   # Thư mục build tạm
        f'--add-data={version_file};.',       # Thêm file version
        '--add-data=src/logger.py;.',         # Thêm các module phụ thuộc
        '--add-data=src/telegram_handler.py;.',
        '--hidden-import=requests',           # Thêm các module ẩn
        '--hidden-import=urllib3',
        '--hidden-import=chardet',
        '--hidden-import=certifi',
        '--hidden-import=idna',
        '--hidden-import=charset_normalizer'
    ])

def main():
    try:
        print("Bắt đầu quá trình build...")
        
        # Đảm bảo đang ở thư mục gốc của project
        project_root = os.path.dirname(os.path.abspath(__file__))
        os.chdir(project_root)
        
        # Xóa các thư mục cũ
        clean_dist()
        
        # Build file exe
        build_exe()
        
        # Copy config files
        copy_configs()
        
        print("\nBuild thành công!")
        print("File exe được tạo tại: dist/PingMonitor.exe")
        
    except Exception as e:
        print(f"\nLỗi trong quá trình build: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main())