n = int(input("Введите кол-во символов "))
a = []
for i in range(n):
    a.append(input(""))
a_palindrom = a[::-1]
if a == a_palindrom:
    print("Является палиндромом")
else:
    print("не является палиндромом")
