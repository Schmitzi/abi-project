STRING_URL=https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz

data:
	mkdir -p data

data/string.txt: data
	curl $(STRING_URL) | gunzip > $@