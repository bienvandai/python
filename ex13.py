x= lambda a: a+10
y = lambda a,b: a + b

print(x(100))
print(y(10,20))

print("------------------------")

def ham_mu(n):
    x = lambda x: x ** n
    return x

kq = ham_mu(2)
print(kq(3))