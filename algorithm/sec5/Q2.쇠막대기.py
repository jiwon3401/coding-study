'''
여러 개의 쇠막대기를 레이저로 절단하려고 한다. 효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다. 
쇠막대기와 레이저의 배치는 다음 조건을 만족한다.
• 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다. - 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
• 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
• 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.
쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하시오.
'''
aa = list(input())
stack = []
cnt = 0
for i in range(len(aa)):
    if aa[i] == '(':
        stack.append(aa[i])
    else: #')'
        #stack.pop() #위에다 한번에 해도 됨.
        if aa[i-1] == '(': # () :레이저 -> 남아있는 막대기 개수 '(' count
            stack.pop()
            cnt+=len(stack)
        elif aa[i-1] ==')': # )) :막대기 끝지점
            stack.pop()
            print(stack)
            cnt+= 1
print(cnt)