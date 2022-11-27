##############################
# APS106 Winter 2022 - Lab 2 #
##############################

###########################################
# PART 1 - Cartesian to Polar Coordinates #
###########################################
import math

def magnitude(x,y):
    """
    (float,float) -> float
    
    Function calculate the magnitude of a 2D vector. The x- and y-components
    of the vector are given as input parameters to the function as floats.
    
    The function returns the magnitude of the vector as a float.
    
    >>> magnitude(10.0,25.5)
    27.391
    
    >>> magnitude(0.0,0.0)
    0.0
    
    >>> magnitude(10.2,63.2)
    64.018
    
    >>> magnitude(-11.3, -3.9)
    11.954
    
    """
    
    ## TODO: YOUR CODE HERE
    #calculate the magnitude of the 2D vector using pythagoras' theorem
    magnitude = math.sqrt((x ** 2) + (y ** 2))
    
    #round the calculated value to three decimal places
    magnitude_rounded = float(round(magnitude, 3))
    
    
    return(magnitude_rounded)


def phase(x,y):
    """
    (float,float) -> float
    
    Function calculates the phase angle of a 2D vector. The x- and y-components
    of the vector are given as input parameters to the function as floats.
    
    The function returns the phase angle in radians as a float.   
    
    >>> phase(10.0,25.5)
    1.197
    
    >>> phase(0.0,0.0)
    0.0
    
    >>> phase(10.2,63.2)
    1.411
    
    >>> phase(-11.3, -3.9)
    -2.809
    
    """
    
    ## TODO: YOUR CODE HERE

    #calculate the phase angle using arctan2 fucntion because it also takes into account the sign of x and y
    angle = math.atan2(y, x)
    
    #round the calculated phase angle to 3 decimal places
    angle_rounded = float(round(angle, 3))
    
    return(angle_rounded)




###########################################
# PART 2 - Particle Position Calculation  #
###########################################

def particle_position(q,E,m,t,L):
    """
    (float,float,float,float,float) -> float
    
    Function calculates the horizontal position of a charged particle
    within a electrostatic precipitator.
    Input parameters:
        q - charge of the particle in nanocoulombs
        E - electric field strength in kilonewtons/coulomb
        m - mass of particle in nanograms
        t - time since the particle entered the precipitator in microseconds
        L - the distance between the parallel plate electrodes in centimetres
        
    Returns the height of the particle in centimetres
    
    >>> particle_position(0,150,9.2,3.6,5.0)
    2.5
    
    >>> particle_position(2.3,150,9.2,26.8,5.0)
    3.847
    
    >>> particle_position(-2.3,160,9.2,36.8,5.0)
    0.0
    
    """
    
    ## TODO: Write your solution here
    
    #calculate horizontal position of particle using the given equation where the intial posiiton is L/2
    hor_pos = ( (q * E * (t ** 2)) / (20000 * m)) + L/2
    
    #compare the calculated horizontal position to the bounds of where the electrodes lie on the x axis
    final_pos = min (L, (max (0, hor_pos)))
    
    #round the value to three decimal places
    hor_pos_rounded = float(round(final_pos, 3))

    return(hor_pos_rounded)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

