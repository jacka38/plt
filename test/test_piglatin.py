
import unittest

from error import PigLatinError
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

    def test_translate_phrase_with_punctuation(self):
        translator_hello_world_exclamation = PigLatin("hello world!")
        self.assertEqual(translator_hello_world_exclamation.translate(), "ellohay orldway!")

        translator_with_punctuation = PigLatin("well-being, good day.")
        self.assertEqual(translator_with_punctuation.translate(), "ellway-eingbay, oodgay ayday.")

    def test_translate_invalid_punctuation(self):
        with self.assertRaises(PigLatinError):
            translator_invalid = PigLatin("hello world@")
            translator_invalid.translate()

    def test_translate_uppercase_word(self):
        translator = PigLatin("APPLE")
        self.assertEqual(translator.translate(), "APPLEYAY")

    def test_translate_titlecase_word(self):
        translator = PigLatin("Hello")
        self.assertEqual(translator.translate(), "Ellohay")

    def test_translate_invalid_case(self):
        translator = PigLatin("biRd")
        with self.assertRaises(PigLatinError):
            translator.translate()

    def test_translate_title_case_phrase(self):
        translator = PigLatin("Hello World")
        self.assertEqual(translator.translate(), "Ellohay Orldway")

    def test_translate_upper_case_phrase(self):
        translator = PigLatin("HELLO WORLD")
        self.assertEqual(translator.translate(), "ELLOHAY ORLDWAY")

if __name__ == "__main__":
    unittest.main()
