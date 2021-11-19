import arcade
import arcade.gui

from game import constants
from game.game_view import GameView


class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """
   
    def on_show(self):
        """ Called when switching to this view"""
        
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        
        arcade.set_background_color(arcade.color.GRAY_ASPARAGUS)
        
    
        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout(x=0, y=0,vertical=False, align="top")

        # Create the buttons

        easy_button = arcade.gui.UIFlatButton(text="Easy", width=200)
        self.v_box.add(easy_button.with_space_around(left=20, right=20))

        medium_button = arcade.gui.UIFlatButton(text="Medium", width=200)
        self.v_box.add(medium_button.with_space_around(left=20, right=20))

        hard_button = arcade.gui.UIFlatButton(text="Hard", width=200)
        self.v_box.add(hard_button.with_space_around(left=20, right=20))        
    
       # assign buttons to actions
        easy_button.on_click = self.on_click_easy
        medium_button.on_click = self.on_click_medium
        hard_button.on_click = self.on_click_hard

      
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_easy(self, event):
        print("easy:", event)
        self.start_game()

    def on_click_medium(self, event):
        print("Medium:", event)
        self.start_game()

    def on_click_hard(self, event):
        print("Hard:", event)
        self.start_game()


    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        self.manager.draw()
        #arcade.draw_text("Menu Screen - click to advance", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2,
         #                arcade.color.BLACK, font_size=30, anchor_x="center")

    
    def start_game (self):
        """ Use a mouse press to advance to the 'game' view. """
        print("START THE GAME!!!")
        
        game_view = GameView()
        #game_view.setup()
        self.window.show_view(game_view)
     
  