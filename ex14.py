class Student:
    def printInfor(self):
        print(f"Fullname: {self.name}")

st = Student()
st.name="Biện Văn Đại"
st.printInfor()

print("")

class Name:
    def __init__(self,name="",age=""):
        self.name = name
        self.age = age
    def getdata(self):
        print("Tên tôi là {} , {} tuổi" .format(self.name,self.age))

tt = Name()
tt.name = ("Đại")
tt.age = ("26")
tt.getdata()

print("")

class Cat:
    def __init__(self,name,year,add):
        self.name=name
        self.year=year
        self.add=add
    def old(self):
        return 2021 - self.year

cat = Cat("Đại",2001,"Hà Tĩnh")
print("Tên tôi là {}, năm nay {} tuổi, quê ở {}".format(cat.name,cat.old(),cat.add))
