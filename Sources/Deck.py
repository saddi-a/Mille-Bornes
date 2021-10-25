from Card import Card,Distance,Safety,Attack,Defense

''' le codage des types de cartes (Type)
0 : Distance
1 : Safety
2 : Attack
3 : Defense
'''

class Deck():
    def __init__(self,cardType=[],ID=[]):
        self.cardsNumber=len(ID)        #attribut de nombre de cartes dans une pille
        self.cardList=[cardType,ID]        #liste des cartes dans la pille
   
    # getters et setters des attributs privés
   
    @property
    def cardsNumber(self):
        return self.__cardsNumber

    @cardsNumber.setter
    def cardsNumber(self,cardsNumber):
        if type (cardsNumber) == int:
                if (cardsNumber<=106):
                    self.__cardsNumber=cardsNumber
                else:
                    print("Erreur : il ne peut pas y avoir plus de 106 cartes")
                    self.__cardsNumber=cardsNumber
        else:
            print("Erreur: cardsNumber prend un type Entier")

    @property
    def cardList(self):
        return self.__cardList

    @cardList.setter
    def cardList(self,cardTypeID=[[],[]]):
        cardType,ID=cardTypeID[0],cardTypeID[1]
        cardList=[]
        for i in range (self.cardsNumber) :
            if(cardType[i]==0):# 0 Distance
                cardList.append(Distance(ID[i]))
            elif(cardType[i]==1):# 1 Safety
                cardList.append(Safety(ID[i]))
            elif(cardType[i]==2): # 2 Attack
                cardList.append(Attack(ID[i]))
            elif(cardType[i]==3): # 3 Defense
                cardList.append(Defense(ID[i]))
            else:
                print (f"Erreur Type {i} non existant")
            
        self.__cardList=cardList


    def __str__(self):
        msg = ""
        for i in range(self.cardsNumber):
            msg += f"{i}: {str(self.cardList[i])}\n"
        
        return msg[0:len(msg)-1]


    #Méthode d'ajout d'une carte dans un Deck 
    def addCard(self,card):
        if isinstance(card,Card) :
            self.cardList.append(card)
        else:
            print (f"Erreur d'ajout de carte")

        self.cardsNumber=len(self.cardList)

    #Méthode de retrait d'une carte dans un Deck 
    def removeCard(self,card):
        remove=False
        #si la carte existe dans la pille
        for c in self.cardList:
            if card == c and not(remove):
                self.cardList.remove(c)
                self.cardsNumber=len(self.cardList)
                remove=True
        #sinon
        if not(remove):
            print ("Erreur de retrait de carte : carte non existante")
    
    #méthode de sauvegarde des attribue de Deck
    def save(self):
        if(self.cardsNumber == 0):
            return " 0"
        ID,TYPE='',''
        msg=f" {self.cardsNumber} "
        for c in self.cardList:
            a,b=c.save()
            ID+=str(a)
            TYPE+=str(b)
        msg+= ID +" " +TYPE
        return msg


    def __eq__(self,other):
        if not(isinstance(other,Deck)): return False
        if self is other : return True
        if other.cardsNumber != self.cardsNumber: return False            
        
        for a,b in zip(self.cardList,other.cardList):
            if a!= b :return False
        else :  return True