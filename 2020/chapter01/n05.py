def create_ngram(seq, n):
    return [tuple(seq[i:i + n]) for i in range(len(seq) - n + 1)]


def main():
    s = "I am an NLPer"
    print(create_ngram(s.split(), 2))
    print(create_ngram(s, 2))


if __name__ == "__main__":
    main()
