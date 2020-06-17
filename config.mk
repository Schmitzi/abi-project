STRING_URL=https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz

PYTHON=python
EXTRACT_NET_SRC=scripts/generate_network.py
EXTRACT_NET_EXE=$(PYTHON) $(GEN_NET_SRC)
NET_SIG_THRESHOLD=500
