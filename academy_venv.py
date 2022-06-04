import random

imiona = ['pki', 'pKO', 'pw', 'go', 'gr', 'w', 'ch', 'k', 'mat', 't', 'l', 'Mar', 'b']
print(random.choice(imiona))

import random

guess_num = random.randint(1, 51)
# print(guess_num)
still_playing = True
counter = 0
print('zgadnij liczbe z zakresu 1- 50')

while still_playing:
    if temp ==-1:
        break
    temp = int(input('podaj liczbe\n'))
    counter += 1
    if temp == guess_num:
        print(f"wygrales w {counter} probach")
        break
    if temp > guess_num:
        print('za duzo')
        continue
    else:
        print('za malo')
        continue
print('koniec programu')