# Faça um programa que leia 5 números e informe o maior número.
# Desenvolvido por Sofia Eduarda

numeros = []
for i in range(5):
    num = int(input(f"Informe o {i+1}º número: "))
    numeros.append(num)
maior = max(numeros)
print(f"O maior número é {maior}.")