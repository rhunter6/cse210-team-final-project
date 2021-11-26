import arcade
import arcade.gui
from game.setup_board import SetupBoard
from game import constants
from game.game_board import GameBoard
from arcade.sound import Sound, stop_sound




class MenuView(arcade.View):
    """ Class that manages the 'menu' view. """
   
    def on_show(self):
        """ Called when switching to this view"""
        
        # --- Required for all code that uses UI element,
        # a UIManager to handle the UI.
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # Set background color
        
        arcade.set_background_color(arcade.color.LIGHT_GRAY)
        '''
        TURNED OFF FOR TESTING ADD BUTTON TO TURN IT BACK ON

        self.audio_sound = arcade.sound.load_sound(f"{constants.PATH}\\sound.mp3")
        arcade.play_sound(self.audio_sound)
        '''
    
        # Create a Horizontal BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout(x=0, y=600,vertical=False, align="top")

        # Create the buttons

        self.easy_button = arcade.gui.UIFlatButton(text="Easy", width=200)
        self.v_box.add(self.easy_button.with_space_around(left=20, right=20))

        self.medium_button = arcade.gui.UIFlatButton(text="Medium", width=200)
        self.v_box.add(self.medium_button.with_space_around(left=20, right=20))

        self.hard_button = arcade.gui.UIFlatButton(text="Hard", width=200)
        self.v_box.add(self.hard_button.with_space_around(left=20, right=20))        
    
       # assign buttons to actions
        self.easy_button.on_click = self.on_click_easy
        self.medium_button.on_click = self.on_click_medium
        self.hard_button.on_click = self.on_click_hard

      
        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def on_click_easy(self, event):
        print("easy:", event)
        SetupBoard("easy")
        print(constants.MINE_LOCATIONS)
        print(constants.MINE_FIELD)

    def on_click_medium(self, event):
        print("Medium:", event)        
        SetupBoard("medium")
        print(constants.MINE_LOCATIONS)
        print(constants.MINE_FIELD)

    def on_click_hard(self, event):
        print("Hard:", event)
        SetupBoard("hard")
        print(constants.MINE_LOCATIONS)
        print(constants.MINE_FIELD)


    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        self.manager.draw()

     
  