#!python3

import pandas as pd
import seaborn as sb
import click


def plot_data(data: pd.DataFrame) -> sb.FacetGrid:
    """Creates a boxplot comparing number of domains between well and badly connected proteins

    Arguments:  
    data -- A DataFrame with ID, connection class and number of domains of proteins

    Returns:  
    A boxplot with connection class on x and number of domains on y axis
    """
    return sb.catplot(x="Well_connected", y="Domains", data=data, kind="box")


@click.command()
@click.option("-i", "--input", help="File with merged data", required=True)
@click.option("-o", "--output", help="Path were plot should be written", required=True)
def main(input, output):
    """Writes a boxplot comparing number of domains between well and badly connected proteins"""
    data = pd.read_csv(input)
    plot = plot_data(data)
    plot.savefig(output)


if __name__ == "__main__":
    main()
