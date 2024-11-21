
def is_prime(num):
    if num <=1:
        return False
        print("Choose a number larger than 1")
    else:
          for i in range (2,num):
            if num % i == 0:
                return False
                print(f"{num} is a composit number.")
                break
            else:
                return True
                print(f"{num} is a prime number.")
                break
        

is_prime(3)