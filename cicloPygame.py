import pygame, sys
import random2

class Runner():
   
    def __init__(self, x=0, y=0):
        self.custom =""
        self.position = [x,y]
        self.name = ""
    
    def avanzar(self):
        self.position[0] += random2.randint(1,6)
        pygame.time.delay(10)

class Game():
    runners = []
    __posY =(160, 200, 240, 280)
    __names = ("¡Hala Madrid!", "Força Barça", "Che em guanyat", "Ahiva la ostia")
    __customs = ('Madrid', 'Barcelona', 'Valencia', 'Bilbao')
    __startLine = 20
    __finishLine = 560
    
        
    def __init__(self):
        self.__screen = pygame.display.set_mode((628, 402))
        #self.__screen.fill((226,147,48))
        self.__background = pygame.image.load("images/campoFutbol.jpg")
        pygame.display.set_caption("Carrera pygame")
        
        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            theRunner.custom = pygame.image.load("images/{}.png".format(self.__customs[i]))
            self.runners.append(theRunner)    

    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            #refresco pantalla tras el evento
            self.__screen.blit(self.__background,(0,0))
            
            for i in self.runners:
                self.__screen.blit(i.custom, i.position)
            #empiezo a jugar con la funcion avanzar creada en la clase runner0
            for activeRunner in self.runners:
                activeRunner.avanzar()
            # acaba el juego + mensaje del ganador   
            for activeRunner in self.runners:
                if activeRunner.position[0] >= self.__finishLine:
                    print("Ha ganado {}".format(activeRunner.name))
                    gameOver = True
                      
            pygame.display.flip()
            
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    
    
if __name__ == "__main__":
    game = Game()
    pygame.font.init()
    game.competir()
    




