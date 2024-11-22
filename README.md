# Ping Monitor

Ứng dụng giám sát ping và gửi thông báo qua Telegram.

![Banner](https://raw.githubusercontent.com/webdep24h/PingMonitorTool/main/images/Ping-monitor-telegram.png)


## 📂 Cấu trúc Project


```plaintext
ping_monitor/
├── src/                 # Mã nguồn chính
├── config/              # File cấu hình
├── assets/              # File icon
├── build.py             # Script build
└── requirements.txt     # Dependencies
```

## 🚀 Hướng dẫn sử dụng cài đặt triển khai
1. Clone repository

2. **Cài đặt môi trường Python**:
   - Cài Python >= 3.9.
   - Cài các thư viện cần thiết:
     ```bash
     pip install -r requirements.txt
     ```

3. **Cấu hình**:
   - Sửa file `config/config.json` và `config/hosts.json` theo nhu cầu.

4. **Chạy ứng dụng**:
   - Chạy trực tiếp:
     ```bash
     python src/ping_monitor.py
     ```
   - Hoặc build thành file thực thi:
     ```bash
     python build.py
     ```

## 📌 Ghi chú

- Đảm bảo các thư viện trong `requirements.txt` được cài đặt đầy đủ.
- Tùy chỉnh file cấu hình trong thư mục `config/`.

## Chi tiết triển khai cài đặt
https://blog.webdep24h.com/2024/11/ping-monitor.html



# [Hướng dẫn sử dụng phần mềm chi tiết dành cho người dùng]

---

### 🛠️ Tải xuống và chạy

Download tool tại: [PingMonitorTool](https://github.com/webdep24h/PingMonitorTool/raw/main/PingMonitor.rar)  ![Download](https://raw.githubusercontent.com/webdep24h/PingMonitorTool/main/images/Download.png)  

---

![Ping](https://raw.githubusercontent.com/webdep24h/PingMonitorTool/main/images/ping-monitor.png)


### 📂 Cấu trúc thư mục
```plaintext
PingMonitor/
├── config/
│   ├── config.json # Chứa thông tin bot telegram, cần thay thông tin bot của bạn để sử dụng
│   └── hosts.json  # Chứa tin IP/ Thiết bị (Sử dụng PM "Quản lý file Hosts" đi kèm để thay đổi, chỉnh sửa)
├── File Import mẫu/ # Chứa các file dữ liệu mẫu cần Inport
├── PingMonitor.exe # Ứng dụng giám sát ping
└── Quản lý file Hosts # Ứng dụng quản lý, thêm sửa, xóa file hosts.json ở trên
```

### 📋 Hướng dẫn sử dụng

1. **Cài đặt Telegram Bot**:
   - Thay thông tin bot của bạn vào file `config/config.json`.

   ![Sửa thông tin file Bot Telegram](https://raw.githubusercontent.com/webdep24h/PingMonitorTool/main/images/ping-bot-telegram.png)  


2. **Cấu hình danh sách thiết bị giám sát**:
   - Sửa file `config/hosts.json` hoặc sử dụng ứng dụng **Quản lý file Hosts** để thêm/sửa/xóa thiết bị.
 

![Quản lý file Hosts](https://raw.githubusercontent.com/webdep24h/PingMonitorTool/main/images/ping-monitor-1.png)


![Chọn file Hosts](https://raw.githubusercontent.com/webdep24h/PingMonitorTool/main/images/ping-monitor-2.png)


![Thêm/ Xóa dữ liệu file Hosts](https://raw.githubusercontent.com/webdep24h/PingMonitorTool/main/images/ping-monitor-3.png)


3. **Chạy ứng dụng**:
   - Chạy file `PingMonitor.exe`.

4. **Xem kết quả**:
   - Kết quả được lưu trong file log hoặc gửi cảnh báo qua Telegram.


### 📌 Ghi chú

- **`config.json`**: Bạn cần thêm thông tin **Bot Token** và **Chat ID** của Telegram Bot.
- **`hosts.json`**: Chứa danh sách các thiết bị theo dõi. Định dạng mẫu:
  ```json
  [
    {"host": "192.168.1.1", "name": "Router"},
    {"host": "google.com", "name": "Google"}
  ]


