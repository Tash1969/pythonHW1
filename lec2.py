n = int(input('Введите число: '))
def check_mult(n):
    return (n % 5 == 0 or n % 10 == 0 or n % 15 == 0) and n % 30 !=0
print(check_mult(n))