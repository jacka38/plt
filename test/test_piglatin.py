
import unittest
from piglatin import PigLatin


class TestPigLatin(unittest.TestCase):

    def test_get_phrase(self):
        translator = PigLatin("hello world")
        self.assertEqual(translator.get_phrase(), "hello world")

    def test_translate_empty_phrase(self):
        translator = PigLatin("")
        self.assertEqual(translator.translate(), "nil")

    def test_translate_word_starting_with_vowel(self):
        translator_any = PigLatin("any")
        self.assertEqual(translator_any.translate(), "anynay")

        translator_apple = PigLatin("apple")
        self.assertEqual(translator_apple.translate(), "appleyay")

        translator_ask = PigLatin("ask")
        self.assertEqual(translator_ask.translate(), "askay")

    def test_translate_word_starting_with_single_consonant(self):
        translator_hello = PigLatin("hello")
        self.assertEqual(translator_hello.translate(), "ellohay")

    def test_translate_word_starting_with_multiple_consonants(self):
        translator_known = PigLatin("known")
        self.assertEqual(translator_known.translate(), "ownknay")

    def test_translate_phrase_with_multiple_words(self):
        translator_hello_world = PigLatin("hello world")
        self.assertEqual(translator_hello_world.translate(), "ellohay orldway")

        translator_well_being = PigLatin("well-being")
        self.assertEqual(translator_well_being.translate(), "ellway-eingbay")


if __name__ == "__main__":
    unittest.main()
