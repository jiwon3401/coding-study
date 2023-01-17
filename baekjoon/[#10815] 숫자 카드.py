
N= int(input())
card = list(map(int, input().split()))
M = int(input())
number = list(map(int, input().split()))

card_dict = {}
for i in range(len(card)):
    card_dict[card[i]] = 0

for i in range(M):
    if number[i] not in card_dict:
        print(0, end=' ')
    else:
        print(1, end=' ')
