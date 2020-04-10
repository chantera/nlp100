import argparse


def main(in_file, out_file1, out_file2):
    with open(out_file1, 'w') as f1, open(out_file2, 'w') as f2:
        for line in open(in_file):
            cols = line.split("\t")
            f1.write(cols[0] + "\n")
            f2.write(cols[1] + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE')

    args = parser.parse_args()
    main(args.file, 'col1.txt', 'col2.txt')
    # cut -f 1 popular-names.txt > col1.txt
    # cut -f 2 popular-names.txt > col2.txt
