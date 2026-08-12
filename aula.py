import aula2

nome = input("Digite seu nome ")
idade = int(input("Digite sua idade "))
print(f'Você digitou o nome {nome} e idade {idade}')

print()
print("Vamos desenhar")

for x in range(idade):
	print ("-", end="")

aula2.main()

print("Fim")
