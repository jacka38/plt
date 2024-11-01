
from error import PigLatinError


class PigLatin:
    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"

        allowed_punctuation = {'.', ',', ';', ':', "'", '?', '!', '(', ')'}
        translated_words = []
        words = self.phrase.split()

        for word in words:
            core_word = ""
            trailing_punctuation = ""
            for i in range(len(word)):
                if word[-(i+1)] in allowed_punctuation:
                    trailing_punctuation = word[-(i+1)] + trailing_punctuation
                else:
                    core_word = word[:len(word)-i]
                    break

            for char in core_word:
                if not char.isalpha() and char != '-':
                    raise PigLatinError(f"Invalid punctuation: '{char}'")

            composite_words = core_word.split('-')
            translated_composite = []

            for composite_word in composite_words:
                if not composite_word:
                    translated_composite.append(composite_word)
                    continue

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

                    translated_core = composite_word[len(consonant_cluster):] + consonant_cluster + "ay"
                    translated_composite.append(translated_core)

            translated_word = '-'.join(translated_composite) + trailing_punctuation
            translated_words.append(translated_word)

        return ' '.join(translated_words)
