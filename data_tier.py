"""All positional data in the data tier that uses pixel units uses a right-handed coordinate system with (0, 0) being
the bottom-right-hand corner of the maze.  This coordinate system is called "physics coordinates" throughout the code.
"""

import copy
import random
import math
import numpy as np

class Maze:
    """Fully defines a maze for the rover to explore."""

    def __init__(self):
        """walls is a list of Zone objects.
        goal is a Zone object.
        has_player_won is a boolean, which keeps track of whether the player has won for this particular maze before.
        """
        (self.walls, self.goal) = self.generate_walls_and_goal()
        self.has_player_won = False

    def generate_walls_and_goal(self):
        """Randomly generates walls and the goal for this maze.
        Uses Prim's Algorithm: https://en.wikipedia.org/wiki/Prim%27s_algorithm
        """
        # TODO: Rework so that diagonally-touching halls are not generated, and so that all walls and halls have thickness of exactly 1 cell.

        def remove_duplicates_from_list(input_list):
            """Returns a version of input_list such that redundant elements are removed."""
            output_list = []
            for item in input_list:
                if item not in output_list:
                    output_list.append(item)
            return output_list

        def get_all_1_neighbors_of_0s(input_array):
            """Returns a list of all indices for neighbors of 0s which are not themselves 0s.
            input_array is an ndarray containing 0s.
            """
            input_height = np.shape(input_array)[0]
            input_width = np.shape(input_array)[1]
            neighbor_indices = []
            for rr in range(input_height):
                for cc in range(input_width):
                    if input_array[rr, cc] == 0:
                        # Check all neighbors.  Add the indices of neighboring non-0s to neighbor_indices.
                        # Upper neighbor
                        if rr - 1 in range(input_height):
                            if input_array[rr - 1, cc] != 0:
                                neighbor_indices.append([rr - 1, cc])
                        # Lower neighbor
                        if rr + 1 in range(input_height):
                            if input_array[rr + 1, cc] != 0:
                                neighbor_indices.append([rr + 1, cc])
                        # Left neighbor
                        if cc - 1 in range(input_width):
                            if input_array[rr, cc - 1] != 0:
                                neighbor_indices.append([rr, cc - 1])
                        # Right neighbor
                        if cc + 1 in range(input_width):
                            if input_array[rr, cc + 1] != 0:
                                neighbor_indices.append([rr, cc + 1])
            neighbor_indices = remove_duplicates_from_list(neighbor_indices)
            return neighbor_indices

        def does_it_have_3_or_more_0_neighbors(query_index, array):
            """Returns True if the cell at query_index has 2 or more neighbors of 0 in any direction
            (not just crosswise).  Else returns False.
            query_index is a list of 2 integers.
            array is an ndarray
            """
            neighbor_counter = 0
            input_height = np.shape(array)[0]
            input_width = np.shape(array)[1]
            r = query_index[0]
            c = query_index[1]
            # Check upper
            if r - 1 in range(input_height):
                if array[r - 1, c] == 0:
                    neighbor_counter += 1
                # Check upper-left
                if c - 1 in range(input_width):
                    if array[r - 1, c - 1] == 0:
                        neighbor_counter += 1
                # Check upper-right
                if c + 1 in range(input_width):
                    if array[r - 1, c + 1] == 0:
                        neighbor_counter += 1
            # Check lower
            if r + 1 in range(input_height):
                if array[r + 1, c] == 0:
                    neighbor_counter += 1
                # Check lower-left
                if c - 1 in range(input_width):
                    if array[r + 1, c - 1] == 0:
                        neighbor_counter += 1
                # Check lower-right
                if c + 1 in range(input_width):
                    if array[r + 1, c + 1] == 0:
                        neighbor_counter += 1
            # Check left
            if c - 1 in range(input_width):
                if array[r, c - 1] == 0:
                    neighbor_counter += 1
            # Check right
            if c + 1 in range(input_width):
                if array[r, c + 1] == 0:
                    neighbor_counter += 1

            # Return based on neighbor_counter.
            if neighbor_counter >= 3:
                return True
            else:
                return False

        def euclidean_dist(pos0, pos1):
            """Returns the distance between pos0 and pos1.
            pos0 is a list of 2 floats, representing a coordinate pair.
            pos1 is a list of 2 floats, representing a coordinate pair.
            Returns a float.
            """
            x0 = pos0[0]
            y0 = pos0[1]
            x1 = pos1[0]
            y1 = pos1[1]
            return ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** 0.5

        def tkinter_coords_to_physics_coords(tkinter_coords):
            """Converts from the tkinter canvas coordinate system to the physics coordinate system.
            tkinter_coords is a list of 2 floats.
            """
            return [800 - tkinter_coords[0], tkinter_coords[1]]

        maze_length = 800   # pixels; the maze is assumed square.  maze_length must be divisible by cell_length.
        cell_length = 40    # pixels; each cell is assumed square.  cell_length must divide maze_length.
        prims_array_length = int(maze_length / cell_length)     # nodes in an array.

        # Create an nxn array, where n = prims_array_length.  Randomly weight each cell.
        weight_array = np.array([[random.random() for _ in range(prims_array_length)] for _ in range(prims_array_length)])

        # Create an nxn array of 0s (halls) and 1s (walls).  At first, have it all be walls.
        halls_and_walls_array = np.array([[1 for _ in range(prims_array_length)] for _ in range(prims_array_length)])   # Initially everything is a wall.
        # Mark the bottom-left spot as a hall.  This will be the starting point.
        halls_and_walls_array[prims_array_length - 1, 0] = 0

        # Generate the rest of the maze.
        are_walls_done = False
        while not are_walls_done:     # Each cycle of this loop creates exactly one new hall cell.
            neighbors = get_all_1_neighbors_of_0s(halls_and_walls_array)    # Get the indices of all walls that are neighbors of a hall.
            # Of the wall cells neighboring a hall cell in halls_and_walls_array, make the one with lowest weight in weight_array a hall.  But if that wall is adjacent to 2 or more hall tiles, try the next-lowest-weight neighboring wall instead.  If you find no such walls, break; the maze is complete.
            while True:
                # Find the index with the lowest weight in neighbors.
                lowest_index = neighbors[0]
                lowest_weight = weight_array[lowest_index[0], lowest_index[1]]
                for index in neighbors:
                    this_weight = weight_array[index[0], index[1]]
                    if this_weight < lowest_weight:
                        lowest_weight = this_weight
                        lowest_index = index
                # If this wall is not adjacent to another hall, turn it into a wall and break, because it's time to make a new hall cell!
                if not does_it_have_3_or_more_0_neighbors(lowest_index, halls_and_walls_array):
                    halls_and_walls_array[lowest_index[0], lowest_index[1]] = 0
                    break
                else:   # Else remove this wall from neighbors and try again, unless neighbors is empty, in which case the maze is complete!
                    neighbors.remove(lowest_index)
                    if len(neighbors) == 0:
                        are_walls_done = True
                        break

        # Put a goal marker at a point of the maze farthest from the bottom-left spot!
        # Find a hall spot with the greatest distance from the bottom-left tile.
        greatest_index = [prims_array_length - 1, 0]
        greatest_distance = 0
        for rr in range(prims_array_length):
            for cc in range(prims_array_length):
                if halls_and_walls_array[rr, cc] == 0:
                    this_distance = euclidean_dist([prims_array_length - 1, 0], [rr, cc])
                    if this_distance > greatest_distance:
                        greatest_index = [rr, cc]
                        greatest_distance = this_distance
        # Change the 0 of that hall to a 2, to represent a goal.
        halls_and_walls_array[greatest_index[0], greatest_index[1]] = 2

        # Use halls_and_walls_array to generate a list of Wall objects which use pixel coordinates.
        output_walls = []
        output_goal = None
        for rr in range(prims_array_length):
            for cc in range(prims_array_length):
                if halls_and_walls_array[rr, cc] == 1:
                    output_walls.append(Zone(ctl=tkinter_coords_to_physics_coords([(rr+1)*cell_length - 1, (cc+1)*cell_length - 1]), cbr=tkinter_coords_to_physics_coords([rr*cell_length, cc*cell_length])))
                elif halls_and_walls_array[rr, cc] == 2:
                    output_goal = Zone(ctl=tkinter_coords_to_physics_coords([(rr+1)*cell_length - 1, (cc+1)*cell_length - 1]), cbr=tkinter_coords_to_physics_coords([rr*cell_length, cc*cell_length]))

        # Return!
        return output_walls, output_goal


class Zone:
    """Coordinates defining a zone (ie wall or goal) in a maze.  These use physics coordinates."""

    def __init__(self, ctl, cbr):
        """ctl is short for "corner top left", and is a list of 2 floats, in pixel coordinates.
        cbr is short for "corner bottom right", and is a list of 2 floats, in pixel coordinates.
        """
        self.ctl = ctl
        self.cbr = cbr


class Rover:
    """Contains all information for the rover's current status and original status.  These use physics coordinates.
    pos is a list of 2 floats.
    reset_pos is a list of 2 floats.
    body_angle is a float.
    body_radius is a float.
    whisker_radius is a float.
    whisker_distance is a float.
    whisker_angle is a float.
    state is an int
    action is an int
    """

    def __init__(self, pos, reset_pos, body_angle, body_angle_original, body_radius, whisker_radius, whisker_distance, whisker_angle):
        self.pos = pos
        self.reset_pos = reset_pos
        self.body_angle = body_angle
        self.body_angle_original = body_angle_original
        self.body_radius = body_radius
        self.whisker_radius = whisker_radius
        self.whisker_distance = whisker_distance
        self.whisker_angle = whisker_angle
        self.state = 1
        self.action = 1

    def set_pos(self, new_pos):
        """new_pos is a list of 2 floats."""
        self.pos = new_pos

    def set_body_angle(self, new_angle):
        """new_angle is a float."""
        self.body_angle = new_angle

    def change_pos_by(self, displacement_vector):
        """displacement vector is a list of 2 floats."""
        self.pos[0] += displacement_vector[0]
        self.pos[1] += displacement_vector[1]

    def change_body_angle_by(self, d_theta):
        """d_theta is a float.  Positive d_theta results in leftward turn."""
        self.body_angle += d_theta

        # Wrap around in case body_angle is outside the range (0, 2pi).
        self.body_angle = self.body_angle % (2 * math.pi)

    def get_pos(self):
        return self.pos

    def get_body_angle(self):
        return self.body_angle
