from tkinter import *
from tkinter import ttk

# colors
preto: str = '#242424'
cinza: str = '#616161'
cinza2: str = '#6d6d6e'
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

frame2 = Frame(janela, width=500, height=245, bg=cinza2)
frame2.grid(row=1, column=0)

frame3 = Frame(janela, width=500, height=40, bg=preto)
frame3.grid(row=2, column=0)

# botoes
# botao inicia jogo
botao_jogar = Button(frame3, command=lambda: jogar(), width=54, height=1, text='  Jogar', anchor=CENTER, bg=preto, fg=branco, font='Arial 12', relief='flat')
botao_jogar.place(x=2, y=1)

def jogar():
    # configurando frame1
    jogador1 = Label(frame1, text='X', font='Arial 18 bold', bg=preto, fg=branco)
    jogador1.place(x=60, y=20)

    separador_jogador1 = Label(frame1, text=':', font='Arial 18 bold', bg=preto, fg=branco)
    separador_jogador1.place(x=100, y=18)

    pontos_jogador1 = Label(frame1, text='0', font='Arial 18 bold', bg=preto, fg=branco)
    pontos_jogador1.place(x=130, y=20)

    vez_jogador1 = Label(frame1, width=180, font='Arial 1', bg=azul)
    vez_jogador1.place(x=0, y=65)


    jogador2 = Label(frame1, text='O', font='Arial 18 bold', bg=preto, fg=branco)
    jogador2.place(x=355, y=20)

    separador_jogador2 = Label(frame1, text=':', font='Arial 18 bold', bg=preto, fg=branco)
    separador_jogador2.place(x=395, y=18)

    pontos_jogador2 = Label(frame1, text='0', font='Arial 18 bold', bg=preto, fg=branco)
    pontos_jogador2.place(x=425, y=20)

    vez_jogador2 = Label(frame1, width=180, font='Arial 1', bg=preto)
    vez_jogador2.place(x=320, y=65)

    # configurando frame2
    # criando hashtag/cerquilha
    botao_jogar.destroy()

    vez_de = Label(frame1, text='vez de', font='Arial 12', bg=preto, fg=branco)
    vez_de.place(x=220, y=25)
    vez_de_jogador = Label(frame1, text='X', font='Arial 12 bold', bg=preto, fg=branco)
    vez_de_jogador.place(x=270, y=25)


    linha1_horizontal = Label(frame2, width=160, height=1, font='Arial 1', bg=cinza)
    linha1_horizontal.place(x=170, y=95)

    linha2_horizontal= Label(frame2, width=160, height=1, font='Arial 1', bg=cinza)
    linha2_horizontal.place(x=170, y=155)

    linha1_vertical1= Label(frame2, width=1, height=80, font='Arial 1', bg=cinza)
    linha1_vertical1.place(x=220, y=50)

    linha2_vertical= Label(frame2, width=1, height=80, font='Arial 1', bg=cinza)
    linha2_vertical.place(x=280, y=50)
    
    # botoes choices
    botao_choicex_1 = Button(frame2, command= lambda: clica(botao_choicex_1), width=3, height=1, text=None, anchor=CENTER, font='Arial 16 bold', bg=cinza2, fg=preto, relief=FLAT)
    botao_choicex_1.place(x=170, y=50)

    botao_choicex_2 = Button(frame2, command=lambda: clica(botao_choicex_2), width=3, height=1, text=None, anchor=CENTER, font='Arial 16 bold', bg=cinza2, fg=preto, relief=FLAT)
    botao_choicex_2.place(x=230, y=50)

    botao_choicex_3 = Button(frame2, command=lambda: clica(botao_choicex_3), width=3, height=1, text=None, anchor=CENTER, font='Arial 16 bold', bg=cinza2, fg=preto, relief=FLAT)
    botao_choicex_3.place(x=290, y=50)

    botao_choicex_4 = Button(frame2, command=lambda: clica(botao_choicex_4), width=3, height=1, text=None, anchor=CENTER, font='Arial 16 bold', bg=cinza2, fg=preto, relief=FLAT)
    botao_choicex_4.place(x=170, y=108)

    botao_choicex_5 = Button(frame2, command=lambda: clica(botao_choicex_5), width=3, height=1, text=None, anchor=CENTER, font='Arial 16 bold', bg=cinza2, fg=preto, relief=FLAT)
    botao_choicex_5.place(x=230, y=108)

    botao_choicex_6 = Button(frame2, command=lambda: clica(botao_choicex_6), width=3, height=1, text=None, anchor=CENTER, font='Arial 16 bold', bg=cinza2, fg=preto, relief=FLAT)
    botao_choicex_6.place(x=290, y=108)

    botao_choicex_7 = Button(frame2, command=lambda: clica(botao_choicex_7), width=3, height=1, text=None, anchor=CENTER, font='Arial 16 bold', bg=cinza2, fg=preto, relief=FLAT)
    botao_choicex_7.place(x=170, y=168)

    botao_choicex_8 = Button(frame2, command=lambda: clica(botao_choicex_8), width=3, height=1, text=None, anchor=CENTER, font='Arial 16 bold', bg=cinza2, fg=preto, relief=FLAT)
    botao_choicex_8.place(x=227, y=168)

    botao_choicex_9 = Button(frame2, command=lambda: clica(botao_choicex_9), width=3, height=1, text=None, anchor=CENTER, font='Arial 16 bold', bg=cinza2, fg=preto, relief=FLAT)
    botao_choicex_9.place(x=290, y=168)

    global jogada
    jogada = 1
 
    def clica(botao_clicado):
        global jogada
        impar = [1, 3, 5, 7, 9]
        par = [2, 4, 6, 8, 10]

        if jogada < 10:
            if jogada in impar:
                vez_de_jogador['text'] = 'X'
                vez_jogador1['bg'] = azul
                vez_jogador2['bg'] = preto

                botao_clicado['text'] = 'X'
                jogada += 1
                
                vez_de_jogador['text'] = 'O'
                vez_jogador1['bg'] = preto
                vez_jogador2['bg'] = azul
                
                # horizontal
                if botao_choicex_1['text'] == 'X' and botao_choicex_2['text'] == 'X' and botao_choicex_3['text'] == 'X':
                    vencedor = Label(frame2, text='X Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()
                    
                    botao_reinicia = Button(frame3, command=lambda: jogar(), width=54, height=1, text='  Reiniciar', anchor=CENTER, bg=preto, fg=branco, font='Arial 12', relief='flat')
                    botao_reinicia.place(x=2, y=1)

                elif botao_choicex_4['text'] == 'X' and botao_choicex_5['text'] == 'X' and botao_choicex_6['text'] == 'X':
                    vencedor = Label(frame2, text='X Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()

                elif botao_choicex_7['text'] == 'X' and botao_choicex_8['text'] == 'X' and botao_choicex_9['text'] == 'X':
                    vencedor = Label(frame2, text='X Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)
                    
                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()

                
                # diagonal
                elif botao_choicex_1['text'] == 'X' and botao_choicex_5['text'] == 'X' and botao_choicex_9['text'] == 'X':
                    vencedor = Label(frame2, text='X Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)
                    
                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()


                elif botao_choicex_7['text'] == 'X' and botao_choicex_5['text'] == 'X' and botao_choicex_3['text'] == 'X':
                    vencedor = Label(frame2, text='X Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()


                # vertical
                elif botao_choicex_1['text'] == 'X' and botao_choicex_4['text'] == 'X' and botao_choicex_7['text'] == 'X':
                    vencedor = Label(frame2, text='X Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()

                elif botao_choicex_2['text'] == 'X' and botao_choicex_5['text'] == 'X' and botao_choicex_8['text'] == 'X':
                    vencedor = Label(frame2, text='X Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()

                elif botao_choicex_3['text'] == 'X' and botao_choicex_6['text'] == 'X' and botao_choicex_9['text'] == 'X':
                    vencedor = Label(frame2, text='X Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()
                    

            elif jogada in par:
                vez_de_jogador['text'] = 'O'
                vez_jogador2['bg'] = azul
                vez_jogador1['bg'] = preto
                
                botao_clicado['text'] = 'O'
                botao_clicado['fg'] = branco
                jogada += 1

                vez_de_jogador['text'] = 'X'
                vez_jogador1['bg'] = azul
                vez_jogador2['bg'] = preto

                # horizontal
                if botao_choicex_1['text'] == 'O' and botao_choicex_2['text'] == 'O' and botao_choicex_3['text'] == 'O':
                    vencedor = Label(frame2, text='O Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()

                elif botao_choicex_4['text'] == 'O' and botao_choicex_5['text'] == 'O' and botao_choicex_6['text'] == 'O':
                    vencedor = Label(frame2, text='O Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()

                elif botao_choicex_7['text'] == 'O' and botao_choicex_8['text'] == 'O' and botao_choicex_9['text'] == 'O':
                    vencedor = Label(frame2, text='O Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()
                
                # diagonal
                elif botao_choicex_1['text'] == 'O' and botao_choicex_5['text'] == 'O' and botao_choicex_9['text'] == 'O':
                    vencedor = Label(frame2, text='O Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()

                elif botao_choicex_7['text'] == 'O' and botao_choicex_5['text'] == 'O' and botao_choicex_3['text'] == 'O':
                    vencedor = Label(frame2, text='O Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()

                # vertical
                elif botao_choicex_1['text'] == 'O' and botao_choicex_4['text'] == 'O' and botao_choicex_7['text'] == 'O':
                    vencedor = Label(frame2, text='O Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=1080)
                    
                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()

                elif botao_choicex_2['text'] == 'O' and botao_choicex_5['text'] == 'O' and botao_choicex_8['text'] == 'O':
                    vencedor = Label(frame2, text='O Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy() 

                elif botao_choicex_3['text'] == 'O' and botao_choicex_6['text'] == 'O' and botao_choicex_9['text'] == 'O':
                    vencedor = Label(frame2, text='O Venceu!', font='Arial 18 bold', bg=preto, fg=branco)
                    vencedor.place(x=190, y=108)

                    linha1_horizontal.destroy(), linha2_horizontal.destroy(), linha1_vertical1.destroy(), linha2_vertical.destroy()
                    botao_choicex_1.destroy(), botao_choicex_2.destroy(), botao_choicex_3.destroy()
                    botao_choicex_4.destroy(), botao_choicex_5.destroy(), botao_choicex_6.destroy()
                    botao_choicex_7.destroy(), botao_choicex_8.destroy(), botao_choicex_9.destroy()
    
                    

                
janela.mainloop()
