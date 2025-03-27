import random
g=random.randint(1,11)
n=-1
count=0

while (n != g) :
    count+=1
    n=int(input("enter the guessed number : "))
    if (n<g) :
        print("greater number please")
    
        
    else :
        print("smaller number please")
9

print(f"wow you have guessed the correct number {g} in {count} attempts")