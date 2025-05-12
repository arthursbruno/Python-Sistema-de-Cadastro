 # Sistema de Cadastro Bancário
def main ():
    banco = ""
    nome = ""
    tipo_de_conta = ""
while True: 
  print("MENU PRINCIPAL")
  print("Escolha uma das opções abaixo:")
  print("Opção 1: Fazer cadastro")
  print("Opção 2: Exibir confirmação de cadastro")
  print("Opção 3: Sair")
  opção = int(input("Digite a opção escolhida: "))

  if opção == 1:
        print("VAMOS FAZER SEU CADASTRO!")
        banco = input("Digite o nome do seu banco: ")
        nome =  input("Digite o seu nome: ")
        tipo_de_conta = input("Digite o tipo de conta(Corrente ou Poupança): ")
        if tipo_de_conta != "Poupança" or tipo_de_conta != "Corrente":
           print("Tipo de conta inválido")
        else:
           print("DADOS CADASTRADOS!")

  elif opção == 2:
    if nome != "":
        print ("Cliente não cadastrado")
    
    else:
        print("DADOS CADASTRADOS COM SUCESSO:")
        print ("Nome do cliente:", nome)
        print("Banco cadastrado: ", banco)
        print("Tipo de conta:", tipo_de_conta)

  elif opção == 3:
    print("Saindo para o menu...")
    break
  else:
    print("Opção inválida") 
    

if __name__=="__main__":
  main()
