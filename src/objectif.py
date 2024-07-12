import pygame
class Objectif(pygame.sprite.Sprite):
    def __init__(self,image,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image=image
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(70,70))
        self.posx=posx
        self.posy=posy
        self.rect=self.image.get_rect()
        self.rect= pygame.Rect(150+posx*70, 120+posy*70, 70,70)





    def update(self):
        pass


