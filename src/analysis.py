import numpy as np

def levenshtein_distance(a, b):
    n, m = len(a), len(b)
    if n == 0: return m
    if m == 0: return n
    dp = np.zeros((n+1, m+1), dtype=int)
    dp[0, :] = np.arange(m+1)
    dp[:, 0] = np.arange(n+1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            dp[i, j] = min(
                dp[i-1, j] + 1,      
                dp[i, j-1] + 1,      
                dp[i-1, j-1] + cost  
            )
    return dp[n, m]

def soundex(word):
    word = word.upper()
    if not word: return ""
    codes = {"BFPV": "1", "CGJKQSXZ": "2", "DT": "3", "L": "4", "MN": "5", "R": "6"}
    first = word[0]
    tail = ""
    for char in word[1:]:
        for key, val in codes.items():
            if char in key:
                c = val
                break
        else:
            c = ""
        tail += c
    tail = tail.replace("0", "")
    tail = "".join(ch for i, ch in enumerate(tail) if i == 0 or ch != tail[i-1])
    return (first + tail + "000")[:4]

def similarity_score(w1, w2):
    if not w1 or not w2:
        return 0.0
    
    lev = levenshtein_distance(w1, w2)
    lev_sim = 1 - lev / max(len(w1), len(w2))
    s1, s2 = soundex(w1), soundex(w2)
    phonetic_sim = sum(c1 == c2 for c1, c2 in zip(s1, s2)) / 4.0
    
    return round((lev_sim + phonetic_sim) / 2, 3)

def add_similarity(df):
    df["similarity"] = [
        similarity_score(t, r)
        for t, r in zip(df["term"], df["related_term"])
    ]
    return df
