import unittest
import os
from classes.UniqueSequenceGenerator import UniqueSequenceGenerator


# Tests for the UniqueSequenceGenerator class
class TestUniqueSequenceGenerator(unittest.TestCase):

    # Tests successful construction of UniqueSequenceGenerator
    def test_construct(self):
        sg = UniqueSequenceGenerator(100)
        self.assertIsNotNone(sg)

    # Tests adding a word to UniqueSequenceGenerator
    def test_add_word(self):
        sg = UniqueSequenceGenerator(4)
        sg.add_word("beard")
        self.assertEquals(sg.get_sequences_and_words(), {'eard': 'beard', 'bear': 'beard'})

    # Tests adding multiple words to UniqueSequenceGenerator
    def test_add_words(self):
        sg = UniqueSequenceGenerator(4)
        sg.add_word("beard")
        sg.add_word("shark")
        self.assertEquals(sg.get_sequences_and_words(),
                          {'bear': 'beard', 'eard': 'beard', 'hark': 'shark', 'shar': 'shark'})

    # Tests adding a word shorter than sequence length in UniqueSequenceGenerator
    def test_add_short_word(self):
        sg = UniqueSequenceGenerator(10)
        sg.add_word("abc")
        self.assertEquals(sg.get_sequences_and_words(), {})

    # Tests adding a blank string in UniqueSequenceGenerator
    def test_add_short_word(self):
        sg = UniqueSequenceGenerator(10)
        sg.add_word("")
        self.assertEquals(sg.get_sequences_and_words(), {})

    # Tests adding a non-string in UniqueSequenceGenerator
    def test_add_short_word(self):
        with self.assertRaises(AttributeError):
            sg = UniqueSequenceGenerator(10)
            sg.add_word(123)

    # Tests behavior of different sequence lengths with UniqueSequenceGenerator
    def test_sequence_lengths(self):
        sg = UniqueSequenceGenerator(1)
        sg.add_word("beard")
        self.assertEquals(sg.get_sequences_and_words(),
                          {'a': 'beard', 'e': 'beard', 'r': 'beard', 'b': 'beard', 'd': 'beard'})

        sg = UniqueSequenceGenerator(3)
        sg.add_word("alpaca")
        self.assertEquals(sg.get_sequences_and_words(),
                          {'aca': 'alpaca', 'alp': 'alpaca', 'lpa': 'alpaca', 'pac': 'alpaca'})

        sg = UniqueSequenceGenerator(6)
        sg.add_word("sharknado")
        self.assertEquals(sg.get_sequences_and_words(),
                          {'arknad': 'sharknado', 'harkna': 'sharknado', 'rknado': 'sharknado', 'sharkn': 'sharknado'})

    # Tests behavior of bad sequence lengths with UniqueSequenceGenerator
    def test_sequence_lengths_out_of_bounds(self):
        with self.assertRaises(IndexError):
            UniqueSequenceGenerator(0)

        with self.assertRaises(IndexError):
            UniqueSequenceGenerator(-1)

    # Tests get_sequences_and_words when nothing has been added
    def test_get_sequences_and_words_empty(self):
        sg = UniqueSequenceGenerator(4)
        self.assertEquals(sg.get_sequences_and_words(), {})


# Tests for overall application functionality
class TestWordsFunctionality(unittest.TestCase):

    # Tests overall functionality of the application against known good unix_dict outputs.
    def test_functionality_unix_dict(self):
        try:
            os.unlink('tests/outputs/unix_dict/sequences')
        except OSError:
            pass

        try:
            os.unlink('tests/outputs/unix_dict/words')
        except OSError:
            pass

        os.system("python words_solution.py inputs/unix_dict.txt tests/outputs/unix_dict -n 4")

        with open("outputs/unix_dict/words", "r") as eSeqHandle, open("tests/outputs/unix_dict/words", "r") as tSeqHandle:
            expect_content = eSeqHandle.read()
            test_content = tSeqHandle.read()
            self.assertGreater(len(expect_content), 0)
            self.assertGreater(len(test_content), 0)
            self.assertEquals(expect_content, test_content)


if __name__ == '__main__':
    unittest.main()
