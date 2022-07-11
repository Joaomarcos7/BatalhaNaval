# Bibliotecas usadas:
# Randint - obtida da random = Será usada para sortear a célula que o navio estará;
# Sleep - obtida da time = Será usada para obter delays quando requisitado;

from random import randint
from time import sleep 

# A seguir temos a ordem das funções:
# Caso queira ir direto, pesquise:
# Por exemplo: "1ª função" ou "7ª função" ou pelo nome de cada uma;

# 1 - configurarJogo;
# 2 - criarTabuleiro;
# 3 - ataque;
# 4 - analisarLetra;
# 5 - resultadoTiro;
# 6 - levarParaImpressao;
# 7 - impressao;
# 8 - letrasParaCabecalho;
# 9 - imprimirSeparacao;
# 10 - mostrarPontuacao;
# 11 - arquivosDoPygame;
# 12 - pygame;

# # # # Funções # # # #


#----- 1ª função -----#

# Ivamberg Silva
# Configuração inicial do jogo
def configurarJogo():
    # Definir as variáveis importantes como globais
    global ordem, nomeJogador1, nomeJogador2, quantidadeDeNavios, tabuleiroJogador1, tabOculto1, pontuacaoDoJogador1,tabuleiroJogador2, pontuacaoDoJogador2, tabOculto2

    ordem = 10
    pontuacaoDoJogador1 = pontuacaoDoJogador2 = 0

    # O programa será iniciado e mostrado na tela a partir deste ponto
    print('\033[30m-\033[m'*38)
    print('🚢 \033[34mBem-vindo ao jogo BATALHA NAVAL\033[m 🚢')
    print('\033[30m-\033[m'*38)
    sleep(1)

    # Pede-se o nome de cada jogador
    nomeJogador1 = str(input('\033[33m🔘 NOME DO PRIMEIRO JOGADOR: \033[m')).upper().strip()
    sleep(0.5)
    nomeJogador2 = str(input('\033[34m🔘 NOME DO SEGUNDO JOGADOR: \033[m')).upper().strip()
    sleep(0.5)

    # Escolher a quantidade de navios que cada jogador possuirá
    while True:
        quantidadeDeNavios = int(input('🚢 Número de navios de cada jogador 🚢 [máximo = 10]: '))
        if quantidadeDeNavios <= 10 and quantidadeDeNavios >= 1:
            break
    sleep(0.5)

    # Tabuleiros ocultos
    tabOculto1 = [['-']* ordem for i in range(ordem)]
    tabOculto2 = [['-']* ordem for i in range(ordem)]

    # Tabuleiros que mostram as frotas
    tabuleiroJogador1 = criarTabuleiro(quantidadeDeNavios)
    tabuleiroJogador2 = criarTabuleiro(quantidadeDeNavios)  

    # Vamos definir se os usuários querem que mostre a frota de navio no tabuleiro ou não durante o jogo
    global mostrarTabuleiro
    while True:
        mostrarTabuleiro = int(input('\n\033[35mMostrar FROTA no tabuleiro?\033[m\n\033[35m[Selecione\033[m \033[33m"1"\033[m \033[35mpara NÃO MOSTRAR a FROTA]\033[m\n\033[35m[Selecione\033[m \033[33m"2"\033[m \033[35mpara MOSTRAR a FROTA]\033[m\n'))
        
        # Observação para as próximas condições. Como temos uma função para imprimir todas as matrizes em todas as possibilidades, passamos parâmetros do tipo "None", pois não serão usados nessa declaração. Porém, não podemos ocultar os 3 últimos, tendo em vista que mesmo essa função recebe 5 parâmetros formais, usados por outras funções;

        # NÃO MOSTRAR AS FROTAS DE NAVIOS DE CADA JOGADOR, DURANTE A PARTIDA
        if mostrarTabuleiro == 1:
            levarParaImpressao(tabuleiroJogador1, 1, None, None, None)
            sleep(1)
            levarParaImpressao(tabOculto1, 1, None, None, None)
            sleep(1)
            break

        # MOSTRAR AS FROTAS DE NAVIOS DE CADA JOGADOR, DURANTE A PARTIDA
        elif mostrarTabuleiro == 2:
            levarParaImpressao(tabuleiroJogador1, 1, None, None, None)     
            sleep(1)
            break

        # USUÁRIO DIGITOU ALGUMA VALOR INVÁLIDO
        else:
            print('⚠️ \033[31mDigite uma opção válida! [Opção 1 ou Opção 2]\033[m⚠️\n')


#----- 2ª função -----#

# João Marcos 
# Função da criação do tabuleiro com espaços vazios e navios
def criarTabuleiro(quantidadeDeNavios):  
    tabuleiro = [['-']*ordem for i in range(ordem)]
    cont = 0

    # Impede que os navios encostem uns nos outros
    while cont < quantidadeDeNavios:
        linha = randint(0, ordem - 1)
        coluna = randint(0, ordem - 1)

        # Verificação para o N na diagonal superior  esquerda
        if linha > 0 and coluna > 0 and tabuleiro[linha-1][coluna-1] == 'N':
            continue #faz o loop voltar para o início identado.
        if linha > 0 and tabuleiro[linha-1][coluna] == 'N': #verificação para o N adjascente acima
            continue
        if linha > 0 and coluna < (ordem - 1) and tabuleiro[linha-1][coluna+1] == 'N': #verificação para o N diagonal superior direita 
            continue
        if coluna > 0 and tabuleiro[linha][coluna-1] == 'N': #verificação para o N adjascente ao lado esquerdo
            continue
        if tabuleiro[linha][coluna] == 'N': #verificação para o N na mesma coordenada 
            continue
        if coluna < (ordem - 1) and tabuleiro[linha][coluna+1] == 'N': #verificação para o N adjascente ao lado direito
            continue
        if linha < (ordem - 1) and coluna > 0 and tabuleiro[linha+1][coluna-1] == 'N': #verificação para o N diagonal inferior esquerda
            continue
        if linha < (ordem - 1) and tabuleiro[linha+1][coluna] == 'N': #verificação para o N adjascente abaixo
            continue
        if linha < (ordem - 1) and coluna < (ordem - 1) and tabuleiro[linha+1][coluna+1] == 'N': #verificação para o N diagonal inferior direita 
            continue
        tabuleiro[linha][coluna] = 'N'
        cont += 1

    return tabuleiro


#----- 3ª função -----#

# Ivamberg Silva
# Função de ataque. Aqui será pedido a letra e o número, representando, respectivamente, a linha e a coluna de ataque.
def ataque(tabuleiro, identidade):
    while True:
        sleep(0.5)
        # Escolher qual será a unidade de célula atacada
        bombardear = str(input('🎯 Digite a posição que você quer atacar. 🎯 \033[33mEx: D8\033[m: ')).upper().strip()
        # Converter as escolhas para números inteiros. Ex: A == 1; B == 2;
        letra = analisarLetra(bombardear[0])
        numero = int(bombardear[1:])
        imprimirSeparacao()
        return resultadoTiro(tabuleiro, identidade, letra, numero)


#----- 4ª função -----#

# Ivamberg Silva
# Escolher unidade para ser atacada; O contador, cada vez que passar para a próxima letra vai contar e isso fará com que as letras virem números inteiros. Ex: A == 1; B == 2;
# [Essa função será chamada na função "ataque"]
def analisarLetra(letra):
    contador = 0
    for i in 'ABCDEFGHIJ':
        contador += 1
        if i == letra:
            return contador


#----- 5ª função -----#

# Ivamberg Silva e João Marcos
# O parâmetro "tabuleiro" é auto explicativo, irá receberá o tabuleiro
# Já o parâmetro "identidade" irá definir de qume é o tabuleiro [1 - refere ao primeiro jogador; 2 - refere ao segundo jogador]
# Os parâmetros "linha" e "coluna" definirá a "linha" e a "coluna" que o jogador mirou no adversário
# O último parâmetro representam a consequência: 0 (Sem consequência); 1 (Fogo); 2 (Água);

def resultadoTiro(tabuleiro, identidade, linha, coluna):
    # QUANDO O JOGADOR ACERTAR ALGUM NAVIO;
    # Irá imprimir os dois tabuleiros; O de quem atacou e o de quem foi atacado, este com o símbolo de 'F' onde foi atingido;
    # Ao retornar True; simboliza que o jogador acertou o navio e continuará jogando;
    
    if tabuleiro[linha-1][coluna-1] == 'N':
        tabuleiro[linha-1][coluna-1] = 'F'
        if identidade == 1:
            if mostrarTabuleiro == 1: # NÃO MOSTRAR A FROTA DE NAVIOS
                levarParaImpressao(tabOculto2, 2, linha, coluna, 1)
            else:
                levarParaImpressao(tabuleiroJogador2, 2, linha, coluna, 0)
        else:
            if mostrarTabuleiro == 1: # NÃO MOSTRAR A FROTA DE NAVIOS
                levarParaImpressao(tabOculto1, 1, linha, coluna, 1)
            else:
                levarParaImpressao(tabuleiroJogador2, 2, linha, coluna, 0)
        pygame(1)
        print(f'\n💥 \033[32mVocê ACERTOU, \033[33m{nomeJogador1}\033[m, é \033[31mFOGO!\033[m 💥\n')
        print('😀 \033[33mJOGUE NOVAMENTE! \033[m😀')
        imprimirSeparacao()
        return True

    # QUANDO O JOGADOR ACERTAR ALGUMA COORDENADA ONDE TERIA UM NAVIO, PORÉM, QUE JÁ FOI ATINGIDA;
    # Irá imprimir os dois tabuleiros como estariam anteriormente;
    # Ao retornar False; simboliza que o jogador atirou novamente algum lugar já acertado; Agora a vez irá ser a do adversário;

    elif tabuleiro[linha-1][coluna-1] == 'F':
        print('\n😞 \033[31mVocê acertou um lugar já BOMBARDEADO! \033[m😞')
        imprimirSeparacao()
        return False

    # QUANDO ERRAR O TIRO - FOR NA ÁGUA
    # Irá imprimir os dois tabuleiros; O de quem atacou e o de quem foi atacado, este com o símbolo de 'A' onde foi atingido;
    # Ao retornar False; simboliza que o jogador errou o navio; Agora a vez irá ser a do adversário;
    
    else:
        if identidade == 1:
            if mostrarTabuleiro == 1: # NÃO MOSTRAR A FROTA DE NAVIOS
                levarParaImpressao(tabOculto2, 2, linha, coluna, 2)
            else:
                levarParaImpressao(tabuleiroJogador2, 2, linha, coluna, 2)
        else:
            if mostrarTabuleiro == 1: # NÃO MOSTRAR A FROTA DE NAVIOS
                levarParaImpressao(tabOculto1, 1, linha, coluna, 2)
            else:
                levarParaImpressao(tabuleiroJogador1, 1, linha, coluna, 2)
        pygame(2)
        print('\n💧 \033[31mVocê ERROU, é ÁGUA! \033[m💧')
        print('👋 \033[31mVOCÊ PERDEU A VEZ! \033[m👋')
        imprimirSeparacao()
        return False


#----- 6ª função -----#

# Ivamberg Silva
# Essa função prepara os tabuleiros com os F de fogo e A de água para levar à impressão
def levarParaImpressao(tabuleiroBase, identidade, linha, coluna, consequencia):
    # Identidade == 1 significa que o tabuleiro pertence ao primeiro jogador.
    if identidade == 1:
        if consequencia == 1:
            tabuleiroBase[linha-1][coluna-1] = 'F'
        elif consequencia == 2:
            tabuleiroBase[linha-1][coluna-1] = 'A'
        impressao(tabuleiroBase)

    # Identidade == 2 significa que o tabuleiro pertence ao segundo jogador.
    elif identidade == 2:
        if consequencia == 1:
            tabuleiroBase[linha-1][coluna-1] = 'F'
        elif consequencia == 2:
            tabuleiroBase[linha-1][coluna-1] = 'A'
        impressao(tabuleiroBase)


#----- 7ª função -----#

# Ivamberg Silva
# Obs do programador: esse foi um desafio bastante legal de realizar;
# Essa função será para imprimir os tabuleiros um ao lado do outro, com cabeçalho e os demais enfeites;
def impressao(tabuleiroBase):
    if tabuleiroBase == tabuleiroJogador1 or tabuleiroBase == tabuleiroJogador2:
        tabuleiroImpresso1 = tabuleiroJogador1
        tabuleiroImpresso2 = tabuleiroJogador2

    elif tabuleiroBase == tabOculto1 or tabuleiroBase == tabOculto2:
        tabuleiroImpresso1 = tabOculto1
        tabuleiroImpresso2 = tabOculto2
    
    print(f'\n🔴 Tabuleiro da(o) \033[33m{nomeJogador1}\033[m', end=' '*(36-len(nomeJogador1)))
    print(f'🔴 Tabuleiro da(o) \033[34m{nomeJogador2}\033[m\n')

    print('🚢', end=' '*4)
    for i in range(ordem):
        if i > 8:
            print(f'\033[34m{i+1}\033[m', end=' '*2)
        else:
            print(f'\033[34m{i+1}\033[m', end=' '*3)
        if i == ordem-1:
            print(' '*3, end='')
            print('🚢', end=' '*5)
            for i in range(ordem):
                if i > 9:
                    print(f'\033[34m{i+1}\033[m', end=' '*2)
                else:
                    print(f'\033[34m{i+1}\033[m', end=' '*3)
    print()

    for i in range(ordem):
        print(f'\033[34m{letrasParaCabecalho(i-1):3}\033[m', end='\033[30m|\033[m  ')
        for j in range(ordem):
            print(f'\033[30m{tabuleiroImpresso1[i][j]:4}\033[m', end='')
        print(f'   \033[34m{letrasParaCabecalho(i-1):3}\033[m', end='\033[30m|\033[m')
        for k in range(ordem):
            if k == 0:
                print(' '*3, end='')
            print(f'\033[30m{tabuleiroImpresso2[i][k]:4}\033[m', end='')
        print()
    print()


#----- 8ª função -----#

# Ivamberg Silva
# Definir letra de cada linha no cabeçalho [essa função será chamada na função "impressao"]
def letrasParaCabecalho(contador):
    l = 'ABCDEFGHIJ'
    contador += 1
    return l[contador]


#----- 9ª função -----#

# Ivamberg Silva
# Essa função serve apenas para imprimir uma separação entre alguns pontos específicos, quando ela for chamada;
def imprimirSeparacao():
    print()
    print('\033[30m=\033[m '*28)
    print()

#----- 10ª função -----#

# Ivamberg Silva
# Função para mostrar a pontuação de cada jogador, quando for solicitada;
def mostrarPontuacao():
    print('🟨 \033[35mTABELA DA PONTUAÇÃO DOS JOGADORES \033[m🟨\n')
    print(f'Pontuação do jogador \033[33m{nomeJogador1}\033[m: \033[32m{pontuacaoDoJogador1}\033[m')
    print(f'Pontuação do jogador \033[34m{nomeJogador2}\033[m: \033[32m{pontuacaoDoJogador2}\033[m')
    imprimirSeparacao()
        

#----- 11ª função -----#
# Ivamberg Silva
# Função para guardar os arquivos do pygame para os sons
def arquivosDoPygame():
    import pygame
    pygame.mixer.init()
    pygame.init()

    global bomba, agua, aplausos
    
    bomba = pygame.mixer.Sound('projetoape/sons/bomba.mp3')
    agua = pygame.mixer.Sound('projetoape/sons/agua.mp3')
    aplausos = pygame.mixer.Sound('projetoape/sons/aplausos.mp3')


#----- 12ª função -----#
# Ivamberg Silva
# Função para tocar os sons de efeitos sonoros
def pygame(som):    
    if som == 1:
        bomba.play(0)
        sleep(2.8)
    elif som == 2:
        agua.play(0)
        sleep(2.5)
    elif som == 3:
        aplausos.play(0)
        sleep(4)