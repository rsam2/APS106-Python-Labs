##############################
# APS106 Winter 2022 - Lab 3 #
##############################


def circle_overlap(circ1_centre_x, circ1_centre_y, circ1_radius,
                    circ2_centre_x, circ2_centre_y, circ2_radius):
    """
    (int, int, int, int, int, int) -> str

    Function determines whether two circles overlap. When circles
    overlap, the function checks for the following scenarios
        1. The two circles perfectly overlap
        2. The first circle is contained within the second
        3. The second circle is contained within the first
        4. The circle have overlapping area, but neither is completely
           contained within the other
    
    Function inputs represent x and y coordinates circle centres and their
    radii (see lab document)
           
    The function returns a string describing the overlap scenario
    
    >>> circle_overlap(0,1,3,6,4,1)
    'no overlap'
    
    >>> circle_overlap(0,1,3,0,1,3)
    'identical circles'
    
    >>> circle_overlap(1,1,10,6,7,1)
    'circle 2 is contained within circle 1'
    
    >>> circle_overlap(-1,-2,2,0,0,11)
    'circle 1 is contained within circle 2'
    
    >>> circle_overlap(1,-2,2,-4,0,5)
    'circles overlap'
    """
 
    
    # store the distance between the two centers of the circles in a variable by using pytahgorean theorem
    centre_dist = (((circ2_centre_x - circ1_centre_x) ** 2) + ((circ2_centre_y - circ1_centre_y) ** 2)) ** 0.5
    
    # use if, elif, and else statements to test the cases
    
    # if the circles do not overlap, the distance between the two centers will be greater than the sum of the radii
    if centre_dist >= (circ1_radius + circ2_radius):
        scenario = "no overlap"
        
        
    # if the circles are identical, they will have the same x and y coordinates for their centres and will also have the same radius 
    elif (circ1_centre_x == circ2_centre_x) and (circ1_centre_y == circ2_centre_y) and (circ1_radius == circ2_radius):
        scenario = "identical circles"
        
        
    # if circle 2 is contianed within circle 1, the sum of radius 2 and centre_dist will be less than or equal to radius 1
    elif (centre_dist + circ2_radius) <= circ1_radius:
        scenario = "circle 2 is contained within circle 1"
        
    # similarly, if circle 1 is contained within circle 2, the sum of radius 1 and centre_dist will be less than or equal to radius 2
    elif (centre_dist + circ1_radius) <= circ2_radius:
        scenario = "circle 1 is contained within circle 2"
        
    # if the paramteres of the fucntion do not meet the above criteria, the circles overlap
    else:
        scenario = "circles overlap"
    
    #return the determined scenario
    return scenario

if __name__ == '__main__':
    import doctest
    doctest.testmod()
