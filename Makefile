include config.mk

.PHONY: all
all: protein_domains_vs_string_degree.png

# Download data
data:
	mkdir -p $@

data/interactions.txt: | data
	curl $(STRING_URL) | gunzip > "$@"

data/domains.txt: | data
	curl $(DOMAIN_URL) > "$@"

# Do some rudimentary preprocessing to strip info we don't need
preprocessing:
	mkdir -p $@

# Protein IDs have version numbers prependend
preprocessing/interactions.txt: data/interactions.txt | preprocessing
	 sed -E 's/[0-9]{4}\.//g' "$<" > "$@"

# Table of domains has a lot of duplicate entries
preprocessing/domains.txt: data/domains.txt | preprocessing
	head -n 1 "$<" > "$@"
	tail -n +2 "$<" | sort -u >> "$@"

# Compute intermediate results
intermediates:
	mkdir -p $@

intermediates/partitions.csv: preprocessing/interactions.txt $(PARTITION_SRC) | intermediates
	$(PARTITION_EXE) --input "$<" \
	--output "$@" \
	--score_threshold "$(SCORE_THRESHOLD)" \
	--degree_threshold "$(DEGREE_THRESHOLD)"

intermediates/domain_counts.csv: preprocessing/domains.txt $(DOMAIN_COUNT_SRC) | intermediates
	$(DOMAIN_COUNT_EXE) --input "$<" --output "$@" 

intermediates/merged_data.csv: intermediates/partitions.csv intermediates/domain_counts.csv $(MERGE_SRC)
	$(MERGE_EXE) --partitions intermediates/partitions.csv \
		--domain_counts intermediates/domain_counts.csv \
		--output $@

# Plot
protein_domains_vs_string_degree.png: intermediates/merged_data.csv $(PLOT_SRC)
	$(PLOT_EXE) --input "$<" --output "$@"

.PHONY: clean
clean: 
	rm -rf data
	rm -rf intermediates
	rm -rf preprocessing