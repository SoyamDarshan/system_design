class Sentence:
    def __init__(self, plain_text):
        self.words = []
        plain_text = plain_text.split(' ')
        print(plain_text)
        for i in range(len(plain_text)):
            word = plain_text[i]
            self.words.append(self.Capitalize(word))

    class Capitalize:
        def __init__(self, word, caps=False):
            self.word = word
            self.__capitalize = caps

        @property
        def capitalize(self):
            return self.__capitalize

        @capitalize.setter
        def capitalize(self, caps):
            self.__capitalize = caps

        def __str__(self):
            return self.word

        def __getitem__(self):
            return self.word

        def upper(self):
            return self.word.upper()

    def __str__(self):
        result = []
        for i in range(len(self.words)):
            print(self.words[i].capitalize)
            if self.words[i].capitalize:
                result.append(self.words[i].word.upper())
            else:
                result.append(self.words[i].word)
        return ' '.join(result)

    def __getitem__(self, index):
        return self.words[index]


sen = Sentence('hello World')
sen[1].capitalize = True
print(sen)
