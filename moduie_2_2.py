first = int(input("Ввидите число: "))
second = int(input("Ввидите число: "))
third = int(input("Ввидите число: "))
if first == second == third:
    print(3)
elif (first == second) or (first == third) or (second == third):
    print(2)
else:
    print(0)