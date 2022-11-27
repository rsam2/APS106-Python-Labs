###############################################
# APS106  2022 - Lab 5 - Measurement Parser   #
###############################################

############################
# Part 1 - Email to Name   #
############################

def email_to_name(email):
    """
    (str) -> str
    
    Given a string with the format "first_name.last_name@domain.com",
    return a string "LAST_NAME,FIRST_NAME" where all the characters are upper
    case
    
    
    >>> email_to_name("anna.conda@mail.utoronto.ca")
    'CONDA,ANNA'
    """
    
    # get position of @ symbol in string
    pos_of_at_symbol = email.find("@")
    
    # get position of . in string
    pos_of_dot = email.find(".")
    
    # slice the email string using the postion of the dot to get the first name
    first_name = email[0:pos_of_dot]
    
    # slice the email stirng using the position of the dot and the ampersand to get the last name
    last_name = email[pos_of_dot + 1: pos_of_at_symbol]
    
    # concatenate the first name and last name into the correct format
    final_name = last_name.upper() + "," + first_name.upper()
    
    return (final_name)    


###############################
# Part 2 - Count Measurements #
###############################

def count_measurements(s):
    """
    (str) -> int
 
    Given s, a string representation of comma separated site-measurement
    pairs, return the total number of measurements
 
    >>> count_measurements("B, 5.6, Control, 5.5, Db, 3.2")
    3
    
    >>> count_measurements("Control, 7.5")
    1
    """
    
    # create a list to place each element separated by a comma into
    split = []
    
    # initialize a variable named element to place each character into, element will represent each word/number separated by a comma
    element = ""
    
    # loop over the length of the string to get each character
    for i in range(len(s)):
        
        # check if the current character is a comma, that means element currently contains one word
        if s[i] == ",":
            # append the current word in element to the list
            split.append(element)
            
            # make element blank so that it can accumulate the next word
            element = ""
            
            # we don't want to add comma anywhere so use continue to get back to the start of the loop
            continue  
        
        # check if i is at the last character
        elif i == (len(s)-1):
            
            # add the final character to element
            element += s[i]
            
            # append the current content of element to the list 'split'
            split.append(element)
        
        # add the current character to the element
        else:
            element += s[i]
    
    # the number of measurements is the number of elements in the list 'split' divided by 2, one for each pair
    num_measurements = int((len(split))/2)    
    
    return (num_measurements)



######################################
# Part 3 - Calculate Site Average    #
######################################

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

    


###############################
# Part 4 - Generate Summary   #
###############################

def generate_summary(measurement_info, site):
    """
    (str, str) -> str
    
    Extract technician name, number of measurements, and average of control
    site pH level measurements from string of technician measurements. Input
    string is formatted as
    
        firstname.lastname@domain.com, date, sitename, measurement, sitename, measurement, ...
    
    returns a string with the extracted information formatted as
    
        LASTNAME,FIRSTNAME,number of measurements,average pH of specified site
 
    >>> generate_summary("dina.dominguez@company.com, 01/11/20, A, 4.2, B, 6.7, Control, 7.1, B, 6.5, Control, 7.8, Control, 6.8, A, 3.9", "Control")
    'DOMINGUEZ,DINA,7,7.2'
    """
    
# first convert the given string into a list with consisting of elements in between the commas in the string

    # initalize variables for the list and the each element in the string
    info_split = []
    element = ""
    
    # loop over the length of the string to get each character
    for i in range(len(measurement_info)):
        
        # check if the current character is a comma, that means element currently contains one word
        if measurement_info[i] == ",":
            
            # append the current word in element to the list
            info_split.append(element)
            
            # make element blank so that it can accumulate the next word
            element = ""
            
            # we don't want to add comma anywhere so use continue to get back to the start of the loop
            continue  
        
        # check if i is at the last character
        elif i == (len(measurement_info)-1):
            
            # add the final character to element
            element += measurement_info[i]
            
            # append the current content of element to the list 'split'
            info_split.append(element)
        
        # add the current character to the element
        else:
            element += measurement_info[i]    
    
    # use the email to name funciton on the first element of the list, the email
    name = email_to_name(info_split[0])
    
    
    
    
    # create a string containing only the measurements and the site info
    measurements = ""
    # store the elements of the list containing measurements and their sites in a separate variable
    list_measurements = info_split[2:]
    
    
    # loop over the list containing the elements of measurements info after the date
    for i in range(len(list_measurements)):
        
        if i == ((len(list_measurements))-1):
            measurements += list_measurements[i]
     
        else:
            measurements += list_measurements[i]
            measurements += ","
    
    # get the number of measurements using the string of measurements and sites
    num_measurement = count_measurements(measurements)
    
    # get the average pH of the sites using the string of measurements and sites
    average = calc_site_average(measurements, site)
     
    # concatenate all the found information into one string
    final_info = (name + "," + str(num_measurement) + "," + str(average))
    
    
    return(final_info)    