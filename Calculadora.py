from tkinter import *
from tkinter import ttk,messagebox
from functools import partial 
from Fraccion import Fraccion
class Calculadora(object):
    __ventana=None
    __operador=None
    __panel=None
    __operadorAux=None
    __primerOperando=None
    __segundoOperando=None
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        self.__ventana.resizable(0,0)
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador=StringVar()
        self.__operadorAux=None
        operatorEntry=ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W,E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right',state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerSimbolo, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerSimbolo,'2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerSimbolo,'3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerSimbolo,'4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerSimbolo,'5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerSimbolo,'6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerSimbolo,'7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerSimbolo,'8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerSimbolo,'9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerSimbolo, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerSimbolo, '/')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='%', command=partial(self.ponerOPERADOR, '%')).grid(column=3, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=1, row=8, sticky=W)
        ttk.Button(mainframe,text='CE',command=self.borrarPanel).grid(column=3, row=8, sticky=W)
        self.__panel.set('0')
        self.__operador.set('')
        panelEntry.focus()
        self.__ventana.mainloop()
    def ponerSimbolo(self, simbolo):
        if self.__operadorAux==None:
            valor = self.__panel.get()
            self.__panel.set(valor+simbolo)
        else:
            self.__operadorAux=None
            valor=self.__panel.get()
            try:
                if valor.count('/')>0:
                    if valor.count('/')>1:
                        raise TypeError
                    else:
                        partesFraccion=valor.split('/')
                        if len(partesFraccion)==2:
                            self.__primerOperando=Fraccion(int(partesFraccion[0]),int(partesFraccion[1]))
                        else:
                            self.__primerOperando=Fraccion(0,int(partesFraccion[0]))
                else:
                    self.__primerOperando=int(valor)
            except TypeError:
                self.errorSimboloFraccion()
            except ValueError:
                self.__panel.set(simbolo)
            else:
                self.__panel.set(simbolo)
    def borrarPanel(self):
        self.__panel.set('0')
        self.__operador.set('')
    def resolverOperacion(self, operando1, operacion, operando2):
        resultado=0
        if operacion=='+':
            resultado=operando1+operando2
        else:
            if operacion=='-':
                resultado=operando1-operando2
            else:
                if operacion=='*':
                    resultado=operando1*operando2
                else:
                    if operacion=='%':
                        resultado=operando1/operando2
        self.__panel.set(str(resultado))
    def ponerOPERADOR(self, op):
        if op=='=':
            operacion=self.__operador.get()
            valor=self.__panel.get()
            try:
                if valor.count('/')>0:
                    if valor.count('/')>1:
                        raise TypeError
                    else:
                        partesFraccion=valor.split('/')
                        if len(partesFraccion)==2:
                            self.__segundoOperando=Fraccion(int(partesFraccion[0]),int(partesFraccion[1]))
                        else:
                            self.__segundoOperando=Fraccion(0,int(partesFraccion[0]))
                else:
                    self.__segundoOperando=int(valor)
            except TypeError:
                self.errorSimboloFraccion()
            else:
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set('')
                self.__operadorAux=None
        else:
            if self.__operador.get()=='':
                self.__operador.set(op)
                self.__operadorAux=op
            else:
                operacion=self.__operador.get()
                valor=self.__panel.get()
                try:
                    if valor.count('/')>0:
                        if valor.count('/')>1:
                            raise TypeError
                        else:
                            partesFraccion=valor.split('/')
                            if len(partesFraccion)==2:
                                self.__segundoOperando=Fraccion(int(partesFraccion[0]),int(partesFraccion[1]))
                            else:
                                self.__segundoOperando=Fraccion(0,int(partesFraccion[0]))
                    else:
                        self.__segundoOperando=int(valor)
                except TypeError:
                    self.errorSimboloFraccion()
                else:
                    self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                    self.__operador.set(op)
                    self.__operadorAux=op
    def errorSimboloFraccion(self):
        messagebox.showerror(title='Error de fracción',message='Solo se admiten fracciones del tipo a/b.')
        self.borrarPanel()