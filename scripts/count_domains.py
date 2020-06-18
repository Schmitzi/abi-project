#!python3

import pandas as pd
import click


def extract_proteins_without_domains(data: pd.DataFrame) -> pd.DataFrame:
    """Finds proteins without domains (i.e. Pfam ID is NaN) and lists them in a DataFrame

    Arguments:  
    data -- A DataFrame of proteins and their domains

    Returns:  
    A DataFrame containing the IDs of proteins without domains and the number of their domains (i.e. 0)
    """
    no_domains = data[data["Pfam ID"].isnull()]["Protein stable ID"]
    result_df = pd.DataFrame(index=no_domains)
    result_df['Domains'] = 0
    return result_df


def get_domain_count(data: pd.DataFrame) -> pd.DataFrame:
    """Finds proteins with at least one domain and counts their number of domains

    Arguments:  
    data -- A DataFrame of proteins and domains contained in them

    Returns:  
    A DataFrame containing protein IDs and the number of domains in the specified proteins
    """
    has_domains = data[~data['Pfam ID'].isnull()]
    count_df = has_domains.groupby('Protein stable ID').count()
    count_df.columns = ["Domains"]
    return count_df


def count_domains(data: pd.DataFrame) -> pd.DataFrame:
    """Calculates the number of domains for each protein

    Arguments:  
    data -- A DataFrame of proteins and contained domains

    Returns:  
    A DataFrame containing protein IDs and the number of domains in the specified proteins
    """
    without_domains = extract_proteins_without_domains(data)
    with_domains = get_domain_count(data)
    return pd.concat([without_domains, with_domains], axis=0)


@click.command()
@click.option("-i", "--input", help="File with protein-domain annotations")
@click.option("-o", "--output", help="File to write counts to")
def main(input, output):
    """Counts the domains in each protein"""
    data = pd.read_csv("data/domains.txt", sep="\t")
    result = count_domains(data)
    result.index.name = "Protein"
    result.to_csv(output)


if __name__ == "__main__":
    main()
