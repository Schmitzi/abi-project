#!python3

import networkx as nx
import pandas as pd
import click


def partition_network(graph: nx.Graph, threshold: float):
    """Partitions the given network based on degree

    Arguments:  
    graph -- the graph to partition
    threshold -- the threshold to use for partitioning

    Returns:  
    A DataFrame containing each protein and whether its degree is above the threshold (column well_connected)
    """
    degree_iter = iter(graph.degree())
    partitions = pd.DataFrame([(name, degree > threshold)
                               for (name, degree) in degree_iter])
    partitions.columns = ['protein', 'well_connected']
    return partitions


@click.command()
@click.option("--input", "-i", help="A CSV file representing a protein network", required=True)
@click.option("--output", "-o", help="File which result is written to", required=True)
@click.option("--threshold", "-t", help="Threshold which is used for partitioning based on degree", default=100)
def main(input, output, threshold):
    """Partitions a graph given by an adjacency list based on whether a node's degree is above a given threshold."""
    graph = nx.read_adjlist(input)
    partitions = partition_network(graph, threshold)
    partitions.to_csv(output, index=False)


if __name__ == "__main__":
    main()
