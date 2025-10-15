# Faça um programa que leia 5 números e informe o maior número.
# Desenvolvido por Sofia Eduarda

soma = 0
for i in range(5):
    numero = int(input(f"Informe o {i+1}º número: "))
    soma += numero
media = soma / 5
print(f"A soma é: {soma}")
print(f"A média é: {media}")