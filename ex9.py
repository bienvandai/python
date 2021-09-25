
while (True):
    print("0.Thoát khỏi chương trình")
    print("1.Nhập thông tin sinh viên")
    print("2.Sắp xếp thông tin sinh viên theo điểm")
    print("3.Tìm kiếm sinh viên")
    print("4.Hiển thị bảng điểm sinh viên")
    
    a = int(input("Lựa chọn của bạn: "))
    if a == 1:
        print("Nhập thông tin sinh viên")
    elif a == 2:
        print("Sắp xếp thông tin sinh viên theo điểm")
    elif a == 3:
        print("Tìm kiếm sinh viên")
    elif a == 4:
        print("Hiển thị bảng điểm sinh viên")
    elif a == 0:
        print("end.") 
    break