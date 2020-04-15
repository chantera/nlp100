import argparse
import os


def main(file, n):
    with open(file) as f:
        lines = f.readlines()
    n_lines = len(lines)
    size = -(-n_lines // n)  # ceil
    basename, ext = os.path.splitext(os.path.basename(file))
    for i, offset in enumerate(range(0, n_lines, size)):
        with open('{}.{:0>2}{}'.format(basename, i, ext), 'w') as f:
            f.writelines(lines[offset: offset + size])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE')
    parser.add_argument('--number', '-n', type=int, default=10, metavar='NUM')

    args = parser.parse_args()
    main(args.file, args.number)
    # L=$(wc -l < popular-names.txt)
    # S=$(python -c "print(-(-$L // NUM))")
    # split --additional-suffix .txt -d -l $S popular-names.txt popular-names.
