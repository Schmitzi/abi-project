#!python3

import pandas as pd
import click


def extract_network(data: pd.DataFrame, threshold: float):
    """Extracts an adjacency list from a DataFrame given an interaction-score threshold

    Arguments:  
    data      -- A DataFrame holding protein1, protein2 and the interaction score as 'combined_score'  
    threshold -- The interaction-score threshold above which two proteins will be considered adjacent

    Returns:  
    A DataFrame containing the adjacency list with columns 'protein1' and 'protein2'
    """
    significant = data[data.combined_score >= threshold]
    return significant[['protein1', 'protein2']]


@click.command()
@click.option("--input", "-i", help="File from STRINGdb with protein-interaction scores", required=True)
@click.option("--output", "-o", help="Output file which network will be written to", required=True)
@click.option("--threshold", "-t", help="Interactions with a score above this threshold will be added to the graph", default=500)
def main(input, output, threshold):
    """Extracts a PPI network from a table of interaction scores and a threshold"""
    string = pd.read_csv(input, sep=" ")
    significant = extract_network(string, threshold)
    significant.to_csv(output, index=False, header=False, sep=" ")


if __name__ == "__main__":
    main()
