"""amharic-health-lexicon: Clinical terminology and tokenization toolkit for Amharic healthcare NLP."""
from .lexicon import ClinicalLexicon, MedicalTerm
from .tokenizer import AmharicClinicalTokenizer

__all__ = ["ClinicalLexicon", "MedicalTerm", "AmharicClinicalTokenizer"]
__version__ = "0.1.0"
