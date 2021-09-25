def hi2(dssv):
    for sv in dssv:
        print("Hello {}".format(sv))

dssv=["Linh","Vy","Khánh","Chi"]
hi2(dssv)

print("------------------------")

def hi1(name= "Nam"):
    print("Toi la: {}".format(name))

hi1()
hi1("Khanh Vy")

print("------------------------")

def thongtinsinhvien(**sinhvien):
    print("Họ tên: {}" .format(sinhvien["hoten"]))
    if 'diachi' in sinhvien.keys(): 
        print("Địa chỉ: {}" .format(sinhvien["diachi"]))
    if 'namsinh' in sinhvien.keys(): 
        tuoi = 2021 - sinhvien["namsinh"]
        print("Tuổi: {}" .format(tuoi))

thongtinsinhvien(hoten="Nhung",namsinh=2001)  
thongtinsinhvien(hoten="Linh",diachi="Hà Tĩnh")    
thongtinsinhvien(hoten="Đại",diachi="Hà Tĩnh",namsinh=2001)    


print("------------------------")

def hello(*name):
    print("Số lượng tham số: {}" .format(len(name)))
    for x in name: print(f"Xin chào: {x}")

hello()
hello("Hoa")
hello("Hoa","Huệ")

print("------------------------")


def hi(name,age):
    print("Tên tôi là {}, {} tuổi ".format(name,age))

hi("Đại",20)
hi(age=20,name="Đại")

