# Faça um programa que verifique se uma letra digitada é vogal ou consoante.
# Desenvolvido por Sofia Eduarda

letra = str(input("Digite uma letra: ")).lower()
if letra in "aeiou":
    print(f"{letra} é uma vogal.")
else:
    print(f"{letra} é uma consoante.")