import random

def main():
    cont_maquina = 0
    cont_pessoa = 0
    while True:
        ppt = ['pedra', 'papel', 'tesoura']
        pessoa = input("Escolha entre pedra, papel ou tesoura: ")
        index = random.randint(0, 2)
        maquina = ppt[index]
        pessoa.lower()

        if ((pessoa != 'pedra') and (pessoa != 'papel') and (pessoa != 'tesoura')):
            print("A expressão não é válida!")
            pessoa = input("Escolha entre pedra, papel ou tesoura: ")
            pessoa.lower()
        
        if ((pessoa =='pedra' and maquina == 'tesoura') or (pessoa == 'papel' and maquina == 'pedra') or (pessoa == 'tesoura' and maquina == 'papel')):
            print("O usuário venceu a máquina!")
            print(f"{pessoa} X {maquina}")
            cont_pessoa += 1
            parada = input("Deseja parar de jogar e ver os resultados? [S/N]: ")
            parada.lower()
            if parada == 's':
                break
        elif(maquina == 'pedra' and pessoa == 'tesoura') or (maquina == 'papel' and pessoa == 'pedra') or (maquina == 'tesoura' and pessoa == 'papel'):
            print("A máquina venceu!")
            print(f"{pessoa} X {maquina}")
            cont_maquina += 1
            parada = input("Deseja parar de jogar e ver os resultados? [S/N]: ")
            parada.lower()
            if parada == 's':
                break
        elif(maquina == pessoa):
            print("O jogo está empatado!")
            print(f"{pessoa} X {maquina}")
            parada = input("Deseja parar de jogar e ver os resultados? [S/N]: ")
            parada.lower()
            if parada == 's':
                break
    if cont_maquina > cont_pessoa:
        print(f"A máquina é a vencedora! \n Resultado: \n Máquina = {cont_maquina} \n Usuário = {cont_pessoa}")
    elif cont_pessoa > cont_maquina:
        print(f"O usuário venceu a máquina! \n Resultado: \n Máquina = {cont_maquina} \n Usuário = {cont_pessoa}")
    elif cont_maquina == cont_pessoa:
        print(f"O jogo terminou emparado! \n Resultado: \n Máquina = {cont_maquina} \n Usuário = {cont_pessoa}")
#---------------------------------------------------------------------------------------------------------------------------------------
    
    return

main()