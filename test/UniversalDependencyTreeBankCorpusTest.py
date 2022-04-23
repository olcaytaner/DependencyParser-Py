import unittest

from DependencyParser.Universal.UniversalDependencyTreeBankCorpus import UniversalDependencyTreeBankCorpus


class TurkishDependencyTreeBankCorpusTest(unittest.TestCase):

    def wordCount(self, corpus: UniversalDependencyTreeBankCorpus)-> int:
        wordCount = 0
        for i in range (0, corpus.sentenceCount()):
            wordCount += corpus.getSentence(i).wordCount()
        return wordCount

    def test_DependencyCorpus1(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_gb-ud-test.conllu")
        self.assertEqual(2802, corpus.sentenceCount())
        self.assertEqual(16881, self.wordCount(corpus))

    def test_DependencyCorpus2(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_imst-ud-dev.conllu")
        self.assertEqual(988, corpus.sentenceCount())
        self.assertEqual(10046, self.wordCount(corpus))

    def test_DependencyCorpus3(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_imst-ud-test.conllu")
        self.assertEqual(983, corpus.sentenceCount())
        self.assertEqual(10029, self.wordCount(corpus))

    def test_DependencyCorpus4(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_imst-ud-train.conllu")
        self.assertEqual(3664, corpus.sentenceCount())
        self.assertEqual(37784, self.wordCount(corpus))

    def test_DependencyCorpus5(self):
        corpus = UniversalDependencyTreeBankCorpus("../tr_pud-ud-test.conllu")
        self.assertEqual(1000, corpus.sentenceCount())
        self.assertEqual(16882, self.wordCount(corpus))

    if __name__ == '__main__':
        unittest.main()
