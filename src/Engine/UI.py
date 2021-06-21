from Engine import Constant
import os
import pygame


class UIEngine:

    def __init__(self):
        self._aimPosX = self.aimPosY = Constant.SCREEN_WIDTH // 2

        self._grassImg = pygame.image.load(os.path.join("../img/Environments",
                                                        "GrassSprite.png"))
        self._skyImg = pygame.image.load(os.path.join("../img/Environments",
                                                      "SkyTileSprite.png"))
        self._aimCursorImg = pygame.image.load(os.path.join("../img/Player",
                                                            "aim.png"))

    def draw(self, screen):
        screen.blit(self._skyImg, (0, 0))
        screen.blit(self._grassImg, (0, 500))
        self.draw_cursor(screen)

    def draw_cursor(self, screen):
        mouseX, mouseY = pygame.mouse.get_pos()
        screen.blit(self._aimCursorImg, (mouseX, mouseY))
        pygame.mouse.set_visible(False)
