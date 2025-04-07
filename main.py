def add(numbers:str):
    sum = 0
    if numbers == "": #handling empty string
        return sum
    else:
        if numbers.startswith("\\") or numbers.startswith("//"): #handling custom delimiter
            delimiter = numbers[1]
            numbers= numbers[2:]
            numbers = numbers.replace("\n", delimiter)
            numbers = numbers.split(delimiter)
        elif '\n' in numbers:
            numbers = numbers.split("\n")
        else:
            numbers = numbers.split(",")
            
        for num in numbers:
            if num!='':
                if ',' in num:
                    num = num.split(",")
                    for n in num:
                        sum += int(n)
                else:
                    sum += int(num) #converting string to int and adding to sum
            
    return sum



#Testcases
def test_add():
    assert add("") == 0, "Test case 1 failed"
    assert add("1,2") == 3, "Test case 2 failed"
    assert add("1\n2") == 3, "Test case 3 failed"
    assert add("1,2\n3") == 6, "Test case 4 failed"
    assert add("1\n2,3") == 6, "Test case 5 failed"
    assert add("\\;\n1;2;3") == 6, "Test case 6 failed"
    assert add("\\;\n1;2\n3") == 6, "Test case 7 failed"
    print("All test cases pass")
    
    
test_add()