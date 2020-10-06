from classImporter import *
from pygame import *
class gameAnimations:
    def mainMenuStartup(mainMenuPlayed,fenetre, frameMainMenuWait,load_images,image_main1,image_main2,titre_fenetre):
        if mainMenuPlayed==False:
            #Titre
            pygame.display.set_caption(titre_fenetre)
            for i in range(len(load_images)):
                accueil = pygame.image.load(load_images[i]).convert()
                fenetre.blit(accueil, (0,0))
                pygame.display.flip()
                sleep(0.5)
            mainMenuPlayed=True
            gameAnimations.mainMenuStartup(mainMenuPlayed,fenetre, frameMainMenuWait,load_images,image_main1,image_main2,titre_fenetre)
        else:
            accueil = pygame.image.load(image_main1).convert()
            fenetre.blit(accueil, (0,0))
            pygame.display.flip()
            sleep(0.5)
            accueil = pygame.image.load(image_main2).convert()
            fenetre.blit(accueil, (0,0))
            pygame.display.flip()
            sleep(0.5)
            #Titre
            pygame.display.set_caption(titre_fenetre)

