import arcade
import arcade.gui
from arcade.sound import Sound, stop_sound
from arcade.window_commands import close_window
from game import constants
from game.menu_view import MenuView
# from game.game_help import HowtoPlayView
import os

path = os.path.dirname(os.path.realpath(__file__))
class PrincipalMenuView(arcade.View):
    """ Class that manages the 'menu' view. """

    def on_show(self):
        """ Called when switching to this view"""

        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color

        arcade.set_background_color(arcade.color.GRAY_ASPARAGUS)

        self.audio_sound = arcade.sound.load_sound(f"{path}\\sound.mp3")
        arcade.play_sound(self.audio_sound)

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout(
            x=0, y=0, vertical=False, align="top")

        # Create the buttons

        play = arcade.gui.UIFlatButton(text="Play", width=200)
        self.v_box.add(play.with_space_around(left=20, right=20))

               
       # assign buttons to actions
        play.on_click = self.click_level_view

                     

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        
    def click_level_view(self, event):
        print(event)
        self.on_mouse_press()
                       
    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        self.manager.draw()

    # def on_hide_view(self):
    #     return super().on_hide_view()

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        """ If the user presses the mouse button, start the game. """
        game_board = MenuView()
        game_board.on_show()
        self.window.show_view(game_board)
       
    # def level_view(self):        
    #     view = MenuView()
    #     view.on_show()
    #     self.window.show_view(view)
        
        

    




