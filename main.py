def add(numbers:str):
    sum = 0
    if numbers == "": #handling empty string
        return sum
    else:
        #handle new lines between numbers and also comma seperated value
        if "\n" in numbers:
            numbers = numbers.split("\n")
        else:
            numbers = numbers.split(",")
        for num in numbers:
            if isinstance(num, str):
                for n in num.split(","):
                    sum += int(n)
            else:
                print(num)
                sum += int(num)
    return sum

assert add("") == 0, "Test case failed: Expected 0 for empty string"
assert add("1,2,3") == 6, "Test case failed: Expected 6 for '1,2,3'"
assert add("1\n2,3") == 6, "Test case failed: Expected 6 for '1\\n2,3'"
assert add("4\n5\n6") == 15, "Test case failed: Expected 15 for '4\\n5\\n6'"