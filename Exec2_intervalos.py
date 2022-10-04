interval1 = []   ## intervalo 1 => [0-25]
interval2 = []   ## intervalo 2 => [26-50]
interval3 = []   ## intervalo 3 => [51-75]
interval4 = []   ## intervalo 4 => [76-100]


while True:
    num = float(input('Entre com numeros positivos: '))
    if num > 0 and num <= 25:
        interval1.append(num)
    elif num >= 26 and num <= 50:
        interval2.append(num)
    elif num >= 51 and num <= 75:
        interval2.append(num)
    elif num >= 76 and num <= 100:
        interval2.append(num)
    
    if num < 0:
        break

print(f"""
    intervalo 1 => [0-25] {interval1} Quantidade de numeros {len(interval1)}
    intervalo 2 => [26-50] {interval2} Quantidade de numeros {len(interval2)}
    intervalo 3 => [51-75] {interval3} Quantidade de numeros {len(interval3)}
    intervalo 4 => [76-100] {interval4} Quantidade de numeros {len(interval4)}
""")