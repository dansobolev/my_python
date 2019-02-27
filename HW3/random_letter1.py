import random
s = ['самовар', 'весна', 'лето']
a = random.choice(s)# random word
sy = random.choice(a)# random symbol
pos = a.index(sy)# index
w = list(str(a))
w[pos] = '?'
print("".join(w))

guess = input("Введите букву: ")

if sy == guess:
    print("Победа!", "\nСлово: ", ''.join(a))
else:
    print("Увы! Попробуйте снова.", "\nСлово: ", ''.join(a))