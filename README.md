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
conda create -n abi-project -f environment.yml
```

Alternatively, install these dependencies through pip

## Execution

Switch to the repo's root directory and run
```
make
```

This will download all data and run the analysis.