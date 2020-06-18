#!python3

import pandas as pd
import networkx as nx
import click


def remove_insignificant_edges(graph: nx.Graph, threshold: float) -> nx.Graph:
    """Removes all edges from a given graph with a score below the threshold

    Arguments:  
    graph: -- The graph to work on  
    threshold: -- The threshold below which edges are removed

    Returns:  
    A reference to the same graph that has been passed
    """
    for u, v in graph.edges():
        attrs = graph.get_edge_data(u, v)
        if attrs['combined_score'] < threshold:
            graph.remove_edge(u, v)
    return graph


def partition_network(graph: nx.Graph, threshold: float) -> pd.DataFrame:
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
    partitions.columns = ['Protein', 'Well_connected']
    return partitions


@click.command()
@click.option("-i", "--input", help="File from STRINGdb with protein-interaction scores", required=True)
@click.option("--output", "-o", help="File which result is written to", required=True)
@click.option("--score_threshold", "-s", help="Interactions with a score above this threshold will be added to the graph", default=500)
@click.option("--degree_threshold", "-d", help="Threshold which is used for partitioning based on degree", default=100)
def main(input, output, score_threshold, degree_threshold):
    """Takes a table of interaction scores and determines for each protein if it is well connected"""
    edgelist = pd.read_csv(input, sep=" ")
    graph = nx.from_pandas_edgelist(
        edgelist, source='protein1', target='protein2', edge_attr='combined_score')
    remove_insignificant_edges(graph, score_threshold)
    result = partition_network(graph, degree_threshold)
    result.to_csv(output, index=False)


if __name__ == "__main__":
    main()
