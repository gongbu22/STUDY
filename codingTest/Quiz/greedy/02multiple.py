data = input()

result = int(data[0]) # 숫자로 바꿔주기

for i in range(1, len(data)):
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)