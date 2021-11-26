import arcade
from arcade.color import BLACK, WHITE
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
        self.h_box = arcade.gui.UIBoxLayout(x=0, y=800,vertical=False, align="center")

        # Create the buttons

        self.easy_button = arcade.gui.UIFlatButton(text="Easy", width=250)
        self.h_box.add(self.easy_button.with_space_around(left=30, right=30, bottom=550))

        self.medium_button = arcade.gui.UIFlatButton(text="Medium", width=250)
        self.h_box.add(self.medium_button.with_space_around(left=30, right=30, bottom=550))

        self.hard_button = arcade.gui.UIFlatButton(text="Hard", width=250)
        self.h_box.add(self.hard_button.with_space_around(left=30, right=30, bottom=550))        
    
       # assign buttons to actions
        self.easy_button.on_click = self.on_click_easy
        self.medium_button.on_click = self.on_click_medium
        self.hard_button.on_click = self.on_click_hard

      
        # Create a widget to hold the h_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.h_box)
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
        arcade.draw_lrtb_rectangle_outline(3,constants.START_SCREEN_WIDTH-3,constants.START_SCREEN_HEIGHT-3, 3,BLACK,5)
        arcade.draw_line(0,constants.START_SCREEN_HEIGHT - constants.HEADER,constants.START_SCREEN_WIDTH,constants.START_SCREEN_HEIGHT - constants.HEADER,BLACK,5)
        arcade.draw_lrtb_rectangle_filled(25,constants.START_SCREEN_WIDTH -25,(constants.START_SCREEN_HEIGHT - constants.HEADER) -25, 25, WHITE)
        arcade.draw_text("This is a game where using logic and a bit of luck you can clear the board of all of the mines.  Hopefully without getting blown up first!\n\nLeft click to dig out a square and expose what is beneath the surface, but be careful because if you dig up a mine it will blow up and you will lose.\n\n We have also buried a lot of clues for you to find so if you dig up a number it will let you know exactly how many mines are touching it.\n\nIf you are sure, you know where a mine is right click on it once to mark it with a flag, if you are not 100% sure right click twice to make it a question mark, and a third right click will return it to its original value so you can act like you were not even there.\n\nThat is pretty much it.  Once you have dug up every hole that does not have a min in it YOU WIN!",
                        70,
                        (constants.START_SCREEN_HEIGHT - constants.HEADER) -70,
                        arcade.color.BLACK,
                        17,
                        multiline=True,
                        width=constants.START_SCREEN_WIDTH - 140)
        arcade.draw_text("Select a difficulty above to start your game!",
                        0,
                        70,
                        arcade.color.BLACK,
                        30,
                        width=constants.START_SCREEN_WIDTH,
                        align="center")


     
  