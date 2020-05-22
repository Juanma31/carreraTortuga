import turtle
import random

class Circuito(): #Crea un circuto (pantalla) con las dimensiones que le demos, la linea de comienzo y fin siempre estan a la misma altura en funcion del ancho
    corredores = [] #las tortugas que van a correr
    __posStartY=(-30,-10,10,30) #represena la posicion en Y de cada tortuga para q esten centradas. Es una tupla (no seria necesario privatizarla pq al ser una tupla es inmutable)
    __colorTurtle= ('red', 'blue','green','orange') #color de cada tortuga
    
    def __init__(self, width, height):
        self.__screen=turtle.Screen() #Privado para que el usuario no modifique la pantalla donde van a correr las tortugas (se puede modificar llamandolo con ._Circuito__screen.
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        self.__startLine= -width/2 + 20
        self.__finishLine= width/2 - 20
        self.__screen.title("Welcome to the World Turtle Race") #Crear titulo
        
        
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
    def competir(self):
        
        hayGanador = False
        while not hayGanador:
            for tortuga in self.corredores:
                avance = random.randint(1,6)
                tortuga.forward(avance) #forward es lo mimsmo q fd
                if tortuga.position()[0] >= self.__finishLine: # si la posicion de la tortuga es mayor o igual a la linea final
                    hayGanador =True
                    if tortuga.color()[0]=="green": #PARA TRADUCIRLO A ESPAÑOL
                        print("la tortuga de color verde ha ganado")
                        break
                    elif tortuga.color()[0]=="blue":
                        print("la tortuga de color azul ha ganado")
                        break
                    elif tortuga.color()[0]=="orange":
                        print("la tortuga de color naranja ha ganado")
                        break
                    elif tortuga.color()[0]=="red":
                        print("la tortuga de color roja ha ganado")
                        #print("la tortuga de color {} ha ganado".format(tortuga.color()[0])) #tortuga.colo() devuelve ('red','red') el primero es el color de la tortuga y el segundo del color del recorrido
                        break #para q cuando llegue una tortuga se pare y no tire la siguiente.
if __name__== '__main__':
    circuito=Circuito(640,480)
    circuito.competir()