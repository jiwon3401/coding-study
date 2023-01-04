#5597

input_num = []
for _ in range(1,29):
    num = int(input())
    input_num.append(num)
    
not_in = [i for i in range(1,31) if i not in input_num]
print(sorted(not_in)[0], sorted(not_in)[1], sep="\n") 




# remove 사용

std_num = [i for i in range(1,31)]
for _ in range(28):
    num = int(input())
    std_num.remove(num)
    
print(min(std_num), max(std_num))
#print(sorted(std_num)[0], std_num[1], sep="\n")