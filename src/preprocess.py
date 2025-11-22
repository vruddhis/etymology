import re

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"[\[\]\{\}]", "", text)
    return text.strip().lower()

def preprocess(df):
    for col in ["term", "related_term", "reltype", "term_lang", "related_lang"]:
        df[col] = df[col].astype(str).apply(clean_text)
    df = df.dropna(subset=["term", "related_term"])
    return df
