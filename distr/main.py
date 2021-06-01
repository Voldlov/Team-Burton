from tkinter import *

#Création de la fenêtre
fenetre = Tk()

#couleur de fond
fenetre['bg']='grey'

#titre de la fenêtre
fenetre.title("ceolcyn")
#taille de la fenêtre
fenetre.geometry("1000x900")
#icone
fenetre.iconbitmap("Ceolcyn_Dragon_1.ico")

#texte d'intro
label = Label(fenetre, text="Ceolcyn").pack()

cadre = Frame(fenetre).pack(side=BOTTOM,padx=10,pady=10)

#bouton pour fermer le jeu
bouton=Button(cadre, text="sortir", relief=RIDGE, command=fenetre.quit,cursor="pirate").pack(side=RIGHT)

#bouton pour rentrer dans le jeu
bouton=Button(cadre, text="entrer", relief=RIDGE).pack(side=LEFT)

#ouverture de la fenêtre
fenetre.mainloop()