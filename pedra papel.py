from random import randint
placar_n=0
placar_pc=0
opc=["pedra","papel","tesoura","spock","lagarto"] 
pedra=1 
papel=2 
tesoura=3
lagarto=4
spock=5

while placar_n<3 and placar_pc<3:
    
    print("Escolha um numero: pedra-1, papel-2, tesoura-3, lagarto-4 ou spock-5")
    n=int(input(""))

    pc=randint(1,5)
    print(pc)
    
    if n==4 and pc==2:
        print("Lagarto come papel, voce ganhou!")
        placar_n+=1
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==2 and pc==4:
        print("Lagarto come papel, computador ganhou!")
        placar_n=0
        placar_pc+=1
        print(placar_n, "X", placar_pc)
        
    if n==2 and pc==1:
        print("Papel cobre pedra, voce ganhou!")
        placar_n+=1
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==1 and pc==2:
        print("Papel cobre pedra, computador ganhou!")
        placar_n=0
        placar_pc+=1
        print(placar_n, "X", placar_pc)
        
    if n==1 and pc==3:
        print("Pedra esmaga tesoura, voce ganhou!")
        placar_n+=1
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==3 and pc==1:
        print("Pedra esmaga tesoura, computador ganhou!")
        placar_n=0
        placar_pc+=1
        print(placar_n, "X", placar_pc)
        
    if n==3 and pc==2:
        print("Tesoura corta papel, voce ganhou!")
        placar_n+=1
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==2 and pc==3:
        print("Tesoura corta papel, computador ganhou!")
        placar_n=0
        placar_pc+=1
        print(placar_n, "X", placar_pc)
        
    if n==5 and pc==1:
        print("Spock vaporiza pedra, voce ganhou!")
        placar_n+=1
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==1 and pc==5:
        print("Spock vaporiza pedra, computador ganhou!")
        placar_n=0
        placar_pc+=1
        print(placar_n, "X", placar_pc)
        
    if n==2 and pc==5:
        print("Papel refuta spock,voce ganhou!")
        placar_n+=1
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==5 and pc==2:
        print("Papel refuta spock, computador ganhou!")
        placar_n=0
        placar_pc+=1
        print(placar_n, "X", placar_pc)
        
    if n==4 and pc==5:
        print("Lagarto envenena Spock, voce ganhou!")
        placar_n+=1
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==5 and pc==4:
        print("Lagarto envenena Spock, computador ganhou!")
        placar_n=0
        placar_pc+=1
        print(placar_n, "X", placar_pc)
        
    if n==3 and pc==4:
        print("Tesoura decapita lagarto, voce ganhou!")
        placar_n+=1
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==4 and pc==3:
        print("Tesoura decapita lagarto, computador ganhou!")
        placar_n=0
        placar_pc+=1
        print(placar_n, "X", placar_pc)
        
    if n==1 and pc==4:
        print("Pedra esmaga lagarto, voce ganhou!")
        placar_n+=1
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==4 and pc==1:
        print("Pedra esmaga lagarto, computador ganhou!")
        placar_n=0
        placar_pc+=1
        print(placar_n, "X", placar_pc)
        
    if n==5 and pc==3:
        print("Spock esmaga tesoura, voce ganhou!")
        placar_n+=1
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==3 and pc==5:
        print("Spock esmaga tesoura, computador ganhou!")
        placar_n=0
        placar_pc+=1
        print(placar_n, "X", placar_pc)
        
    if n==1 and pc==1:
        print("Ambos escolheram pedra, temos um empate")
        placar_n=0
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==2 and pc==2:
        print("Ambos escolheram papel, temos um empate")
        placar_n=0
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==3 and pc==3:
        print("Ambos escolheram tesoura, temos um empate")
        placar_n=0
        placar_pc=0
        print(placar_n, "X", placar_pc) 
        
    if n==4 and pc==4:
        print("Ambos escolheram lagarto, temos um empate")
        placar_n=0
        placar_pc=0
        print(placar_n, "X", placar_pc)
        
    if n==5 and pc==5:
        print("Ambos escolheram spock, temos um empate")
        placar_n=0
        placar_pc=0
        print(placar_n, "X", placar_pc) 
        
        
    #caso aconteca um empate, o placar nao se altera
    

    
    
    
    
    
     

    
    
    
    
    
    
    
     
    
     
    
    
    
    





