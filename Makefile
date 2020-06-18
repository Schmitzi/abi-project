include config.mk

data:
	mkdir -p $@

data/interactions.txt: data
	curl $(STRING_URL) | gunzip > $@

intermediates:
	mkdir -p $@

intermediates/interactions_preprocessed.txt: data/interactions.txt intermediates
	 sed -E 's/[0-9]{4}\.//g' "$<" > "$@"

intermediates/network.csv: intermediates/interactions_preprocessed.txt $(EXTRACT_NET_SRC) intermediates
	$(EXTRACT_NET_EXE) --input "$<" --output "$@" --threshold "$(NET_SIG_THRESHOLD)"

intermediates/partitions.csv: intermediates/network.csv $(PARTITION_SRC) intermediates
	$(PARTITION_EXE) --input "$<" --output "$@" --threshold "$(PARTITION_THRESHOLD)"

intermediates/domain_counts.csv: data/domains.txt $(DOMAIN_COUNT_SRC) intermediates
	$(DOMAIN_COUNT_EXE) --input "$<" --output "$@" 

intermediates/merged_data.csv: intermediates/partitions.csv intermediates/domain_counts.csv $(MERGE_SRC)
	$(MERGE_EXE) --partitions intermediates/partitions.csv \
		--domain_counts intermediates/domain_counts.csv \
		--output $@

.PHONY: clean
clean: 
	rm -rf intermediates