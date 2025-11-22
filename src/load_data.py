import json
import pandas as pd

def load_english_csv(filepath):
    df = pd.read_csv(filepath)
    df["term_lang"] = "English"
    return df[["term", "term_lang", "reltype", "related_term", "related_lang"]]

def load_kaikki_jsonl(filepath):
    records = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            try:
                entry = json.loads(line)
                word = entry.get("word", "")
                lang = entry.get("lang", "")
                if "etymology_templates" in entry:
                    for ety in entry["etymology_templates"]:
                        args = ety.get("args", {})
                        reltype = ety.get("name", "")
                        related_lang = args.get("2", "")
                        related_term = args.get("3", "")
                        if related_term:
                            records.append({
                                "term": word,
                                "term_lang": lang,
                                "reltype": reltype,
                                "related_term": related_term,
                                "related_lang": related_lang
                            })
            except json.JSONDecodeError:
                continue
    return pd.DataFrame(records)

def load_all(english_csv, hindi_jsonl, marathi_jsonl):
    en = load_english_csv(english_csv)
    hi = load_kaikki_jsonl(hindi_jsonl)
    mr = load_kaikki_jsonl(marathi_jsonl)
    return pd.concat([en, hi, mr], ignore_index=True)
