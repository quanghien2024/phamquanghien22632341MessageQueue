import pika
import json

# Kết nối với RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Đảm bảo tạo ra hàng đợi
channel.queue_declare(queue='event_queue')

# Nội dung sự kiện (chi tiết hơn, tiếng Việt)
message = {
    "service": "Service 1",
    "loai_su_kien": "Tao_don_hang",
    "ma_don_hang": "DH001",
    "khach_hang": "Nguyễn Văn A",
    "tong_tien": 1500000,
    "noi_dung": "Khách hàng đã tạo đơn hàng mới trên hệ thống",
    "thoi_gian": "2026-01-12 19:30"
}

# Chuyển dict sang JSON string
channel.basic_publish(
    exchange='',
    routing_key='event_queue',
    body=json.dumps(message, ensure_ascii=False)
)

print("Service 1: Đã gửi sự kiện:")
print(message)

connection.close()
