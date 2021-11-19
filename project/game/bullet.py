from game.actor import Actor
from game.player import Player
from game import constants
import math
import arcade

class Bullet(Actor):
    def __init__(self):
        super().__init__()
        self.radius = 1
        self.velocity.dx= constants.BULLET_SPEED
        self.angle = 0
        
    def draw(self):
        bull_img = "imagefilename"
        texture = arcade.load_texture(bull_img)
        
        width = texture.width
        height = texture.height

        x = self.center.x
        y = self.center.y
        angle = self.angle
        arcade.draw_texture_rectangle(x, y, width, height, texture, (angle ) , 255)

    def fire(self, playervelocity, playercenter, playerangle):
        self.angle = playerangle
        self.center.x = playercenter.x
        self.center.y = playercenter.y
        self.velocity.dy = playervelocity.dy
        self.velocity.dx = playervelocity.dx
        self.velocity.dx += math.cos(math.radians(playerangle)) * constants.BULLET_SPEED
        self.velocity.dy += math.sin(math.radians(playerangle)) * constants.BULLET_SPEED
        
