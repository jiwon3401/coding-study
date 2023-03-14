'''
세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.
'''
import sys 
input = sys.stdin.readline

aa = input().rstrip()
aa_list = []
for i in aa.split('-'):
    tmp = 0
    for j in i.split('+'):
        #print(j)
        tmp += int(j)
    aa_list.append(tmp)

for i in range(1,len(aa_list)):
    aa_list[0] -= aa_list[i]
    
print(aa_list[0])
