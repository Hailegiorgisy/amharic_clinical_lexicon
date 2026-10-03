import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from amharic_health import ClinicalLexicon, AmharicClinicalTokenizer

class TestAmharicLexicon(unittest.TestCase):
    def setUp(self):
        self.lexicon = ClinicalLexicon()
        self.tokenizer = AmharicClinicalTokenizer()

    def test_english_lookup(self):
        term = self.lexicon.lookup("Tuberculosis")
        self.assertIsNotNone(term)
        self.assertEqual(term.amharic, "ሳንባ ነቀርሳ")
        self.assertEqual(term.icd10_code, "A15.0")

    def test_amharic_lookup(self):
        term = self.lexicon.lookup("ወባ")
        self.assertIsNotNone(term)
        self.assertEqual(term.english, "Malaria")
        self.assertEqual(term.icd10_code, "B54")

    def test_tokenizer(self):
        text = "በሽተኛው ሳንባ ነቀርሳ እና ወባ አለበት።"
        tokens = self.tokenizer.tokenize(text)
        self.assertIn("ሳንባ", tokens)
        self.assertIn("ነቀርሳ", tokens)
        self.assertIn("ወባ", tokens)

if __name__ == "__main__":
    unittest.main()
