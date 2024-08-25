def is_year_leap(y):
    return f'год {y} высокостный?: {y %4 == 0}'
print (is_year_leap (2024))
print (is_year_leap (2023))
print (is_year_leap (2022))