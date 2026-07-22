import time

current_time = time.time()

seconds_in_a_day = 24 * 60 * 60
seconds_in_an_hour = 60 * 60
seconds_in_a_minute = 60

days = int(current_time // seconds_in_a_day)

remaining_seconds = current_time % seconds_in_a_day

hours = int(remaining_seconds // seconds_in_an_hour)
remaining_seconds %= seconds_in_an_hour

minutes = int(remaining_seconds // seconds_in_a_minute)
seconds = int(remaining_seconds % seconds_in_a_minute)

print("Số ngày kể từ epoch:", days)
print(f"Giờ hiện tại (GMT): {hours:02d}:{minutes:02d}:{seconds:02d}")