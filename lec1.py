N = int(input('Введите число: '))

def get_numbers(N):
    return [i for i in range(-N, N + 1)]
  
print(get_numbers(N))