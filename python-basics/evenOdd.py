
number = -1

while(int(number) < 1 or int(number) >= 10):
    number = input("Insert A NUMBER FROM ONE TO TEN: ")

if (int(number) % 2 == 0):
    print("Number is even")
else:
    print("This number is odd")
