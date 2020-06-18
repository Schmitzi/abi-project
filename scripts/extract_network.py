#!python3

import pandas as pd
import click


@click.command()
@click.option("--input", "-i", help="File from STRINGdb with protein-interaction scores", required=True)
@click.option("--output", "-o", help="Output file which network will be written to", required=True)
@click.option("--threshold", "-t", help="Significance threshold", default=500)
def extract_network(input, output, threshold):
    string = pd.read_csv(input, sep=" ")
    significant = string[string.combined_score >= threshold]
    significant.to_csv(
        output, columns=['protein1', 'protein2'], index=False, header=False, sep=" ")


if __name__ == "__main__":
    extract_network()
