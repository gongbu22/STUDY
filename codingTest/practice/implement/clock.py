#  시각문제

# h 입력 받기
h = int(input())

count = 0
for i in range(h + 1):  # 시간
    for j in range(60):  # 분
        for k in range(60):  # 초
            # 매 시각 안에 3이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)