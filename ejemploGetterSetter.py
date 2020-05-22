class ClaseConGetterySetter():
    def __init__(self):
        self.__propiedad_privada = None
        
    def setPropiedadPrivada(self, valor): #Setter. Coge un valor que le da el usuario para cambiar el nombre de propiedad privada
            self.__propiedad_privada=valor
            
    def getPropiedadPrivada(self): #Getter. Muestra el valor que tiene propiedad privada, por defecto es None a menos que se le haya asignado otro con el setter.
            return self.__propiedad_privada
        
    def propiedadPrivada(self, valor =None): #Getter y Setter a la vez. Esto es mas util. Es como la funcion dentro de turtle: turtle.shape() en la q t muestra la forma (getter) o puedes cambiarla poniendo la forma dentro del parentesis(setter)
            if valor==None:
                #Actúa como getter
                return self.__propiedad_privada
            else:
                #Actúa como setter
                self.__propiedad_privada = valor
        
    def __str__(self):
            return "ClaseConGetterySetter con propiedadPrivada ->"
    
if __name__=='__main__':
    c = ClaseConGetterySetter()