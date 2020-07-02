# Course Project for Applied Bioinformatics

## Requirements

This pipeline requires
* Python 3.8
* NetworkX
* Pandas
* Seaborn
* Click

Create a new conda environment from [`environment.yml`](./environment.yml) and you are ready to go:

```
conda env create --file environment.yml
```

Alternatively, install these dependencies through pip

## Execution

1. Switch to the repo's root directory
2. Activate the environment (if you created one): `conda activate abi-project`
3. Start the analysis: `make`

This will download all data and run the analysis.

The resulting plot is written to `protein_domains_vs_string_degree.png`.