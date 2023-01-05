# 10818번 최소, 최대

N = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))


# 2562번 최댓값

input_num = []
for i in range(1,10):
    nums = int(input())
    input_num.append(nums)
print(max(input_num))
print(input_num.index(max(input_num))+1)

