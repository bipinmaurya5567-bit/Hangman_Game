import random
print("welcome to pypassword generator! ")
word=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'''
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
number=['1','2','3','4','5','6','7','8','9','0']
symbol=['!','@','#','$','%','^','&','*','+','-','(',')']
print("Welcome to pypassword generator! ")
letter=int(input("How many number of words to generate? \n"))
nr_number=int(input("How many number of number to generate? \n"))
nr_symbol=int(input("How many number of symbol to generate? \n"))


password=[]
for i in range(1,letter+1):
    password+=random.choice(word)
for i in range(1,nr_number+1):
    password+=random.choice(number)
for i in range(1,nr_symbol+1):
    password+=random.choice(symbol)
random.shuffle(password)

password1=""
for i in password:
    password1+=i
print(f"Your random password is generated:  {password1}")