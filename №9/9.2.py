def bank(a, years):
    for _ in range(years):
        a = a+(a*0.22)
    return a

print(f"К оплате - {bank(1000, 1)} рублей")