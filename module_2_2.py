number_str = int(input("Введите число: "))
number_str = str(number_str)
if len(number_str) == 3:
    if number_str[0] == number_str[1] == number_str[2]:
        print(3)
    elif number_str[0] == number_str[1] or number_str[1] == number_str[2] or number_str[0] == number_str[2]:
        print(2)
    else:
        print(0)
else:
    print("Введите 3 цифры")



