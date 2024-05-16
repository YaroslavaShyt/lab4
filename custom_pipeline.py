from spacy.lang.uk import Ukrainian

custom_lemmas = {
        "епефілум": "епефілум",
        "троянд": "троянда",
        "стапелі": "стапелія",
        "різдвяник": "різдвяник",
        "гвоздик": "гвоздика"
    }

@Ukrainian.factory("custom_lemma")
def create_uk_lemmatizer(nlp, name):
    return CustomLemmatizer(custom_lemmas)


class CustomLemmatizer:
    def __init__(self, custom_lemmas):
        self.custom_lemmas = custom_lemmas

    def __call__(self, doc):
        for token in doc:
            isSame = False
            for lemma in self.custom_lemmas:
                for index in range(len(lemma)):
                    if lemma[index] == token.text.lower()[index]:
                        isSame = True
                    else:
                        isSame = False
                        break
                if isSame:
                    token.lemma_ = self.custom_lemmas[lemma]
        return doc