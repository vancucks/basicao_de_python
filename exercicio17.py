num = 0
for y in range(1,11,1):
    numero = int(input(f"entre com o numero {y}: "))
    if numero%2==1:
        num = num+numero
        print(num)