import os
import argparse

from classes.unique_sequence_generator import UniqueSequenceGenerator


parser = argparse.ArgumentParser(description='An n-length unique sequence generator.')
parser.add_argument('file_in')
parser.add_argument('directory_out')
parser.add_argument('-n', type=int, default=4, help='Sequence length, defaults to 4')
args = parser.parse_args()

seqGen = UniqueSequenceGenerator(args.n)

try:
    with open(args.file_in) as inHandle:
        for line in inHandle:
            seqGen.add_word(line)
except IOError:
    exit("There was a problem reading from the input file.")

# Using path.join prevents issues with trailing slashes
outSeqFile = os.path.join(args.directory_out, "sequences")
outWordFile = os.path.join(args.directory_out, "words")

try:
    with open(outSeqFile, "w+") as outSeqHandle, open(outWordFile, "w+") as outWordsHandle:
        seq_word = seqGen.get_sequences_and_words()

        for seq in seq_word.iterkeys():
            outSeqHandle.write(seq + "\n")
            outWordsHandle.write(seq_word[seq] + "\n")
except IOError:
    exit("There was a problem writing to the output files.")