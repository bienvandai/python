for x in range(5):
    print(x)
    if x == 2:break
else:
    print("Vong lap ket thuc tai x = {}" .format(x))

danhsachsinhvien = ["Nam","Linh","Na","Thuận"]

for sinhvien in danhsachsinhvien:
    print(sinhvien)


for char in danhsachsinhvien[1]:
    print(char)


tong = 0
for i in range(11):
    tong += i
print(f"Tổng từ 1 -> 10 là: {tong}")