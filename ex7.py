tongtien = int(input("Số tiền đã có: "))
songuoidong = 0
while tongtien <= 100000 :
    dg = int(input("Hãy đóng thêm: "))
    tongtien +=dg
    songuoidong +=1
else:
    print("Ngân khố đã đủ!")    
print("Ngân khố sau khi đóng {} từ {} người!" .format(tongtien,songuoidong))