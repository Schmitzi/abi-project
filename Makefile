include config.mk

data:
	mkdir -p $@

data/string.txt: data
	curl $(STRING_URL) | gunzip > $@

intermediates:
	mkdir -p $@

intermediates/network.csv: data/string.txt $(EXTRACT_NET_SRC) intermediates
	$(EXTRACT_NET_EXE) --input "$<" --output "$@" --threshold "$(NET_SIG_THRESHOLD)"

intermediates/partitions.csv: intermediates/network.csv $(PARTITION_SRC) intermediates
	$(PARTITION_EXE) --input "$<" --output "$@" --threshold "$(PARTITION_THRESHOLD)"

intermediates/domain_counts.csv: data/domains.txt $(DOMAIN_COUNT_SRC) intermediates
	$(DOMAIN_COUNT_EXE) --input "$<" --output "$@" 

.PHONY: clean
clean: 
	rm -rf intermediates