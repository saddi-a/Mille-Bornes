from Player import Player
from Deck import Deck
from random import randint
from Card import Card,Distance,Safety,Attack,Defense
from Board import Board

class Game():
    def __init__(self):
        self.numberPlayer=2 #Nombre de joueur
        self.tabPlayers=[Player("A"),Player("B")]  #Tableau des joueur
        self.currentPlayer=0 #numéro du joueur actuelle
        self.rounds=1 #Tableau du round
        self.winner=None #Joueur Gagnant 
        self.end=False #booleen de fin de partie
        self.gameDeck=Deck() #Deck de pioche
        self.garbageDeck=Deck() #Deck de défausse pioche

    # getters et setters des attributs privés
    @property
    def end(self):
        return self.__end
    @end.setter
    def end(self,value):
        if type(value)!= bool: 
            print("Erreur : end prend un type Booleen")
        else :
            self.__end=value
    @property
    def tabPlayers(self):
        return self.__tabPlayers

    @tabPlayers.setter
    def tabPlayers(self,tabPlayer):
        for p in tabPlayer:
            if not(isinstance(p,Player)):
                print("Erreur: tabPlayers prend que des types Player")

        self.__tabPlayers=tabPlayer
            
    @property
    def gameDeck(self):
        return self.__gameDeck


    @gameDeck.setter
    def gameDeck(self,gameDeck):
        CARDTYPE=[1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ID=[0,1,2,3,0,0,0,1,1,1,2,2,2,3,3,3,3,4,4,4,4,4,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4]
        #ID et Type des 106 cartes du jeux (pille principale)

        if not isinstance(gameDeck,Deck):
            print("Erreur : gameDeck prend une pile de type Deck")
        elif (gameDeck==Deck()): 
            self.__gameDeck=Deck(CARDTYPE,ID)
        else :
            self.__gameDeck=gameDeck  

    
    @property
    def numberPlayer(self):
        return self.__numberPlayer

    @numberPlayer.setter
    def numberPlayer(self,numberPlayer):
        if type(numberPlayer) != int: 
            print("Erreur : numberPlayer prend un type int")
        elif numberPlayer<2 or numberPlayer>4:
            print("Erreur : numberPlayer ne peut pas prendre une valeur < 2 ou > 4")
        else :
            self.__numberPlayer=numberPlayer  
    
    @property
    def winner(self):
        return self.__winner
    @winner.setter
    def winner(self,value):
        if not(isinstance(value,Player)) and value!=None: 
            print("Erreur : winner prend un type Player")
        else :
            self.__winner=value 

    @property
    def currentPlayer(self):
        return self.__currentPlayer

    @currentPlayer.setter
    def currentPlayer(self,currentPlayer):
        if type(currentPlayer) != int: 
            print("Erreur : currentPlayer prend un type int")
        elif currentPlayer<-1 or currentPlayer>self.numberPlayer:
            print("Erreur : currentPlayer ne peut pas prendre une valeur < 0 ou > self.numberPlayer")
        else :
            self.__currentPlayer=currentPlayer 
    
    @property
    def rounds(self):
        return self.__rounds

    @rounds.setter
    def rounds(self,rounds):
        if type(rounds) != int: 
            print("Erreur : rounds prend un type int")
        elif rounds<0 :
            print("Erreur : rounds ne peut pas prendre une valeur negative")
        else :
            self.__rounds=rounds 

    @property
    def garbageDeck(self):
        return self.__garbageDeck  
    
    @garbageDeck.setter
    def garbageDeck(self,deck):
        if not(isinstance(deck,Deck)):
            print("Erreur: garbageDeck ne peut prendre qu'une pile de type Deck")
        else :
            self.__garbageDeck=deck

    def __str__(self):
        msg=""
        for i in self.tabPlayers:
            msg+=f"{i} \n"
        return msg[0:len(msg)-2]

    #Méthode de lancement d'une partie
    def start(self):
        print("+-------------------------------------+")
        print("|  Bienvenue dans le jeu 1000 bornes  |")
        print("+-------------------------------------+")
        c=int(input("voulez vous charger une partie ? (0 : Oui | 1 : Non) "))
        while(c!=0 and c!=1) :
            c=int(input("voulez vous charger une partie ? (0 : Oui | 1 : Non) "))       
        if c == 0 :
            self.loadGame()
        else:
            
            nbJoueurs=int(input("combien de joueurs ? "))
            while not(nbJoueurs<5 and nbJoueurs>1):
                print("Veuillez choisir un nombre entre 2-4")
                nbJoueurs=int(input("combien de joueurs ? "))
            tabNames=[]
            
            for i in range(nbJoueurs):
                nom_OK=False
                name=input(f"veuillez entrer le nom du joueur {i+1} : ")
                while not(nom_OK) and (i>0):
                    for n in tabNames:
                        if name == n :
                            print("Nom joueur déja existant !")
                            name=input(f"veuillez entrer à nouveau le nom du joueur {i+1} : ")
                        else:
                            nom_OK=True        
                tabNames.append(name)
            
            self.numberPlayer=nbJoueurs
            self.tabPlayers=[Player(tabNames[i]) for i in range(nbJoueurs)]  
            self.DistributeCards()

        self.playGame()


    #Méthode de distribution de carte pour le début de partie
    def DistributeCards(self):
        #pour distribuer 6 cartes
        for _ in range(6):
            for p in self.tabPlayers:
                #distribuer une carte aléatoirement au joueur et enlever de la pille
                r=randint(0,self.gameDeck.cardsNumber - 1)
                c=self.gameDeck.cardList[r]
                self.gameDeck.removeCard(c)
                p.hand.addCard(c)
    
    #Méthode de pioche
    def drawCard(self):
        r=randint(0,self.gameDeck.cardsNumber - 1)
        c=self.gameDeck.cardList[r]
        self.gameDeck.removeCard(c)
        self.tabPlayers[self.currentPlayer].hand.addCard(c)
        #si la pille du jeu est finie , la partie est finie

        if (self.gameDeck.cardsNumber==0):
            self.end=True
        
    #Méthode de déffause
    def throwCard(self):
        n=int(input("choisissez une carte à defaussser 0 - 6 : "))
        while not(n<7 and n>=0):
            print("Erreur: numero de carte errone")
            n=int(input("choisissez une carte à defaussser 0 - 6 : "))
        card=self.tabPlayers[self.currentPlayer].hand.cardList[n]
        self.tabPlayers[self.currentPlayer].hand.removeCard(card)
        self.garbageDeck.addCard(card)
        print(f"vous defaussez la carte {card} !")

    #méthode permettant de joueur une carte
    def playCard(self):
        played = False
        coupFourre = False
        cardCoupFourre = None
        n=int(input("Que souhaitez vous faire (0 - 8) ? "))
        while not(n<9 and n>=0):
            print("Erreur: numero de carte errone")
            n=int(input("Que souhaitez vous faire (0 - 8) ? "))
        if n == 7 : 
            self.throwCard() #Carte déffaussée
            return True
        elif n == 8:
            self.help() #Carte mémo (help)
            print(f"C'est a Joueur {self.tabPlayers[self.currentPlayer]} de jouer :")

            return False
        else:  #Utilisation d'une des cartes
            card=self.tabPlayers[self.currentPlayer].hand.cardList[n]
            
            if isinstance(card,Attack) : 
                victimNumber=self.attackPlayer() #Appelle de la méthode du choix de la victime 
                victim=self.tabPlayers[victimNumber] 
                played,coupFourre,cardCoupFourre = card.useCard(victim) #Appelle de la méthode d'utilsation de la carte de Card
            else :
                played = card.useCard(self.tabPlayers[self.currentPlayer]) #Appelle de la méthode d'utilsation de la carte de Card

            if played: #On enleve la carte si elle a été jouée 
                self.tabPlayers[self.currentPlayer].hand.removeCard(card) 
            
            if (self.end==False and isinstance(card,Safety)): #On rejoue si la carte est une safety et qu'il reste encore des cartes 
                played=False
                self.drawCard()
                print()
                print(f"C'est a Joueur {self.tabPlayers[self.currentPlayer]} de rejouer :")
            
            if coupFourre :
                self.coupFourre(victim,victimNumber,cardCoupFourre) #appelle de la méthode coup fourré

        return played

    #méthode de gestion du coup fourré
    def coupFourre(self,victim,victimNumber,cardCoupFourre):
        print()
        print("--------------------------------")
        print(f"Joueur {victim}, Vous venez de vous faire attaque !!! ")    
        n=int(input(f"Vous possedez la carte {cardCoupFourre}, voulez vous faire un coup fourré ? (0 : Oui | 1 : Non) "))
        while(n!=0 and n!=1) :
            n=int(input(f"Vous possedez la carte {cardCoupFourre}, voulez vous faire un coup fourré ? (0 : Oui | 1 : Non) "))
        if n==0 :
            #le victime joue la carte botte
            cardCoupFourre.useCard(victim)
            victim.hand.removeCard(cardCoupFourre)
            #le joueur victime rejoue le prochain tour 
            self.currentPlayer=victimNumber
            self.drawCard()

            self.currentPlayer=victimNumber-1   

        print()

    #méthode permettant de choisir une victime
    def attackPlayer(self):
        A=0
        print()
        #afficher les joueurs a attaquer
        for i in range(self.numberPlayer):
            if(i == self.currentPlayer):
                i+=1
            elif(i != self.currentPlayer):
                print(f"{A}: {self.tabPlayers[i]}")
                A+=1
        
        victimNumber=int(input(f"Quelle joueur voulez vous attaquer (0 - {self.numberPlayer-2}) ? "))
        while not(victimNumber<self.numberPlayer-1 and victimNumber>=0):
            print("Erreur: mauvais numero de joueur")
            victimNumber=int(input(f"Quelle joueur voulez vous attaquer (0 - {self.numberPlayer-2}) ? "))
        
        if(victimNumber<self.currentPlayer):
            return victimNumber
        else: 
            return victimNumber+1 

    #méthode de gestion d'un tour pour un joueur
    def playTurn(self):
        played=False
        self.drawCard()
        print(f"C'est a Joueur {self.tabPlayers[self.currentPlayer]} de jouer :")
        while not played:
            print(self.tabPlayers[self.currentPlayer].hand)
            print("7: Defausser une carte")
            print("8: Afficher carte memo (help)\n")
            played=self.playCard()
            print()
            #si le joueur dépasse 1000 bornes
        if(self.tabPlayers[self.currentPlayer].distance==1000):
            self.end=True
            self.winner=self.tabPlayers[self.currentPlayer]

    #méthode de gestion d'un tour complet
    def playRound(self):
        print(f"--------------- Round {self.rounds} ---------------")
        #possibilité de sauvegarder la partie chaque tour
        x=int(input("Interrompre partie et sauvegarder ? (0 : Oui | 1 : Non) "))
        while (x!=0 and x!=1):
            x=int(input("Interrompre partie et sauvegarder ? (0 : Oui | 1 : Non) "))
        print()
        if(x==0):
            self.saveGame()
        #jouer un tour complet
        while (self.currentPlayer<self.numberPlayer):
            self.playTurn()
            self.currentPlayer+=1
            if(self.end):
                self.endGame()
        self.currentPlayer=0

    #méthode de gestion de la partie
    def playGame(self):
        print("--------------------------------")
        for p in self.tabPlayers:
            print(p)
        print("\nC'est parti ! ") 
        #tant que la partie n'est pas finie 
        while not(self.end) :
            self.playRound()
            self.rounds+=1
    
    #méthode de fin de partie
    def endGame(self):

        #Classement des joueur

        for i in range(self.numberPlayer):
            maxIndex=i
            for j in range(i+1,self.numberPlayer):
                if self.tabPlayers[i].distance< self.tabPlayers[j].distance:
                    maxIndex=j
            self.tabPlayers[i],self.tabPlayers[maxIndex]=self.tabPlayers[maxIndex],self.tabPlayers[i]

        fin=f"Joueur {self.winner} a gagne apres {self.rounds} tours!\n"
        fin+="Voici le classement des joueurs:\n"
        for i in range(self.numberPlayer):
            fin+=f"{i+1} - Joueur {self.tabPlayers[i]}\n"
        print(fin)
        exit()



    #méthode help permetant d'afficher l'aide
    def help(self):
        print("Carte memo:")
        print("-----------------------------------------------------------------------------")
        print("Cartes Bornes:")
        print("Ces cartes vous permettent d’avancer. Le nombre indiqué dessus représente les kilomètres à parcourir." )
        print("-----------------------------------------------------------------------------")
        print("Cartes attaque:")
        print("Limite de vitesse: Cette carte empêche de poser des cartes Bornes supérieures à 50 km")
        print("Feu Rouge: Cette carte empêche de poser de nouvelles cartes Bornes.")
        print("Panne d essence: Cette carte empêche de poser de nouvelles cartes Bornes.")
        print("Crevaison: Cette carte empêche de poser de nouvelles cartes Bornes.")
        print("Accident: Cette carte empêche de poser de nouvelles cartes Bornes." )        
        print("-----------------------------------------------------------------------------")
        print("Cartes Defense: ")
        print("Fin de limite de vitesse: Cette carte annule l effet de la carte attaque limite de vitesse")
        print("Feu Vert: Cette carte permet de commencer la course et annule l'effet de la carte attaque feu rouge")
        print("Essence: Cette carte annule l effet de la carte attaque panne d essence")
        print("Roue de secours: Cette carte annule l effet de la carte attaque Crevaison")
        print("Reparations: Cette carte annule l effet de la carte attaque Accident" )
        print("-----------------------------------------------------------------------------")
        print("Cartes Bottes: ")
        print("Increvable: vos adversaires ne peuvent plus vous attaquer avec une carte Crevaison.")
        print("Citerne d essence: vos adversaires ne peuvent plus vous attaquer avec une carte Panne d’Essence.")
        print("As du volant: vos adversaires ne peuvent plus vous attaquer avec une carte Accident.")
        print("Vehicule prioritaire: vos adversaires ne peuvent plus vous attaquer avec une carte Feu Rouge ni avec une carte Limite de Vitesse.")
        print("-----------------------------------------------------------------------------")

    #méthode de sauvegarde de la partie
    def saveGame(self):
        fichierName=input("Veuillez saisir un nom de sauvegarde ! ")
        fichier=open(f'{fichierName}.txt','w')
        fichier.write(self.save())
        for p in self.tabPlayers:
           fichier.write(p.save())
        fichier.close()
        print(f"Partie sauvegarde avec succes avec le nom de sauvegarde {fichierName}")
        print("A bientot !")
        exit()

    #méthode de sauvegarde des attribus de la classe Game
    def save(self):
        msg=""
        msg=f"{self.numberPlayer}"
        msg+=f" {self.rounds}"
        msg+=self.gameDeck.save()
        msg+=self.garbageDeck.save()
        return msg+"\n"
    
    #méthode de chargement de la partie
    def loadGame(self):
        fichierName=input("Veuillez saisir le nom de sauvegarde ")
        fichier=open(f'{fichierName}.txt','r')
        gameLoad=fichier.readline()[0:-1]
        gameLoad=gameLoad.split(' ')
        numberPlayer = int(gameLoad[0])
        playersLoad=[[] for _ in range(numberPlayer)]
        for i in range(numberPlayer):
            playersLoad[i]=fichier.readline()[0:-1]
            playersLoad[i]=playersLoad[i].split(' ')
        
        self.load(gameLoad,playersLoad)
        fichier.close()

        print(f"Partie charge avec succes avec le nom de sauvegarde {fichierName}")

    #méthode de chargement des attribus de la classe Game
    def load(self,gameLoad,playersLoad):
        i=0
        numberPlayer = int(gameLoad[i]);i+=1
        rounds = int(gameLoad[i]);i+=1

        if(int(gameLoad[i])>0):
            i+=1
            gameDeckIDstring=gameLoad[i];i+=1
            gameDeckTYPEstring=gameLoad[i]
            gameId,gameType=[],[]
            for x,y in zip(gameDeckIDstring,gameDeckTYPEstring):
                gameId.append(int(x))
                gameType.append(int(y))   
            gameDeck=Deck(gameType,gameId) 
        else:
            gameDeck=Deck()  
        
        i+=1

        if(int(gameLoad[i])>0):
            i+=1
            garbageDeckIdString=gameLoad[i];i+=1
            garbageDeckyTpeString=gameLoad[i]
            garbageId,garbageType=[],[]
            for x,y in zip(garbageDeckIdString,garbageDeckyTpeString):
                garbageId.append(int(x))
                garbageType.append(int(y))    
            garbageDeck=Deck(garbageType,garbageId)
        else:
            garbageDeck=Deck()


        tabPlayer=[]
        for i in range(numberPlayer): 
            tabPlayer.append(Player(playersLoad[i][0]))

        self.numberPlayer=numberPlayer
        self.tabPlayers=tabPlayer
        self.rounds=rounds
        self.gameDeck=gameDeck
        self.garbageDeck=garbageDeck

        for i in range(self.numberPlayer):
            self.tabPlayers[i].load(playersLoad[i])

        
        
