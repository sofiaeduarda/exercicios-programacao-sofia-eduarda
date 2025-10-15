# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
# Desenvolvido por Sofia Eduarda

while True:
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a sua senha: ")
    if senha == usuario:
        print("Erro: a senha não pode ser igual ao usuário. Tente denovo.\n")
    else:
        print("Cadastro realizado com sucesso!")
        break