# -*- coding: utf-8 -*-
"""
Calculate the term frequency - inverse document frequency which indicates how unique a word(token) is to a
specific document. Assumes words are separated by white space and documents have been pre-processed to
remove stop words/punctuation.
"""

import math


class TFIDF:

    @staticmethod
    def word_frequency(word, document):
        """Return number of times a word appears in a document."""
        return document.split(None).count(word)

    @staticmethod
    def word_count(document):
        """Return how many words are in a document."""
        return len(document.split(None))

    @staticmethod
    def number_docs_containing(word, document_list):
        """Return how many documents contain the word"""
        count = 0
        for document in document_list:
            if TFIDF.word_frequency(word, document) > 0:
                count += 1
        return count

    @staticmethod
    def term_frequency(word, document):
        """
        Return the number of times a word occurs relative to the total number of words in the document.
        Normalizes the term frequency to avoid biasing towards longer documents.
        """
        freq = TFIDF.word_frequency(word, document)
        return freq / float(TFIDF.word_count(document))

    @staticmethod
    def inverse_document_frequency(word, document_list):
        """
        Return the relative frequency of all documents to documents containing the word.
        Normalizes the term frequency across all documents so common words have little weight.
        """
        total = len(document_list)
        containing = TFIDF.number_docs_containing(word, document_list)
        return math.log(float(total / containing), 10)

    @staticmethod
    def term_frequency_inverse_document_frequency(word, document, document_list):
        """Return the TF-IDF of a word."""
        term_freq = TFIDF.term_frequency(word, document)
        inv_doc_freq = TFIDF.inverse_document_frequency(word, document_list)
        return term_freq * inv_doc_freq


from unittest import TestCase


class TestTFIDF(TestCase):

    _document_list = []
    _document = "A cat saw a sea shell by the sea shore"

    @classmethod
    def setUpClass(cls):
        cls._document_list.append(cls._document)
        cls._document_list.append("The quick brown fox jumped over the flamed out wreck")
        cls._document_list.append("Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor.")
        cls._document_list.append("The cat was extremely helpful in all the things")
        cls._document_list.append("While doing science the cat fell asleep in a box")

    def test_word_frequency(self):
        result = TFIDF.word_frequency("sea", self._document)
        self.assertEqual(result, 2)

    def test_word_count(self):
        result = TFIDF.word_count(self._document)
        self.assertEqual(result, 10)

    def test_number_docs_containing(self):
        result = TFIDF.number_docs_containing("cat", self._document_list)
        self.assertEqual(result, 3)

    def test_term_frequency_common(self):
        result = TFIDF.term_frequency("sea", self._document)
        # 2 / 10
        self.assertAlmostEquals(result, 0.2, 1)

    def test_term_frequency_rare(self):
        result = TFIDF.term_frequency("shore", self._document)
        # 1 / 10
        self.assertAlmostEquals(result, 0.1, 1)

    def test_inverse_document_frequency_common(self):
        result = TFIDF.inverse_document_frequency("cat", self._document_list)
        self.assertAlmostEquals(result, 0.0, 1)

    def test_inverse_document_frequency_rare(self):
        result = TFIDF.inverse_document_frequency("helpful", self._document_list)
        self.assertAlmostEquals(result, 0.70, 2)

    def test_term_frequency_inverse_document_frequency_common(self):
        result = TFIDF.term_frequency_inverse_document_frequency("the", self._document, self._document_list)
        self.assertAlmostEquals(result, 0.0, 1)

    def test_term_frequency_inverse_document_frequency_rare(self):
        result = TFIDF.term_frequency_inverse_document_frequency("shore", self._document, self._document_list)
        self.assertAlmostEquals(result, 0.07, 3)

    def test_rare_has_higher(self):
        common = TFIDF.term_frequency_inverse_document_frequency("cat", self._document, self._document_list)
        rare = TFIDF.term_frequency_inverse_document_frequency("shore", self._document, self._document_list)
        self.assertTrue(common < rare)

    def test_single_occurances_have_same(self):
        one = TFIDF.term_frequency_inverse_document_frequency("shell", self._document, self._document_list)
        two = TFIDF.term_frequency_inverse_document_frequency("shore", self._document, self._document_list)
        self.assertAlmostEquals(one, two, 0.3)
