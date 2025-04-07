def add(numbers:str):
    sum = 0
    if numbers == "": #handling empty string
        return sum
    else:
        numbers = numbers.split(",") #handling values if passed comma seperated
        for num in numbers:
            sum += int(num)
    return sum

assert add("") == 0, "Test case failed: Expected 0 for empty string"
assert add("1,2,3") == 6, "Test case failed: Expected 6 for '1,2,3'"
assert add("4,5,6") == 12, "Test case failed: Expected 15 for '4,5,6'"