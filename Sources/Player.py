from abc import ABC, abstractmethod
from Card import Card,Distance,Safety,Attack,Defense
from Deck import Deck
from Board import Board
from random import randint

class Player() :
    def __init__(self,name):
        self.name=name          #nom du joueur
        
        self.played200=0        #nombre de fois la carte hirondelle est jouée
        self.distance=0         #distance du joueur(score)
        self.maxSpeed=200       #vitesse maximale du joueur

        self.hand=Deck()        #la main du joueur de type Deck
        self.board=Board()      #table du jeu du joueur de type Board

        self.canMove=False      #boolean qui indique si le joueur peut bouger
        #des attribut des cartes bottes : True si le joueur a joué la carte botte correspondante, False sinon
        self.drivingAce=False
        self.fuelTank=False
        self.punctureProof=False
        self.emergencyVehicle=False
    

    # getters et setters des attributs privés
    
    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self,value):
        if type(value) != int: 
            print("Erreur : distance prend un type int")
        elif value<0:
            print("Erreur : distance ne peux etre négative")
        else :
            self.__distance=value
    
    @property
    def maxSpeed(self):
        return self.__maxSpeed
    
    @maxSpeed.setter
    def maxSpeed(self,value):
        if type(value) != int: 
            print("Erreur : maxSpeed prend un type int")
        elif value<0:
            print("Erreur : maxSpeed ne peux etre négative")
        else :
            self.__maxSpeed=value

    @property
    def canMove(self):
        return self.__canMove
    @canMove.setter
    def canMove(self,value):
        if type(value) != bool: 
            print("Erreur : canMove prend un type Booleen")
        else :
            self.__canMove=value

    @property
    def drivingAce(self):
        return self.__drivingAce
    @drivingAce.setter
    def drivingAce(self,value):
        if type(value)!= bool: 
            print("Erreur : drivingAce prend un type Booleen")
        else :
            self.__drivingAce=value   

    @property
    def fuelTank(self):
        return self.__fuelTank
    @fuelTank.setter
    def fuelTank(self,value):
        if type(value)!= bool: 
            print("Erreur : fuelTank prend un type Booleen")
        else :
            self.__fuelTank=value 

    @property
    def punctureProof(self):
        return self.__punctureProof
    @punctureProof.setter
    def punctureProof(self,value):
        if type(value)!= bool: 
            print("Erreur : punctureProof prend un type Booleen")
        else :
            self.__punctureProof=value  

    @property
    def emergencyVehicle(self):
        return self.__emergencyVehicle
    @emergencyVehicle.setter
    def emergencyVehicle(self,value):
        if type(value)!= bool: 
            print("Erreur : emergencyVehicle prend un type Booleen")
        else :
            self.__emergencyVehicle=value

    @property
    def hand(self):
        return self.__hand  
    
    @hand.setter
    def hand(self,deck):
        if not(isinstance(deck,Deck)):
            print("Erreur: hand ne peut prendre qu'une pile de type Deck")
        else :
            self.__hand=deck
    
    @property
    def board(self):
        return self.__board 
    
    @board.setter
    def board(self,board):
        if not(isinstance(board,Board)):
            print("Erreur: board ne peut prendre qu'une pile de type Board")
        else :
            self.__board=board
    
    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self,name):
        if type(name) != str: 
            print("Erreur: name ne peut prendre qu'une chaine de caracteres")
        else :
            self.__name=name

    @property
    def played200(self):
        return self.__played200
    
    @played200.setter
    def played200(self,value):
        if type(value) != int: 
            print("Erreur : played200 prend un type int")
        elif value>2:
            print("Erreur : played200 ne peut pas prendre une valeur >2")
        else :
            self.__played200=value

    def __str__(self):
        msg=self.name
        msg+=f" ({self.distance} km{self.board})"
        return msg
    
    #methode de sauvegarde du joueur
    def save(self):
        msg=f"{self.name}"
        msg+=f" {self.played200}"
        msg+=f" {self.distance}"
        msg+=f" {self.maxSpeed}"
        msg+=f" {self.canMove}"
        msg+=f" {self.drivingAce}"
        msg+=f" {self.fuelTank}"
        msg+=f" {self.punctureProof}"
        msg+=f" {self.emergencyVehicle}"
        msg+=self.hand.save()
        msg+=self.board.save()
        return msg+"\n"
    #méthode de chargement des attribut du joueur       
    def load(self,playersLoad):
        self.played200=int(playersLoad[1])
        self.distance=int(playersLoad[2])
        self.maxSpeed=int(playersLoad[3])
        
        if playersLoad[4] == 'True': self.canMove=True
        else:self.canMove=False
        
        if playersLoad[5] == 'True':self.drivingAce=True
        else: self.drivingAce=False
        
        if playersLoad[6] == 'True': self.fuelTank=True
        else: self.fuelTank=False
        
        if playersLoad[7] == 'True': self.punctureProof=True
        else: self.punctureProof=False
        
        if playersLoad[8] == 'True':self.emergencyVehicle=True
        else:self.emergencyVehicle=False

        handIdString=playersLoad[10]
        handTypeString=playersLoad[11]
        handId,handType=[],[]
        for x,y in zip(handIdString,handTypeString):
            handId.append(int(x))
            handType.append(int(y))    
        self.hand=Deck(handType,handId)
        self.board.load(playersLoad[12:len(playersLoad)])