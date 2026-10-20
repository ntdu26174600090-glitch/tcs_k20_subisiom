# Đoạn mã đã được sửa hoàn chỉnh:
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: ")) # Sửa Lỗi 1: Ép kiểu float() cho input
so_phut = int(input("Nhập số phút: "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh") # Sửa Lỗi 2 & 3: Đổi dien_nang thành dien_nang_kwh và thêm dấu ')' đóng ngoặc

# --- MÔ TẢ CÁC LỖI ĐÃ PHÁT HIỆN ---
# 1. File "src/cau07_chan_doan_loi.py", line 4, TypeError: can't multiply sequence by non-int of type 'float'
#    Nguyên nhân: cong_suat_w nhận giá trị kiểu str từ input() nên không thực hiện được phép nhân số học.
# 2. File "src/cau07_chan_doan_loi.py", line 7, NameError: name 'dien_nang' is not defined
#    Nguyên nhân: Gọi sai tên biến (đúng phải là dien_nang_kwh).
# 3. File "src/cau07_chan_doan_loi.py", line 7, SyntaxError: unexpected EOF while parsing / '(' was never closed
#    Nguyên nhân: Cú pháp thiếu dấu ngoặc đóng ')' cho hàm print().