#Solução do programa da semana...
DIA = input ( "Digite o dia da semna:")

match DIA:
   case "segunda":
        print ("Vou para academia!")
   case "terça":
       print ("Melhor não contar...")
   case "quarta":
       print ("Vou na praia.")
   case "quinta":
       print ("Vou na cinema.")
   case "sexta":
       print ("Vou beber todas!")
   case "Sábado":
       print ("Vou descansar")
   case "Dominggo":
       print ("Vou a missa")
   case _:
       print ("Não entendi...")
        
