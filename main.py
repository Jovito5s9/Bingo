from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.widget import Widget 
from kivy.graphics import Ellipse, Color

import random 

numero_maximo=75
numeros_por_letra=int(numero_maximo/5)
numeros_sorteados=[]

def sortear_numero():
    numero=random.randint(1,numero_maximo)
    while numero in numeros_sorteados or not numero:
        numero=random.randint(1,numero_maximo)
    numeros_sorteados.append(numero)
    numeros_sorteados.sort()
    return numero

def descobrir_letra(numero):
    letras="BINGO"
    letra= int((numero-1) / numeros_por_letra)
    return letras[letra]

x=sortear_numero()
print(x)
letra=descobrir_letra(x)
print(letra)

class Bola(Widget):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0.1,0.1,0.4,1)
            Ellipse(pos=self.pos,size=self.size)

class Tabela(BoxLayout):
    def __init__(self,tamanho=15,**kwargs):
        super().__init__(**kwargs)
        self.size=(tamanho*20,tamanho*100)
        self.orientation='vertical'
        size=self.width/5
        for i in range(0,5):
            linha=BoxLayout(orientation='horizontal')
            for j in range(0,numeros_por_letra):
                bola=Bola(pos= (self.x + self.width - i*1.2*size, self.y + self.height - j*1.2*size),size=(size,size))
                linha.add_widget(bola)
            self.add_widget(linha)
        

class BingoApp(App):
    def build(self):
        return Tabela(tamanho=15)

BingoApp().run()
