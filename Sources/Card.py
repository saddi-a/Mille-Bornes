from abc import ABC, abstractmethod

''' le codage des types de cartes (Type)
0 : Distance
1 : Safety
2 : Attack
3 : Defense
'''

#Classe Card 
class Card(ABC):
    def __init__(self,ID,name) :
        self._ID=ID         #ID de chaque type de carte
        self._name=name        #nom de la carte

    # getters et setters des attributs privés
    @property
    def ID(self):
        return self._ID
    @property
    def name(self):
        return self._name
    @ID.setter
    def ID(self,id):
        self._ID=id
    @name.setter
    def name(self,n):
        self._name=n
       
    @abstractmethod
    def __str__(self) :
        pass
    
    #Méthode permettant de jouer une carte
    @abstractmethod
    def useCard(self,player) :
        pass
    
    def __eq__(self,other):
        if not(isinstance(other,Card)): return False
        if self is other : return True
        if other.ID != self.ID: return False            
        
        if other.name != self.name: return False
        else :  return True
    
    #Méthode permettant de récupérer les éléments nécessaires 
    #à la sauvegarde d'une carte lors du sauvegarde d'une partie
    @abstractmethod
    def save(self):
        pass


class Distance(Card):
    def __init__(self,ID):
        self.ID=ID

    @property
    def name(self):
        return self.__name
    @property
    def ID(self):
        return self.__ID
    @property
    def speed(self):
        return self.__speed
        
    @ID.setter
    def ID(self,ID):
        #setter des cartes selon ID
        if(ID==0):self.__ID=ID;self.__name="hirondelle"; self.__speed=200
        elif(ID==1):self.__ID=ID;self.__name="lievre";self.__speed=100
        elif(ID==2):self.__ID=ID;self.__name="papillon";self.__speed=75
        elif(ID==3):self.__ID=ID;self.__name="canard";self.__speed=50
        elif(ID==4):self.__ID=ID;self.__name="escargot";self.__speed=25
        else:
            print("Erreur carte Bornes non existante")


    def __str__(self):
        msg=f"Bornes: {self.name}, {self.speed}"
        return msg
    

    #Méthode permettant de jouer une carte
    def useCard(self,player):
        played=False
        if (player.played200>=2 and self.speed == 200): #Vérification du nombre d'utilisation de la carte 200 bornes
            print(f"Vous avez deja joue 2 fois la carte {Distance(0)}")
            print("Veuillez jouer une autre carte")
        else :
            if player.canMove: #Vérifiaction de la capacité du joueur à se déplacer
                if  (player.board.lastBattle == None) and (player.board.lastSpeed == None) : 
                    if self.speed+player.distance<=1000: #Vérification du non dépassement des 1000 bornes
                        player.distance+=self.speed
                        played=True
                        if (self.speed == 200):
                            #compteur des fois de jeu du carte hirondelle
                            player.played200+=1
                    else:
                        print("Vous ne pouvez pas dépasser les 1000 bornes, Veuillez jouer une autre carte")

                elif (player.board.lastBattle == None) and (player.board.lastSpeed == Attack(3)) : #Le joueur à une limitation de vitesse
                    if self.speed>50:
                        print(f"Vous ne pouvez pas depasser les 50 km/h, vous avez une {player.board.lastSpeed} devant vous!")
                        print("Veuillez jouer une autre carte")
                    else :
                        if self.speed+player.distance<=1000:
                            player.distance+=self.speed
                            played=True
                        else:
                            print("Vous ne pouvez pas dépasser les 1000 bornes, Veuillez jouer une autre carte")
            else :
                print(f"Vous ne pouvez pas avancer, vous avez une carte {player.board.lastBattle} devant vous!")
                print("Veuillez jouer une autre carte")

            if played:
                print(f"Vous avez joue la carte {self} !")
                player.board.speedDeck.addCard(self)
                 
        return played #on retourne True si la carte à été joué, False sinon
    
    def save(self):
        return self.ID,0 #on retourne l'ID et le TYPE de la carte


class Safety(Card):
    def __init__(self,ID):
        self.ID=ID

    @property
    def name(self):
        return self.__name
    @property
    def ID(self):
        return self.__ID   
        
    @ID.setter
    def ID(self,ID):
        #setter des cartes selon ID
        if(ID==0):self.__ID=ID;self.__name="as du volant"
        elif(ID==1):self.__ID=ID;self.__name="increvable"
        elif(ID==2):self.__ID=ID;self.__name="citerne d'essence"
        elif(ID==3):self.__ID=ID;self.__name="vehicule prioritaire"
        else:
            print("Erreur carte Bottes non existante")

    def __str__(self):
        msg=f"Botte: {self.name}"
        return msg
    
    
    def useCard(self,player):
        if(self.ID==0): #Carte As du volant
            player.drivingAce=True 
            if(player.board.lastBattle == Attack(0)):
                player.board.lastBattle=None
                player.canMove=True
                if(player.board.lastSpeed == None):
                    player.maxSpeed=200
                else :
                    player.maxSpeed=50
        elif(self.ID==1): #Carte anti crevaison
            player.punctureProof=True
            if(player.board.lastBattle == Attack(1)):
                player.board.lastBattle = None
                player.canMove=True
                if(player.board.lastSpeed == None):
                    player.maxSpeed=200
                else :
                    player.maxSpeed=50
        elif(self.ID==2): #Carte citerne d'essence
            player.fuelTank=True 
            if(player.board.lastBattle == Attack(2)):
                player.board.lastBattle = None
                player.canMove=True
                if(player.board.lastSpeed == None):
                    player.maxSpeed=200
                else :
                    player.maxSpeed=50        
        elif(self.ID==3): #carte véhicule prioritaire
            player.emergencyVehicle=True
            player.board.lastSpeed=None
            if((player.board.lastBattle == None) or (player.board.lastBattle == Attack(4))):
                player.board.lastBattle = None
                player.canMove = True 
                player.maxSpeed = 200
        else:
            print("Erreur carte Botte non existante")
            return False
        
        player.board.safetyDeck.addCard(self)
        print(f"Vous avez jouer la carte {Safety(self.ID)} ! ")
        return True #on retourne True si la carte à été joué, False sinon

    def save(self):
        return self.ID,1 #on retourne l'ID et le TYPE de la carte

class Attack(Card):
    def __init__(self,ID):
        self.ID=ID
    
    @property
    def name(self):
        return self.__name
    @property
    def ID(self):
        return self.__ID   
        
    @ID.setter
    def ID(self,ID):
        #setter des cartes selon ID
        if(ID==0):self.__ID=ID;self.__name="Accident"
        elif(ID==1):self.__ID=ID;self.__name="Crevaison"
        elif(ID==2):self.__ID=ID;self.__name="Panne d'essence"
        elif(ID==3):self.__ID=ID;self.__name="Limite de vitesse"
        elif(ID==4):self.__ID=ID;self.__name="Feu rouge"
        else:
            print("Erreur carte Attack non existante")
   

    def __str__(self):
        msg=f"Attaque: {self.name}"
        return msg

    def useCard(self,victim):
        played = False
        coupFourre=False
        cardCoupFourre=None
        if(self.ID==0):
            #si le joueur ne dispose d'une carte botte opposante dans sa pile de botte
            if not victim.drivingAce :
                if victim.board.lastBattle == None : played = True
                else : print(f"Vous ne pouvez pas attaquer {victim} dans sa pille de bataille avec une carte {self}, Il est déja attaque")
            else : print(f"Vous ne pouvez pas attaquer {victim} dans sa pille de bataille avec une carte {self}, il a une {Safety(0)} ")
        if(self.ID==1):
            #si le joueur ne dispose d'une carte botte opposante dans sa pile de botte
            if not victim.punctureProof :
                #si le joueur n'est pas déja attaqué
                if victim.board.lastBattle == None : played = True
                else : print(f"Vous ne pouvez pas attaquer {victim} dans sa pille de bataille avec une carte {self}, Il est déja attaque")
            else : print(f"Vous ne pouvez pas attaquer {victim} dans sa pille de bataille avec une carte {self}, il a une {Safety(1)} ")
        if(self.ID==2):
            #si le joueur ne dispose d'une carte botte opposante dans sa pile de botte
            if not victim.fuelTank :
                #si le joueur n'est pas déja attaqué
                if victim.board.lastBattle == None : played = True
                else : print(f"Vous ne pouvez pas attaquer {victim} dans sa pille de bataille avec une carte {self}, Il est déja attaque")
            else : print(f"Vous ne pouvez pas attaquer {victim} dans sa pille de bataille avec une carte {self}, il a une {Safety(2)} ")
        if(self.ID==4):
            #si le joueur ne dispose d'une carte botte opposante dans sa pile de botte
            if not victim.emergencyVehicle :
                #si le joueur n'est pas déja attaqué
                if victim.board.lastBattle == None :
                    played = True
                else : print(f"Vous ne pouvez pas attaquer {victim} dans sa pille de bataille avec une carte {self}, Il est déja attaque")
            else : print(f"Vous ne pouvez pas attaquer {victim} dans sa pille de bataille avec une carte {self}, il a une {Safety(3)} ")
        if(self.ID==3):
            #si le joueur ne dispose d'une carte botte opposante dans sa pile de botte
            if not victim.emergencyVehicle :
                #si le joueur n'est pas déja attaqué
                if victim.board.lastSpeed == None :
                    played = True
                else :
                    print(f"Vous ne pouvez pas attaquer {victim} dans sa pille de vitesse avec une carte {self}, Il est déja attaque")
            else :
                print(f"Vous ne pouvez pas attaquer {victim} dans sa pille de bataille avec une carte {self}, il a une {Safety(3)} ")

        #si la carte est jouée
        if(played):
            #si carte differnte de limite de vitesse
            if (self.ID != 3):
                victim.maxSpeed=0
                victim.canMove=False
                victim.board.battleDeck.addCard(self)
                #ajouter la carte a la pile de bataille 
                victim.board.lastBattle = self
                print(f"Vous avez attaque {victim} dans sa pille de bataille avec une carte {self}")
            #sinon
            else:
                if (victim.board.lastBattle == None):
                    victim.maxSpeed=50
                    victim.canMove=True
                victim.board.speedDeck.addCard(self)
                #ajouter la carte a la pile de vitesse
                victim.board.lastSpeed = self
                print(f"Vous avez attaque {victim} dans sa pille de vitesse avec une carte {self}")
            #si carte differnte de feu rouge  
            if self.ID!=4 :
                #parcourir les cartes dans la main du joueur victim
                for c in victim.hand.cardList:
                    #si il possede la carte botte opposante
                    if c == Safety(self.ID):
                        coupFourre=True
                        cardCoupFourre=c
            else :
                for c in victim.hand.cardList:
                    #si il possede la carte botte opposante
                    if c == Safety(3):
                        coupFourre=True
                        cardCoupFourre=c
        else:
            print("Veuillez jouer une autre carte")
        return played,coupFourre,cardCoupFourre


    def save(self):
        return self.ID,2 #on retourne l'ID et le TYPE de la carte

class Defense(Card):
    def __init__(self,ID):
        self.ID=ID          #ID de carte du type defense
    
    @property
    def name(self):
        return self.__name
    @property
    def ID(self):
        return self.__ID   
        
    @ID.setter
    def ID(self,ID):
        #creation des attribut selon ID
        if(ID==0):self.__ID=ID;self.__name="Reparations"
        elif(ID==1):self.__ID=ID;self.__name="Roue de secours"
        elif(ID==2):self.__ID=ID;self.__name="Essence"
        elif(ID==3):self.__ID=ID;self.__name="Fin de limite de vitesse"
        elif(ID==4):self.__ID=ID;self.__name="Feu vert"
        else:
            print("Erreur carte Defense non existante")
   
    def __str__(self):
        msg=f"Parade: {self.name}"

        return msg
    
    def useCard(self,player):
        played=False
        played2=False
    #verifier si le joueur est attaqué avec la carte opposé a la carte defense posée
        if(self.ID==0) and (player.board.lastBattle == Attack(0)) :
            played=True
        elif(self.ID==1) and (player.board.lastBattle == Attack(1)) :
            played=True
        elif(self.ID==2) and (player.board.lastBattle == Attack(2)) :
            played=True
        elif(self.ID==4) and (player.board.lastBattle == Attack(4)) :
            played=True
        elif (self.ID==3) and (player.board.lastSpeed == Attack(3)):
            played2=True
        elif(self.ID == 0 or self.ID ==1 or self.ID ==2 or self.ID==4) and (player.board.lastBattle == None):
            print("veuillez jouer une autre carte, attaque correspondante non-existante")
        elif(self.ID==3) and (player.board.lastSpeed == None):
            print("veuillez jouer une autre carte, attaque correspondante non-existante")
        else:
            print("veuillez jouer une autre carte, attaque correspondante non-existante")

        if played:
            player.board.battleDeck.addCard(self)
            player.board.lastBattle = None
            player.canMove=True 
            print(f"Vous avez joue la carte {self}, vous avez annule l effet de  {Attack(self.ID)}!")
            #si il n est pas limité en vitesse
            if player.board.lastSpeed == None:
                player.maxSpeed=200   
            #sinon
            else :
                player.maxSpeed=50 
            return True
        if played2:
            player.board.speedDeck.addCard(self)
            player.board.lastSpeed = None
            player.canMove=True 
            print(f"Vous avez joue la carte {self} ,vous avez annule l effet de  {Attack(self.ID)}! ")

            #si il n'est pas attaqué
            if player.board.lastBattle == None:
                player.maxSpeed=50   
            else :
                player.maxSpeed=0 
            return True #on retourne True si la carte à été joué, False sinon

        return False 

    def save(self):
        return self.ID,3 #on retourne l'ID et le TYPE de la carte