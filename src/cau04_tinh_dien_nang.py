# Yêu cầu 15: Dự đoán kết quả với so_phut = 90
# dien_nang_kwh = 250 * 90 / 60 / 1000 = 22500 / 60 / 1000 = 375 / 1000 = 0.375 kWh
# chi_phi = 0.375 * 3000 = 1125.0 VND

cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# Yêu cầu 13: Tính điện năng và chi phí
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

# Yêu cầu 14: In giá trị và kiểu dữ liệu
print("--- Lần 1 (so_phut = 90) ---")
print("Điện năng (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "| Kiểu:", type(chi_phi))

# Yêu cầu 16: Thay so_phut bằng 60 rồi chạy lại
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- Lần 2 (so_phut = 60) ---")
print("Điện năng (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "| Kiểu:", type(chi_phi))