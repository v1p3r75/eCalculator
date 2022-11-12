#coding:utf-8
#Script Name : Calculator
#Author : Elfried (Viper75)
#Version : 1.0.0
#Downloads : www.elfriedworks.go.yo.fr


from tkinter import *
from tkinter.messagebox import *
import sys

#if sys.platform != "win32":
#	showinfo("Error !","Ce programme ne peut pas s'éxecuter correctement sur une machine différentes de windows x ")

#Fonction qui gère le calcul....

def gerer(exp, *args):
	global tableau
	global expression
	global history,history_expression, history_ajou
	if len(expression) < 30:
		if exp == "=":
			try:
				resultat = eval(expression)
				history_expression = expression
				tableau.set(resultat)
				expression = str(resultat)
				history_ajou = history_expression,resultat
				if history_ajou == history[-1]:
					pass
				else:
					history.append(history_ajou)

			except NameError:
				expression = "Erreur !"
				tableau.set(expression)
				expression = ""
			except SyntaxError:
				expression = "Erreur de Syntaxe"
				tableau.set(expression)
				expression = ""
		elif exp == "moins":
			expression = expression[:-1]
			resultat = expression
			tableau.set(resultat)
		else:
			expression += str(exp)
			tableau.set(expression)
	else:
		tableau.set("Dépassement de la capacité")
		
#Fonction effacer (clear)
def historique(*args):
	global history
	top = Toplevel()
	top.title("Historique")
	TecranW = int(top.winfo_screenwidth())
	TecranH = int(top.winfo_screenheight())
	Twidth = 280
	Theight = 250
	TposX = (TecranW // 2) - (Twidth // 2)
	TposY = (TecranH // 2) - (Theight // 2)
	Tgeo =  f"{Twidth}x{Theight}+{TposX}+{TposY}"
	top.geometry(Tgeo)
	for i in history:
		j = "{} = {} ".format(i[0],i[1])
		h = Label (
			top,
			text = j,
			font = ("Agency fb",12,"bold"),
			)
		h.pack()
def clear():
	global expression
	expression = ""
	tableau.set(expression)

def infos(*args):
	help = """Nom du logiciel : eCalculator \nAuteur : Elfried (V1P3R 75) \nVersion : 1.0.0 \nSite : github.com/Elfried-Works \nGitHub: ElfriedWorks \nYoutube : ElfriedWorks \nEmail: elfried@works.com"""
	
	showinfo("À propos de eCalculator", help)

def quitter(*args):
        reply = askquestion("Quitter", "Voulez-vous vraiment quitter ?")
        if reply == "yes":
                x.destroy()
        else:
                pass
def touche(event):
	if event.keysym == "Return":
		gerer("=")
	elif event.keysym == "BackSpace":
		gerer("moins")
	elif event.keysym == "c" or event.keysym == "C":
		clear()
	elif event.keysym == "parenlelft":
		gerer("(")
	elif event.keysym == "parenright":
		gerer(")")
	elif event.keysym == "e" or event.keysym == "E":
		gerer("**")
	else:
		gerer(event.char)

def menu():
	menu = Menu(x)

	menu_programs = Menu(menu, tearoff = 0)
	menu_programs.add_command(label = "Convertor")

	menu_aide = Menu(menu, tearoff = 0)
	menu_aide.add_command(label = "Aide en ligne",)
	menu_aide.add_command(label = "A propos", command = infos)

	menu_history = Menu(menu, tearoff = 0)
	menu_history.add_command(label = "Votre historique", command = historique)

	menu.add_cascade(label = "Programmes", menu = menu_programs)
	menu.add_cascade(label = "Historique", menu = menu_history)
	menu.add_cascade(label = "Aide", menu = menu_aide)

	x.config(menu = menu)
x = Tk()
x.title("eCalcultor")
x.resizable(width=False, height=False)
ecranW = int(x.winfo_screenwidth())
ecranH = int(x.winfo_screenheight())
width = 280
height = 430
posX = (ecranW // 2) - (width // 2)
posY = (ecranH // 2) - (height // 2)
geo =  f"{width}x{height}+{posX}+{posY}"
x.geometry(geo)
x.iconbitmap("favicon.ico")

expression = ""
tableau = StringVar() #Variable de controle associèe avec le Label (le tableau d'affichage)
history = [("","")] 
history_expression = ""
history_ajou = ""

text = Label(x, textvariable=tableau,height=3, bg="black", fg="white", font = ("Agency fb",13,"bold"))
text.grid(row=1, column=0, columnspan = 3, sticky="news")
moins = Button(x, text="DEL",fg="white",width=10,height=3, bg="green",command = lambda: gerer("moins"), font = ("Agency fb",11,"bold"))
moins.grid(row=1, column=3, sticky="news")
c = Button(x, text="C",fg="white",width=10,height=2, bg="red",command = lambda:clear(), font = ("Agency fb",11,"bold"))
c.grid(row=2, column=0, sticky="news")
p1 = Button(x, text="(",fg="white",width=10,height=2, bg="blue",command = lambda: gerer("("), font = ("Agency fb",11,"bold"))
p1.grid(row=2, column=1, sticky="news")
p2 = Button(x, text=")",fg="white",width=10,height=2, bg="blue",command = lambda: gerer(")"), font = ("Agency fb",11,"bold"))
p2.grid(row=2, column=2, sticky="news")
p3 = Button(x, text="x^y",fg="white",width=10,height=2, bg="red",command = lambda: gerer("**"), font = ("Agency fb",11,"bold"))
p3.grid(row=2, column=3, sticky="news")
b1 = Button(x,text="1",width=10,height=3, command = lambda:gerer(1), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b1.grid(row=3, column = 0,sticky = "news")
b2 = Button(x,text="2",width=10,height=3, command = lambda: gerer(2), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b2.grid(row=3, column = 1,sticky = "news")
b3 = Button(x,text="3",width=10,height=3, command = lambda: gerer(3), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b3.grid(row=3, column = 2,sticky = "news")
b4 = Button(x,text="4",width=10,height=3, command = lambda: gerer(4), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b4.grid(row=4, column = 0,sticky = "news")
b5 = Button(x,text="5",width=10,height=3,  command = lambda: gerer(5), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b5.grid(row=4, column = 1,sticky = "news")
b6 = Button(x,text="6",width=10,height=3,  command = lambda: gerer(6), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b6.grid(row=4, column = 2,sticky = "news")
b7 = Button(x,text="7",width=10,height=3,  command = lambda: gerer(7), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b7.grid(row=5, column = 0,sticky = "news")
b8 = Button(x,text="8",width=10,height=3,  command = lambda: gerer(8), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b8.grid(row=5, column = 1,sticky = "news")
b9 = Button(x,text="9",width=10,height=3, command = lambda: gerer(9), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b9.grid(row=5, column = 2,sticky = "news")
b10 = Button(x,text="0",width=10,height=3, command = lambda: gerer(0), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b10.grid(row=6, column = 1,sticky = "news")
b11 = Button(x,text=".",width=10,height=3, command = lambda: gerer("."), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b11.grid(row=6, column=0,sticky = "news")
b12 = Button(x,text="=",width=10,height=3,  command = lambda: gerer("="), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b12.grid(row=6, column=2,sticky = "news")
b13 = Button(x,text="+",width=10,height=3, command = lambda: gerer("+"), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b13.grid(row=3, column=3,sticky = "news")
b14 = Button(x,text="-",width=10,height=3, command = lambda: gerer("-"), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b14.grid(row=4, column=3, sticky="news")
b15 = Button(x,text="x",width=10,height=3, command = lambda: gerer("*"), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b15.grid(row=5, column=3,sticky = "news")
b16 = Button(x,text="÷",width=10,height=3, command = lambda: gerer("/"), font = ("Agency fb",11,"bold"), activebackground = "silver", activeforeground = "white")
b16.grid(row=6, column=3,sticky = "news")

lbl_info = Label(x, text = "eCalculator - Copyright 2020",  font = ("Agency fb",10,"italic"))
lbl_info.grid(row = 7, column = 0, columnspan = 2, sticky = "nsw")
lbl_info = Label(x, text = "By : Elfried (V1P3R 75)",  font = ("Agency fb",10,"italic"))
lbl_info.grid(row = 7, column = 2, columnspan = 2, sticky = "nes")


#Evenements
x.bind("<KeyPress-1>",touche)
x.bind("<KeyPress-2>",touche)
x.bind("<KeyPress-3>",touche)
x.bind("<KeyPress-4>",touche)
x.bind("<KeyPress-5>",touche)
x.bind("<KeyPress-6>",touche)
x.bind("<KeyPress-7>",touche)
x.bind("<KeyPress-8>",touche)
x.bind("<KeyPress-9>",touche)
x.bind("<KeyPress-0>",touche)
x.bind("<KeyPress-Return>",touche)
x.bind("<asterisk>",touche)
x.bind("<plus>",touche)
x.bind("<minus>",touche)
x.bind("<slash>",touche)
x.bind("<period>",touche)
x.bind("<BackSpace>",touche)
x.bind("<c>",touche)
x.bind("<C>",touche)
x.bind("<e>",touche)
x.bind("<E>",touche)
x.bind("<parenleft>",touche)
x.bind("<parenright>",touche)
x.bind("<Control-h>",infos)
x.bind("<h>",historique)
x.protocol("WM_DELETE_WINDOW", quitter)
x.bind("<Control-q>",quitter)

menu()

x.mainloop()

