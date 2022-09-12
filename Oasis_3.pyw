card_baze = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '1': 10, 'J': 11, 'Q': 12, 'K': 13,
                 'A': 14
             }

www = []
i = 0
r = 0
j = 0     # ценность комбинации оперативная.


def rrr():
    pass


def passy():
    print(f'ggg{r}')
oil = []
st = ['2', '2', '2', 'A', 'J', 'Q']

while i <= 4:
    oil = st[i] in card_baze
    if 0 <= i <= 4:
         # www.append(st[i])
        g = card_baze[st[i]]
        www.append(g)
        j += g
        r = j    # ценность комбинации глобальная.
        i += 1
    if i == 5:
        print(r)
    else:
        pass
else:
    print(www)
    print(3v)




