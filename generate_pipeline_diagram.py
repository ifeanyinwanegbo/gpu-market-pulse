from graphviz import Digraph
import os

def generate_pipeline_diagram():
    # Ensure diagrams folder exists
    os.makedirs("diagrams", exist_ok=True)

    dot = Digraph(
        comment="GPU Market Pulse Pipeline",
        format="png"
    )

    # Pipeline nodes
    dot.node("A", "Data Source\n(GPU Price APIs / CSVs)")
    dot.node("B", "Ingestion\nload_gpu_prices.py")
    dot.node("C", "Processing\nclean_gpu_prices.py")
    dot.node("D", "Analytics\nanalyze_gpu_market.py")
    dot.node("E", "Outputs\nInsights • Charts • Reports")

    # Pipeline flow
    dot.edge("A", "B")
    dot.edge("B", "C")
    dot.edge("C", "D")
    dot.edge("D", "E")

    # Render diagram
    output_path = "diagrams/gpu_market_pipeline"
    dot.render(output_path, cleanup=True)

    print(f"Pipeline diagram generated at {output_path}.png")


if __name__ == "__main__":
    generate_pipeline_diagram()
