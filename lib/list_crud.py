def create_an_empty_list():
    return []

print(create_an_empty_list())

def create_a_list():
    return [1, 2, 3, 4]

def add_element_to_end_of_list(l, element):
    l.append(element)
    return l

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(add_element_to_end_of_list(list, 11))



def add_element_to_start_of_list(l, element):
    l.insert(0, element)
    return l
print(add_element_to_start_of_list(list, 0))

def remove_element_from_end_of_list(l):
    l.pop()
    return l
print(remove_element_from_end_of_list(list))

def remove_element_from_start_of_list(l):
    del l[0]
    return l

print(remove_element_from_start_of_list(list))

def retrieve_first_element_from_list(l):
    return l[0]

print(retrieve_first_element_from_list(list))

def retrieve_element_from_index(l, index):
    return l[index]

print(retrieve_element_from_index(list, 2))

def retrieve_last_element_from_list(l):
    return l[len(l)-1]

print(retrieve_last_element_from_list(list))