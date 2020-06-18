#!python3

import pandas as pd
import click


def extract_proteins_without_domains(data):
    no_domains = data[data["Pfam ID"].isnull()]["Protein stable ID"]
    result_df = pd.DataFrame(index=no_domains)
    result_df['Domains'] = 0
    return result_df


def get_domain_count(data):
    has_domains = data[~data['Pfam ID'].isnull()]
    count_df = has_domains.groupby('Protein stable ID').count()
    count_df.columns = ["Domains"]
    return count_df


def count_domains(data):
    without_domains = extract_proteins_without_domains(data)
    with_domains = get_domain_count(data)
    return pd.concat([without_domains, with_domains], axis=0)


@click.command()
@click.option("-i", "--input", help="File with protein-domain annotations")
@click.option("-o", "--output", help="File to write counts to")
def main(input, output):
    data = pd.read_csv("data/domains.txt", sep="\t")
    result = count_domains(data)
    result.to_csv(output)


if __name__ == "__main__":
    main()
