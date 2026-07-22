import math

r = 5
volume = (4 / 3) * math.pi * (r ** 3)
print(f"1. Thể tích hình cầu (r=5): {volume:.2f}")

cover_price = 24.95
discount_rate = 0.40
discounted_price = cover_price * (1 - discount_rate)

num_books = 60

shipping_cost = 3 + (num_books - 1) * 0.75

total_cost = (discounted_price * num_books) + shipping_cost
print(f"2. Tổng chi phí mua 60 cuốn sách: ${total_cost:.2f}")

start_seconds = (6 * 3600) + (52 * 60)

easy_pace_sec = (8 * 60) + 15
tempo_pace_sec = (7 * 60) + 12

total_run_seconds = (2 * easy_pace_sec) + (3 * tempo_pace_sec)

finish_seconds = start_seconds + total_run_seconds

finish_hour = finish_seconds // 3600
finish_minute = (finish_seconds % 3600) // 60
finish_second = finish_seconds % 60

print(f"3. Thời gian về đến nhà: {finish_hour:02d}:{finish_minute:02d}:{finish_second:02d} AM")