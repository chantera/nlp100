ALPHA = set("abcdefghijklmnopqrstuvwxyz")


def cipher(s):
    return ''.join(chr(219 - ord(c)) if c in ALPHA else c for c in s)


def main():
    s = '1 In the beginning God created the heavens and the earth. 2 Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters. 3 And God said, "Let there be light," and there was light. 4 God saw that the light was good, and he separated the light from the darkness. 5 God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.'  # NOQA
    e = cipher(s)
    print(e)
    d = cipher(e)
    print(d)


if __name__ == "__main__":
    main()
