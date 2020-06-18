STRING_URL=https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz

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
