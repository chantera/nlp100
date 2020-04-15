import argparse


def main(file):
    s = {line.split("\t")[0] for line in open(file)}
    for v in sorted(s):
        print(v)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE')

    args = parser.parse_args()
    main(args.file)  # cut -f1 popular-names.txt | sort | uniq
