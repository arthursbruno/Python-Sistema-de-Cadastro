def main ():
  nome = ""
  idade = 0 
  opção = 0

while True: 
  print ("MENU PRINCIPAL")
  print ("Escolha uma das opções abaixo")
  print("Opção 1: Fazer cadastro do usuario")
  print("Opção 2: Ver dados cadastrados")
  print ("Opção 3: Voltar para o menu")
  opção = int(input("Escolha uma opção: "))
  

  if  opção == 1:
   nome = input("Digite seu nome: ")
   idade = int(input("Digite sua idade: "))
   print ("Usuario cadastrado")


  elif  opção == 2:
    if nome == "" or idade ==0:
      print ("Usuario não cadastrado")

    else:
      print("Dados do usuario: ")
      print(f"Nome: {nome}")
      print (f"Idade: {idade}")

  
  elif  opção == 3:
    print ("Voltando para o menu...")
    break
  else:
    print ("Opção invalida")
    
    
    
if __name__=="__main__":
  main()



    
   

