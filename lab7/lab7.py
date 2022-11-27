#####################################################
# APS106 Winter 2022 - Lab 7 - Chemical Eqn Checker #
#####################################################

######################################################
# PART 1 - Complete the function below to deocompose
#          a compound formula written as a string
#          in a dictionary
######################################################

def mol_form(compound_formula):
    """(str) -> dictionary
    When passed a string of the compound formula, returns a dictionary 
    with the elements as keys and the number of atoms of that element as values.
    
    >>> mol_form("C2H6O")
    {'C': 2, 'H': 6, 'O': 1}
    >>> mol_form("CH4")
    {'C': 1, 'H': 4}
    """
     
    split_compound = dict()
    element = ""
    number = ""
    
    for i in range(len(compound_formula)):              # loop thorugh compound to look at each element and number
        
        if compound_formula[i].isalpha():               # all alphabets are elements
            element += compound_formula[i]
            
            if i == (len(compound_formula) - 1):        # if index is at last character and last character is an alphabet, append the element onto the list with the value 1
                
                if element not in split_compound:
                    split_compound[element] = 1
                else:
                    split_compound[element] += 1
                
            elif compound_formula[i+1].isalpha():       
                
                if compound_formula[i+1].isupper():     # check if the next index in the list is an upper case letter, if it is that means that there is only 1 of the current element
                    
                    if element not in split_compound:
                        split_compound[element] = 1         # append the current element w a value of 1
                    else:
                        split_compound[element] += 1
                    
                    element = ""                        # clear the element variable for the next element
                
        else:
            number += compound_formula[i]               # check if the number is at the last index, if is, append the current element with the current number
            if i == (len(compound_formula) - 1):
                
                if element not in split_compound:
                    split_compound[element] = int(number)
                else:
                    split_compound[element] += int(number)
                
            elif compound_formula[i+1].isalpha():       # if the next index is an alphabet, make the current number the value for the current element as key
                
                if element not in split_compound:
                    split_compound[element] = int(number)
                else:
                    split_compound[element] += int(number)
                    
                element = ""
                number = ""                             # clear the current element and number values for the next iteration
            
                
    return split_compound

######################################################
# PART 2 - Complete the function below that takes two 
#          tuples representing one side of a
#          chemical equation and returns a dictionary
#          with the elements as keys and the total
#          number of atoms in the entire expression
#          as values.
######################################################
    
def expr_form(expr_coeffs,expr_molecs):
    """
    (tuple (of ints), tuple (of dictionaries)) -> dictionary
    
    This function accepts two input tuples that represent a chemical expression,
    or one side of a chemical equation. The first tuple contains integers that
    represent the coefficients for molecules within the expression. The second
    tuple contains dictionaries that define these molecules. The molecule
    dictionaries have the form {'atomic symbol' : number of atoms}. The order
    of the coefficients correspond to the order of molecule dictionaries.
    The function creates and returns a dictionary containing all elements within
    the expression as keys and the corresponding number of atoms for each element
    within the expression as values.
    
    For example, consider the expression 2NaCl + H2 + 5NaF
    
    >>> expr_form((2,1,5), ({"Na":1, "Cl":1}, {"H":2}, {"Na":1, "F":1}))
    {'Na': 7, 'Cl': 2, 'H': 2, 'F': 5}
    
    """
    total_num_elements = dict()
    
    for i in range(len(expr_coeffs)):             # expr_coeffs and expr_molecs have the same number of elements, so loop through the length of one of them
        for element in expr_molecs[i]:            # loop through the keys of for the ith dictionary in expr_molecs
            
            if element not in total_num_elements:
                total_num_elements[element] = 0
            
            total_num_elements[element] += expr_coeffs[i] * expr_molecs[i][element]

    return(total_num_elements)

########################################################
# PART 3 - Check if two dictionaries representing
#          the type and number of atoms on two sides of
#          a chemical equation contain different
#          key-value pairs
########################################################

def find_unbalanced_atoms(reactant_atoms, product_atoms):
    """
    (Dict,Dict) -> Set
    
    Determine if reactant_atoms and product_atoms contain equal key-value
    pairs. The keys of both dictionaries are strings representing the 
    chemical abbreviation, the value is an integer representing the number
    of atoms of that element on one side of a chemical equation.
    
    Return a set containing all the elements that are not balanced between
    the two dictionaries.
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 1, "Cl" : 2})
    {'Na'}
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "Na" : 2, "Cl" : 2})
    set()
    
    >>> find_unbalanced_atoms({"H" : 2, "Cl" : 2, "Na" : 2}, {"H" : 2, "F" : 2, "Cl" : 2})
    {'F', 'Na'}
    """
    
    not_balanced_elements = set()
    
    # loop through each reactant
    for reactant in reactant_atoms:
        #check if reactant is not in products, then add it to set
        if reactant not in product_atoms:
            not_balanced_elements.add(reactant)
        # check if reactant is in products but their key values don't match, add reactant to set    
        elif reactant in product_atoms:
            
            if reactant_atoms[reactant] != product_atoms[reactant]:
                not_balanced_elements.add(reactant)
    # repeat same process as above to loop through products; this is in case the products and reactants are completely different/are different in number        
    for product in product_atoms:
        
        if product not in reactant_atoms:
            not_balanced_elements.add(product)
            
        elif product in reactant_atoms:
            
            if product_atoms[product] != reactant_atoms[product]:
                not_balanced_elements.add(product)
    
    return(not_balanced_elements)


########################################################
# PART 4 - Check if a chemical equation represented by
#          two nested tuples is balanced
########################################################

def check_eqn_balance(reactants,products):
    """
    (tuple,tuple) -> Set
    
    Check if a chemical equation is balanced. Return any unbalanced
    elements in a set.
    
    Both inputs are nested tuples. The first element of each tuple is a tuple
    containing the coefficients for molecules in the reactant or product expression.
    The second element is a tuple containing strings of the molecules within
    the reactant or product expression. The order of the coefficients corresponds
    to the order of the molecules. The function returns a set containing any
    elements that are unbalanced in the equation.
    
    For example, the following balanced equation
    C3H8 + 5O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,5), ("C3H8","O2"))
    products: ((4,3), ("H2O","CO2"))
    
    >>> check_eqn_balance(((1,5), ("C3H8","O2")),((4,3), ("H2O","CO2")))
    set()
    
    Similarly for the unbalanced equation
    
    C3H8 + 2O2 <-> 4H2O + 3CO2
    
    would be input as the following two tuples:
    reactants: ((1,2), ("C3H8","O2"))
    products: ((4,3), ("H2O","CO2"))
    
    >>> check_eqn_balance(((1,2), ("C3H8","O2")),((4,3), ("H2O","CO2")))
    {'O'}
    
    """
    
    mol_form_reactants = tuple()
    mol_form_products = tuple()
    
    # loop through each compound in the second element of the reactants tuple and products tuple and apply the mol_form function to each compound
    # append the dictionary to the corresponding mol_form_reactants or mol_form_products tuple
    for reac_compound in reactants[1]:
        mol_form_reactants += (mol_form(reac_compound),)
        
    for prod_compound in products[1]:
        mol_form_products += (mol_form(prod_compound),)
    
    # find the sum of each element in the reactatns and products using expr_form
    sum_reactants = expr_form(reactants[0], mol_form_reactants)
    sum_products = expr_form(products[0], mol_form_products)
    
    # find unbalanced elements using find_unbalanced_atoms function
    unbalanced_elements = find_unbalanced_atoms(sum_reactants, sum_products)
    
    return unbalanced_elements