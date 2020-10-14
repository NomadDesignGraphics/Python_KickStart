def ucgen(a,b,hipotenus):
    if a**2 + b**2 == hipotenus**2:
        return "Üçgen bulundu"
    else:
        return "Üçgen bozuk, üçgen sayılmaz"

print(ucgen(3,4,5)) # print etmeden yazrsan kod çalışmaz

print(ucgen(1,2,5))