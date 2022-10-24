from tkinter import *
from tkinter import ttk

# colors
preto: str = '#242424'
cinza: str = '#383838'
cinza2: str = '#909190'
branco: str = '#ffffff'
azul: str = '#83ccca'


# configurando janela
janela = Tk()
janela.title('Jogo da velha')
janela.geometry('500x350')
janela.config(bg = preto)
janela.resizable(width=False, height=False)

# criando frames
frame1 = Frame(janela, width=500, height=70, bg=preto)
frame1.grid(row=0, column=0)

frame2 = Frame(janela, width=500, height=245, bg=cinza)
frame2.grid(row=1, column=0)

frame3 = Frame(janela, width=500, height=40, bg=preto)
frame3.grid(row=2, column=0)

# configurando frame1
jogador1 = Label(frame1, text='X', font='Arial 18 bold', bg=preto, fg=branco)
jogador1.place(x=60, y=20)

separador_jogador1 = Label(frame1, text=':', font='Arial 18 bold', bg=preto, fg=branco)
separador_jogador1.place(x=100, y=18)

pontos_jogador1 = Label(frame1, text='0', font='Arial 18 bold', bg=preto, fg=branco)
pontos_jogador1.place(x=130, y=20)

vez_jogador1 = Label(frame1, width=180, font='Arial 1', bg=azul)
vez_jogador1.place(x=0, y=65)



vez_de = Label(frame1, text='vez de', font='Arial 12', bg=preto, fg=branco)
vez_de.place(x=220, y=25)
vez_de = Label(frame1, text='X', font='Arial 12 bold', bg=preto, fg=branco)
vez_de.place(x=270, y=25)



jogador2 = Label(frame1, text='O', font='Arial 18 bold', bg=preto, fg=branco)
jogador2.place(x=355, y=20)

separador_jogador2 = Label(frame1, text=':', font='Arial 18 bold', bg=preto, fg=branco)
separador_jogador2.place(x=395, y=18)

pontos_jogador2 = Label(frame1, text='0', font='Arial 18 bold', bg=preto, fg=branco)
pontos_jogador2.place(x=425, y=20)

vez_jogador2 = Label(frame1, width=180, font='Arial 1', bg=azul)
vez_jogador2.place(x=325, y=65)

# configurando frame2
# criando hashtag/cerquilha
linha1_horizontal = Label(frame2, width=150, height=1, font='Arial 1', bg=cinza2)
linha1_horizontal.place(x=175, y=95)

linha2_horizontal= Label(frame2, width=150, height=1, font='Arial 1', bg=cinza2)
linha2_horizontal.place(x=175, y=155)

linha1_vertical1= Label(frame2, width=1, height=75, font='Arial 1', bg=cinza2)
linha1_vertical1.place(x=220, y=50)

linha1_vertical2= Label(frame2, width=1, height=75, font='Arial 1', bg=cinza2)
linha1_vertical2.place(x=280, y=50)

# botao
botao_reiniciar = Button(frame3, width=54, height=1, text='  Reiniciar', anchor=CENTER, bg=preto, fg=branco, font='Arial 12', relief='flat')
botao_reiniciar.place(x=2, y=1)




janela.mainloop()
