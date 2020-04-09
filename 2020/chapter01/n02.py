def main():
    s1 = "パトカー"
    s2 = "タクシー"
    assert len(s1) == len(s2)
    print(''.join(c for chars in zip(s1, s2) for c in chars))


if __name__ == "__main__":
    main()
