# Chatbot AI Agent - Movie & Cinema Recommendation Demo

## Giới thiệu
Đây là dự án demo chatbot AI Agent được xây dựng trên nền tảng **n8n** nhằm hỗ trợ người dùng tra cứu thông tin phim hay trong tuần và gợi ý rạp chiếu phim phù hợp.

## Tính năng chính
- Chào hỏi và hướng dẫn sử dụng
- Tra cứu phim hay trong tuần
- Gợi ý rạp chiếu phim gần nhất
- Tích hợp Telegram

## Công nghệ sử dụng
- **n8n**: Nền tảng tự động hóa quy trình làm việc
- **Docker**: Containerization
- **Telegram Bot API**: Giao diện giao tiếp
- **TMDB API**: Dữ liệu phim (tuỳ chọn)

## Cấu trúc dự án
```
chatbot-demo/
├── n8n-workflows/          #  Workflow n8n
│   └── cinema-recommend-workflow.json
├── docker/                 # Docker compose files
│   ├── docker-compose.yml
│   ├── .env.example
│   └── .env
└── README.md              # File này

## Bắt đầu nhanh

### Yêu cầu hệ thống
- Docker & Docker Compose
- Telegram Bot Token 
- n8n (chạy trong Docker)

### Cài đặt

1. **Clone dự án và vào thư mục:**
```bash
cd chatbot-demo
```

2. **Cấu hình biến môi trường:**
```bash
cp docker/.env.example docker/.env
# Chỉnh sửa docker/.env với token của bạn
```

3. **Khởi động n8n với Docker Compose:**
```bash
cd docker
docker-compose up -d
```

4. **Truy cập n8n:**
- Mở trình duyệt: `http://localhost:5678`
- Tạo tài khoản và đăng nhập

5. **Import workflows:**
- Mở file workflow trong `n8n-workflows/`
- Import vào n8n
- Cấu hình Telegram

## Các kịch bản sử dụng

### Kịch bản 1: Chào hỏi
```
Người dùng: "Xin chào"
Bot: "Chào bạn! 👋 Tôi có thể giúp bạn:
1. Tìm phim hay trong tuần
2. Gợi ý rạp chiếu phim
3. Hỗ trợ khác..."
```

### Kịch bản 2: Tra cứu phim
```
Người dùng: "Gợi ý phim hay trong tuần"
Bot: "[Danh sách phim với tên, thể loại, mô tả ngắn]"
```

### Kịch bản 3: Gợi ý rạp
```
Người dùng: "Gợi ý rạp chiếu phim gần tôi"
Bot: "[Danh sách rạp với địa chỉ và thông tin]"
```

---
**Ngày tạo:** February 2026
**Phiên bản:** 1.0.0
