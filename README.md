# Ping Monitor

Ứng dụng giám sát ping và gửi thông báo qua Telegram.

## Cấu trúc Project
ping_monitor/
├── src/ # Mã nguồn chính
├── config/ # File cấu hình
├── assets/ # File icon
├── build.py # Script build
└── requirements.txt # Dependencies

## Cài đặt dành cho nhà phát triển

1. Clone repository
2. Cài đặt dependencies: `pip install -r requirements.txt`
3. Cấu hình trong config/
4. Chạy build.py để tạo file exe

## Chi tiết triển khai cài đặt
https://blog.webdep24h.com/2024/11/ping-monitor.html

## [Hướng dẫn sử dụng phần mềm chi tiết dành cho người dùng]
Tiến hành tải về giải nén thư mục là chạy được
Cấu trúc thư mục
PingMonitor/
├── src/ # Mã nguồn chính
├── config/
│   ├── config.json # Chứa thông tin bot telegram, cần thay thôn tin bot của bạn để sử dụng
│   └── hosts.json  # Chứa tin IP/ Thiết bị (Sử dụng PM Quản lý file Hosts đi kèm để thay đổi, chỉnh sửa)
├── File Import mẫu/ # Chứa các file dữ liệu mẫu cần Inport
├── PingMonitor.exe # Ứng dụng giám sát ping
└── Quản lý file Hosts # Ứng dụng quản lý, thêm sửa, xóa file hosts.json ở trên

