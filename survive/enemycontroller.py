from survive.controller import Controller
from survive.models.enemymodel import Enemy
from survive.models.hogmodel import Hog


class EnemyController(Controller):
    def __init__(self):
        self._enemy = Enemy()

    def generate_enemy(self):
        self._enemy = Hog()
        return self._enemy
