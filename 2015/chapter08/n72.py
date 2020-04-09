#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

from n71 import is_stopword
from nltk import PorterStemmer

stemmer = PorterStemmer()


class BagOfWords:

    """retrive bag-of-words from Documents

    Attributes:
        docs: Target for Parsing
        words: All words in bags
    """

    def __init__(self, docs):
        """initialize"""
        self.docs = docs
        self.exclude_stopwords = True
        self.use_stems = True
        self._make_list()

    def _make_list(self):
        """Make a word list from docs"""
        words = []
        attribute = "words" if not self.use_stems else "stems"
        for doc in self.docs:
            source = getattr(doc, attribute)
            for word in source:
                if self.exclude_stopwords and is_stopword(word):
                    continue
                if word not in words:
                    words.append(word)
        self.words = words

    def get_vector(self):
        """
            get vector of each doc

            Returns:
                Array of vectors
        """
        vectors = []
        attribute = "words" if not self.use_stems else "stems"
        for doc in self.docs:
            vector = []
            source = getattr(doc, attribute)
            for word in self.words:
                value = source.get(word, 0)
                vector.append(value)
            vectors.append(vector)
        return vectors


class Document:

    def __init__(self, text):
        self.source = text
        self._extract(text)

    def _extract(self, text):
        words = text.lower().split(" ")
        word_count = {}
        stem_count = {}
        for word in words:
            word = word.strip()
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
            stem = stemmer.stem(word)
            if stem in stem_count:
                stem_count[stem] += 1
            else:
                stem_count[stem] = 1
        self.words = word_count
        self.stems = stem_count


if __name__ == "__main__":
    with open("sentiment.txt", "r") as train_f:
        labels = []
        docs = []
        for line in train_f:
            label = int(line[0:2])
            labels.append(1 if label > 0 else 0)
            docs.append(Document(line[3:]))
        bow = BagOfWords(docs)
        vectors = bow.get_vector()
        print("\t".join(["<LABEL>"] + bow.words))
        for i, vector in enumerate(vectors):
            vector = [str(v) for v in vector]
            print("\t".join([str(labels[i])] + vector))
