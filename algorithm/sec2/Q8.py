#[#8. 뒤집은 소수]
'''
N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 
예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 그러면 23을 출력한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 
첫 자리부터의 연속된 0은 무시한다.
뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하여 프로그래밍 한다.
'''

import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

def reverse(x):
    reversed_num = []
    for i in nums:
        rev = str(i)[::-1]
        reversed_num.append(int(rev))
    return reversed_num
    

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1): #절반까지만 돌기
        if x%i == 0:
            return False
    else: #return 당하지 않고 정상적으로 될때
        return True
 
reverse_num = reverse(nums)
 
for i in reverse_num:
    if isPrime(i):
        print(i, end=' ')   
  