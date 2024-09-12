entradaN1 = int(input("entre com o primeiro: "))
while entradaN1 == 0:
    print("repita\n")
    entradaN1 = int(input("entre com o primeiro:"))


entradaN2 = int(input("entre com o segundo: "))
while entradaN2 == 0:
    print("repita\n")
    entradaN2 = int(input("entre com o segundo:"))
media = entradaN1 / entradaN2


print(media)