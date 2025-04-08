def split(input_string, delimiters):
    result = [input_string]
    for d in delimiters:
        temp = []
        for part in result:
            temp.extend(part.split(d))
        result = temp
    return result

def add(numbers: str):
    total = 0
    negatives = []
    delimiters = [",", "\n", "|"]

    if numbers == "":  # Handle empty string
        return total

    # Handle custom delimiter syntax
    if numbers.startswith("\\") or numbers.startswith("//"):
        custom_delimiters = list(numbers[1])
        delimiters.extend(custom_delimiters)
        numbers = numbers.split("\n", 1)[1]

    # Split numbers using all delimiters
    number_list = split(numbers, delimiters)
    
    for num in number_list:
        if num.startswith("-"):
            negatives.append(num)
        else:
            total += int(num)

    if negatives:
        raise ValueError(f"Negative numbers not allowed {','.join(negatives)}")

    return total

# Test cases
def test_add():
    assert add("") == 0, "Test case 1 failed"
    assert add("1,2") == 3, "Test case 2 failed"
    assert add("1\n2") == 3, "Test case 3 failed"
    assert add("1,2\n3") == 6, "Test case 4 failed"
    assert add("1\n2,3") == 6, "Test case 5 failed"
    assert add("\\;\n1;2;3") == 6, "Test case 6 failed"
    assert add("\\;\n1;2\n3") == 6, "Test case 7 failed"
    # assert add("\\;\n1;2\n3;-4;-5") == 6, "Test case 8 failed"
    print("All test cases pass")

test_add()