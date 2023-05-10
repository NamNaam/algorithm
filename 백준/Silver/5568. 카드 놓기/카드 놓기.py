from itertools import permutations

n = int(input())
k = int(input())
card = []
num = set()

for _ in range(n):
    card.append(input())

for per in permutations(card, k):
    num.add(''.join(per))

print(len(num))