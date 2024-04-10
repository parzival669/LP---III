def preco_por_tipo(quantidade_kwh,tipo):
    
    if tipo == 'R':
        if quantidade_kwh <= 500:
            preco = 0.40
        else:
            preco = 0.65
    
    elif tipo == 'C':
        if quantidade_kwh <= 1000:
            preco = 0.55
        else:
            preco = 0.60
    
    else:
        if quantidade_kwh <= 5000:
            preco = 0.55
        else: 
            preco = 0.60
    
    return preco

if __name__ == '__main__':
    quantidade_kwh = float(input('Digite o kWh consumido :'))
    tipo = input('[R] Residencial / [C] Comercial / [I] Industrial').upper()
    tipos = ['R','C','I']

    while tipo not in tipos:
         print ('DIGITE UMA OPÇÃO VÁLIDA!!!')
         tipo = input('[R] Residencial / [C] Comercial / [I] Industrial').upper()
    preco = preco_por_tipo(quantidade_kwh,tipo)

    preco_final = preco * quantidade_kwh

    print (f'Preço final : R${preco_final} ')