# src/lang_map.py

import pandas as pd
import plotly.graph_objects as go

LAMG_TO_COORD = {
    "hindi": (28.7, 77.2),
    "urdu": (28.7, 77.2),
    "marathi": (18.5, 73.9),
    "old marathi": (18.5, 73.9),
    "sanskrit": (30.0, 70.0),
    "bhojpuri": (25.6, 85.1),
    "bengali": (23.7, 90.4),
    "assamese": (26.1, 91.8),
    "maithili": (26.3, 85.9),
    "gujarati": (23.2, 72.7),
    "punjabi": (31.1, 74.3),
    "old hindi": (28.7, 77.2),
    "early assamese": (26.1, 91.8),
    "middle assamese": (26.1, 91.8),
    "magahi": (24.8, 85.0),
    "oriya": (20.3, 85.8),
    "kashmiri": (34.1, 74.8),
    "nepali": (27.7, 85.3),
    "sauraseni prakrit": (28.7, 77.2),
    "maharastri prakrit": (18.5, 73.9),
    "prakrit": (23.5, 78.0),
    "ashokan prakrit": (25.5, 80.0),
    "takka apabhramsa": (31.1, 75.0),
    "gawar apabhramsa": (28.7, 77.2),
    "gurjar apabhramsa": (23.2, 72.7),
    "tamil": (10.8, 78.7),
    "old tamil": (10.8, 78.7),
    "middle tamil": (10.8, 78.7),
    "kannada": (15.4, 75.1),
    "old kannada": (15.4, 75.1),
    "middle kannada": (15.4, 75.1),
    "telugu": (15.9, 80.0),
    "malayalam": (10.5, 76.2),
    "tulu": (13.0, 74.8),
    "english": (51.5, -0.1),
    "old english": (51.5, -0.1),
    "middle english": (51.5, -0.1),
    "german": (50.1, 8.7),
    "old high german": (49.0, 10.0),
    "middle high german": (50.0, 10.0),
    "middle low german": (53.5, 10.0),
    "german low german": (53.5, 10.0),
    "dutch": (52.3, 4.9),
    "old dutch": (51.5, 4.5),
    "middle dutch": (51.5, 4.5),
    "french": (48.9, 2.3),
    "old french": (48.9, 2.3),
    "middle french": (48.9, 2.3),
    "italian": (43.8, 11.2),
    "spanish": (40.4, -3.7),
    "old spanish": (42.0, -3.0),
    "portuguese": (40.0, -8.0),
    "old portuguese": (42.8, -7.9),
    "galician": (42.8, -7.9),
    "catalan": (41.4, 2.2),
    "occitan": (43.6, 1.4),
    "romansh": (46.8, 9.5),
    "franco-provençal": (45.8, 6.1),
    "swedish": (59.3, 18.1),
    "old swedish": (59.3, 18.1),
    "danish": (55.7, 12.6),
    "norwegian": (60.0, 10.0),
    "norwegian nynorsk": (60.0, 5.0),
    "norwegian bokmål": (59.9, 10.7),
    "icelandic": (64.1, -21.8),
    "old norse": (60.0, 10.0),
    "russian": (55.8, 37.6),
    "ukrainian": (50.5, 30.5),
    "polish": (52.2, 21.0),
    "old polish": (50.0, 20.0),
    "czech": (50.1, 14.4),
    "old czech": (50.1, 14.4),
    "slovak": (48.1, 17.1),
    "bulgarian": (42.7, 23.3),
    "serbo-croatian": (44.8, 20.5),
    "slovene": (46.1, 14.5),
    "belarusian": (53.9, 27.6),
    "lithuanian": (54.7, 25.3),
    "old lithuanian": (54.7, 25.3),
    "latvian": (56.9, 24.1),
    "arabic": (21.5, 39.2),
    "egyptian arabic": (30.0, 31.2),
    "moroccan arabic": (33.6, -7.6),
    "najdi arabic": (24.7, 46.7),
    "sudanese arabic": (15.5, 32.5),
    "hebrew": (31.8, 35.2),
    "samaritan hebrew": (32.2, 35.2),
    "assyrian neo-aramaiac": (37.5, 43.5),
    "assyrian neo-aramaic": (37.5, 43.5),
    "aramaic": (34.5, 40.0),
    "classical syriac": (37.2, 38.8),
    "akkadian": (33.3, 44.4),
    "ugaritic": (35.6, 35.8),
    "sabaean": (15.5, 45.3),
    "old south arabian": (15.5, 45.3),
    "ethiopic": (13.0, 39.5),
    "amharic": (9.0, 38.7),
    "georgian": (41.7, 44.8),
    "armenian": (40.2, 44.5),
    "old georgian": (41.7, 44.8),
    "old armenian": (40.2, 44.5),
    "chinese": (34.0, 113.0),
    "japanese": (34.7, 135.5),
    "old japanese": (34.7, 135.5),
    "korean": (37.6, 127.0),
    "old korean": (37.6, 127.0),
    "middle korean": (37.6, 127.0),
    "early modern korean": (37.6, 127.0),
    "vietnamese": (21.0, 105.8),
    "latin": (41.9, 12.5),
    "ancient greek": (37.9, 23.7),
    "greek": (37.9, 23.7),
    "classical mongolian": (47.9, 106.9),
    "mongolian": (47.9, 106.9),
    "persian": (35.7, 51.4), 
    "unknown": (0, 0),
}




def lang_to_coords(lang):
    if lang is None:
        return None
    lang_norm = str(lang).strip().lower()
    if lang_norm not in LAMG_TO_COORD:
        lang_norm = "unknown"
    return LAMG_TO_COORD[lang_norm]


def make_language_map(df, root_word, output_path=None):
    root_word = root_word.strip().lower()
    results = df[(df["term"] == root_word) | (df["related_term"] == root_word)]

    if results.empty:
        return

    points = {}  
    arrows = [] 

    for _, row in results.iterrows():
        term = row.get("term", "")
        term_lang = row.get("term_lang", "")
        related_term = row.get("related_term", "")
        related_lang = row.get("related_lang", "")

        src_coords = lang_to_coords(term_lang)
        dst_coords = lang_to_coords(related_lang)

        if src_coords is None or dst_coords is None:
            continue

        src_lat, src_lon = src_coords
        dst_lat, dst_lon = dst_coords

        tl = str(term_lang).strip()
        rl = str(related_lang).strip()

        if tl not in points:
            points[tl] = {"lat": src_lat, "lon": src_lon, "labels": set()}
        points[tl]["labels"].add("{0} ({1})".format(term, tl))

        if rl not in points:
            points[rl] = {"lat": dst_lat, "lon": dst_lon, "labels": set()}
        points[rl]["labels"].add("{0} ({1})".format(related_term, rl))

        arrows.append({
            "src_lat": src_lat,
            "src_lon": src_lon,
            "dst_lat": dst_lat,
            "dst_lon": dst_lon,
            "term": term,
            "term_lang": tl,
            "related_term": related_term,
            "related_lang": rl,
            "reltype": row.get("reltype", ""),
            "similarity": row.get("similarity", ""),
        })

    if not arrows:
        return

    fig = go.Figure()


    for a in arrows:
        fig.add_trace(
            go.Scattergeo(
                lon=[a["src_lon"], a["dst_lon"]],
                lat=[a["src_lat"], a["dst_lat"]],
                mode="lines",
                line=dict(width=2),
                opacity=0.6,
                hoverinfo="text",
                showlegend=False,
                text="{} ({}) → {} ({})<br>Relation: {}<br>Similarity: {}".format(
                    a["term"], a["term_lang"],
                    a["related_term"], a["related_lang"],
                    a["reltype"], a["similarity"],
                ),
            )
        )


    lats, lons, texts, sizes = [], [], [], []

    for lang, info in points.items():
        lats.append(info["lat"])
        lons.append(info["lon"])
        texts.append(lang)
        if any(root_word == lab.split()[0].lower() for lab in info["labels"]):
            sizes.append(14)
        else:
            sizes.append(10)

    fig.add_trace(
        go.Scattergeo(
            lon=lons,
            lat=lats,
            mode="markers+text",
            text=texts,
            textposition="top center",
            marker=dict(size=sizes),
        )
    )

    fig.update_layout(
        title="Language map for root '{0}'".format(root_word),
        geo=dict(
            projection_type="natural earth",
            showland=True,
            landcolor="rgb(240,240,240)",
            showcountries=True,
        ),
        margin=dict(l=0, r=0, t=40, b=0),
    )

    if output_path is None:
        output_path = "outputs/lang_map_{0}.html".format(root_word)

    fig.write_html(output_path)
    print("Language map saved to: {0}".format(output_path))
