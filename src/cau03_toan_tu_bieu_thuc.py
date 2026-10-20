tong_phut = 135
cong_suat_w = 250

# Yêu cầu 9: Tính số giờ trọn vẹn và số phút còn lại
so_gio = tong_phut // 60
phut_con_lai = tong_phut % 60
print(f"Thời gian: {so_gio} giờ và {phut_con_lai} phút")

# Yêu cầu 10: Biến su_dung_lau (True nếu tong_phut > 60)
su_dung_lau = tong_phut > 60
print("Sử dụng lâu (>60p):", su_dung_lau)

# Yêu cầu 11: Biến du_lieu_hop_le (True nếu cong_suat_w > 0 và tong_phut > 0)
du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

# Yêu cầu 12: Dự đoán và kiểm chứng hai biểu thức
# Dự đoán:
# 100 + 20 * 3 = 100 + 60 = 160 (do phép nhân * có độ ưu tiên cao hơn phép cộng +)
# (100 + 20) * 3 = 120 * 3 = 360 (do dấu ngoặc () có độ ưu tiên cao nhất)
expr1 = 100 + 20 * 3
expr2 = (100 + 20) * 3
print("Kết quả 100 + 20 * 3:", expr1)
print("Kết quả (100 + 20) * 3:", expr2)