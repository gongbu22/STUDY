n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0]*11

for i in data:
    array[i] += 1 # 볼링공 갯수 카운트

result = 0
for i in range(1, m+1):
    n -= array[i] # 무게가 i인 볼링공의 개수 제외 ( A가 선택할 수 있는 개수 )
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기