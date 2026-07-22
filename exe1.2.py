tong_giay = 42 * 60 + 42
print("1. Tổng số giây:", tong_giay)

tong_dam = 10 / 1.61
print("2. Tổng số dặm:", tong_dam)

tong_phut = tong_giay / 60
pace_thap_phan = tong_phut / tong_dam

so_phut = int(pace_thap_phan)
so_giay = int((pace_thap_phan - so_phut) * 60)

print(f"3a. Pace trung bình: {so_phut} phút {so_giay} giây / dặm")

tong_gio = tong_giay / 3600
toc_do = tong_dam / tong_gio

print(f"3b. Tốc độ trung bình: {toc_do:.2f} dặm/giờ")