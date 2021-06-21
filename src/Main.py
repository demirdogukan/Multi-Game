from Engine import Constant
from Engine.Character import Player
from Engine.UI import UIEngine
from Network.ClientHandler import ClientManager
import pygame


class GameEngine:

    list_of_players: list = []

    def __init__(self):
        self._uiEngine = UIEngine()
        self._p1 = Player((200, 400), "p1", 100, 5)
        self._p2 = Player((300, 500), "p2", 100, 5)
        self._clientManager = ClientManager()

    def start(self):
        pygame.init()
        pygame.display.set_caption('Game')

        self.screen = pygame.display.set_mode((Constant.SCREEN_WIDTH,
                                              Constant.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self._p1 = self._clientManager.get_player1()

    def update(self):
        # pre server and client settings
        self.start()
        # Run the game
        run = True
        while run:
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            p2data = self._clientManager.send_data(self._p1)
            if p2data is not None:
                self._p2 = p2data

            self.draw()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    # Draw UI Elements
    def draw(self):
        self._uiEngine.draw(self.screen)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self._p1.move("LEFT", self.screen)
        elif keys[pygame.K_RIGHT]:
            self._p1.move("RIGHT", self.screen)
        else:
            self._p1.move("IDLE", self.screen)

        self._p2.draw(self.screen)


if __name__ == "__main__":
    _game = GameEngine()
    _game.update()
