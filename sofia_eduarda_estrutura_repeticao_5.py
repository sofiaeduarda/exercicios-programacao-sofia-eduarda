# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Desenvolvido por Sofia Eduarda

numero = int(input("Digite um número para ver a tabuada dele: "))
if 1 <= numero <= 10:
    print(f"\nTabuada de {numero}: ")
    for i in range(1, 11):
        print(f"{numero} X {i} = {numero * i}")
else:
    print("Número inválido! Somente entre 1 e 10.")