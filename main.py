print("Hello Github")

def thong_ke_day_so():
    n = int(input("Nhập số lượng phần tử: "))
    
    # Tạo một list rỗng để lưu trữ các số
    danh_sach_so = []
    
    # 1. Dùng vòng lặp để nhập và thêm vào list
    for i in range(n):
        x = int(input(f"Nhập số thứ {i + 1}: "))
        danh_sach_so.append(x) # Lệnh .append() dùng để thêm phần tử vào cuối list
    
    # 2. Xử lý thống kê dựa trên list đã có
    tong_chan = 0
    dem_nguyen_to = 0
    
    for x in danh_sach_so:
        if x % 2 == 0:
            tong_chan += x
        if la_so_nguyen_to(x):
            dem_nguyen_to += 1
            
    # Kết quả
    print(f"\nDãy số bạn đã nhập là: {danh_sach_so}")
    print(f"Tổng các số chẵn: {tong_chan}")
    print(f"Số lượng số nguyên tố: {dem_nguyen_to}")

if __name__ == "__main__":
    thong_ke_day_so()