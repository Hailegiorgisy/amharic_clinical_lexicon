# Amharic Clinical Lexicon

A zero-dependency Python toolkit for bilingual clinical terminology support in Ethiopian healthcare systems. It provides structured English-Amharic mappings for common medical terms, ICD-10 support, transliteration, normalization, and tokenization utilities for healthcare NLP workflows.

## Project Overview

This project was designed to support Amharic-language clinical software, digital health records, and medical informatics tools. It helps bridge language gaps between clinical documentation, coding systems, and interoperable medical data models.

## Key Features

- Bilingual English-Amharic clinical term mappings
- ICD-10 and MeSH-aligned lookup support
- Automatic transliteration for Amharic medical terms
- Text normalization and tokenization for healthcare NLP
- Zero-dependency Python implementation
- Suitable for health information systems, dashboards, and research pipelines

## Why This Matters

Medical systems often rely on a mix of local language inputs and international coding standards. This project helps convert and standardize Amharic healthcare language into structured, searchable, and machine-readable forms.

## Installation

```bash
git clone https://github.com/Hailegiorgisy/amharic_clinical_lexicon.git
cd amharic_clinical_lexicon
pip install -r requirements.txt
```

If the repository is used directly as a module:

```bash
python -m pip install .
```

## Quickstart

```python
from amharic_health import ClinicalLexicon

lex = ClinicalLexicon()
term = lex.lookup("ሳንባ ነቀርሳ")
print(f"{term.english} -> ICD-10: {term.icd10_code} ({term.transliteration})")
```

## Example Use Cases

- Clinical term lookup for Amharic EHR forms
- Medical NLP preprocessing for local-language notes
- Terminology standardization in telemedicine systems
- ICD coding assistance for Ethiopian healthcare datasets

## Repository Structure

```text
amharic_clinical_lexicon/
├── amharic_health/
├── data/
├── tests/
├── README.md
├── requirements.txt
└── setup.py
```

## Data Coverage

The lexicon is intended to include common clinical concepts in Amharic and English, including:

- Symptoms and diagnoses
- Body systems and anatomy
- Medication names and common conditions
- Standard diagnostic coding references

## Contributing

Contributions are welcome, especially for expanding terminology coverage and improving transliteration quality.

## License

This project is open-source and distributed under the MIT license unless otherwise noted in the repository.
