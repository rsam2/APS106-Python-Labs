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
    
    name = ""
    
    first_name = ""
    
    last_name = ""
    
    for i in email[0:pos_of_at_symbol]:
        
        if i == ".":
            first_name = name
            name = ""       
        
        name += i
        
        last_name = name[1:]
        
    final_name = last_name.upper()+","+first_name.upper()
    
    return (final_name)