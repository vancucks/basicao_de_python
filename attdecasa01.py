#Preços dos combustíveis
precog = 5.80
precoe = 4.90

#Entrada de litros
lvendidos = float(input("Digite o número de litros vendidos: "))

#Entrada do tipo de combustível
tipo_combustivel = input("Digite o tipo de combustível (E para Etanol, G para Gasolina): ").upper()

#Cálculo do valor total a ser pago com base no tipo de combustível
if tipo_combustivel == 'G':
    valor_total = lvendidos * precog
    #Exibir o resultado
    print(f"O valor total é: R$ {valor_total:.2f}")
else:
    if tipo_combustivel == 'E':
        valor_total = lvendidos * precoe
        #Exibir o resultado
        print(f"O valor total é: R$ {valor_total:.2f}")
    else:
        #Exibir o resultado
        print("Tipo de combustível inválido.")