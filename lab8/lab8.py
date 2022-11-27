###################################################
# APS106 - Winter 2022 - Lab 8 - Corner Detection #
###################################################

# 51 lines of code (w/o comments)
#from lab8_image_utils import display_image, image_to_pixels
from operator import itemgetter

################################################
# PART 1 - RGB to Grayscale Conversion         #
################################################

def rgb_to_grayscale(rgb_img):
    """
    (tuple) -> tuple
    
    Function converts an image of RGB pixels to grayscale.
    Input tuple is a nested tuple of RGB pixels.
    
    The intensity of a grayscale pixel is computed from the intensities of
    RGB pixels using the following equation
    
        grayscale intensity = 0.3 * R + 0.59 * G + 0.11 * B
    
    where R, G, and B are the intensities of the R, G, and B components of the
    RGB pixel. The grayscale intensity should be *rounded* to the nearest
    integer.
    """
    # 4 lines
    # initalize tuple to store grayscale values
    gray_img = tuple()
    
    # for each pixel in rbg_img, compute the corresponding grayscale value and add it to the gray_img tuple
    for pixel in range(len(rgb_img)):
        gray_img += ((round(0.3 * (rgb_img[pixel][0]) + 0.59 * (rgb_img[pixel][1]) + 0.11 * rgb_img[pixel][2])),)
        
    return gray_img


############################
# Part 2b - Dot Product    #
############################

def dot(x,y):
    """
    (tuple, tuple) -> float
    
    Performs a 1-dimensional dot product operation on the input vectors x
    and y. 
    """
    # 4 lines
    # initialize variable to store final dot product
    sum = 0
    
    # loop through each value in vector x and multiply it with the corresponding value in vector y
    for i in range(len(x)):
        # add it to the sum variable
        sum += (x[i] * y[i])
    
    return sum


######################################
# Part 2c - Extract Image Segment    #
######################################

def extract_image_segment(img, width, height, centre_coordinate, N):
    """
    (tuple, int, int, tuple, int) -> tuple
    
    Extracts a 2-dimensional NxN segment of a image centred around
    a given coordinate. The segment is returned as a tuple of pixels from the
    image.
    
    img is a tuple of grayscale pixel values
    width is the width of the image
    height is the height of the image
    centre_coordinate is a two-element tuple defining a pixel coordinate
    N is the height and width of the segment to extract from the image
    
    """
    # 7 lines
    segment = tuple()
    
    # define the coordinates of top left corner of the segment
    x_top_left = int(centre_coordinate[0] - ((N-1)/2))
    y_top_left = int(centre_coordinate[1] - ((N-1)/2))
        
    # loop through each "row" in the segment
    for y in range(y_top_left, y_top_left + N):
        # loop through each "column" in each row
        for x in range(x_top_left, x_top_left + N):
            # add the pixel value at the coordinate to the segment tuple
            segment += ((img[y * width + x]),)
            
    return segment    
    

######################################
# Part 2d - Kernel Filtering         #
######################################

def kernel_filter(img, width, height, kernel):
    """
    (tuple, int, int, tuple) -> tuple
    
    Apply the kernel filter defined within the two-dimensional tuple kernel to 
    image defined by the pixels in img and its width and height.
    
    img is a 1 dimensional tuple of grayscale pixels
    width is the width of the image
    height is the height of the image
    kernel is a 2 dimensional tuple defining a NxN filter kernel, n must be an odd integer
    
    The function returns the tuple of pixels from the filtered image
    """
    # 15 lines
    N = len(kernel)
    
    filtered_img = tuple()
    filter_tup = tuple()
    
    for y in range(N):
        for x in range(N):
            filter_tup += ((kernel[y][x]),)
    
    # loop through each row and then each column of each row
    for y in range(height):
        for x in range(width):
            # check if the the x and y coordinates fall in the edge region where the window cannot be executed
            if (((N-1)/2) > x or ((N-1)/2) > ((width-1) - x)) or (((N-1)/2) > y or ((N-1)/2) > ((height - 1) - y)):
                filtered_img += (0,)
            # apply dot product to segment and filter    
            else:
                segment = extract_image_segment(img, width, height, (x, y), N)
                pixel = int(dot(segment, filter_tup))
                filtered_img += (pixel,)
    
    return filtered_img


###############################
# PART 3 - Harris Corners     #
###############################

def harris_corner_strength(Ix,Iy):
    """
    (tuple, tuple) -> float
    
    Computes the Harris response of a pixel using
    the 3x3 windows of x and y gradients contained 
    within Ix and Iy respectively.
    
    Ix and Iy are  lists each containing 9 integer elements each.

    """

    # calculate the gradients
    Ixx = [0] * 9
    Iyy = [0] * 9
    Ixy = [0] * 9
    
    for i in range(len(Ix)):
        Ixx[i] = (Ix[i] / (4*255))**2
        Iyy[i] = (Iy[i] / (4*255))**2
        Ixy[i] = (Ix[i] / (4*255) * Iy[i] / (4*255))
    
    # sum  the gradients
    Sxx = sum(Ixx)
    Syy = sum(Iyy)
    Sxy = sum(Ixy)
    
    # calculate the determinant and trace
    det = Sxx * Syy - Sxy**2
    trace = Sxx + Syy
    
    # calculate the corner strength
    k = 0.03
    r = det - k * trace**2
    
    return r

def harris_corners(img, width, height, threshold):
    """
    (tuple, int, int, float) -> tuple
    
    Computes the corner strength of each pixel within an image
    and returns a tuple of potential corner locations. Each element in the
    returned tuple is a two-element tuple containing an x- and y-coordinate.
    The coordinates in the tuple are sorted from highest to lowest corner
    strength.
    """
    
    # perform vertical edge detection
    vertical_edge_kernel = ((-1, 0, 1),
                            (-2, 0, 2),
                            (-1, 0, 1))
    Ix = kernel_filter(img, width, height, vertical_edge_kernel)
    
    # perform horizontal edge detection
    horizontal_edge_kernel = ((-1,-2,-1),
                              ( 0, 0, 0),
                              ( 1, 2, 1))
    Iy = kernel_filter(img, width, height, horizontal_edge_kernel)
    
    # compute corner scores and identify potential corners
    border_sz = 1
    corners = []
    for i_y in range(border_sz, height-border_sz):
        for i_x in range(border_sz, width-border_sz):
            Ix_window = extract_image_segment(Ix, width, height, (i_x, i_y), 3)
            Iy_window = extract_image_segment(Iy, width, height, (i_x, i_y), 3)
            corner_strength = harris_corner_strength(Ix_window, Iy_window)
            if corner_strength > threshold:
                #print(corner_strength)
                corners.append([corner_strength,(i_x,i_y)])

    # sort
    corners.sort(key=itemgetter(0),reverse=True)
    corner_locations = []
    for i in range(len(corners)):
        corner_locations.append(corners[i][1])

    return tuple(corner_locations)


###################################
# PART 4 - Non-maxima Suppression #
###################################

def non_maxima_suppression(corners, min_distance):
    """
    (tuple, float) -> tuple
    
    Filters any corners that are within a region with a stronger corner.
    Returns a tuple of corner coordinates that are at least min_distance away from
    any other stronger corner.
    
    corners is a tuple of two-element coordinate tuples representing potential
        corners as identified by the Harris Corners Algorithm. The corners
        are sorted from strongest to weakest.
    
    min_distance is a float specifying the minimum distance between any
        two corners returned by this function
    """
    #21 lines
    F = list()
    
    # check if there are any corners in the image
    if len(corners) == 0:
        return tuple(F)
    
    # loop over each corner
    for i in corners:
        
        # if F is empty, add the first corner
        if len(F) == 0:
            F.append(i)
            
        else:
            distances = list()
            counter = 0
            index = 0
            # loop through each value in the corners in F and calcualte the euclidean distance between each corner in F and the current corner in corners
            
            for j in F:
                euc_dist = (((i[0] - j[0]) ** 2) + ((i[1] - j[1]) ** 2)) ** 0.5
                
                # append each distance to a list
                distances.append(euc_dist)
                
            # keep track of how many distances are above the threshold    
            while distances[index] >= min_distance:
                counter += 1
                index += 1
                if index == (len(distances)):
                    break
            # if all the distances are above the threshold, append the value to F    
            if counter == len(distances):
                F.append(i)
            
            
    return tuple(F)
    