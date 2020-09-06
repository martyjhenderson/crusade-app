## I know I need to write tests, I am unsure how to do it
## Until I get the actual Crusade bits built

##Forgive me

def test_primes():
    assert 17 in {
        num
        for num in range(1, 50)
        if num != 1 and not any([num % div == 0 for div in range(2, num)])
    }
