i, f = map(int, input().split())
t = 0
if i < f:
    t = f - i
else:
    t = (24 - i) + f

print(F"O JOGO DUROU {t} HORA(S)")