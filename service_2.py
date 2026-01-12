import pika
import json

def callback(ch, method, properties, body):
    # Chuyển JSON string về dict
    message = json.loads(body.decode('utf-8'))

    print("Service 2: Đã nhận sự kiện")
    print(f"  - Dịch vụ gửi: {message['service']}")
    print(f"  - Loại sự kiện: {message['loai_su_kien']}")
    print(f"  - Mã đơn hàng: {message['ma_don_hang']}")
    print(f"  - Khách hàng: {message['khach_hang']}")
    print(f"  - Tổng tiền: {message['tong_tien']} VND")
    print(f"  - Nội dung: {message['noi_dung']}")
    print(f"  - Thời gian: {message['thoi_gian']}")

    print("Service 2: Xử lý sự kiện xong.\n")

# Kết nối đến RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Đảm bảo hàng đợi tồn tại
channel.queue_declare(queue='event_queue')

# Lắng nghe sự kiện
channel.basic_consume(
    queue='event_queue',
    on_message_callback=callback,
    auto_ack=True
)

print("Service 2: Đang chờ sự kiện... (CTRL+C để thoát)")
channel.start_consuming()
