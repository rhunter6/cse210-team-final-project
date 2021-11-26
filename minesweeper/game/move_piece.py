import arcade
from game import constants
 
class MovePiece:
    def __init__(self,) -> None:
        self.move_piece()


    def move_piece(row, column, img_name):     
        x = column * (constants.WIDTH + constants.MARGIN) + (constants.WIDTH / 2 + constants.MARGIN)
        y = row * (constants.HEIGHT + constants.MARGIN) + (constants.HEIGHT / 2 + constants.MARGIN)
        new_sprite = arcade.Sprite (constants.PATH+"/icons/" + img_name + ".png",
            center_x = column * (constants.WIDTH + constants.MARGIN) + (constants.WIDTH / 2 + constants.MARGIN), 
            center_y = row * (constants.HEIGHT + constants.MARGIN) + (constants.HEIGHT / 2 + constants.MARGIN),
                image_height=constants.HEIGHT + constants.MARGIN,
                image_width=constants.WIDTH + constants.MARGIN,
                scale=.85)
        return new_sprite
                        