import functions
from random import randint
from time import sleep 
# # # # #  Programa principal  # # # # #

#Ivamberg Silva e João Marcos
while True:
    functions.arquivosDoPygame()
    #Fábio - Adicionei o while abaixo para caso a opção escolhida seja diferente de 1 ou 2 volte a pergunta e seja solicitado que se digite um valor válido
    while True:
        escolha = int(input('😀 Olá, o que você deseja fazer?\n\033[32m[1 - Iniciar um novo jogo?]\033[m ✔️\n\033[31m[2 - Sair]\033[m 👋\n'))
        if escolha == 1 or escolha == 2:
            break
    if escolha == 2:
            break
    sleep(1)
    print('🎉 Vamos começar 🎉')
    sleep(1)
    functions.configurarJogo()
    while True:
        while True:
            print(f'\n👉 Agora é a vez do jogador \033[33m{functions.nomeJogador1}\033[m atacar o jogador \033[34m{functions.nomeJogador2}\033[m\n')
            resultadoDoAtaque = functions.ataque(functions.tabuleiroJogador2, 1)
            if resultadoDoAtaque == True:
                functions.pontuacaoDoJogador1 += 1
                functions.mostrarPontuacao()
                if functions.pontuacaoDoJogador1 == functions.quantidadeDeNavios:
                    sleep(1)
                    print('\033[35mEspereeem.... alguém ganhou...\033[m\n')
                    sleep(2)
                    print(f'\n👏 \033[32mPARABÉNS!\033[m \033[33m{functions.nomeJogador1}\033[m \033[32mGANHOU!\033[m 👏\n')
                    functions.pygame(3)
                    break
            else:
                functions.mostrarPontuacao()
                break

        if functions.pontuacaoDoJogador1 == functions.quantidadeDeNavios:
            break

        while True:
            print(f'👉 Agora é a vez do jogador \033[34m{functions.nomeJogador2}\033[m atacar o jogador \033[33m{functions.nomeJogador1}\033[m\n')
            resultadoDoAtaque = functions.ataque(functions.tabuleiroJogador1, 2)
            if resultadoDoAtaque == True:
                functions.pontuacaoDoJogador2 += 1
                functions.mostrarPontuacao()
                if functions.pontuacaoDoJogador2 == functions.quantidadeDeNavios:
                    sleep(1)
                    print('\033[35mEspereeem.... alguém ganhou...\033[m\n')
                    sleep(2)
                    print(f'\n👏 \033[32mPARABÉNS!\033[m \033[34m{functions.nomeJogador2}\033[m \033[32mGANHOU! \033[m👏\n')
                    functions.pygame(3)
                    break 
            else:
                functions.mostrarPontuacao()
                break
        if functions.pontuacaoDoJogador2 == functions.quantidadeDeNavios:
            break
print('\n😀 \033[33mFoi um prazer ter esse momento com você. 👏 Volte sempre!\033[m 👋\n')
