from PIL import Image
from functools import reduce
from io import BytesIO
import requests

def es_palindromo(word):
    return word.lower().replace(" ", "") == word.lower().replace(" ", "")[::-1]

def impares_de(numbers):
    return list(filter(lambda x: x % 2 != 0, numbers))

def cuadrados_sumados(n):
    return reduce(lambda x, y: x + y * y, range(1, n + 1))

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

def img_to_bw(file):
    if file.startswith("http"):
        img = Image.open(BytesIO(requests.get(file).content))
    else:
        img = Image.open(file)
    img.convert("L").show()
    return img

strings = ["ana", "casa", "radar", "reconocer", "somos", "oro", "palabra", "salas", "civic", "level"]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbersXnumbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15]]
images = ["Practica_2\img1.jpg", "https://m.media-amazon.com/images/I/711+zZY-eQL._AC_SL1500_.jpg", "Practica_2\img3.jpg", "Practica_2\img4.jpg", "https://d500.epimg.net/cincodias/imagenes/2019/05/28/lifestyle/1559073183_258744_1559073334_rrss_normal.jpg"]

iterator1 = map(es_palindromo, strings)
iterator2 = map(impares_de, numbersXnumbers)
iterator3 = map(cuadrados_sumados, numbers)
iterator4 = map(factorial, numbers)
iterator5 = map(img_to_bw, images)

print(list(iterator1))
print(list(iterator2))
print(list(iterator3))
print(list(iterator4))
print(list(iterator5))