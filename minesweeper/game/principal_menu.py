import arcade
import arcade.gui
from game import constants
from game.menu_view import MenuView


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

        # Create a vertical BoxGroup to align buttons
        self.v_box = arcade.gui.UIBoxLayout(
            x=0, y=0, vertical=False, align="top")

        # Create the buttons

        play = arcade.gui.UIFlatButton(text="Play", width=200)
        self.v_box.add(play.with_space_around(left=20, right=20))

        how_to_play = arcade.gui.UIFlatButton(text="How to Play", width=200)
        self.v_box.add(how_to_play.with_space_around(left=20, right=20))

        
       # assign buttons to actions
        play.on_click = self.click_level_view
        how_to_play.on_click = self.click_how_play
        

        # Create a widget to hold the v_box widget, that will center the buttons
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

    def click_level_view(self, event):
        print("easy:", event)
        self.level_view()

    def click_how_play(self):
        # print("Medium:", event)
        self.instructions()    

    def on_draw(self):
        """ Draw the menu """
        arcade.start_render()
        self.manager.draw()
       
    def level_view(self):
        
        view = MenuView()
        self.window.show_view(view)

    # def instructions(self):




