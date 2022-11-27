def calc_site_average(measurements, site):
    """
    (str, str) -> float
 
    Given s, a string representation of comma separated site-measurement
    pairs, and the name of a site, 
    return the average of the site measurements to one decimal place
    
    
    >>> calc_site_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    7.2
    """
    # initialize varibles for the sum of measurements and the number of measurements
    
    total = 0
    num_measurements = 0
    
    # create a list to place each element separated by a comma into
    split = []
    
    # initialize a variable named element to place each character into, element will represent each word/number separated by a comma
    element = ""    
    
    
    # loop over the length of the string to get each character
    for i in range(len(measurements)):
        
        # check if the current character is a comma, that means element currently contains one word
        if measurements[i] == ",":
            # append the current word in element to the list
            split.append(element)
            
            # make element blank so that it can accumulate the next word
            element = ""
            
            # we don't want to add comma anywhere so use continue to get back to the start of the loop
            continue  
        
        # check if i is at the last character
        elif i == (len(measurements)-1):
            
            # add the final character to element
            element += measurements[i]
            
            # append the current content of element to the list 'split'
            split.append(element)
        
        # add the current character to the element
        else:
            element += measurements[i]
             
    # loop through each element in the list 'split'
    for i in range(len(split)):
        
        # check if the site is in the current element
        if site in split[i]:
            
            # add the next element in the list, the measurement for the site, to the total
            total += float(split[i+1])
            
            # increase the number of measurements by one
            num_measurements += 1
            
    average = total/num_measurements
        
    rounded = round(average, 1)
        
    return rounded

print(calc_site_average("A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control"))