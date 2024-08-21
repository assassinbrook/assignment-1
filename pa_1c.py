#determine whether a number is divisible by both 3 and 5

a=int(input("enter a number: "))
if (a%3)==0 and (a%5)==0:
        print("the number is divisbile by both 3 and 5")
else:
    print("the number is not divisible by both 3 and 5")