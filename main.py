import csv
import json
from collections import Counter


def load_english_csv(filepath):
    data = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append({
                    "term": row.get("term", "").strip(),
                    "term_lang": "English",
                    "reltype": row.get("reltype", "").strip(),
                    "related_term": row.get("related_term", "").strip(),
                    "related_lang": row.get("related_lang", "").strip(),
                })
    except FileNotFoundError:
        print(f"ile not found at {filepath}")
    return data

def load_kaikki_jsonl(filepath):
    data = []
    try:
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
                                data.append({
                                    "term": word,
                                    "term_lang": lang,
                                    "reltype": reltype,
                                    "related_term": related_term,
                                    "related_lang": related_lang
                                })
                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        print(f"File not found at {filepath}")
    return data

def search_etymology(data, word):
    results = [row for row in data if row["term"] == word]
    if not results:
        #print(f"\n No etymology found for '{word}'.")
        return

    print(f"\n Etymology Relations for '{word}':\n" + "-" * 45)
    for row in results:
        print(f"{row['term']} ({row['term_lang']}) —[{row['reltype']}]→ {row['related_term']} ({row['related_lang']})")


def loanword_stats(data, lang):
    borrowed = [
        row["related_lang"]
        for row in data
        if row.get("term_lang") == lang and "bor" in row.get("reltype", "")
    ]
    return Counter(borrowed)


if __name__ == "__main__":
    english_csv = "etymology.csv"  
    marathi_jsonl = "kaikki.org-dictionary-Marathi.jsonl"  
    hindi_jsonl = "kaikki.org-dictionary-Hindi.jsonl"     

    english_data = load_english_csv(english_csv)

    hindi_data = load_kaikki_jsonl(hindi_jsonl)

    marathi_data = load_kaikki_jsonl(marathi_jsonl)

    all_data = english_data + hindi_data + marathi_data

    while True:
        word = input("\nEnter a word (or 'exit'): ").strip()
        if word.lower() == "exit":
            break
        else:
            search_etymology(all_data, word)
