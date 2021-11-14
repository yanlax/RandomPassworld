import random
import string

numberPassword = int(input(" Number of passwords: "))

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,._-"

all = upper + numbers + symbols

for x in range(numberPassword):
    Password = ''.join([random.choice(list('qwertyuiopasdfghjklzxcvbnm')) for x in range(10)])
    Passworda = ''.join([random.choice(list(all)) for x in range(10)])
    Pass = Password + Passworda
    PassOut = string.capwords(Pass)
    print(PassOut)
