from argparse import ArgumentParser
from . import fibonacci

parser = ArgumentParser()
parser.add_argument('n', type=int)
parser.add_argument('-l', '--list', action='store_true')

def main():
    args = parser.parse_args()
    if args.list:
        for i in range(args.n + 1):
            print(fibonacci(i))
    else:
        print(fibonacci(args.n))


if __name__ == '__main__':
    main()
