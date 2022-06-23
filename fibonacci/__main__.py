from argparse import ArgumentParser
from . import fibonacci, fibonacci_tiling, fibonacci_word, fibonacci_fractal

parser = ArgumentParser()
parser.add_argument('n', type=int)
parser.add_argument('-l', '--list', action='store_true')
parser.add_argument('-t', '--tiles', action='store_true')
parser.add_argument('-w', '--word', action='store_true')
parser.add_argument('-f', '--fractal', action='store_true')

def main():
    args = parser.parse_args()
    if args.list:
        for i in range(args.n + 1):
            print(fibonacci(i))
    if args.tiles:
        fibonacci_tiling(args.n)
    if args.word:
        print(fibonacci_word(args.n))
    if args.fractal:
        fibonacci_fractal(args.n)
    else:
        print(fibonacci(args.n))


if __name__ == '__main__':
    main()
