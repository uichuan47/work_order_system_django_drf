import datetime
import random


def generate_order_number():
    current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    random_number = random.randint(1000, 9999)  # 生成一个四位随机数
    order_number = f'{current_time}{random_number}'
    return order_number
