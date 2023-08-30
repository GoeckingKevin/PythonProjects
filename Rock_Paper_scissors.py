import random
user_score = 0
computer_score = 0

options = ["r", "t", "p"]
print("Vamos jogar!\n")
while True:
    user_choice = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").lower()

    if user_choice == 'q':
        break

    if user_choice not in options:
        continue

    computer_choice = random.randint(0, 2)
    # 0 : R, 1 : T, 2 : P
    computer_option = options[computer_choice]

    print("O computador escolheu " + computer_option)

    if user_choice == computer_option:
        print("Empate!")
    elif user_choice == "r" and computer_option == "t":
        print("Você ganhou!")
        user_score = user_score + 1

    elif user_choice == "p" and computer_option == "r":
        print("Você ganhou!")
        user_score = user_score + 1
    
    elif user_choice == "t" and computer_option == "p":
        print("Você ganhou!")
        user_score = user_score + 1
    else:
        print("Você perdeu!")
        computer_score = computer_score + 1

print("Sua pontuação " + str(user_score))
print("Pontuação da máquina " + str(computer_score))

if computer_score > user_score:
    print("Você perdeu!")
elif user_score > computer_score:
    print("Você ganhou!")
else:
    print("Empatou")
print("\n")
print("GoodBye!")