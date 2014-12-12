from mrjob.job import MRJob
class MRAnagram(MRJob):

    def mapper(self, _, line):
        # Get the list of letters
        letters=list(line)
        letters.sort()
        yield letters, line

    def reducer(self, _, words):
        # Get the list of words containing these letters.
        anagrams = [w for w in words]

        # Only yield results if there are at least two words which are
        # anagrams of each other.
        if len(anagrams)>1:
            yield len(anagrams), anagrams


if __name__ == "__main__":
    MRAnagram.run()