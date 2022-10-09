from tkinter import filedialog
import numpy as np

#vérifie les contraintes du tableau
def contraintes(grid,Possible_value, y,x) :
    if Possible_value in grid[y]:
            return False
    for i in range(9):
        if Possible_value == grid[i][x]:
            return False
    x=x-(x%3)
    y=y-(y%3)
    for i in range(3):
        for j in range(3):
                if grid[y+j][x+i]==Possible_value:
                    return False
    return True


#permet l'affichage de la grille
def sudoku_grid(grid):
    for i in range(9):
        if (i%3==0 and i!=0):
            print("- "*15)
        for j in range(9):
            if(j%3==0 and j!=0):
                print("| ",end="")
                print(str(grid[i][j])," ", end="")
            else:
                print(str(grid[i][j])," ", end="")
        print('')
        

#permet de définir le dictionnaire de domaines pour chaque position où l'on pourra ajouter une valeur
def domaines(grid,dictionnaire_yx) :
    for y in range(9):
        for x in range(9):
            if grid[y][x]==0:
                domaine=[i for i in range(1,10)]
                for Possible_value in grid[y]:
                    if Possible_value!=0:
                        domaine.remove(Possible_value)
                for Possible_value in domaine:    
                    for i in range(9):
                        if Possible_value==grid[i][x] and Possible_value!=0 :
                            domaine.remove(Possible_value)
                for Possible_value in domaine:
                    x1=x-(x%3)
                    y1=y-(y%3)
                    for i in range(3):
                        for j in range(3):
                                if grid[y1+j][x1+i]==Possible_value and Possible_value!=0:
                                    domaine.remove(Possible_value) 
                dictionnaire_yx[(y,x)]=domaine
    return dictionnaire_yx


#permet de déterminer la position avec le plus petit domaine
def mrv(dictionnaire_xy):
    mini=10
    #y,x=list(dictionnaire_xy.keys())[0]
    for key in dictionnaire_xy.keys():
        if len(dictionnaire_xy[key])<mini:
            mini=len(dictionnaire_xy[key])
            a=key
    if len(dictionnaire_xy)>0:
        return a
    else:
        return -1,-1
    
 
#permet d'effectuer le backtracking   
def solution(grid,dictionnaire_yx):
    dico=domaines(grid,dictionnaire_yx)
    y,x=mrv(dico)
    if len(dico)<=0 : 
        return grid
    domaine=dico[(y,x)]
    for Possible_value in domaine:
        if contraintes(grid,Possible_value,y,x):
            grid[y][x]=Possible_value
            del dico[(y,x)]
            #print("taille=",len(dico),"y=",y,"x=",x, Possible_value)
            #sudoku_grid(grid)
            if solution(grid,dico):
                return grid
        grid[y][x]=0
        dico[(y,x)]=Possible_value
    return False



