# Yêu cầu 5 & 6: Tạo các biến theo snake_case và gán kiểu dữ liệu phù hợp
ma_phien = "LAB026"         # str
ma_may = "PC12"             # str
cong_suat_w = 250.0        # float
thoi_gian_phut = 90         # int
trang_thai_hoat_dong = True # bool
ghi_chu = None              # NoneType

# Yêu cầu 7: In từng giá trị và dùng type() kiểm tra kiểu
print("Mã phiên:", ma_phien, "| Kiểu:", type(ma_phien))
print("Mã máy:", ma_may, "| Kiểu:", type(ma_may))
print("Công suất (W):", cong_suat_w, "| Kiểu:", type(cong_suat_w))
print("Thời gian (phút):", thoi_gian_phut, "| Kiểu:", type(thoi_gian_phut))
print("Trạng thái hoạt động:", trang_thai_hoat_dong, "| Kiểu:", type(trang_thai_hoat_dong))
print("Ghi chú:", ghi_chu, "| Kiểu:", type(ghi_chu))

# Yêu cầu 8: Thay thời gian sử dụng từ 90 thành 120 bằng phép gán lại và in giá trị mới
thoi_gian_phut = 120
print("Thời gian sử dụng mới (phút):", thoi_gian_phut)