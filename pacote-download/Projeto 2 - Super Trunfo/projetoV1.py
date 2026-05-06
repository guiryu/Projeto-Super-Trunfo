import random

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


def singleplayer():
    j1 = "Jogador"
    j2 = "Computador"
    baralho = baralho1()
    random.shuffle(baralho)
    maojog = baralho[:3]
    maocomp = baralho[3:]
    monte_empate = []
    
    while maojog != [] and maocomp !=[]:
            #TODO Alternar as rodadas de quem seleciona o atributo? nao sei se precisa isso
        while True:
            print("="*30)
            atributo = int(input("Selecione o atributo (1 a 3): "))

            if atributo >= 1 and atributo <=3:
                break
            else:
                print("Valor inválido!", end="")
    
        ctopo_jog = maojog[0]
        ctopo_comp = maocomp[0]

        print("="*30)
        print(f"Jogador: {ctopo_jog}")
        print(maojog)
        print("="*30)
        print(f"Computador: {ctopo_comp}")
        print(maocomp)

        maojog, maocomp, monte_empate = vencedor(j1, j2, atributo, ctopo_jog, ctopo_comp, maojog, maocomp, monte_empate)
        

    if maojog == []:
        print("="*30)
        print("O computador venceu o jogo!")
    elif maocomp == []:
        print("="*30)
        print("Parabéns! O jogador venceu o jogo!")
    else:
        print("="*30)
        print("O jogo empatou!")
       


def dualplayer():
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

