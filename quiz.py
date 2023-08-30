print("Welcome to the Kevin's Quiz!")
answer_user = input("Podemos começar? (S/N) ")
print(answer_user)

if answer_user != "S".lower():
    quit()

score = 0

print("!!!Vamos Nessa!!!\n")
print("Qual o desenvolvedor do game Grand Theft Auto (GTA) ?\n (A) Ubisoft \n (B) EA \n (C) Actvision \n (D) Rockstar Games \n")
answer_1 = input("Resposta: ")

if answer_1 == "D":
    print("Você Acertou!")
    score = score + 1
else:
    print("Você Errou! \n")

print("Qual o nome do protagonista do game Grand Theft Auto (GTA) ?\n (A) Carl Jonhson \n (B) Cidiei \n (C) Carlos Jonh \n (D) Carl Vegas \n")
answer_2 = input("Resposta: ")

if answer_2 == "A":
    print("Você Acertou!")
    score = score + 1
else:
    print("Você Errou!\n")

print("O que acontece com CJ assim que começa o jogo ?\n (A) Sequestrado por um taxi \n (B) Roubado por uma gangue rival \n (C) Pego pela polícia e solto num beco \n (D) Ele é preso\n")
answer_2 = input("Resposta: ")

if answer_2 == "C":
    print("Você Acertou!")
    score = score + 1
else:
    print("Você Errou!\n")

print("Como se chamam as gangues rivais de CJ?\n (A) Ballas e Doces \n (B) Ballas e Vagos \n (C) Grove e Ballas \n (D) Grove e Vagos\n")
answer_2 = input("Resposta: ")

if answer_2 == "B":
    print("Você Acertou!")
    score = score + 1
else:
    print("Você Errou!\n")

print("Em sua primeira missão com Ryder ele te apresentam 2 lugares quais são?\n (A) Delegacia e Cabeleleiro\n (B) Pizzaria e Delegacia \n (C) Pizzaria e Cabeleleiro \n (D) Loja de Armas e Pizzaria\n")
answer_2 = input("Resposta: ")

if answer_2 == "C":
    print("Você Acertou!")
    score = score + 1
else:
    print("Você Errou!\n")

print(f"Chegamos ao fim! O seu placar foi de {score}/5")

