# Avaliação de filme ou série de tv
CONTEUDO = input ("Qual o filme preferido?")
AVALIAÇÃO = int ( input ( "Atribuir umanota e 1 a 5 :"))

# Realizae a avaliação...
match AVALIAÇÃO:

    case 1 :
        print ( "Péssimo")
    case 2 :
        print ( "Ruim")
    case 3 :
        print ( "Razoável")
    case 4 :
        print ( "Bom")
    case 5 :
        print ( "Otimo")
    case _:
        print ("Opção não reconhecida...")
      


