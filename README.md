# amharic-health-lexicon: Bilingual English-Amharic Clinical Terminology & NLP

A zero-dependency Python toolkit providing structured bilingual medical mappings (MeSH, ICD-10), phonetic transliterations, and text tokenization for Ethiopian healthcare software.

## Quickstart
```python
from amharic_health import ClinicalLexicon

lex = ClinicalLexicon()
term = lex.lookup("ሳንባ ነቀርሳ")
print(f"{term.english} -> ICD-10: {term.icd10_code} ({term.transliteration})")
```
