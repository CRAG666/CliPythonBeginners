import sys

if __name__ == "__main__":
    arg = "-d"
    if arg in sys.argv:
        print("argumento pasado")

    else:
        print("Este programa necesita argumentos posicionales")
