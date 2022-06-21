from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('n', type=int)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    args = parser.parse_args()
    print(fibonacci(args.n))


if __name__ == '__main__':
    main()
