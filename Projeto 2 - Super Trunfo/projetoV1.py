#Feito por Guilherme Ryu Ojima - 10769513
          #Ana Paula Paes Landim Ferro - 10769791



import random
import time

def jogadores():
    while True: 
        Tipo = input("Singleplayer ou Dualplayer (S/D): ")
        if Tipo in "SsDd":
            break
    if Tipo in "Ss":
        return "singleplayer"
    else:
        return "dualplayer"

def baralho1():
    # Cartas exemplo: nome, vmax, cv, ano
    carta1 = ["Ferrari LaFerrari", 360, 963, 2013]
    carta2 = ["Lamborghini SVJ", 350, 770, 2018]
    carta3 = ["Porsche 911", 296, 525, 2026]
    carta4 = ["Audi R8", 330, 610, 2021]
    carta5 = ["Mercedes C63 AMG", 290, 680, 2025]
    carta6 = ["McLaren P1", 330, 916, 2013]
    baralho = [carta1, carta2, carta3, carta4, carta5, carta6]
    return baralho

def imprimir_baralho(mao1, mao2, monteEmpate):
        print("="*30)
        print(mao1)
        print("="*30)
        print(mao2)
        print("="*30)
        print(f"Monte de empate: {monteEmpate}")



def vencedor(j1, j2, n, ctopo1, ctopo2, mao1, mao2, monte_empate):
    if ctopo1[n] > ctopo2[n]:
        print("="*30)
        print(f">>{j1} venceu a rodada!<<")
        mao2.remove(ctopo2)
        mao1.append(ctopo2)
        if monte_empate != []:
            mao1.append(monte_empate) 
      
        mao1.append(ctopo1) # move para o fim da lista
        mao1.remove(ctopo1)


    elif ctopo1[n] < ctopo2[n]:
        print("="*30)
        print(f">>{j2} venceu a rodada!<<")
        mao1.remove(ctopo1)
        mao2.append(ctopo1)
        if monte_empate != []:
            mao2.append(monte_empate)
        
        mao2.append(ctopo2)  # move para o fim da lista
        mao2.remove(ctopo2)
    else:
        print("="*30)
        print(">>Empate!<<")
        monte_empate.append(ctopo1)
        monte_empate.append(ctopo2)
        mao1.remove(ctopo1)
        mao2.remove(ctopo2)

    return mao1, mao2, monte_empate


def singleplayer():  #TODO Arrumar os prints baguncados (Colocar time.sleep ajuda)
    j1 = "Jogador"
    j2 = "Computador"
    baralho = baralho1() #chama baralho e embaralha
    random.shuffle(baralho)
    maojog = baralho[:3]
    maocomp = baralho[3:]
    monte_empate = []

    
    while maojog != [] and maocomp !=[]:
        
        ctopo_jog = maojog[0]
        ctopo_comp = maocomp[0]

        print("----Rodada do JOGADOR----") #RODADA JOGADOR

        print("Carta do jogador 1: ")
        print(f"Nome: {ctopo_jog[0]}")
        print(f"1 - Velocidade: {ctopo_jog[1]}")
        print(f"2 - Cavalos: {ctopo_jog[2]}")
        print(f"3 - Ano: {ctopo_jog[3]}")

        while True:             #Escolha de atributo: jogador
            print("="*30)
            atributo = int(input("Selecione o atributo (1 a 3): "))

            if atributo >= 1 and atributo <=3:
                break
            else:
                print("Valor inválido!")

        print("="*30)
        print("Carta do computador: ")
        print(f"Nome: {ctopo_comp[0]}")
        print(f"1 - Velocidade: {ctopo_comp[1]}")
        print(f"2 - Cavalos: {ctopo_comp[2]}")
        print(f"3 - Ano: {ctopo_comp[3]}")

        maojog, maocomp, monte_empate = vencedor(j1, j2, atributo, ctopo_jog, ctopo_comp, maojog, maocomp, monte_empate)

        print(f"Cartas Jogador: {len(maojog)}")
        print(f"Cartas Computador: {len(maocomp)}")

        if maojog == [] or maocomp == []:  #Finaliza caso acabe por aqui
            break

        ctopo_jog = maojog[0]
        ctopo_comp = maocomp[0]
        
        
        time.sleep(10)


        print("="*30)   #RODADA COMPUTADOR
        print("----Rodada do COMPUTADOR----")
        print("Carta do computador: ")
        print(f"Nome: {ctopo_comp[0]}")
        print(f"1 - Velocidade: {ctopo_comp[1]}")
        print(f"2 - Cavalos: {ctopo_comp[2]}")
        print(f"3 - Ano: {ctopo_comp[3]}")
    

        print("="*30)
        print("Carta do jogador")
        print(f"Nome: {ctopo_jog[0]}")
        print(f"1 - Velocidade: {ctopo_jog[1]}")
        print(f"2 - Cavalos: {ctopo_jog[2]}")
        print(f"3 - Ano: {ctopo_jog[3]}")

        print("="*30)
        
        atributo = random.randint(1, 3)   #Computador escolhe atributo
        print(f"O computador escolheu o atributo {atributo}")


        maojog, maocomp, monte_empate = vencedor(j1, j2, atributo, ctopo_jog, ctopo_comp, maojog, maocomp, monte_empate)
        print(f"Cartas Jogador: {len(maojog)}")
        print(f"Cartas Computador: {len(maocomp)}")

        
        time.sleep(10)

    if maojog == []:  #Declara vencedor final
        print("="*30)
        print("O computador venceu o jogo!")
    elif maocomp == []:
        print("="*30)
        print("Parabéns! O jogador venceu o jogo!")

       


def dualplayer():  #TODO Multiplayer
    j1 = "jogador 1"
    j2 = "jogador 2 "

    baralho = baralho1()

    random.shuffle(baralho)


    maoj1 = baralho [:3]

    maoj2 = baralho [3:]

    monte_empate = []

    while maoj1 !=  [] and maoj2 != []:

        ctopo_j1 = maoj1[0]
        ctopo_j2 = maoj2[0]


        print("----Rodada do JOGADOR 1----")
        print("Carta do jogador 1: ")
        print(f"Nome: {ctopo_j1[0]}")
        print(f"1 - Velocidade: {ctopo_j1[1]}")
        print(f"2 - Cavalos: {ctopo_j1[2]}")
        print(f"3 - Ano: {ctopo_j1[3]}")
        print("=" * 30)

        while True:

            atributo = int(input("Jogador 1, escolha o atributo de 1 a 3: "))

            if atributo >= 1 and atributo <= 3:
                break
        
            else:
                print("Valor invalido")


        print("=" * 30)
        print("Carta do jogador 2: ")
        print(f"Nome: {ctopo_j2[0]}")
        print(f"1 - Velocidade: {ctopo_j2[1]}")
        print(f"2 - Cavalos: {ctopo_j2[2]}")
        print(f"3 - Ano: {ctopo_j2[3]}")

        maoj1, maoj2, monte_empate = vencedor(j1, j2, atributo, ctopo_j1, ctopo_j2, maoj1, maoj2, monte_empate)

        print("="*30)
        print(f"Cartas Jogador 1: {len(maoj1)}")
        print(f"Cartas Jogador 2: {len(maoj2)}")
        print("="*30)
        time.sleep(10)

        if maoj1 == [] or maoj2 == []:  #Finaliza caso acabe por aqui
            break
        ctopo_j1 = maoj1[0]
        ctopo_j2 = maoj2[0]
        
        print("----Rodada do JOGADOR 2----")
        print("Carta do jogador 2: ")
        print(f"Nome: {ctopo_j2[0]}")
        print(f"1 - Velocidade: {ctopo_j2[1]}")
        print(f"2 - Cavalos: {ctopo_j2[2]}")
        print(f"3 - Ano: {ctopo_j2[3]}")
        print("=" * 30)
        
        while True:

            atributo = int(input("Jogador 2, escolha o atributo de 1 a 3: "))

            if atributo >= 1 and atributo <= 3:
                break
        
            else:
                print("Valor invalido")

        print("="*30)
        print("Carta do jogador 1: ")
        print(f"Nome: {ctopo_j1[0]}")
        print(f"1 - Velocidade: {ctopo_j1[1]}")
        print(f"2 - Cavalos: {ctopo_j1[2]}")
        print(f"3 - Ano: {ctopo_j1[3]}")

        maoj1, maoj2, monte_empate = vencedor(j1, j2, atributo, ctopo_j1, ctopo_j2, maoj1, maoj2, monte_empate)

        print("="*30)
        print(f"Cartas Jogador 1: {len(maoj1)}")
        print(f"Cartas Jogador 2: {len(maoj2)}")
        print("="*30)
        time.sleep(10)

    if maoj1 == []:
        print("Jogador 2 venceu o jogo!")
    else:
        print("Jogador 1 venceu o jogo!")

def main():
    tipo = jogadores()
    if tipo == "singleplayer":
        singleplayer()
    else:
        dualplayer()
    print("--FIM DO PROGRAMA--")

main()

