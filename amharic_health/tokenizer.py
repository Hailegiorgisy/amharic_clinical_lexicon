import re
from typing import List

class AmharicClinicalTokenizer:
    """Lightweight rule-based tokenizer for Ge'ez/Amharic clinical notes."""
    def __init__(self):
        # Ethiopic punctuation markers: ። (full stop), ፣ (comma), ፤ (semicolon), ፥ (colon)
        self.delim_regex = re.compile(r"[\s።፣፤፥]+")

    def tokenize(self, text: str) -> List[str]:
        tokens = self.delim_regex.split(text.strip())
        return [t for t in tokens if t]
