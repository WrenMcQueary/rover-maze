"""Rover maze game.  Working name: "Lab Rat"  Credit to MIT 6.004.1x for the idea!
The board is assumed square.
Canvas dimensions: 800px x 800px, 20cells x 20cells
Cell size (each maze portion is 1 cell wide): 40px x 40px
Throughout this project, the words "antenna" and "whisker" are used interchangeably.
"""

import presentation_tier


#
# TODOs
#

# TODO: BUGFIX: Rover can sometimes clip through diagonally connected walls (eg between the 1s in [[0, 1], [1, 0]])
# TODO: BUGFIX: Clean up the help messagebox.

# TODO: LOGISTICS: Do lots of playtesting!  Get help from KID Museum.

# TODO: INTERNAL QUALITY: Scan all handwritten/drawn docs and add to project folder.
# TODO: INTERNAL QUALITY: Current setup does not follow the principle of least knowledge very well.
# TODO: INTERNAL QUALITY: logic_tier.update_whisker_contact() and presentation_tier.redraw_canvas() have redundant functionality.
# TODO: INTERNAL QUALITY: logic_tier.update_whisker_contact() and logic_tier.is_rover_in_wall() have redundant functionality.
# TODO: INTERNAL QUALITY: Much of the functionality from logic_tier.UserProgramRunner was merged into presentation_tier.GUI.  Rename UserProgramRunner or adjust what it does to fit the name.

# TODO: IDEAS: Add Kaeden's bug art to the game!
# TODO: IDEAS: Simplify the UI by having a state determine actions, and whiskers only determine the next state.
# TODO: IDEAS: Include an option to enable/disable active status highlighting, because disabling this significantly speeds up the program.
# TODO: IDEAS: Gray out comboboxes with "Action n" and "Go to state (same)".
# TODO: IDEAS: Make a version with just 1 state.
# TODO: IDEAS: A way to save your FSM as a .txt and load it back up later.
# TODO: IDEAS: Add character select!  Different skins!
# TODO: IDEAS: Add different shapes to character select too?
# TODO: IDEAS: Make the bug do a little dance when it reaches the end of the maze!
# TODO: IDEAS: Let the bois tunnel by turning off collision for a bit?  Could be for a bird character or mole character.


#
# MAIN SCRIPT
#

# Create an instance of the GUI class.
my_gui = presentation_tier.GUI()
