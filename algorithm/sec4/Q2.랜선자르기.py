#[#Q2. 랜선자르기(결정알고리즘)]
#결정알고리즘에서 이분탐색이 사용됨
'''
엘리트 학원은 자체적으로 K개의 랜선을 가지고 있다. 그러나 K개의 랜선은 길이가 제각각이다. 
선생님은 랜선을 모두 N개의 같은 길이의 랜선으로 만들고 싶었기 때문에 K개의 랜선을 잘라서 만들어야 한다. 
예를 들어 300cm 짜리 랜선에서 140cm 짜리 랜선을 두 개 잘라내면 20cm 은 버려야 한다. (이미 자른 랜선은 붙일 수 없다.)
편의를 위해 랜선을 자를때 손실되는 길이는 없다고 가정하며, 기존의 K개의 랜선으로 N개의 랜선을 만들 수 없는 경우는 없다고 가정하자. 
그리고 자를 때는 항상 센티미터 단위로 정수 길이만큼 자른다고 가정하자. N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. 
이때 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline 
K, N = map(int, input().split())
line = []
for i in range(K):
    li = input()
    line.append(int(li))
    
first = 0
end = max(line)
while first<=end:
    mid = (first+end)//2
    cnt= 0
    for i in range(K):
        cnt += line[i]//mid        
    if cnt>=N:
        first = mid+1
    else:
        end = mid-1
print(end)