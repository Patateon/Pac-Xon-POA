import numpy as np
from enum import Enum


class Grid:

    def __init__(self, nX, nY, tr):
        self.nX = nX
        self.nY = nY
        self.grid = np.zeros((nX,nY))
        self.endGame = False #variable que l'on donne pour savoir si la partie est finie
        self.tr = tr#taux remplissage requis pour victoire
        self.endPath=False#variable que le code de pacman pourra changer
    

    def initGrid(self):
        self.grid[0,:]=1
        self.grid[:,0]=1
        self.grid[-1,:]=1
        self.grid[:,-1]=1

    def getSize(self):
        return [self.nX, self.nY]

    def getValue(self, x, y):
        return self.grid[x, y]

    def setValue(self, x, y, v):
        self.grid[x,y]=v

    def getEndGame(self): 
        return self.endGame

    def setEndGame(self, value:bool): 
        self.endGame = value

    def setEndPath(self,value:bool) :#accesseur pour pacman quand il atteint un 1 apres avoir commencer a former chemin(trouve un 1 après avoir mis un 2 position précédente)
        self.endPath=value
 
    
    def update(self,x,y,x2,y2):
        end=False
        traite=np.array([[x, y]]) #On initialise traite avec la position du ghost x,y
        for i in range (self.nX) : 
            for j in range (self.nY) : 
                if(self.getValue(i,j)==4) :
                    self.setValue(i,j,0)
        self.setValue(x,y,4)
        self.setValue(x2,y2,4)
        #On lui donne sa valeur
        
        if(self.endPath==True) :
            self.setValue(x, y, 6)
            self.endPath=False
            while not end:
                aTraite=[]  #On prépare les nouveaux points a traiter
                for i in range(traite.shape[0]):
                    tx, ty = traite[i]
                    # Ca c'est vraiment smart pour pas avoir 4 boucles et ouais
                    dx = [0, 0, -1, 1]
                    dy = [-1, 1, 0, 0]
                    for j in range(4):#On propage de 1 de chaque coté
                        new_tx, new_ty = tx + dx[j], ty + dy[j]
                        if (0 <= new_tx < self.nX and 0 <= new_ty < self.nY and self.getValue(new_tx, new_ty) not in [1, 2, 3, 6]):#On vérifié si l'on depasse les bords et si la valeur ne veut pas dire qu'on peut plus propager
                            self.setValue(new_tx, new_ty, 6)
                            aTraite.append([new_tx, new_ty])

                if (len(aTraite)==0) : #Si aTraite est toujours vide c'est que c'est fini
                    end=True  
                else:
                    traite=np.array(aTraite)  #On ajoute les points a traiter dans ce que l'on traite pour la prochaine boucle
            #Une fois que l'on a traité le premier ghost il faut traiter le second , pour cela on va tout simplement regarder si il est a un endroit qui vaut 6 si c'est le cas on à rien de spécial a faire
            if(self.getValue(x2,y2)!=6) :
                #même méthode mais on remplira avec 7 la zone du second ghost qui n'es pas la même que celle du premier
                end=False
                traite=np.array([[x2, y2]]) #On initialise traite avec la position du ghost x,y

                #On lui donne sa valeur
                self.setValue(x2, y2, 7)
                while not end:
                    aTraite=[]  #On prépare les nouveaux points a traiter
                    for i in range(traite.shape[0]):
                        tx, ty = traite[i]
                        # Ca c'est vraiment smart pour pas avoir 4 boucles et ouais
                        dx = [0, 0, -1, 1]
                        dy = [-1, 1, 0, 0]
                        for j in range(4):#On propage de 1 de chaque coté
                            new_tx, new_ty = tx + dx[j], ty + dy[j]
                            if (0 <= new_tx < self.nX and 0 <= new_ty < self.nY and self.getValue(new_tx, new_ty) not in [1, 2, 3, 7]):#On vérifié si l'on depasse les bords et si la valeur ne veut pas dire qu'on peut plus propager
                                self.setValue(new_tx, new_ty, 7)
                                aTraite.append([new_tx, new_ty])

                    if (len(aTraite)==0) : #Si aTraite est toujours vide c'est que c'est fini
                        end=True  
                    else:
                        traite=np.array(aTraite)  #On ajoute les points a traiter dans ce que l'on traite pour la prochaine boucle
                    
                   

            #Il nous reste à changer les valeurs de la grille en la traversant
            for i in range(self.nX) :
                for j in range(self.nY) :
                    if(self.getValue(i,j)==0 or self.getValue(i,j)==2 or self.getValue(i,j) == 3) : 
                        self.setValue(i,j,1)
                    if(self.getValue(i,j)==6 or self.getValue(i,j)==7) :
                        self.setValue(i,j,0)


            c = np.sum(self.grid[self.grid==1])-(2*self.nX+2*self.nY-4)
            
            # c=0#comptage du nombre de 1 pour taux de remplissage
            # for i in range(1,self.nX-1,1) :
            #     for j in range(1,self.nY-1,1) :
            #         if(self.getValue(i,j)==1) :
            #             c+=1
            if(c/((self.nX-2)*(self.nY-2))>self.tr) :#test du taux de remplissage
                self.setEndGame(True)
            print("taux de remplissage actuel : "+str(c/((self.nX-2)*(self.nY-2))))
            print("taux remplissage requis : " + str(self.tr))
            

    def propagation(self):
        redPoint = np.where(self.grid==3)
        for i in range(redPoint[0].shape[0]):
            self.propage(redPoint[0][i], redPoint[1][i])

    def propage(self, x, y):
        if (self.getValue(x-1, y)==2):
            self.setValue(x-1, y, 3)
        if (self.getValue(x, y-1)==2):
            self.setValue(x, y-1, 3)
        if (self.getValue(x+1, y)==2):
            self.setValue(x+1, y, 3)
        if (self.getValue(x, y+1)==2):
            self.setValue(x, y+1, 3)
            
        
