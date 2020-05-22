import turtle

class Circuito(): #Crea un circuto (pantalla) con las dimensiones que le demos, la linea de comienzo y fin siempre estan a la misma altura en funcion del ancho
    corredores = [] #las tortugas que van a correr
    __posStartY=(-30,-10,10,30) #represena la posicion en Y de cada tortuga para q esten centradas. Es una tupla (no seria necesario privatizarla pq al ser una tupla es inmutable)
    __colorTurtle= ('red', 'blue','green','orange') #color de cada tortuga
    
    def __init__(self, width, height):
        self.__screen=turtle.Screen() #Privado para que el usuario no modifique la pantalla donde van a correr las tortugas (se puede modificar llamandolo con ._Circuito__screen.
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine= -width/2 + 20
        self.__finishLine= width/-20
        
        self.__createRunners()
        
    def __createRunners(self):  #crea a las tortugas  
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.color(self.__colorTurtle[i])#dandole colores a cada tortuga
            new_turtle.shape('turtle')
            new_turtle.penup() #truqui para q no pinten las tortugas cuando se posicionen
            new_turtle.setpos(self.__startLine, self.__posStartY[i]) #colocar la posicion de las tortugas
            
            
            self.corredores.append(new_turtle)
            #print(self.corredores[i],"corredor", i+1) #lo he creado yo para ver los corredores






if __name__== '__main__':
    circuito=Circuito(640,480)