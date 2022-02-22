import data_tier
import math


class UserProgramRunner:
    """Runs the Finite-State Machine program written by the user."""

    def __init__(self):
        """State is the state of the FSM.  left_touch and right_touch are whether the left and right whiskers are
        touching a wall, respectively.
        state is an int.
        left_touch is a boolean.
        right_touch is a boolean.
        """
        self.physics = Physics()
        self.left_touch = self.check_for_whisker_contact("left")
        self.right_touch = self.check_for_whisker_contact("right")

    def check_for_whisker_contact(self, which_whisker):
        """Returns if the chosen whisker is touching a wall.
        which_whisker is a string determining the whisker to check for contact.  It may only be "left" or "right".
        """
        # Check for invalid input of which_whisker
        if which_whisker not in ["left", "right"]:
            raise ValueError("which_whisker must be 'left' or 'right'.")

        # Determine the location of the whisker bulb in question.
        rover_pos = self.physics.rover.pos
        rover_ang = self.physics.rover.body_angle
        whisker_dis = self.physics.rover.whisker_distance
        whisker_ang = self.physics.rover.whisker_angle
        whisker_rad = self.physics.rover.whisker_radius
        if which_whisker == "left":
            whisker_pos = [rover_pos[0] + math.cos(rover_ang + whisker_ang) * whisker_dis, rover_pos[1] + math.sin(rover_ang + whisker_ang) * whisker_dis]
        else:   # We deduce which_whisker == "right"
            whisker_pos = [rover_pos[0] + math.cos(rover_ang - whisker_ang) * whisker_dis, rover_pos[1] + math.sin(rover_ang - whisker_ang) * whisker_dis]

        # Check for edge-of-board collisions:
        if whisker_pos[1] - whisker_rad < 0:
            return True
        if whisker_pos[1] + whisker_rad > 799:
            return True
        if whisker_pos[0] + whisker_rad > 799:
            return True
        if whisker_pos[0] - whisker_rad < 0:
            return True

        # If the whisker bulb is within a wall, return True.  Else False.
        for wall in self.physics.current_maze.walls:
            # If colliding with top wall or bottom edge of board...
            if abs(whisker_pos[1] - wall.ctl[1]) <= whisker_rad and (wall.ctl[0] - whisker_rad) <= whisker_pos[0] <= (wall.cbr[0] + whisker_rad):
                return True
            # If colliding with bottom wall or top edge of board...
            if abs(whisker_pos[1] - wall.cbr[1]) <= whisker_rad and (wall.ctl[0] - whisker_rad) <= whisker_pos[0] <= (wall.cbr[0] + whisker_rad):
                return True
            # If colliding with left wall or right edge of board...
            if abs(whisker_pos[0] - wall.ctl[0]) <= whisker_rad and (wall.cbr[1] - whisker_rad) <= whisker_pos[1] <= (wall.ctl[1] + whisker_rad):
                return True
            # If colliding with right wall or left edge of board...
            if abs(whisker_pos[0] - wall.cbr[0]) <= whisker_rad and (wall.cbr[1] - whisker_rad) <= whisker_pos[1] <= (wall.ctl[1] + whisker_rad):
                return True

        # We've gotten through all walls with no returns.  Therefore return False.
        return False

    def update_whisker_statuses(self):
        self.left_touch = self.check_for_whisker_contact("left")
        self.right_touch = self.check_for_whisker_contact("right")


class Physics:
    """Covers motion and collision."""

    def __init__(self):
        """current_maze is a maze object representing the maze currently being used in the game."""
        self.current_maze = data_tier.Maze()
        self.rover = data_tier.Rover(pos=[20, 20], reset_pos=[20, 20], body_angle=math.pi/2, body_angle_original=math.pi/2, body_radius=10, whisker_radius=3, whisker_distance=19, whisker_angle=math.pi/4)

    def vector_to_magnitude(self, vector):
        """Given a 2D vector, returns the magnitude of that vector.
        vector is a list of length 2.
        """
        return (vector[0] ** 2 + vector[1] ** 2) ** 0.5

    def vector_to_angle(self, vector):
        """Given a 2D vector, returns the angle of that vector in radians.  0 radians points right.
        vector is a list of length 2.
        """
        vector_magnitude = self.vector_to_magnitude(vector)
        angle = math.acos((vector[0]) / vector_magnitude) if vector[1] > 0 else 2 * math.pi - math.acos(
            (vector[0]) / vector_magnitude)
        return angle

    def angle_to_vector(self, angle, vector_magnitude):
        """Given an angle in radians and a vector_magnitude, returns a 2D vector with that angle and magnitude.
        angle is a scalar.
        vector_magnitude is a scalar.
        """
        return [math.cos(angle) * vector_magnitude, math.sin(angle) * vector_magnitude]

    def move_forward(self, distance):
        """Moves forward, limitedly if a collision would occur.
        distance is an integer.
        """

        def is_rover_in_wall():
            """Checks to see if the rover is in a wall.
            Returns a list of collision strings indicating the wall being collided with: "top", "bottom", "left", "right".
            """
            _collisions = []

            # Check for edge-of-board collisions
            if self.rover.pos[1] - self.rover.body_radius < 0:  # bottom edge of board (collision from top)
                _collisions.append("top")
            if self.rover.pos[1] + self.rover.body_radius > 799:    # top edge of board (collision from bottom)
                _collisions.append("bottom")
            if self.rover.pos[0] + self.rover.body_radius > 799:    # right edge of board (collision from right)
                _collisions.append("left")
            if self.rover.pos[0] - self.rover.body_radius < 0:  # left edge of board (collision from left)
                _collisions.append("right")

            # For each wall Zone in current_maze.walls, check if the body of the rover is within body_radius of the wall
            for wall in self.current_maze.walls:
                # If colliding with top wall...
                if abs(self.rover.pos[1] - wall.ctl[1]) <= self.rover.body_radius and (wall.ctl[0] - self.rover.body_radius) <= self.rover.pos[0] <= (wall.cbr[0] + self.rover.body_radius):
                    _collisions.append("top")
                # If colliding with bottom wall...
                if abs(self.rover.pos[1] - wall.cbr[1]) <= self.rover.body_radius and (wall.ctl[0] - self.rover.body_radius) <= self.rover.pos[0] <= (wall.cbr[0] + self.rover.body_radius):
                    _collisions.append("bottom")
                # If colliding with left wall...
                if abs(self.rover.pos[0] - wall.ctl[0]) <= self.rover.body_radius and (wall.cbr[1] - self.rover.body_radius) <= self.rover.pos[1] <= (wall.ctl[1] + self.rover.body_radius):
                    _collisions.append("left")
                # If colliding with right wall...
                if abs(self.rover.pos[0] - wall.cbr[0]) <= self.rover.body_radius and (wall.cbr[1] - self.rover.body_radius) <= self.rover.pos[1] <= (wall.ctl[1] + self.rover.body_radius):
                    _collisions.append("right")

            return _collisions

        would_be_collisionless_step_vector = self.angle_to_vector(self.rover.body_angle, 1)

        # Repeatedly step forward 1 unit, then round to the nearest non-occupied space.
        for _ in range(distance):
            self.rover.change_pos_by(would_be_collisionless_step_vector)
            collisions = is_rover_in_wall()
            if "top" in collisions:
                self.rover.set_pos([self.rover.pos[0], math.ceil(self.rover.pos[1]) + self.rover.body_radius])
            if "bottom" in collisions:
                self.rover.set_pos([self.rover.pos[0], math.floor(self.rover.pos[1]) - self.rover.body_radius])
            if "left" in collisions:
                self.rover.set_pos([math.floor(self.rover.pos[0]) - self.rover.body_radius, self.rover.pos[1]])
            if "right" in collisions:
                self.rover.set_pos([math.ceil(self.rover.pos[0]) + self.rover.body_radius, self.rover.pos[1]])

    def move_backward(self, distance):
        """Moves backward, limitedly if a collision would occur.
        distance is an integer.
        """
        self.move_forward(-distance)

    def turn_left(self, angle):
        """Turns left.  Does not check for collisions; the whiskers are treated as collisionless.
        angle is a float, in radians.
        """
        self.rover.change_body_angle_by(angle)

    def turn_right(self, angle):
        """Turns right.  Does not check for collisions; the whiskers are treated as collisionless.
        angle is a float, in radians.
        """
        self.turn_left(-angle)

