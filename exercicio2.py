nome = input('Digite o seu nome:\n')
nota1 = input("Digite a sua primeira nota:\n")
nota1 = float(nota1)
nota2 = input("Digite a sua segunda nota: ")
nota2 = float(nota2)
media = (nota1+nota2)/2

if media < 6:
    print("Que pena. Você está reprovado!")
else:
    print("Parabéns você pasosu de ano!!")
