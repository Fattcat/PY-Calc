import os
from time import sleep

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
#orange = '\033[033m'
orange = '\033[38;5;208m'
reset = '\033[0m'

def spinkaj():
    sleep(2)

def plus(x, y):
    return x + y

def mnus(x, y):
    return x - y

def krat(x, y):
    return x * y

def deleno(x, y):
    return x / y

def nadruhu(x, y):
    return x ** y

while True:
    os.system("cls")
    print(" ")
    a = float(input(f"Napíšte {green}prve{reset} číslo : "))
    print(" ")
    b = float(input(f"Napíšte {orange}druhe{reset} číslo : "))

    print(" ")
    print(f"Pre {green}PLUS{reset}", ":\n",a, "+", b, "=", plus(a, b),"\n")
    print(f"Pre {green}MINUS{reset}", ":\n",a, "-", b, "=", mnus(a, b),"\n")
    print(f"Pre {green}DELENO{reset}", ":\n",a, ":", b, "=", krat(a, b),"\n")
    print(f"Pre {green}KRAT{reset}", ":\n",a, "*", b, "=", deleno(a, b),"\n")
    print(f"Pre {green}Na Druhu{reset}", ":\n",a, "**", b, "=", nadruhu(a, b),"\n")
    print(f"Chcete spustiť tento script ZNOVU ?")
    c = input("Napíšte Ano / Nie : ")
    if c =="Áno" or c=="Ano" or c=="ano" or c=="a" or c=="A":
        continue
    elif c =="Nie" or c=="nie" or c=="n" or c=="N":
        print("Ukončujem ...")
        spinkaj()
        print("\nDOVIDENIA :D")
        break
    else:
        break
