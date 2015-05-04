class UniqueSequenceGenerator:
    """ Utility class that accepts a variable number of dictionary words and calculates n-length unique sequences """

    ##
    # __init__ constructs the class
    #
    # @param self a UniqueSequenceGenerator
    # @param sequence_length the length of sequences to generate
    def __init__(self, sequence_length):
        if sequence_length <= 0:
            raise IndexError

        self.sequence_length = sequence_length
        self.sequence_map = {}

    ##
    # add_word accepts a dictionary word and then splits it into as many unique sequences as possible. These sequences
    # are then added to a map which keeps track of the source word and uniqueness.
    #
    # @param self a UniqueSequenceGenerator
    # @param word the dictionary word

    def add_word(self, word):
        word = word.strip().lower()

        for i in range(0, len(word) - self.sequence_length + 1):
            seq = word[i:i+self.sequence_length]

            if seq in self.sequence_map:
                self.sequence_map[seq]["unique"] = False
            else:
                self.sequence_map[seq] = {"word": word, "unique": True}

    ##
    # get_sequences_and_words returns a filtered map where duplicate sequences are removed
    #
    # @returns dict the filtered map

    def get_sequences_and_words(self):
        return {k: v["word"] for k, v in self.sequence_map.iteritems() if v["unique"]}