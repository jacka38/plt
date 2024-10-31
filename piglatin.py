
class PigLatin:

    def __init__(self, phrase: str):
        self.phrase = phrase

    def get_phrase(self) -> str:
        return self.phrase

    def translate(self) -> str:
        if self.phrase == "":
            return "nil"

        vowels = "aeiouAEIOU"
        if len(self.phrase.split()) == 1 and self.phrase[0] in vowels:
            if self.phrase[-1] == "y":
                return self.phrase + "nay"
            elif self.phrase[-1] in vowels:
                return self.phrase + "yay"
            else:
                return self.phrase + "ay"

        return ""
