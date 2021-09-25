import random
QTD_MINIMA_INTERACAO = 7
salaSorteada = [1,2,3,4,5]
countInteracao = 0
sala = 1

def menu (opcao):
    if(sala == 6):
        return "Esta sala existe apenas um caminho: "
    return "Escolha seu caminho:\n[1] Caminho vermelho\n[2] Caminho preto"

def resultCaminho (sala):
    if(caminho == 2 or sala == 6):
        if(sala == 8):
            return sala + 1
        return sala + 2  
    return sala + 1
    
while(countInteracao < QTD_MINIMA_INTERACAO and sala < 8):
    print("Você está na sala: ", sala)
    
    if(sala != 6):
        print(menu(sala))
        caminho = int(input())
        sala = resultCaminho(sala)
        countInteracao = countInteracao + 1
    else:
        print(menu(sala))
        sala = resultCaminho(sala)

if(sala == 8 and countInteracao < QTD_MINIMA_INTERACAO):
    print("Você está na sala: 8")

    print(menu(sala))

    caminho = int(input())
    countInteracao = countInteracao + 1
    
    if(caminho == 1 and countInteracao < QTD_MINIMA_INTERACAO):
        pass
    
    else:
        sala = (random.choice(salaSorteada)) 
   
        while(countInteracao < QTD_MINIMA_INTERACAO and sala < 9):
            print("Você está na sala: ", sala)

            if(sala != 6):
                print(menu(sala))
                caminho = int(input())
                sala = resultCaminho(sala)
                countInteracao = countInteracao + 1
            else:
                print(menu(sala))
                sala = resultCaminho(sala)


if(countInteracao < QTD_MINIMA_INTERACAO and sala < 9):
    print("Você está na sala: 9\nParabéns, você venceu!")
else:
    print("Perdeu! Você realizou 7 ou mais interações")