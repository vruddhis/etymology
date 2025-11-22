import pandas as pd
import networkx as nx
from pyvis.network import Network

from src.stemming import get_root_form
from src.map import make_language_map

def main():
    df = pd.read_csv("outputs/similarity_scores.csv")

    while True:
        query = input("\nEnter a word to explore its etymology (or 'exit' to quit): ").strip().lower()
        
        if query == "exit":
            break

        query = get_root_form(query)
        
        results = df[(df["term"] == query) | (df["related_term"] == query)]

        if results.empty:
            print(f"No etymology found for '{query}'. Try another word.")
            continue


        print(f"\nEtymology for '{query}':")
        for _, row in results.iterrows():
            term = row.get("term", "")
            term_lang = row.get("term_lang", "")
            related_term = row.get("related_term", "")
            related_lang = row.get("related_lang", "")
            reltype = row.get("reltype", "")
            similarity = row.get("similarity", "")

            print(
                " - {0} ({1}) → {2} ({3}) | Relation: {4} | Similarity: {5}".format(
                    term, term_lang, related_term, related_lang, reltype, similarity
                )
            )


        subG = nx.DiGraph()
        for _, row in results.iterrows():
            term = row.get("term")
            related_term = row.get("related_term")
            if pd.isna(term) or pd.isna(related_term):
                continue

            subG.add_edge(
                term,
                related_term,
                reltype=row.get("reltype", ""),
                similarity=row.get("similarity", 0),
            )

        net = Network(
            height="600px",
            width="100%",
            directed=True,
            notebook=False
        )

        net.from_nx(subG)

        
        for node in net.nodes:
            node_id = node["id"]
            if isinstance(node_id, str) and node_id.lower() == query:
                node["color"] = "pink"
                node["size"] = 30
            else:
                node["color"] = "green"
                node["size"] = 15

        for edge in net.edges:
            u = edge["from"]
            v = edge["to"]
            data = subG.get_edge_data(u, v, {})
            reltype = data.get("reltype", "")
            similarity = data.get("similarity", "")

            edge["title"] = "Relation: {0}, similarity: {1}".format(reltype, similarity)

        output_path = "outputs/etymology_network_{0}.html".format(query)
        net.write_html(output_path)

        print("\nGraph saved to: {0}".format(output_path))

        lang_map_path = "outputs/lang_map_{0}.html".format(query)
        make_language_map(df, query, output_path=lang_map_path)
        print("Language map for root '{0}' saved to: {1}".format(query, lang_map_path))



main()
