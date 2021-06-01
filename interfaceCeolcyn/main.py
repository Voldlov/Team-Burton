from tkinter import *

#Création de la fenêtre
fenetre = Tk()

#texte d'intro
label = Label(fenetre, text="Ceolcyn")
label.pack()

#bouton pour fermer le jeu
bouton=Button(fenetre, text="sortir", command=fenetre.quit)
bouton.pack()

#bouton pour rentrer dans le jeu
bouton=Button(fenetre, text="entrer")
bouton.pack()

#ouverture de la fenêtre
fenetre.mainloop()