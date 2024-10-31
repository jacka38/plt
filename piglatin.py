
class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"

        translated_words = []
        words = self.phrase.split()

        for word in words:
            composite_words = word.split('-')
            translated_composite = []

            for composite_word in composite_words:
                vowels = "aeiouAEIOU"

                if composite_word[0] in vowels:
                    if composite_word[-1] == "y":
                        translated_composite.append(composite_word + "nay")
                    elif composite_word[-1] in vowels:
                        translated_composite.append(composite_word + "yay")
                    else:
                        translated_composite.append(composite_word + "ay")
                else:
                    consonant_cluster = ""
                    for char in composite_word:
                        if char in vowels:
                            break
                        consonant_cluster += char

                    translated_composite.append(composite_word[len(consonant_cluster):] + consonant_cluster + "ay")

            translated_words.append('-'.join(translated_composite))

        return ' '.join(translated_words)
