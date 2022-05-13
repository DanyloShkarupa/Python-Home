import random
user_number = int(input("Вкажіть число: "))
random_number = random.randint(1, 10)

if user_number == random_number:
    print("Ви вгадали число. Вітаю!")
else:
    print("Не пощастило. Спробуйте ще!")