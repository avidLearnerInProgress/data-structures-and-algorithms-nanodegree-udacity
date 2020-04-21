def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.
    Args:
       input_list(list): List to be sorted
    """
    length = len(input_list) - 1
    if length == 0:
        return input_list
    
    midpoint, start_index, end_index = 0, 0, 0
    end_index = length - start_index
    while midpoint <= end_index:
        if input_list[midpoint] == 0:
            input_list[start_index], input_list[midpoint] = input_list[midpoint], input_list[start_index]
            start_index += 1
            midpoint += 1
        elif input_list[midpoint] == 1:
            midpoint += 1
        else:
            input_list[midpoint], input_list[end_index] = input_list[end_index], input_list[midpoint]
            end_index -= 1
    return input_list    
    
def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
    
#Testcases
test_function([])
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])