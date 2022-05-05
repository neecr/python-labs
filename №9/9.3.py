def date(day, mouth, year):
    mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day < 0 or mouth < 0 or year < 0:
        return False
    if year % 400 == 0 or ((year % 4 == 0) and (year % 100 != 0)):
        mon[1] = 29
    if 1 <= mouth <= 12 and 0 < day <= mon[mouth - 1]:
            return True
    return False


print(f'Дата 29.02.2020 - {date(29, 2, 2020)}')
print(f'Дата 32.02.2020 - {date(32, 2, 2020)}')
print(f'Дата 29.31.2020 - {date(29, 31, 2020)}')
print()