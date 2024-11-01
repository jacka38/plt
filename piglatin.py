
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
                if word[-(i + 1)] in allowed_punctuation:
                    trailing_punctuation = word[-(i + 1)] + trailing_punctuation
                else:
                    core_word = word[:len(word) - i]
                    break

            if not (core_word.isupper() or core_word.istitle() or core_word.islower()):
                raise PigLatinError(f"Invalid case format: '{core_word}'")

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
                is_upper = composite_word.isupper()
                is_title = composite_word.istitle()

                if composite_word[0] in vowels:
                    if composite_word[-1] == 'y':
                        translation = composite_word + ("NAY" if is_upper else "nay")
                    elif composite_word[-1] in vowels:
                        translation = composite_word + ("YAY" if is_upper else "yay")
                    else:
                        translation = composite_word + ("AY" if is_upper else "ay")
                else:
                    consonant_cluster = ""
                    for char in composite_word:
                        if char in vowels:
                            break
                        consonant_cluster += char

                    translation = composite_word[len(consonant_cluster):] + consonant_cluster + (
                        "AY" if is_upper else "ay")

                if is_title:
                    translation = translation.capitalize()
                elif is_upper:
                    translation = translation.upper()

                translated_composite.append(translation)

            translated_word = '-'.join(translated_composite) + trailing_punctuation
            translated_words.append(translated_word)

        return ' '.join(translated_words)
