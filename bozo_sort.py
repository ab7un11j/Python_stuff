from random import randint as random_integer_picker

def check_if_list_is_sorted(list_to_be_checked):
    list_is_sorted = True
    lenght_of_the_list: int = len(list_to_be_checked)
    
    for element_index in range(1, lenght_of_the_list):
        if list_to_be_checked[element_index - 1] > list_to_be_checked[element_index]:
            list_is_sorted = False
            
    return list_is_sorted
    
    
def bozo_sort_algorithm(random_list_to_sort: list):
    lenght_of_the_list: int = len(random_list_to_sort)
    list_is_not_sorted = not check_if_list_is_sorted(random_list_to_sort) 
    
    while list_is_not_sorted:
        first_guess_index = random_integer_picker(0, lenght_of_the_list-1)
        second_guess_index = random_integer_picker(0, lenght_of_the_list-1)
        
        first_guess_element = random_list_to_sort[first_guess_index]
        second_guess_element = random_list_to_sort[second_guess_index]
        random_list_to_sort[second_guess_index] = first_guess_element
        random_list_to_sort[first_guess_index] = second_guess_element
        
        list_is_not_sorted = not check_if_list_is_sorted(random_list_to_sort)
        
    sorted_list_after_all_this = random_list_to_sort
    return sorted_list_after_all_this


def main():
    print(bozo_sort_algorithm(list(range(10, -1, -1))))        


if __name__ == "__main__":
    main()
        