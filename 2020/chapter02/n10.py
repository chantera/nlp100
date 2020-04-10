import argparse


def main(file):
    print(sum(1 for _ in open(file)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE')

    args = parser.parse_args()
    main(args.file)  # wc popular-names.txt
