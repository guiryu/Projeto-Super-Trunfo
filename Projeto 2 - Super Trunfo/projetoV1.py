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
    carta1 = ["Ferrari F40", 360, 963, 2013]
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
        print(f"{j1} venceu a rodada!")
        mao2.remove(ctopo2)
        mao1.append(ctopo2)
        if monte_empate != []:
            mao1.append(monte_empate) 
      
        mao1.append(ctopo1) # move para o fim da lista
        mao1.remove(ctopo1)


    elif ctopo1[n] < ctopo2[n]:
        print("="*30)
        print(f"{j2} venceu a rodada!")
        mao1.remove(ctopo1)
        mao2.append(ctopo1)
        if monte_empate != []:
            mao2.append(monte_empate)
        
        mao2.append(ctopo2)  # move para o fim da lista
        mao2.remove(ctopo2)
    else:
        print("="*30)
        print("Empate!")
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

        print("Rodada do JOGADOR") #RODADA JOGADOR
        print("^"*20)
        print(f"Jogador: {ctopo_jog}")
        print("~"*20)

        while True:             #Escolha de atributo: jogador
            print("="*30)
            atributo = int(input("Selecione o atributo (1 a 3): "))

            if atributo >= 1 and atributo <=3:
                break
            else:
                print("Valor inválido!", end="")

        print("="*30)
        print(f"Carta do computador: {ctopo_comp}")

        maojog, maocomp, monte_empate = vencedor(j1, j2, atributo, ctopo_jog, ctopo_comp, maojog, maocomp, monte_empate)

        if maojog == [] or maocomp == []:  #Finaliza caso acabe por aqui
            break

        ctopo_jog = maojog[0]
        ctopo_comp = maocomp[0]
        
        imprimir_baralho(maojog, maocomp, monte_empate) #TODO Não sei se pode deixar isso
        
        time.sleep(3)


        print("="*30)   #RODADA COMPUTADOR
        print("Rodada do COMPUTADOR")
        print("^"*20)
        print(f"Carta do computador: {ctopo_comp}")
        print("~"*20)
        print(f"Sua carta: {ctopo_jog}")

        print("="*30)
        
        atributo = random.randint(1, 3)   #Computador escolhe atributo
        print(f"O computador escolheu o atributo {atributo}")


        maojog, maocomp, monte_empate = vencedor(j1, j2, atributo, ctopo_jog, ctopo_comp, maojog, maocomp, monte_empate)

        imprimir_baralho(maojog, maocomp, monte_empate) #TODO Não sei se pode deixar isso
        
        time.sleep(3)

    if maojog == []:  #Declara vencedor final
        print("="*30)
        print("O computador venceu o jogo!")
    elif maocomp == []:
        print("="*30)
        print("Parabéns! O jogador venceu o jogo!")
       


def dualplayer():  #TODO Multiplayer
    baralho = baralho1()
    random.shuffle(baralho)
    maoj1 = baralho[0, 1, 2]
    maoj2 = baralho[3, 4, 5]
    

def main():
    tipo = jogadores()
    if tipo == "singleplayer":
        singleplayer()
    else:
        dualplayer()


main()

