import pygame
import os


class Player:

    _walk1 = pygame.image.load(os.path.join("../img/Player", "walk1.png"))
    _walk2 = pygame.image.load(os.path.join("../img/Player", "walk2.png"))
    _imgIdle = pygame.image.load(os.path.join("../img/Player", "idle.png"))

    _rightStep = True
    _leftStep = True

    def __init__(self, pos, name, hp=100, speed=5):
        self._name = name
        self._hp = hp
        self._speed = speed
        (self.posX, self.posY) = pos
        self._id = -1

    def get_position(self):
        return self.posX, self.posY

    def set_position(self, pos):
        self.posX, self.posY = pos

    def get_id(self):
        return self._id if self._id != -1 else -1

    def set_id(self, id):
        self._id = id

    def draw(self, screen):
        screen.blit(self._imgIdle, self.get_position())

    def move(self, direction, screen):
        if direction == "RIGHT":
            self.posX += self._speed

            if self._rightStep:
                screen.blit(self._walk2, self.get_position())

                self._rightStep = False
                self._leftStep = True
            else:
                screen.blit(self._walk1, self.get_position())
                self._rightStep = True

        elif direction == "LEFT":
            self.posX -= self._speed

            if self._leftStep:
                screen.blit(self._walk1, self.get_position())

                self._leftStep = False
                self._rightStep = True
            else:
                screen.blit(self._walk2,
                            self.get_position())
                self._leftStep = True

        elif direction == "IDLE":
            screen.blit(self._imgIdle, self.get_position())
