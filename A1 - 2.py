def opções():
    print("[1] - Cadastrar novo usuário")
    print("[2] - Buscar usuário")
    print("[3] - Lista de usuários")
    print("[4] - Alterar nome de usuário")
    print("[5] - Remover usuário")
    print("[6] - Sair")
    return

def criarUsuário():
    cadastrarUsuário = {}
    cadastrarUsuário["nome"] = input("Digite o nome completo: ")
    cadastrarUsuário["email"] = input("Digite o email: ")
    return cadastrarUsuário

def mostrarUsuários(listaUsuários):
    opçãoLista = int(input())

    if(opçãoLista == 1):
        for usuário in listaUsuários:
            print("Nome: ", usuário["nome"], "Email: ", usuário["email"])
    elif(opçãoLista ==2):
        def ordemAlf(str):
            return str["nome"]
        
        listaUsuáriosOrdenados = listaUsuários.copy()
        listaUsuáriosOrdenados.sort(key = ordemAlf)
        for usuário in listaUsuáriosOrdenados:
            print("Nome: ", usuário["nome"], "Email: ", usuário["email"])

def buscarUsuário(listaUsuários):
    usuárioInformado = input("Digite o nome do usuário:")

    for usuário in listaUsuários:
        if(usuário["nome"] == usuárioInformado):
            return usuário  
    return False

def removerUsuário(listaUsuários):
    usuárioInformado = input("Digite o email do usuário: ")

    for usuário in listaUsuários:
        if(usuário["email"] == usuárioInformado):
            return usuário  
    return False

def alterarNomeDoUsuário(listaUsuários):
    usuárioInformado = input("Digite o email do usuário: ")

    for usuário in listaUsuários:
        if(usuário["email"] == usuárioInformado):
            return usuário    
    return False

def main():
    listaUsuários = []
    opção = 0

    while(opção != 6):
        opções()
        opção = int(input())

        if(opção == 1):
            cadastrarUsuário = criarUsuário()
            listaUsuários.append(cadastrarUsuário)

        elif(opção == 2):           
            usuárioInformado = buscarUsuário(listaUsuários)
            if(usuárioInformado == False):
                print("Usuário não encontrado!\n")
            else:
                print("Nome: ",usuárioInformado["nome"],"Email: ", usuárioInformado["email"])  

        elif(opção == 3):
            print("[1] - Lista por ordem de cadastro")
            print("[2] - Lista por ordem alfabética")
            mostrarUsuários(listaUsuários)

        elif(opção == 4):
            usuárioInformado = alterarNomeDoUsuário(listaUsuários)
            if(usuárioInformado == False):
                print("Usuário não encontrado!\n")
            else:
                novoNome = input("Digite o novo nome do usuário:")
                usuárioInformado.update({"nome":novoNome})        
                print("Usuário alterado!\n")    

        elif(opção == 5):
            usuárioInformado = removerUsuário(listaUsuários)           
            if(usuárioInformado == False):
                print("Usuário não encontrado!\n")
            else:
                listaUsuários.remove(usuárioInformado)
                print("Usuário", usuárioInformado["nome"], "removido!")
          
if __name__ == "__main__":
    main()
