#!/usr/bin/env python
import wx
from wx.lib.calendar import Calendar
from wx.animate import GIFAnimationCtrl

# funcao que recebe um elemento  com posicao e tamanho e retorna a posicao embaixo dele.


def embaixo(elemento):
    return elemento.GetPosition()[0], elemento.GetPosition()[1] + elemento.GetSize()[1]


# funcao que recebe um elemento com posicao e tamanho e retorna a posicao na direita.
def na_direita(elemento):
    return elemento.GetPosition()[0] + elemento.GetBestSize()[0], elemento.GetPosition()[1]

# Create a new app, don't redirect stdout/stderr to a window.
app = wx.App()

# A Frame is a top-level window.
frame = wx.Frame(None, title="Hello World")

# Iniciando um Panel no frame.
panel = wx.Panel(frame)

# Criando um controle de texto no Panel.
text_ctrl1 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)

# Criando outro controle de texto embaixo do primeiro.
text_ctrl2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE, pos=embaixo(text_ctrl1))

# Criando um Botao embaixo do text_ctrl2.
button1 = wx.Button(panel, pos=embaixo(text_ctrl2))

# Calculando o melhor tamanho do Panel e configurando o tamanho do panel com isso.
panel.SetSize(panel.GetBestSize())

# Adicionando outro botao embaixo do panel.
button2 = wx.Button(frame, pos=embaixo(panel))

# Adicionando outro botao embaixo do button2.
button3 = wx.Button(frame, pos=embaixo(button2))

# Calendar
calendar = Calendar(frame, pos=na_direita(panel))

# GIFAnimationCtrl
gif_animation_ctrl = GIFAnimationCtrl(frame, filename="giphy.gif", pos=na_direita(calendar))

# Criando um manipulador para o botao 2
frame.Bind(wx.EVT_BUTTON, lambda event: text_ctrl2.AppendText("%d " % calendar.GetDay()), button2)

# Criando um manipulador ao EVT_BUTTON.
panel.Bind(wx.EVT_BUTTON, lambda event: text_ctrl1.AppendText(" oi"), button1)

# Criando um manipulador para o botao 3.
frame.Bind(
    wx.EVT_BUTTON,
    lambda event: gif_animation_ctrl.Stop() if gif_animation_ctrl.IsPlaying() else gif_animation_ctrl.Play(),
    button3
)

# Calculando melhor tamanho.
size = frame.GetBestSize()

# Configurando o tamanho do frame.
frame.SetSize(size)

# Configurando o tamanho minimo do frame.
frame.SetMinSize(size)

# Tornando o frame visivel para o usuario.
frame.Show(True)

# Habilitando tratamento dos eventos.
app.MainLoop()
