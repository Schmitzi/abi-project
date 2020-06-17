#!python3

import pandas as pd
import click


@click.command()
@click.option("-i", help="File from STRINGdb with protein-interaction scores", required=True)
@click.option("-o", help="Output file which network will be written to", required=True)
@click.option("-t", help="Significance threshold", default=500)
def extract_network(i, o, t):
    string = pd.read_csv(i, sep=" ")
    significant = string[string.combined_score >= t]
    significant.to_csv(o)


if __name__ == "__main__":
    extract_network()
