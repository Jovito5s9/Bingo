from kivy.app import App
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.widget import Widget 
from kivy.uix.label import Label 
from kivy.uix.button import Button 
from kivy.graphics import Ellipse, Color
from kivy.properties import BooleanProperty

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
    chamado=BooleanProperty(False)
    def __init__(self,numero=[],**kwargs):
        super().__init__(**kwargs)
        self.numero=self.descobrir_numero(numero)
        self.numero_chamado=[0.1,0.1,0.4,1]
        self.numero_nao_chamado=[0.1,0.1,0.1,1]
        with self.canvas:
            Color(*self.numero_nao_chamado)
            Ellipse(pos=self.pos,size=self.size)
        self.numero_label=Label(text=f'{self.numero}',pos=self.pos)
        self.add_widget(self.numero_label)
        self.bind(chamado=self.foi_chamado)
    
    def foi_chamado(self,*args):
        with self.canvas:
            Color(*self.numero_chamado)
            Ellipse(pos=self.pos,size=self.size)
    
    def descobrir_numero(self,numero):
        if not numero:
            return
        coluna, linha=numero
        numero=coluna*numeros_por_letra + linha + 1
        return numero

class Tabela(BoxLayout):
    def __init__(self,tamanho=15,**kwargs):
        super().__init__(**kwargs)
        self.bolas={}
        self.size=(tamanho*20,tamanho*70)
        self.orientation='vertical'
        size=self.width/5
        for i in range(0,5):
            linha=BoxLayout(orientation='horizontal')
            for j in range(0,numeros_por_letra):
                bola=Bola(numero=(i,j),pos= (i*1.2*size, self.y + self.height - j*1.2*size),size=(size,size))
                linha.add_widget(bola)
                self.bolas[bola.numero]=bola
            self.add_widget(linha)
        
    def numero_chamado(self,numero):
        bola=self.bolas[numero]
        bola.chamado=True
        
class Bingo(FloatLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.size_hint = None, None 
        self.tabela=Tabela(tamanho=18)
        self.add_widget(self.tabela)
        self.sortear_button=Button(size=(100,100))
        self.sortear_button.bind(on_release = self.sortear_numero)
        self.add_widget(self.sortear_button)
    
    def sortear_numero(self,*args):
        numero=sortear_numero()
        self.tabela.numero_chamado(numero)

class BingoApp(App):
    def build(self):
        return Bingo()

BingoApp().run()
