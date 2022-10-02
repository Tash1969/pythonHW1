from random import randint

quarter = randint(1, 4)
diapasones = ['(x > 0, y > 0)', '(x < 0, y > 0)', '(x < 0, y < 0)', '(x > 0, y < 0)']

def show_diapasone (quart, diapasones):
    return diapasones[quart-1]

print (f'{quarter}: {diapasones[quarter-1]}')