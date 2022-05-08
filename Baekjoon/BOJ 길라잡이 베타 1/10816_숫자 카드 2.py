import collections
from sys import stdin

N = int(stdin.readline())
myCards = list(map(int, stdin.readline().split()))

M = int(stdin.readline())
target_cards = list(map(int, stdin.readline().split()))

cards_counter = collections.Counter(myCards)
for card in target_cards:
    print(cards_counter[card], end=" ")
