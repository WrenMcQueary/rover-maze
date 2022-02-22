import logic_tier
import math
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import *


class GUI:
    """Manages the GUI for the game."""

    def __init__(self):
        """Initializes the GUI and puts it on the user's screen!"""
        self.user_program_runner = logic_tier.UserProgramRunner()
        self.play_pause_mode = "pause"  # Flag to tell the play() function when to stop.
        self.background_color = "#2B2B2B"   # Default background color for window.  Common choices are #F6C5A5 and #2B2B2B
        self.combobox_font_color = "#000000"  # Default font color for comboboxes.
        self.hall_color = "#ED7D30"     # Default hall color for canvas
        self.wall_color = "#2B2B2B"    # Default wall color for canvas
        self.rover_color = "#4472C4"    # Default rover color for canvas
        self.label_color = "#FFFFFF"    # Default color for labels
        self.illumination_color = "#FF5733"  # Default color for illuminating the active state, whisker status, and action.  One common choice is #FF5733

        self.window = tkinter.Tk()
        self.window.title("Rover Maze!")
        self.window.geometry("1600x1000")
        self.window["background"] = self.background_color

        # SPECIAL MESSAGE WIDGET
        self.label_special_message = tkinter.Label(self.window, text="", font=("Arial", 18), foreground=self.label_color, background=self.background_color)
        self.label_special_message.grid(row=0, column=1, rowspan=1, columnspan=7)

        # ANTENNAE WIDGETS
        self.label_no_antennae_touching = tkinter.Label(self.window, text="No antennae\ntouching wall", font=("Arial", 18), foreground=self.label_color, background=self.background_color)
        self.label_no_antennae_touching.grid(row=3, column=0, rowspan=5, columnspan=1)

        self.label_left_antenna_touching = tkinter.Label(self.window, text="Left antenna\ntouching wall", font=("Arial", 18), foreground=self.label_color, background=self.background_color)
        self.label_left_antenna_touching.grid(row=9, column=0, rowspan=5, columnspan=1)

        self.label_right_antenna_touching = tkinter.Label(self.window, text="Right antenna\ntouching wall", font=("Arial", 18), foreground=self.label_color, background=self.background_color)
        self.label_right_antenna_touching.grid(row=15, column=0, rowspan=5, columnspan=1)

        self.label_both_antennae_touching = tkinter.Label(self.window, text="Both antennae\ntouching wall", font=("Arial", 18), foreground=self.label_color, background=self.background_color)
        self.label_both_antennae_touching.grid(row=21, column=0, rowspan=5, columnspan=1)

        # STATE WIDGETS
        self.label_state_1 = tkinter.Label(self.window, text="State 1", font=("Arial", 18), foreground=self.label_color, background=self.background_color)
        self.label_state_1.grid(row=1, column=2)

        self.label_state_2 = tkinter.Label(self.window, text="State 2", font=("Arial", 18), foreground=self.label_color, background=self.background_color)
        self.label_state_2.grid(row=1, column=4)

        self.label_state_3 = tkinter.Label(self.window, text="State 3", font=("Arial", 18), foreground=self.label_color, background=self.background_color)
        self.label_state_3.grid(row=1, column=6)

        self.label_state_4 = tkinter.Label(self.window, text="State 4", font=("Arial", 18), foreground=self.label_color, background=self.background_color)
        self.label_state_4.grid(row=1, column=8)

        # COMBOBOXES FOR PROGRAMMING
        # State 1------------------------------
        # Whisker condition 1
        self.combobox_w1_s1_a1 = tkinter.ttk.Combobox(self.window)  # Stands for Whisker condition 1, State 1, Action 1
        self.combobox_w1_s1_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s1_a1.current(0)
        self.combobox_w1_s1_a1.grid(row=3, column=2)

        self.combobox_w1_s1_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s1_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s1_a2.current(0)
        self.combobox_w1_s1_a2.grid(row=4, column=2)

        self.combobox_w1_s1_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s1_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s1_a3.current(0)
        self.combobox_w1_s1_a3.grid(row=5, column=2)

        self.combobox_w1_s1_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s1_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s1_a4.current(0)
        self.combobox_w1_s1_a4.grid(row=6, column=2)

        self.combobox_w1_s1_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s1_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w1_s1_a5.current(0)
        self.combobox_w1_s1_a5.grid(row=7, column=2)

        # Whisker condition 2
        self.combobox_w2_s1_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s1_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s1_a1.current(0)
        self.combobox_w2_s1_a1.grid(row=9, column=2)

        self.combobox_w2_s1_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s1_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s1_a2.current(0)
        self.combobox_w2_s1_a2.grid(row=10, column=2)

        self.combobox_w2_s1_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s1_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s1_a3.current(0)
        self.combobox_w2_s1_a3.grid(row=11, column=2)

        self.combobox_w2_s1_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s1_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s1_a4.current(0)
        self.combobox_w2_s1_a4.grid(row=12, column=2)

        self.combobox_w2_s1_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s1_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w2_s1_a5.current(0)
        self.combobox_w2_s1_a5.grid(row=13, column=2)

        # Whisker condition 3
        self.combobox_w3_s1_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s1_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s1_a1.current(0)
        self.combobox_w3_s1_a1.grid(row=15, column=2)

        self.combobox_w3_s1_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s1_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s1_a2.current(0)
        self.combobox_w3_s1_a2.grid(row=16, column=2)

        self.combobox_w3_s1_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s1_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s1_a3.current(0)
        self.combobox_w3_s1_a3.grid(row=17, column=2)

        self.combobox_w3_s1_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s1_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s1_a4.current(0)
        self.combobox_w3_s1_a4.grid(row=18, column=2)

        self.combobox_w3_s1_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s1_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w3_s1_a5.current(0)
        self.combobox_w3_s1_a5.grid(row=19, column=2)

        # Whisker condition 4
        self.combobox_w4_s1_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s1_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s1_a1.current(0)
        self.combobox_w4_s1_a1.grid(row=21, column=2)

        self.combobox_w4_s1_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s1_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s1_a2.current(0)
        self.combobox_w4_s1_a2.grid(row=22, column=2)

        self.combobox_w4_s1_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s1_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s1_a3.current(0)
        self.combobox_w4_s1_a3.grid(row=23, column=2)

        self.combobox_w4_s1_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s1_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s1_a4.current(0)
        self.combobox_w4_s1_a4.grid(row=24, column=2)

        self.combobox_w4_s1_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s1_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w4_s1_a5.current(0)
        self.combobox_w4_s1_a5.grid(row=25, column=2)

        # State 2------------------------------
        # Whisker condition 1
        self.combobox_w1_s2_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s2_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s2_a1.current(0)
        self.combobox_w1_s2_a1.grid(row=3, column=4)

        self.combobox_w1_s2_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s2_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s2_a2.current(0)
        self.combobox_w1_s2_a2.grid(row=4, column=4)

        self.combobox_w1_s2_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s2_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s2_a3.current(0)
        self.combobox_w1_s2_a3.grid(row=5, column=4)

        self.combobox_w1_s2_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s2_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s2_a4.current(0)
        self.combobox_w1_s2_a4.grid(row=6, column=4)

        self.combobox_w1_s2_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s2_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w1_s2_a5.current(1)
        self.combobox_w1_s2_a5.grid(row=7, column=4)

        # Whisker condition 2
        self.combobox_w2_s2_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s2_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s2_a1.current(0)
        self.combobox_w2_s2_a1.grid(row=9, column=4)

        self.combobox_w2_s2_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s2_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s2_a2.current(0)
        self.combobox_w2_s2_a2.grid(row=10, column=4)

        self.combobox_w2_s2_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s2_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s2_a3.current(0)
        self.combobox_w2_s2_a3.grid(row=11, column=4)

        self.combobox_w2_s2_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s2_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s2_a4.current(0)
        self.combobox_w2_s2_a4.grid(row=12, column=4)

        self.combobox_w2_s2_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s2_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w2_s2_a5.current(1)
        self.combobox_w2_s2_a5.grid(row=13, column=4)

        # Whisker condition 3
        self.combobox_w3_s2_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s2_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s2_a1.current(0)
        self.combobox_w3_s2_a1.grid(row=15, column=4)

        self.combobox_w3_s2_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s2_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s2_a2.current(0)
        self.combobox_w3_s2_a2.grid(row=16, column=4)

        self.combobox_w3_s2_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s2_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s2_a3.current(0)
        self.combobox_w3_s2_a3.grid(row=17, column=4)

        self.combobox_w3_s2_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s2_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s2_a4.current(0)
        self.combobox_w3_s2_a4.grid(row=18, column=4)

        self.combobox_w3_s2_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s2_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w3_s2_a5.current(1)
        self.combobox_w3_s2_a5.grid(row=19, column=4)

        # Whisker condition 4
        self.combobox_w4_s2_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s2_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s2_a1.current(0)
        self.combobox_w4_s2_a1.grid(row=21, column=4)

        self.combobox_w4_s2_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s2_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s2_a2.current(0)
        self.combobox_w4_s2_a2.grid(row=22, column=4)

        self.combobox_w4_s2_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s2_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s2_a3.current(0)
        self.combobox_w4_s2_a3.grid(row=23, column=4)

        self.combobox_w4_s2_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s2_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s2_a4.current(0)
        self.combobox_w4_s2_a4.grid(row=24, column=4)

        self.combobox_w4_s2_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s2_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w4_s2_a5.current(1)
        self.combobox_w4_s2_a5.grid(row=25, column=4)

        # State 3------------------------------
        # Whisker condition 1
        self.combobox_w1_s3_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s3_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s3_a1.current(0)
        self.combobox_w1_s3_a1.grid(row=3, column=6)

        self.combobox_w1_s3_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s3_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s3_a2.current(0)
        self.combobox_w1_s3_a2.grid(row=4, column=6)

        self.combobox_w1_s3_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s3_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s3_a3.current(0)
        self.combobox_w1_s3_a3.grid(row=5, column=6)

        self.combobox_w1_s3_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s3_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s3_a4.current(0)
        self.combobox_w1_s3_a4.grid(row=6, column=6)

        self.combobox_w1_s3_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s3_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w1_s3_a5.current(2)
        self.combobox_w1_s3_a5.grid(row=7, column=6)

        # Whisker condition 2
        self.combobox_w2_s3_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s3_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s3_a1.current(0)
        self.combobox_w2_s3_a1.grid(row=9, column=6)

        self.combobox_w2_s3_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s3_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s3_a2.current(0)
        self.combobox_w2_s3_a2.grid(row=10, column=6)

        self.combobox_w2_s3_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s3_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s3_a3.current(0)
        self.combobox_w2_s3_a3.grid(row=11, column=6)

        self.combobox_w2_s3_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s3_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s3_a4.current(0)
        self.combobox_w2_s3_a4.grid(row=12, column=6)

        self.combobox_w2_s3_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s3_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w2_s3_a5.current(2)
        self.combobox_w2_s3_a5.grid(row=13, column=6)

        # Whisker condition 3
        self.combobox_w3_s3_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s3_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s3_a1.current(0)
        self.combobox_w3_s3_a1.grid(row=15, column=6)

        self.combobox_w3_s3_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s3_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s3_a2.current(0)
        self.combobox_w3_s3_a2.grid(row=16, column=6)

        self.combobox_w3_s3_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s3_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s3_a3.current(0)
        self.combobox_w3_s3_a3.grid(row=17, column=6)

        self.combobox_w3_s3_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s3_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s3_a4.current(0)
        self.combobox_w3_s3_a4.grid(row=18, column=6)

        self.combobox_w3_s3_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s3_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w3_s3_a5.current(2)
        self.combobox_w3_s3_a5.grid(row=19, column=6)

        # Whisker condition 4
        self.combobox_w4_s3_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s3_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s3_a1.current(0)
        self.combobox_w4_s3_a1.grid(row=21, column=6)

        self.combobox_w4_s3_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s3_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s3_a2.current(0)
        self.combobox_w4_s3_a2.grid(row=22, column=6)

        self.combobox_w4_s3_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s3_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s3_a3.current(0)
        self.combobox_w4_s3_a3.grid(row=23, column=6)

        self.combobox_w4_s3_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s3_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s3_a4.current(0)
        self.combobox_w4_s3_a4.grid(row=24, column=6)

        self.combobox_w4_s3_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s3_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w4_s3_a5.current(2)
        self.combobox_w4_s3_a5.grid(row=25, column=6)

        # State 4------------------------------
        # Whisker condition 1
        self.combobox_w1_s4_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s4_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s4_a1.current(0)
        self.combobox_w1_s4_a1.grid(row=3, column=8)

        self.combobox_w1_s4_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s4_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s4_a2.current(0)
        self.combobox_w1_s4_a2.grid(row=4, column=8)

        self.combobox_w1_s4_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s4_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s4_a3.current(0)
        self.combobox_w1_s4_a3.grid(row=5, column=8)

        self.combobox_w1_s4_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s4_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w1_s4_a4.current(0)
        self.combobox_w1_s4_a4.grid(row=6, column=8)

        self.combobox_w1_s4_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w1_s4_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w1_s4_a5.current(3)
        self.combobox_w1_s4_a5.grid(row=7, column=8)

        # Whisker condition 2
        self.combobox_w2_s4_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s4_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s4_a1.current(0)
        self.combobox_w2_s4_a1.grid(row=9, column=8)

        self.combobox_w2_s4_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s4_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s4_a2.current(0)
        self.combobox_w2_s4_a2.grid(row=10, column=8)

        self.combobox_w2_s4_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s4_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s4_a3.current(0)
        self.combobox_w2_s4_a3.grid(row=11, column=8)

        self.combobox_w2_s4_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s4_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w2_s4_a4.current(0)
        self.combobox_w2_s4_a4.grid(row=12, column=8)

        self.combobox_w2_s4_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w2_s4_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w2_s4_a5.current(3)
        self.combobox_w2_s4_a5.grid(row=13, column=8)

        # Whisker condition 3
        self.combobox_w3_s4_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s4_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s4_a1.current(0)
        self.combobox_w3_s4_a1.grid(row=15, column=8)

        self.combobox_w3_s4_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s4_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s4_a2.current(0)
        self.combobox_w3_s4_a2.grid(row=16, column=8)

        self.combobox_w3_s4_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s4_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s4_a3.current(0)
        self.combobox_w3_s4_a3.grid(row=17, column=8)

        self.combobox_w3_s4_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s4_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w3_s4_a4.current(0)
        self.combobox_w3_s4_a4.grid(row=18, column=8)

        self.combobox_w3_s4_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w3_s4_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w3_s4_a5.current(3)
        self.combobox_w3_s4_a5.grid(row=19, column=8)

        # Whisker condition 4
        self.combobox_w4_s4_a1 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s4_a1["values"] = ("Action 1", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s4_a1.current(0)
        self.combobox_w4_s4_a1.grid(row=21, column=8)

        self.combobox_w4_s4_a2 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s4_a2["values"] = ("Action 2", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s4_a2.current(0)
        self.combobox_w4_s4_a2.grid(row=22, column=8)

        self.combobox_w4_s4_a3 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s4_a3["values"] = ("Action 3", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s4_a3.current(0)
        self.combobox_w4_s4_a3.grid(row=23, column=8)

        self.combobox_w4_s4_a4 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s4_a4["values"] = ("Action 4", "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15")
        self.combobox_w4_s4_a4.current(0)
        self.combobox_w4_s4_a4.grid(row=24, column=8)

        self.combobox_w4_s4_a5 = tkinter.ttk.Combobox(self.window)
        self.combobox_w4_s4_a5["values"] = ("GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4")
        self.combobox_w4_s4_a5.current(3)
        self.combobox_w4_s4_a5.grid(row=25, column=8)

        # BORDERS BETWEEN COMBOBOXES
        self.border_horizontal_1 = tkinter.Label(self.window, text="", font=("Arial", 10), foreground=self.label_color, background=self.background_color)
        self.border_horizontal_1.grid(row=2, column=1, rowspan=1, columnspan=9)

        self.border_horizontal_2 = tkinter.Label(self.window, text="", font=("Arial", 10), foreground=self.label_color, background=self.background_color)
        self.border_horizontal_2.grid(row=8, column=1, rowspan=1, columnspan=9)

        self.border_horizontal_3 = tkinter.Label(self.window, text="", font=("Arial", 10), foreground=self.label_color, background=self.background_color)
        self.border_horizontal_3.grid(row=14, column=1, rowspan=1, columnspan=9)

        self.border_horizontal_4 = tkinter.Label(self.window, text="", font=("Arial", 10), foreground=self.label_color, background=self.background_color)
        self.border_horizontal_4.grid(row=20, column=1, rowspan=1, columnspan=9)

        self.border_horizontal_5 = tkinter.Label(self.window, text="", font=("Arial", 10), foreground=self.label_color, background=self.background_color)
        self.border_horizontal_5.grid(row=26, column=1, rowspan=1, columnspan=9)

        self.border_vertical_1 = tkinter.Label(self.window, text="", font=("Arial", 10), foreground=self.label_color, background=self.background_color)
        self.border_vertical_1.grid(row=2, column=1, rowspan=25, columnspan=1)

        self.border_vertical_2 = tkinter.Label(self.window, text="", font=("Arial", 10), foreground=self.label_color, background=self.background_color)
        self.border_vertical_2.grid(row=2, column=3, rowspan=25, columnspan=1)

        self.border_vertical_3 = tkinter.Label(self.window, text="", font=("Arial", 10), foreground=self.label_color, background=self.background_color)
        self.border_vertical_3.grid(row=2, column=5, rowspan=25, columnspan=1)

        self.border_vertical_4 = tkinter.Label(self.window, text="", font=("Arial", 10), foreground=self.label_color, background=self.background_color)
        self.border_vertical_4.grid(row=2, column=7, rowspan=25, columnspan=1)

        self.border_vertical_5 = tkinter.Label(self.window, text="", font=("Arial", 10), foreground=self.label_color, background=self.background_color)
        self.border_vertical_5.grid(row=2, column=9, rowspan=25, columnspan=1)

        # BUTTON WIDGETS
        def update_one_step():
            """Gets Physics to simulate another frame of the simulation.
            Checks to see if the rover has won.  Returns True if so, else False.
            Alters rover.state, rover.action, rover.left_touch, and rover.right_touch.
            """

            def execute_rover_command(input_string):
                """Calls the appropriate rover move from logic_tier based on input_string
                To make this helper function do anything other than pass, input_string should be
                one of the following: "FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15", "GO TO STATE 1", "GO TO STATE 2",
                "GO TO STATE 3", "GO TO STATE 4", "GO TO STATE 5".
                """
                if input_string not in ["FORWARD 5", "BACK 5", "LEFT 15", "RIGHT 15", "GO TO STATE 1", "GO TO STATE 2", "GO TO STATE 3", "GO TO STATE 4", "GO TO STATE 5"]:
                    return

                if input_string == "FORWARD 5":
                    self.user_program_runner.physics.move_forward(5)
                elif input_string == "BACK 5":
                    self.user_program_runner.physics.move_backward(5)
                elif input_string == "LEFT 15":
                    self.user_program_runner.physics.turn_left(15 * math.pi / 180)
                elif input_string == "RIGHT 15":
                    self.user_program_runner.physics.turn_right(15 * math.pi / 180)
                elif input_string[:-1] == "GO TO STATE ":
                    self.user_program_runner.physics.rover.state = int(input_string[-1])

            def congratulate_for_winning():
                """Produces a popup to congratulate the player for reaching the goal!"""
                self.user_program_runner.physics.current_maze.has_player_won = True
                messagebox.showinfo("Congratulations!!!", "Nice work coding your robot!  You've reached the end of the maze!\nTo test your same code on a new maze, try clicking the 'New Maze' button!  Your code will still be there if you make a new maze, but not if you close out of the game.")

            # Get the current action int, state int, and 2 whisker booleans.
            current_action = self.user_program_runner.physics.rover.action
            current_state = self.user_program_runner.physics.rover.state
            current_left_touch = self.user_program_runner.left_touch
            current_right_touch = self.user_program_runner.right_touch

            # Execute the user-set instruction (if any) that the above values indicate.
            if current_state == 1:
                if not current_left_touch and not current_right_touch:  # If neither whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w1_s1_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w1_s1_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w1_s1_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w1_s1_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w1_s1_a5.get())
                if current_left_touch and not current_right_touch:  # If left whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w2_s1_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w2_s1_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w2_s1_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w2_s1_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w2_s1_a5.get())
                if not current_left_touch and current_right_touch:  # If right whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w3_s1_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w3_s1_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w3_s1_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w3_s1_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w3_s1_a5.get())
                if current_left_touch and current_right_touch:  # If both whiskers touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w4_s1_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w4_s1_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w4_s1_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w4_s1_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w4_s1_a5.get())
            elif current_state == 2:
                if not current_left_touch and not current_right_touch:  # If neither whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w1_s2_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w1_s2_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w1_s2_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w1_s2_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w1_s2_a5.get())
                if current_left_touch and not current_right_touch:  # If left whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w2_s2_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w2_s2_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w2_s2_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w2_s2_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w2_s2_a5.get())
                if not current_left_touch and current_right_touch:  # If right whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w3_s2_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w3_s2_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w3_s2_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w3_s2_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w3_s2_a5.get())
                if current_left_touch and current_right_touch:  # If both whiskers touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w4_s2_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w4_s2_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w4_s2_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w4_s2_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w4_s2_a5.get())
            elif current_state == 3:
                if not current_left_touch and not current_right_touch:  # If neither whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w1_s3_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w1_s3_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w1_s3_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w1_s3_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w1_s3_a5.get())
                if current_left_touch and not current_right_touch:  # If left whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w2_s3_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w2_s3_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w2_s3_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w2_s3_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w2_s3_a5.get())
                if not current_left_touch and current_right_touch:  # If right whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w3_s3_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w3_s3_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w3_s3_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w3_s3_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w3_s3_a5.get())
                if current_left_touch and current_right_touch:  # If both whiskers touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w4_s3_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w4_s3_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w4_s3_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w4_s3_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w4_s3_a5.get())
            elif current_state == 4:
                if not current_left_touch and not current_right_touch:  # If neither whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w1_s4_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w1_s4_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w1_s4_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w1_s4_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w1_s4_a5.get())
                if current_left_touch and not current_right_touch:  # If left whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w2_s4_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w2_s4_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w2_s4_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w2_s4_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w2_s4_a5.get())
                if not current_left_touch and current_right_touch:  # If right whisker touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w3_s4_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w3_s4_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w3_s4_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w3_s4_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w3_s4_a5.get())
                if current_left_touch and current_right_touch:  # If both whiskers touching:
                    if current_action == 1:
                        execute_rover_command(self.combobox_w4_s4_a1.get())
                    if current_action == 2:
                        execute_rover_command(self.combobox_w4_s4_a2.get())
                    if current_action == 3:
                        execute_rover_command(self.combobox_w4_s4_a3.get())
                    if current_action == 4:
                        execute_rover_command(self.combobox_w4_s4_a4.get())
                    if current_action == 5:
                        execute_rover_command(self.combobox_w4_s4_a5.get())

            # Update rover.action, and if it's now 1, recalculate rover.left_touch and rover.right_touch.
            self.user_program_runner.physics.rover.action = self.user_program_runner.physics.rover.action % 5 + 1
            if self.user_program_runner.physics.rover.action == 1:
                self.user_program_runner.update_whisker_statuses()

            # Update the canvas.
            self.redraw_canvas()

            # Illuminate active statuses for the next step which will happen!
            self.illuminate_statuses()

            # If the rover has won, produce a special popup!
            if not self.user_program_runner.physics.current_maze.has_player_won:
                if self.user_program_runner.physics.current_maze.goal.ctl[0] <= self.user_program_runner.physics.rover.pos[0] <= self.user_program_runner.physics.current_maze.goal.cbr[0]:
                    if self.user_program_runner.physics.current_maze.goal.cbr[1] <= self.user_program_runner.physics.rover.pos[1] <= self.user_program_runner.physics.current_maze.goal.ctl[1]:
                        congratulate_for_winning()

        def display_help():  # TODO
            """Displays a popup with help text."""  # TODO: Explain that your work persists between mazes, but it is not saved if you relaunch the program.
            pass    # TODO: Indicate that the active status is highlighted BEFORE it is acted upon.

        def play():
            """Calls update_one_step multiple times."""
            self.play_pause_mode = "play"
            while self.play_pause_mode == "play":
                update_one_step()

        def pause():
            """Stops updating frames of the simulation."""
            self.play_pause_mode = "pause"

        def reset():
            """Resets the simulation to its initial setup, including resetting the rover's internal state."""
            pause()
            # Save a copy of the maze
            maze_backup = self.user_program_runner.physics.current_maze
            # Reinitialize Physics
            self.user_program_runner.physics = logic_tier.Physics()
            # Replace the automatically generated new maze with the old one.
            self.user_program_runner.physics.current_maze = maze_backup
            self.redraw_canvas()
            self.illuminate_statuses()

        def new_maze():
            """Calls for a new maze to be generated, and a reset to the rover's position and state."""
            pause()
            self.user_program_runner.physics = logic_tier.Physics()
            self.redraw_canvas()
            self.illuminate_statuses()

        self.photo_help = PhotoImage(file="Button Images/Help.png")
        self.button_help = tkinter.Button(self.window, image=self.photo_help, command=display_help)
        self.button_help.grid(row=27, column=4)

        self.photo_play = PhotoImage(file="Button Images/Play.png")
        self.button_play = tkinter.Button(self.window, image=self.photo_play, command=play)
        self.button_play.grid(row=27, column=10)

        self.photo_pause = PhotoImage(file="Button Images/Pause.png")
        self.button_pause = tkinter.Button(self.window, image=self.photo_pause, command=pause)
        self.button_pause.grid(row=27, column=11)

        self.photo_step = PhotoImage(file="Button Images/Step.png")
        self.button_step = tkinter.Button(self.window, image=self.photo_step, command=update_one_step)
        self.button_step.grid(row=27, column=12)

        self.photo_stop = PhotoImage(file="Button Images/Stop.png")
        self.button_stop = tkinter.Button(self.window, image=self.photo_stop, command=reset)
        self.button_stop.grid(row=27, column=13)

        self.photo_new_maze = PhotoImage(file="Button Images/New Maze.png")
        self.button_new_maze = tkinter.Button(self.window, image=self.photo_new_maze, command=new_maze)
        self.button_new_maze.grid(row=27, column=14)

        # CANVAS WIDGET
        self.canvas = tkinter.Canvas(self.window, width=800, height=800, background=self.hall_color)
        self.canvas.grid(row=0, column=10, rowspan=25, columnspan=5)

        # MAIN LOOP
        self.canvas.after(500, self.redraw_canvas)
        self.canvas.after(500, self.illuminate_statuses)
        self.window.mainloop()

    def redraw_canvas(self):
        """Updates the canvas."""

        def physics_coords_to_tkinter_coords(physics_coords):
            """Converts from the physics coordinate system to the tkinter canvas coordinate system.
            physics_coords is a list of 2 floats.
            """
            return [physics_coords[0], 800 - physics_coords[1]]

        # Wipe old contents of canvas.
        self.canvas.delete("all")

        # Draw the walls of the maze to the canvas.
        for wall in self.user_program_runner.physics.current_maze.walls:
            this_ctl_in_tk_coords = physics_coords_to_tkinter_coords(wall.ctl)
            this_cbr_in_tk_coords = physics_coords_to_tkinter_coords(wall.cbr)
            self.canvas.create_rectangle(this_ctl_in_tk_coords[0], this_ctl_in_tk_coords[1], this_cbr_in_tk_coords[0], this_cbr_in_tk_coords[1], outline=self.wall_color, fill=self.wall_color)

        # Draw the goal of the maze to the canvas.
        goal_ctl_in_tk_coords = physics_coords_to_tkinter_coords(self.user_program_runner.physics.current_maze.goal.ctl)
        goal_cbr_in_tk_coords = physics_coords_to_tkinter_coords(self.user_program_runner.physics.current_maze.goal.cbr)
        self.canvas.create_rectangle(goal_ctl_in_tk_coords[0], goal_ctl_in_tk_coords[1], goal_cbr_in_tk_coords[0], goal_cbr_in_tk_coords[1], fill="green")

        # Draw the rover's body and antennae to the canvas.
        rover_pos = self.user_program_runner.physics.rover.pos
        rover_rad = self.user_program_runner.physics.rover.body_radius
        rover_ang = self.user_program_runner.physics.rover.body_angle
        whisker_dis = self.user_program_runner.physics.rover.whisker_distance
        whisker_ang = self.user_program_runner.physics.rover.whisker_angle
        whisker_rad = self.user_program_runner.physics.rover.whisker_radius
        left_whisker_tip = [rover_pos[0] + math.cos(rover_ang + whisker_ang) * whisker_dis, rover_pos[1] + math.sin(rover_ang + whisker_ang) * whisker_dis]
        right_whisker_tip = [rover_pos[0] + math.cos(rover_ang - whisker_ang) * whisker_dis, rover_pos[1] + math.sin(rover_ang - whisker_ang) * whisker_dis]

        rover_pos_in_tk_coords = physics_coords_to_tkinter_coords(rover_pos)
        rover_ctl_in_tk_coords = physics_coords_to_tkinter_coords([rover_pos[0] - rover_rad, rover_pos[1] + rover_rad])
        rover_cbr_in_tk_coords = physics_coords_to_tkinter_coords([rover_pos[0] + rover_rad, rover_pos[1] - rover_rad])

        left_whisker_tip_in_tk_coords = physics_coords_to_tkinter_coords(left_whisker_tip)
        right_whisker_tip_in_tk_coords = physics_coords_to_tkinter_coords(right_whisker_tip)

        left_whisker_ctl_in_tk_coords = physics_coords_to_tkinter_coords([left_whisker_tip[0] - whisker_rad, left_whisker_tip[1] + whisker_rad])
        left_whisker_cbr_in_tk_coords = physics_coords_to_tkinter_coords([left_whisker_tip[0] + whisker_rad, left_whisker_tip[1] - whisker_rad])
        right_whisker_ctl_in_tk_coords = physics_coords_to_tkinter_coords([right_whisker_tip[0] - whisker_rad, right_whisker_tip[1] + whisker_rad])
        right_whisker_cbr_in_tk_coords = physics_coords_to_tkinter_coords([right_whisker_tip[0] + whisker_rad, right_whisker_tip[1] - whisker_rad])

        self.canvas.create_line(rover_pos_in_tk_coords[0], rover_pos_in_tk_coords[1], left_whisker_tip_in_tk_coords[0], left_whisker_tip_in_tk_coords[1], fill=self.rover_color)    # Left antenna line
        self.canvas.create_line(rover_pos_in_tk_coords[0], rover_pos_in_tk_coords[1], right_whisker_tip_in_tk_coords[0], right_whisker_tip_in_tk_coords[1], fill=self.rover_color)    # Right antenna line
        self.canvas.create_oval(rover_ctl_in_tk_coords[0], rover_ctl_in_tk_coords[1], rover_cbr_in_tk_coords[0], rover_cbr_in_tk_coords[1], fill=self.rover_color)    # Body
        self.canvas.create_oval(left_whisker_ctl_in_tk_coords[0], left_whisker_ctl_in_tk_coords[1], left_whisker_cbr_in_tk_coords[0], left_whisker_cbr_in_tk_coords[1], fill=self.rover_color)   # Left antenna bulb
        self.canvas.create_oval(right_whisker_ctl_in_tk_coords[0], right_whisker_ctl_in_tk_coords[1], right_whisker_cbr_in_tk_coords[0], right_whisker_cbr_in_tk_coords[1], fill=self.rover_color)   # Right antenna bulb

        # Update the canvas.
        self.canvas.update()

    def illuminate_statuses(self):
        """Indicates the current state, antenna status, and action, as well as highlighting the rover's own whiskers
        on the canvas if touching a wall.
        """
        # Undo all highlights.
        self.label_state_1.config(background=self.background_color)
        self.label_state_2.config(background=self.background_color)
        self.label_state_3.config(background=self.background_color)
        self.label_state_4.config(background=self.background_color)

        self.label_no_antennae_touching.config(background=self.background_color)
        self.label_left_antenna_touching.config(background=self.background_color)
        self.label_right_antenna_touching.config(background=self.background_color)
        self.label_both_antennae_touching.config(background=self.background_color)

        self.combobox_w1_s1_a1.config(foreground=self.combobox_font_color)
        self.combobox_w1_s1_a2.config(foreground=self.combobox_font_color)
        self.combobox_w1_s1_a3.config(foreground=self.combobox_font_color)
        self.combobox_w1_s1_a4.config(foreground=self.combobox_font_color)
        self.combobox_w1_s1_a5.config(foreground=self.combobox_font_color)

        self.combobox_w2_s1_a1.config(foreground=self.combobox_font_color)
        self.combobox_w2_s1_a2.config(foreground=self.combobox_font_color)
        self.combobox_w2_s1_a3.config(foreground=self.combobox_font_color)
        self.combobox_w2_s1_a4.config(foreground=self.combobox_font_color)
        self.combobox_w2_s1_a5.config(foreground=self.combobox_font_color)

        self.combobox_w3_s1_a1.config(foreground=self.combobox_font_color)
        self.combobox_w3_s1_a2.config(foreground=self.combobox_font_color)
        self.combobox_w3_s1_a3.config(foreground=self.combobox_font_color)
        self.combobox_w3_s1_a4.config(foreground=self.combobox_font_color)
        self.combobox_w3_s1_a5.config(foreground=self.combobox_font_color)

        self.combobox_w4_s1_a1.config(foreground=self.combobox_font_color)
        self.combobox_w4_s1_a2.config(foreground=self.combobox_font_color)
        self.combobox_w4_s1_a3.config(foreground=self.combobox_font_color)
        self.combobox_w4_s1_a4.config(foreground=self.combobox_font_color)
        self.combobox_w4_s1_a5.config(foreground=self.combobox_font_color)

        self.combobox_w1_s2_a1.config(foreground=self.combobox_font_color)
        self.combobox_w1_s2_a2.config(foreground=self.combobox_font_color)
        self.combobox_w1_s2_a3.config(foreground=self.combobox_font_color)
        self.combobox_w1_s2_a4.config(foreground=self.combobox_font_color)
        self.combobox_w1_s2_a5.config(foreground=self.combobox_font_color)

        self.combobox_w2_s2_a1.config(foreground=self.combobox_font_color)
        self.combobox_w2_s2_a2.config(foreground=self.combobox_font_color)
        self.combobox_w2_s2_a3.config(foreground=self.combobox_font_color)
        self.combobox_w2_s2_a4.config(foreground=self.combobox_font_color)
        self.combobox_w2_s2_a5.config(foreground=self.combobox_font_color)

        self.combobox_w3_s2_a1.config(foreground=self.combobox_font_color)
        self.combobox_w3_s2_a2.config(foreground=self.combobox_font_color)
        self.combobox_w3_s2_a3.config(foreground=self.combobox_font_color)
        self.combobox_w3_s2_a4.config(foreground=self.combobox_font_color)
        self.combobox_w3_s2_a5.config(foreground=self.combobox_font_color)

        self.combobox_w4_s2_a1.config(foreground=self.combobox_font_color)
        self.combobox_w4_s2_a2.config(foreground=self.combobox_font_color)
        self.combobox_w4_s2_a3.config(foreground=self.combobox_font_color)
        self.combobox_w4_s2_a4.config(foreground=self.combobox_font_color)
        self.combobox_w4_s2_a5.config(foreground=self.combobox_font_color)

        self.combobox_w1_s3_a1.config(foreground=self.combobox_font_color)
        self.combobox_w1_s3_a2.config(foreground=self.combobox_font_color)
        self.combobox_w1_s3_a3.config(foreground=self.combobox_font_color)
        self.combobox_w1_s3_a4.config(foreground=self.combobox_font_color)
        self.combobox_w1_s3_a5.config(foreground=self.combobox_font_color)

        self.combobox_w2_s3_a1.config(foreground=self.combobox_font_color)
        self.combobox_w2_s3_a2.config(foreground=self.combobox_font_color)
        self.combobox_w2_s3_a3.config(foreground=self.combobox_font_color)
        self.combobox_w2_s3_a4.config(foreground=self.combobox_font_color)
        self.combobox_w2_s3_a5.config(foreground=self.combobox_font_color)

        self.combobox_w3_s3_a1.config(foreground=self.combobox_font_color)
        self.combobox_w3_s3_a2.config(foreground=self.combobox_font_color)
        self.combobox_w3_s3_a3.config(foreground=self.combobox_font_color)
        self.combobox_w3_s3_a4.config(foreground=self.combobox_font_color)
        self.combobox_w3_s3_a5.config(foreground=self.combobox_font_color)

        self.combobox_w4_s3_a1.config(foreground=self.combobox_font_color)
        self.combobox_w4_s3_a2.config(foreground=self.combobox_font_color)
        self.combobox_w4_s3_a3.config(foreground=self.combobox_font_color)
        self.combobox_w4_s3_a4.config(foreground=self.combobox_font_color)
        self.combobox_w4_s3_a5.config(foreground=self.combobox_font_color)

        self.combobox_w1_s4_a1.config(foreground=self.combobox_font_color)
        self.combobox_w1_s4_a2.config(foreground=self.combobox_font_color)
        self.combobox_w1_s4_a3.config(foreground=self.combobox_font_color)
        self.combobox_w1_s4_a4.config(foreground=self.combobox_font_color)
        self.combobox_w1_s4_a5.config(foreground=self.combobox_font_color)

        self.combobox_w2_s4_a1.config(foreground=self.combobox_font_color)
        self.combobox_w2_s4_a2.config(foreground=self.combobox_font_color)
        self.combobox_w2_s4_a3.config(foreground=self.combobox_font_color)
        self.combobox_w2_s4_a4.config(foreground=self.combobox_font_color)
        self.combobox_w2_s4_a5.config(foreground=self.combobox_font_color)

        self.combobox_w3_s4_a1.config(foreground=self.combobox_font_color)
        self.combobox_w3_s4_a2.config(foreground=self.combobox_font_color)
        self.combobox_w3_s4_a3.config(foreground=self.combobox_font_color)
        self.combobox_w3_s4_a4.config(foreground=self.combobox_font_color)
        self.combobox_w3_s4_a5.config(foreground=self.combobox_font_color)

        self.combobox_w4_s4_a1.config(foreground=self.combobox_font_color)
        self.combobox_w4_s4_a2.config(foreground=self.combobox_font_color)
        self.combobox_w4_s4_a3.config(foreground=self.combobox_font_color)
        self.combobox_w4_s4_a4.config(foreground=self.combobox_font_color)
        self.combobox_w4_s4_a5.config(foreground=self.combobox_font_color)

        # Get information with which to highlight.
        current_action = self.user_program_runner.physics.rover.action
        current_state = self.user_program_runner.physics.rover.state
        current_left_touch = self.user_program_runner.left_touch
        current_right_touch = self.user_program_runner.right_touch

        # Highlight the appropriate state.
        if current_state == 1:
            self.label_state_1.config(background=self.illumination_color)
        elif current_state == 2:
            self.label_state_2.config(background=self.illumination_color)
        elif current_state == 3:
            self.label_state_3.config(background=self.illumination_color)
        elif current_state == 4:
            self.label_state_4.config(background=self.illumination_color)

        # Highlight the appropriate antenna status.
        if not current_left_touch and not current_right_touch:
            self.label_no_antennae_touching.config(background=self.illumination_color)
        elif current_left_touch and not current_right_touch:
            self.label_left_antenna_touching.config(background=self.illumination_color)
        elif not current_left_touch and current_right_touch:
            self.label_right_antenna_touching.config(background=self.illumination_color)
        elif current_left_touch and current_right_touch:
            self.label_both_antennae_touching.config(background=self.illumination_color)

        # Highlight the appropriate action.
        if current_state == 1:
            if not current_left_touch and not current_right_touch:  # If neither whisker touching:
                if current_action == 1:
                    self.combobox_w1_s1_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w1_s1_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w1_s1_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w1_s1_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w1_s1_a5.config(foreground=self.illumination_color)
            if current_left_touch and not current_right_touch:  # If left whisker touching:
                if current_action == 1:
                    self.combobox_w2_s1_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w2_s1_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w2_s1_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w2_s1_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w2_s1_a5.config(foreground=self.illumination_color)
            if not current_left_touch and current_right_touch:  # If right whisker touching:
                if current_action == 1:
                    self.combobox_w3_s1_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w3_s1_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w3_s1_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w3_s1_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w3_s1_a5.config(foreground=self.illumination_color)
            if current_left_touch and current_right_touch:  # If both whiskers touching:
                if current_action == 1:
                    self.combobox_w4_s1_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w4_s1_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w4_s1_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w4_s1_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w4_s1_a5.config(foreground=self.illumination_color)
        elif current_state == 2:
            if not current_left_touch and not current_right_touch:  # If neither whisker touching:
                if current_action == 1:
                    self.combobox_w1_s2_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w1_s2_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w1_s2_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w1_s2_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w1_s2_a5.config(foreground=self.illumination_color)
            if current_left_touch and not current_right_touch:  # If left whisker touching:
                if current_action == 1:
                    self.combobox_w2_s2_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w2_s2_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w2_s2_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w2_s2_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w2_s2_a5.config(foreground=self.illumination_color)
            if not current_left_touch and current_right_touch:  # If right whisker touching:
                if current_action == 1:
                    self.combobox_w3_s2_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w3_s2_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w3_s2_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w3_s2_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w3_s2_a5.config(foreground=self.illumination_color)
            if current_left_touch and current_right_touch:  # If both whiskers touching:
                if current_action == 1:
                    self.combobox_w4_s2_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w4_s2_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w4_s2_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w4_s2_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w4_s2_a5.config(foreground=self.illumination_color)
        elif current_state == 3:
            if not current_left_touch and not current_right_touch:  # If neither whisker touching:
                if current_action == 1:
                    self.combobox_w1_s3_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w1_s3_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w1_s3_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w1_s3_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w1_s3_a5.config(foreground=self.illumination_color)
            if current_left_touch and not current_right_touch:  # If left whisker touching:
                if current_action == 1:
                    self.combobox_w2_s3_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w2_s3_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w2_s3_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w2_s3_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w2_s3_a5.config(foreground=self.illumination_color)
            if not current_left_touch and current_right_touch:  # If right whisker touching:
                if current_action == 1:
                    self.combobox_w3_s3_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w3_s3_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w3_s3_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w3_s3_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w3_s3_a5.config(foreground=self.illumination_color)
            if current_left_touch and current_right_touch:  # If both whiskers touching:
                if current_action == 1:
                    self.combobox_w4_s3_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w4_s3_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w4_s3_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w4_s3_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w4_s3_a5.config(foreground=self.illumination_color)
        elif current_state == 4:
            if not current_left_touch and not current_right_touch:  # If neither whisker touching:
                if current_action == 1:
                    self.combobox_w1_s4_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w1_s4_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w1_s4_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w1_s4_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w1_s4_a5.config(foreground=self.illumination_color)
            if current_left_touch and not current_right_touch:  # If left whisker touching:
                if current_action == 1:
                    self.combobox_w2_s4_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w2_s4_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w2_s4_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w2_s4_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w2_s4_a5.config(foreground=self.illumination_color)
            if not current_left_touch and current_right_touch:  # If right whisker touching:
                if current_action == 1:
                    self.combobox_w3_s4_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w3_s4_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w3_s4_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w3_s4_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w3_s4_a5.config(foreground=self.illumination_color)
            if current_left_touch and current_right_touch:  # If both whiskers touching:
                if current_action == 1:
                    self.combobox_w4_s4_a1.config(foreground=self.illumination_color)
                if current_action == 2:
                    self.combobox_w4_s4_a2.config(foreground=self.illumination_color)
                if current_action == 3:
                    self.combobox_w4_s4_a3.config(foreground=self.illumination_color)
                if current_action == 4:
                    self.combobox_w4_s4_a4.config(foreground=self.illumination_color)
                if current_action == 5:
                    self.combobox_w4_s4_a5.config(foreground=self.illumination_color)
