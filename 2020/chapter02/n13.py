import argparse


def main(in_file1, in_file2, out_file):
    with open(out_file, 'w') as f:
        for line1, line2 in zip(open(in_file1), open(in_file2)):
            f.write("{}\t{}\n".format(line1.rstrip(), line2.rstrip()))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE')

    args = parser.parse_args()
    main('col1.txt', 'col2.txt', args.file)  # paste col1.txt col2.txt > FILE
