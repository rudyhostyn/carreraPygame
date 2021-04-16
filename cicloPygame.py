import pygame, sys
import random

class Runner():
    
    def __init__(self, x=0, y=0):
        self.custom = pygame.image.load("images/smallball.png")
        self.position = [x,y]
        self.name = "Madrid"
    
    def avanzar(self):
        self.position[0] += random.randint(1,6)

class Game():
    runners = []
    __startLine = -5
    __finishLine = 600
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        #self.__screen.fill((226,147,48))
        self.__background = pygame.image.load("images/campoFutbol.jpg")
        pygame.display.set_caption("Carrera pygame")
        
        firstRunner = Runner(self.__startLine,240)
        firstRunner.name = "seepdy"
        self.runners.append(firstRunner)
        
                
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
    #refresco pantalla tras el evento
            self.__screen.blit(self.__background,(0,0))
            self.__screen.blit(self.runners[0].custom, self.runners[0].position)
            #empiezo a jugar con la funcion avanzar creada en la clase runner0
            self.runners[0].avanzar()
            
            if self.runners[0].position[0] >= self.__finishLine:
                print("Ha ganado {}".format(self.runners[0].name))
                gameOver = True
                      
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()
    
    
if __name__ == "__main__":
    game = Game()
    pygame.font.init()
    game.competir()
    




