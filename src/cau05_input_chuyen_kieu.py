# Yêu cầu 17: Nhập 4 giá trị bằng input() và in type()
ma_may = input("Nhập mã máy: ")
print("Mã máy:", ma_may, "| Kiểu:", type(ma_may))

cong_suat_raw = input("Nhập công suất W: ")
print("Công suất (raw):", cong_suat_raw, "| Kiểu:", type(cong_suat_raw))

so_phut_raw = input("Nhập số phút: ")
print("Số phút (raw):", so_phut_raw, "| Kiểu:", type(so_phut_raw))

don_gia_raw = input("Nhập đơn giá: ")
print("Đơn giá (raw):", don_gia_raw, "| Kiểu:", type(don_gia_raw))

# Yêu cầu 18: Ép kiểu dữ liệu
cong_suat_w = float(cong_suat_raw)
so_phut = int(so_phut_raw)
don_gia_kwh = float(don_gia_raw)

# Yêu cầu 19: Tính lại điện năng và chi phí
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- Kết quả sau chuyển đổi kiểu ---")
print("Điện năng (kWh):", dien_nang_kwh)
print("Chi phí (VND):", chi_phi)