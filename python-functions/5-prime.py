def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
        return True
        
is_prime(7)   # True
is_prime(14)   # False
is_prime(23)   # True
is_prime(100)  # False