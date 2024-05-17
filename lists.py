def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 1 and len(list_to_remove_elements) < 5:
        del list_to_remove_elements[0]
        return list_to_remove_elements
    
    elif len(list_to_remove_elements) == 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    
    elif len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
        return list_to_remove_elements
    else:
        return list_to_remove_elements


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, "Pink")
    long = len(list_to_add_elements)
    list_to_add_elements.insert(long, "Yellow")
    return list_to_add_elements


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
        else:
            return False
    else:
        return False


def list_of_lists(list_of_lists_to_modify):
    first_modification = []
    second_modification = []
    third_modification = []
    if len(list_of_lists_to_modify[0])==0:
        first_modification = first_modification
        
    elif len(list_of_lists_to_modify[0])==1:
        first_modification = [list_of_lists_to_modify[0][0]]
        
    else:
        first_modification = list_of_lists_to_modify[0][0:2]
        
    if len(list_of_lists_to_modify[1]) < 2:
        second_modification = second_modification
        
    elif len(list_of_lists_to_modify[1]) <= 4:
        second_modification = list_of_lists_to_modify[1][1:]
        
    else:
        second_modification = list_of_lists_to_modify[1][1:4]
    
    if len(list_of_lists_to_modify[2])==0:
        third_modification = third_modification

    elif len(list_of_lists_to_modify[2])==1:
        third_modification = [list_of_lists_to_modify[2][0]]

    else:
        third_modification = list_of_lists_to_modify[2][-2:]

    list_of_lists_to_modify[0] = first_modification
    list_of_lists_to_modify[1] = second_modification
    list_of_lists_to_modify[2] = third_modification

    return list_of_lists_to_modify
