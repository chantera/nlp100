import argparse


def main(file):
    for line in open(file):
        print(line.replace("\t", ' '), end='')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE')

    args = parser.parse_args()
    main(args.file)  # sed -e "s/\t/ /g" popular-names.txt
