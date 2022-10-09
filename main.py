from backtracking import *
import numpy as np
if __name__ == '__main__':
    print("souhaitez vous : \n1-Générer un tableau Sudoku automatiquement\n2- Générer un tableau à partir d'un fichier .txt")
    choice=int(input("votre choix :"))
    while choice!=1 and choice!=2:
        print("souhaitez vous : \n1-Générer un tableau Sudoku automatiquement\n2- Générer un tableau à partir d'un fichier .txt")
        choice=int(input("votre choix :"))
    if choice==1:
        base=3
        side=base*base

        # pattern for a baseline valid solution
        def pattern(r,c): return (base*(r%base)+r//base+c)%side

        # randomize rows, columns and numbers (of valid base pattern)
        from random import sample
        def shuffle(s): return sample(s,len(s)) 
        rBase = range(base) 
        rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1,base*base+1))

        # produce board using randomized baseline pattern
        grid= [ [nums[pattern(r,c)] for c in cols] for r in rows ]

        squares = side*side
        empties = squares * 3//4
        for p in sample(range(squares),empties):
            grid[p//side][p%side] = 0
    
    if choice==2:
        grid=[]
        file=filedialog.askopenfilename(initialdir="/", title="select a file",filetypes=[("text file","*.txt")])
        file=open(file,"r")
        lines=file.read().splitlines()
        print()
        for line in lines:
            grid.extend(line.split())
        for i in range(len(grid)):
            grid[i]=list(grid[i])
        for j in range(len(grid)):
            for i in range(len(grid)):
                grid[j][i]=int(grid[j][i])
    
    dico={}
    dico=domaines(grid,dico)
    print("la grille initiale")
    sudoku_grid(grid)
    grid=solution(grid,dico)
    print("\n la grille finale")
    sudoku_grid(grid)