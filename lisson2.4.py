def month_to_season(num):
    if num == 12 and num >= 1 and num < 3:
        print("Зима")
    if num >= 3 and num <= 5:
        print("Весна")
    if num >= 3 and num <= 5:
            print("Лето")
    if num >= 9 and num <= 11:
        print("Осень")

try:
    num = int(input("Введите число месяца: "))
except ValueError: 
    print("Это не число.")
month_to_season(num)
