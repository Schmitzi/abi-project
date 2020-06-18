#!python3

import networkx as nx
import pandas as pd
import click


@click.command()
@click.option("--input", "-i", help="A CSV file representing a protein network")
@click.option("--output", "-o", help="File which result is written to")
@click.option("--threshold", "-t", help="Threshold which is used for partitioning based on degree", default=100)
def partition_network(input, output, threshold):
    graph = nx.read_adjlist(input)
    degree_iter = iter(graph.degree())
    partitions = pd.DataFrame([(name, degree > threshold)
                               for (name, degree) in degree_iter])
    partitions.columns = ['protein', 'well_connected']
    partitions.to_csv(output, index=False)


if __name__ == "__main__":
    partition_network()
