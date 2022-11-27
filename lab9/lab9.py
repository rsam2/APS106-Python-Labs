############################################################
# APS106 Winter 2022 - LAB 9 - Wind Turbine Placement OOP  #
############################################################

import csv

class Point:
    """
    A point in a two-dimensional coordinate plane
    """
    
    def __init__(self, x, y):
        """
        Create a point with an x and y coordinate
        """
        self.x = x
        self.y = y
        
    def __str__(self):
        """
        Generate a string representation of a point
        """
        return "(" + str(self.x) + "," + str(self.y) + ")"


############################
# Part 1 - Circle Class
############################
class Circle:
    """
    A circle in a two-dimensional coordinate plane
    """
    
    def __init__(self, centre_x, centre_y, radius):
        """
        Create a rectangle defined by its bottom left and top right corner
        coordinates
        """
        self.centre = Point(centre_x, centre_y)
        self.radius = radius
        
    def __str__(self):
        """
        Generate a string representation of a rectangle
        """
        return ("Circle with centre coordinate " + 
                str(self.centre) + " and radius " + str(self.radius))
    
    def move(self, horizontal_translation, vertical_translation):
        """
        (Circle, int, int) -> None
        
        Alters the location of a circle by translating the coordinates
        of its centre coordinates.
        """
        self.centre.x += horizontal_translation
        self.centre.y += vertical_translation
    
    def overlap(self, circB):
        """
        (Circle, Circle) -> bool
        
        Checks whether two circles overlap, return true if they overlap, false otherwise
        """
        
        # compute the distance between the centres
        d = ((self.centre.x - circB.centre.x) ** 2 + (self.centre.y - circB.centre.y) ** 2) ** (1/2)
        return d < (self.radius + circB.radius)


##############################
# Part 2 - Wind Turbine Class
##############################
class WindTurbine:
    """
    A wind turbine placed in a two-dimensional area
    """
    
    def __init__(self, id_number, placement_centre_x, placement_centre_y, placement_radius):
        """
        Create a wind turbine
        """
        self.id_number = id_number
        self.placement = Circle(placement_centre_x,placement_centre_y, placement_radius)
        
        self.overlapping_turbines = []
    
    def __str__(self):
        """
        Generate a string representation of a WindTurbine object
        """
        return ("Wind Turbine ID: " + str(self.id_number) + 
                ", Placement: " + str(self.placement))

        
    def move(self, horizontal_translation, vertical_translation):
        """
        (WindTurbine, int, int) -> None
        
        Alters the location of a wind turbine by translating the coordinates
        of its bottom left and top right corner coordinates. After moving the 
        turbine, the overlapping turbine list should be reset to an empty
        list.
        
        The change in the x and y coordinates are specified by the
        horizontal_translation and vertical_translation parameters, respectively.
        """
        # call move method in cricle class to move the turbine
        self.placement.move(horizontal_translation, vertical_translation)
        
        # empty overlapping_turbines list
        self.overlapping_turbines = []
    
    def overlap(self, turbineB):
        """
        (WindTurbine, WindTurbine) -> bool
        
        Checks for overlap between a wind turbine and another turbine (turbineB).
        """
        
        # call overlap method on self and turbineB
        return self.placement.overlap(turbineB.placement)

    def validate_placement(self, turbines):
        """
        (WindTurbine, list of WindTurbines) -> None
        
        Check if the postion of a wind turbine is valid by checking for
        overlapping areas with all other wind turbines.
        """
        for turbine in turbines:
            # check if its the same turbine, skip if it is
            if self.id_number == turbine.id_number:
                continue
            # if the two turbines overlap, append to the overlapping turbine list
            elif self.overlap(turbine):
                self.overlapping_turbines.append(turbine)


##########################################
# Part 3 - Load Wind Turbines from File
##########################################

def load_turbine_placements(turbine_filename):
    """
    (str) -> list of WindTurbines

    Opens a csv file containing wind turbine IDs, and placement 
    info (centre coordinates and radius) and returns a list
    of WindTurbine objects for each turbine defined in the file
    """

    turbine_list = []
    
    # open the csv file            
    with open(turbine_filename, "r") as csvfile:
        turbine_reader = csv.reader(csvfile)
        # convert the csv file to a list of lists
        turbine_as_list = list(turbine_reader)
        
        # loop through the list to create a wind turbine object out of each element
        for x in turbine_as_list:
            turbine = WindTurbine(x[0], x[1], x[2], x[3])
            turbine_list.append(turbine)
    # the final list should not inlcude the first wind turbine object which is the column names        
    final_turbine_list = turbine_list[1:]
                                              
    return final_turbine_list


##########################################
# Part 4 - Testing Wind Turbine Placement
##########################################

def check_turbine_placements(turbines):
    """
    (list of WindTurbines) -> int
    
    Checks a list of wind turbines to identify turbines with invalid (overlapping)
    placements. The function should return the number of turbines with 
    invalid placements.
    
    All placements should be evaluated using the validate_placement method from
    the WindTurbine class.
    """
    
    num_overlaps = 0
    
    # loop through each turbine
    for turbine in turbines:
        turbine.validate_placement(turbines)
        if (len(turbine.overlapping_turbines)) > 0:
            num_overlaps += 1
                
    return num_overlaps


