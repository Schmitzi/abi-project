STRING_URL=https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz
DOMAIN_URL=http://www.ensembl.org/biomart/martservice?query=<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE Query><Query  virtualSchemaName = "default" formatter = "TSV" header = "1" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" ><Dataset name = "hsapiens_gene_ensembl" interface = "default" ><Attribute name = "pfam" /><Attribute name = "ensembl_peptide_id" /></Dataset></Query>
PYTHON=python

PARTITION_SRC=scripts/partition_network.py
PARTITION_EXE=$(PYTHON) $(PARTITION_SRC)
SCORE_THRESHOLD=500
DEGREE_THRESHOLD=100

DOMAIN_COUNT_SRC=scripts/count_domains.py
DOMAIN_COUNT_EXE=$(PYTHON) $(DOMAIN_COUNT_SRC)

MERGE_SRC=scripts/merge_data.py
MERGE_EXE=$(PYTHON) $(MERGE_SRC)

PLOT_SRC=scripts/plot.py
PLOT_EXE=$(PYTHON) $(PLOT_SRC)
