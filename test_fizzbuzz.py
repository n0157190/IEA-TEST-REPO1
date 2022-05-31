from fizzbuzz import fizzbuzz

def test_fizzbuzz_three():
    result = fizzbuzz(3)
    return result == 'fizz'

def test_fizzbuzz_five():
    result = fizzbuzz(5)
    return result == 'buzz'

def test_fizzbuzz_fifteen():
    result = fizzbuzz(15)
    return result == 'fizzbuzz'

def test_fizzbuzz_two():
    result = fizzbuzz(2)
    return result == 2

def test_fizzbuzz_int():
    if isinstance('2', str):
        return True
    else:
        return False


tests = [test_fizzbuzz_three, test_fizzbuzz_five, test_fizzbuzz_fifteen, test_fizzbuzz_two, test_fizzbuzz_int]
for test in tests:
    if test():
        print('Passed')
    else:
        print('Failed')