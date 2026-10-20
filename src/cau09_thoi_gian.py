from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

# Bổ sung theo yêu cầu bài 9
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

# Dự đoán kết quả phép trừ: 15:05 - 13:15 = 1 giờ 50 phút = 1:50:00[cite: 4]
thoi_luong = ket_thuc - bat_dau

print(thoi_luong)
print(type(thoi_luong))

"""
GIẢI THÍCH SỰ KHÁC NHAU:
1. datetime: Đại diện cho một mốc thời gian cụ thể (Bao gồm Ngày, Tháng, Năm, Giờ, Phút, Giây,...).
2. str: Dạng chuỗi ký tự thể hiện thông tin thời gian theo một định dạng cụ thể (dùng để in ra giao diện).
3. timedelta: Đại diện cho khoảng thời gian (khoảng lệch/hiệu số giữa hai mốc datetime).
"""