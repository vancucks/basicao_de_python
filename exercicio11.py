hora_1 = int(input("Hora 1: "))
minuto_1 = int(input("Minutos 1: "))
hora_2 = int(input("Hora 2: "))
minuto_2 = int(input("Minutos 2: "))

transforma_hora_1 = (hora_1 * 60) + minuto_1
transforma_hora_2 = (hora_2 * 60) + minuto_2

minutos_totais = transforma_hora_1 + transforma_hora_2
horas = (minutos_totais // 60) % 12
minutos = minutos_totais % 60

#:02d é para deixar so 2 digitos
print(f"Total em horas: {horas:02d}:{minutos:02d}")