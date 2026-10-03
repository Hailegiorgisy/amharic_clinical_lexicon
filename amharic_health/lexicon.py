from dataclasses import dataclass
from typing import Optional, List, Dict

@dataclass
class MedicalTerm:
    english: str
    amharic: str
    transliteration: str
    icd10_code: Optional[str]
    category: str

CLINICAL_DICTIONARY: List[MedicalTerm] = [
    MedicalTerm("Tuberculosis", "ሳንባ ነቀርሳ", "Sanba Nekersa", "A15.0", "Infectious Disease"),
    MedicalTerm("Malaria", "ወባ", "Woba", "B54", "Vector-Borne Disease"),
    MedicalTerm("Diabetes Mellitus", "የስኳር በሽታ", "Yesukuar Beshita", "E11", "Endocrine / Metabolic"),
    MedicalTerm("Malnutrition", "ተመጣጣኝ ያልሆነ አመጋገብ", "Temetatagn Yalhone Amegageb", "E46", "Nutritional Deficiency"),
    MedicalTerm("Hypertension", "የደም ግፊት", "Yedem Gifit", "I10", "Cardiovascular"),
    MedicalTerm("Pneumonia", "የሳንባ ምች", "Yesanba Mich", "J18.9", "Respiratory"),
    MedicalTerm("Anemia", "የደም ማነስ", "Yedem Manes", "D64.9", "Hematological"),
    MedicalTerm("Pregnancy", "እርግዝና", "Irgzina", "Z33.1", "Maternal Health"),
    MedicalTerm("Vaccination", "ክትባት", "Kitibat", "Z28", "Preventive Care"),
    MedicalTerm("Severe Acute Malnutrition", "ከባድ አጣዳፊ የተመጣጠነ ምግብ እጥረት", "Kebad Atadafi Yetemetatene Migib Itret", "E43", "Nutritional Deficiency")
]

class ClinicalLexicon:
    """Bilingual dictionary lookup and concept standardization for Amharic healthcare text."""
    def __init__(self):
        self._en_index: Dict[str, MedicalTerm] = {t.english.lower(): t for t in CLINICAL_DICTIONARY}
        self._am_index: Dict[str, MedicalTerm] = {t.amharic: t for t in CLINICAL_DICTIONARY}

    def lookup(self, term: str) -> Optional[MedicalTerm]:
        term_clean = term.strip()
        if term_clean.lower() in self._en_index:
            return self._en_index[term_clean.lower()]
        if term_clean in self._am_index:
            return self._am_index[term_clean]
        return None

    def search_by_category(self, category: str) -> List[MedicalTerm]:
        return [t for t in CLINICAL_DICTIONARY if category.lower() in t.category.lower()]
