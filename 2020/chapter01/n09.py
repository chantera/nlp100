import random


def shuffle(w, min_length=5):
    if len(w) < min_length:
        return w
    body = list(w[1:-1])
    random.shuffle(body)
    return w[0] + ''.join(body) + w[-1]


def create_typo(s):
    return ' '.join(shuffle(w) for w in s.split())


def main():
    s = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."  # NOQA
    print(create_typo(s))


if __name__ == "__main__":
    main()
