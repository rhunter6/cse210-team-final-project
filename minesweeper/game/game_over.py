import arcade
from game import menu_view
from game import constants


class GameOver(arcade.View):

    '''
    
    This will either show a you win screen or a you lose screen depending on weather
    you win or lose. 

    '''
    def __init__(self):
        super().__init__()
        self.time_taken = 0
        print("game overrrrrr")
        
        self.on_draw()

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", 340, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 430, 300, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         constants.START_SCREEN_WIDTH / 2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = menu_view.MenuView()
        self.window.show_view(game_view)
