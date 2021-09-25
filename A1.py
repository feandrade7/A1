import random
QTD_MINIMA_INTERACAO = 7

def menu (opcao):
    if(sala == 6):
        return "Esta sala existe apenas um caminho:\n[1] Caminho preto"
    return "Escolha seu caminho:\n[1] Caminho vermelho\n[2] Caminho preto"

salaSorteada = [1,2,3,4,5]
countInteracao = 0
sala = 1

while(countInteracao < QTD_MINIMA_INTERACAO and sala < 8):
    print("Você está na sala: ", sala)

    print(menu(sala))

    caminho = int(input())
    countInteracao = countInteracao + 1
    
    if(caminho == 2 or sala == 6):
        sala = sala + 2
    else:
        sala = sala + 1    

if(sala == 8 and countInteracao < QTD_MINIMA_INTERACAO):
    print("\nVocê está na sala: 8")

    print(menu(sala))

    caminho = int(input())
    countInteracao = countInteracao + 1
    
    if(caminho == 1 and countInteracao < QTD_MINIMA_INTERACAO):
        print("Você está na sala: 9\nParabéns, você venceu!")
    
    else:
        sala = (random.choice(salaSorteada)) 
   
        while(countInteracao < QTD_MINIMA_INTERACAO):
            print("Você está na sala: ", sala)
        
            print(menu(sala))
            caminho = int(input())
            countInteracao = countInteracao + 1
    
            if(caminho == 2 or sala == 6):
                 sala = sala + 2
            else:
                 sala = sala + 1 


if(countInteracao < QTD_MINIMA_INTERACAO and sala == 9):
    print("Você está na sala: 9\nParabéns, você venceu!")
else:
    print("Perdeu! Você realizou 7 ou mais interações")