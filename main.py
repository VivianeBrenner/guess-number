import random

print("Bem-vindo ao Guess Number!")
choice_number = input("Digite o número teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: valor informado não é númerico!")
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input("Adivinhe o número: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado não é númerico, por favor informe um número!")
        continue

    n_choices = n_choices + 1
    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("Chutou alto! O número é menor que isso...")
    else:
         print("Chutou baixo! O número é maior que isso...")
print("Número de tentativas: " + str(n_choices))
