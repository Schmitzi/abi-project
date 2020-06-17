include config.mk

data:
	mkdir -p $@

data/string.txt: data
	curl $(STRING_URL) | gunzip > $@

intermediates:
	mkdir -p $@

intermediates/network.csv: data/string.txt $(EXTRACT_NET_SRC) intermediates
	$(EXTRACT_NET_EXE) -i "$<" -o "$@" -t "$(NET_SIG_THRESHOLD)"