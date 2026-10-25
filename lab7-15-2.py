n = int(input("Введите кол-во символов "))
nums = []
for i in range(n):
    nums.append(int(input("")))
k = int(input("k= "))
max_len = 0
for i in range(len(nums)):
    summa = 0
    for j in range(i, len(nums)):
        summa += nums[i]
        if summa == k:
            dlina = j-i+1
            if dlina > max_len:
                max_len = dlina
print(max_len)
