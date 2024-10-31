
class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"

        words = self.phrase.split()
        if len(words) == 1:
            word = words[0]
            vowels = "aeiouAEIOU"

            if word[0] in vowels:
                if word[-1] == "y":
                    return word + "nay"
                elif word[-1] in vowels:
                    return word + "yay"
                else:
                    return word + "ay"

            consonant_cluster = ""
            for char in word:
                if char in vowels:
                    break
                consonant_cluster += char

            return word[len(consonant_cluster):] + consonant_cluster + "ay"

        return ""
