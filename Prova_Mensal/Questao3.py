def cm(km, c):
    cm = km / c
    return cm

if __name__ == "__main__":
    km = float(input("Digite o distância [Km]: "))
    c = float(input("Digite o combustivel gasto [L]: "))
    cm = cm(km, c)
    print(f'{cm} km/L')
