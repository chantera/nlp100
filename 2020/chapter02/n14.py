import argparse


def main(file, n):
    for i, line in enumerate(open(file)):
        if i >= n:
            break
        print(line, end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE')
    parser.add_argument('--lines', '-n', type=int, default=10, metavar='NUM')

    args = parser.parse_args()
    main(args.file, args.lines)  # head -n NUM popular-names.txt
