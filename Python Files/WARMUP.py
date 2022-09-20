def is_prime(num):
    if num < 2:
        return False
    else: 
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

print(is_prime(5))
print(is_prime(10))