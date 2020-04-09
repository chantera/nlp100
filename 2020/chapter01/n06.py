from n05 import create_ngram


def main():
    s1 = "paraparaparadise"
    s2 = "paragraph"
    x = set(create_ngram(s1, 2))
    y = set(create_ngram(s2, 2))
    print(x | y)
    print(x & y)
    print(x - y)
    print(('s', 'e') in x)
    print(('s', 'e') in y)


if __name__ == "__main__":
    main()
