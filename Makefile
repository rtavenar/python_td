SRC          := $(wildcard src/*.md)
TARGETS_HTML := $(patsubst src/%.md,_build/html/%.html,$(SRC))
TARGETS_EPUB := $(patsubst src/%.md,_build/epub/%.epub,$(SRC))
TARGETS_PDF  := $(patsubst src/%.md,_build/pdf/%.pdf,$(SRC))
TARGETS      := $(TARGETS_HTML) $(TARGETS_EPUB) $(TARGETS_PDF)

all: $(TARGETS)

html/%.html: src/%.md
	pandoc --self-contained -s -o $@ --highlight-style pygments --columns 1000 --css assets/td.css --ascii --number-sections --mathml $^

epub/%.epub: src/%.md
	pandoc -o $@ --columns 1000 --number-sections --css assets/td_epub.css --mathml $^

pdf/%.pdf: src/%.md
	pandoc -V lang=fr -o $@ --columns 1000 --variable urlcolor=cyan --number-sections $^

clean:
	rm -f $(TARGETS)
