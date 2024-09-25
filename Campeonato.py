# Atividade #1...

CLUBE = input ( "Digite o seu clube:")
POSICAO = int ( input ( "Digite a posição:"))

if POSICAO == 1:
    print ("campeão!")
elif POSICAO >1 and POSICAO <= 6:
    print ("Libertadores!")
elif POSICAO >=7 and POSICAO <= 12:
    print ("Sul - Americana.")
elif POSICAO >= 17:
    print ("Rebaixado...")
else :
    print ("Não sei dizer...")    



    