def apply_all_func(int_list, *functions):
    results = {}
    
    for func in functions:
        
        func_name = func.__name__
        
        results[func_name] = func(int_list)
    
    return results


def sum_numbers(numbers):
    return sum(numbers)

def max_number(numbers):
    return max(numbers)

def min_number(numbers):
    return min(numbers)

def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


int_list = [1, 2, 3, 4, 5]
results = apply_all_func(int_list, sum_numbers, max_number, min_number, average)

print(results)
