def first_missing_positive(numbers):
    positive_numbers = []
    for number in numbers:
        if number > 0:  
            positive_numbers.append(number)  
    positive_numbers.sort()
    expected_positive = 1
    for num in positive_numbers:
        if num == expected_positive:
            expected_positive += 1
        elif num > expected_positive:
            break
    return expected_positive

print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([1, 2, 0]))