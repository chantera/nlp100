import argparse


def main(file, n):
    with open(file) as f:
        for line in f.readlines()[-n:]:
            print(line, end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE')
    parser.add_argument('--lines', '-n', type=int, default=10, metavar='NUM')

    args = parser.parse_args()
    main(args.file, args.lines)  # tail -n NUM popular-names.txt
