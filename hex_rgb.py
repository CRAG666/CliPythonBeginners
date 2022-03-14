import argparse
import sys


def hex_to_rgb(hex):
    hex = hex.lstrip("#")
    return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))


def infer(args):
    for color in args.colors:
        print(f"rgb{hex_to_rgb(color)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(usage=f"{sys.argv[0]} -c #ec7802 #a37513")

    parser.add_argument(
        "-c", "--colors", type=str, nargs="+", help=f"{sys.argv[0]} -c #f2f2f2"
    )
    args = parser.parse_args()
    infer(args)
