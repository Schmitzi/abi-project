STRING_URL=https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz

PYTHON=python

EXTRACT_NET_SRC=scripts/extract_network.py
EXTRACT_NET_EXE=$(PYTHON) $(EXTRACT_NET_SRC)
NET_SIG_THRESHOLD=500

PARTITION_SRC=scripts/partition_network.py
PARTITION_EXE=$(PYTHON) $(PARTITION_SRC)
PARTITION_THRESHOLD=100

DOMAIN_COUNT_SRC=scripts/count_domains.py
DOMAIN_COUNT_EXE=$(PYTHON) $(DOMAIN_COUNT_SRC)
