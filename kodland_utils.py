import random

def pass_gen(length):
    character = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    pass_length = length
    password = ""

    for i in range(pass_length):
        password += random.choice(character)

    return password

def flip_coin():
    coin = random.randint(1, 2)
    if coin == 1:
        return 'is upper coin'
    else:
        return 'is bottom coin'

def random_emoji():
    emoji = '😀😃😄😁😆'
    selected = random.choice(emoji)
    return selected

def name_selector():
    nama = ['revian', 'michael', 'kenandra']
    selected = random.choice(nama)
    return selected

organik = ['sayur busuk', 'makanan basi', 'kotoran hewan', 'dedaunan']
kertas = ['kardus', 'kertas gorengan', 'kertas', 'paperbag', 'tisu']
plastik = ['kresek', 'botol plastik', 'cup plastik', 'mangkok plastik']
logam = ['kaleng', 'baterai', 'hp', 'elektronik', 'kabel', 'besi berkarat']
