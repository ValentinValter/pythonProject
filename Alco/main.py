def alco(a):
    if a < 10:
        return ('Иди в магазин')
    elif 12 >= a >= 10:
        return('Твоя норма')
    elif a <= 15:
        return('Ты бухой')
    else:
        return('Ты в гавно')


print(f'0 бутылок', alco(0))
print(f'-2 бутылки', alco(-2))
print(f'5 бутылок', alco(5))
print(f'10 бутылок', alco(10))
print(f'12 бутылок', alco(12))
print(f'14 бутылок', alco(14))
print(f'16 бутылок', alco(16))