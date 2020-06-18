#!python3

import pandas as pd
import click


def merge_data(partitions: pd.DataFrame, domain_counts: pd.DataFrame) -> pd.DataFrame:
    """Merges partition and domain-count information

    Arguments:  
    partitions -- DataFrame of partitioning  
    domain_counts -- DataFrame of domain counts

    Returns:  
    A merged DataFrame
    """
    result = pd.merge(left=partitions, right=domain_counts,
                      left_on='Protein', right_on='Protein')
    return result


@click.command()
@click.option("-p", "--partitions", help="File containing partition information", required=True)
@click.option("-d", "--domain_counts", help="File containing domain counts", required=True)
@click.option("-o", "--output", help="Output file for merged information", required=True)
def main(partitions, domain_counts, output):
    """Merges partitioning and domain counts into one file"""
    partition_df = pd.read_csv(partitions)
    domain_counts_df = pd.read_csv(domain_counts)
    result = merge_data(partition_df, domain_counts_df)
    result.to_csv(output)


if __name__ == "__main__":
    main()
