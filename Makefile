# Variables
TEXFILE = thesis.tex
BIB = references.bib
PDF = thesis.pdf

# Default target
all: $(PDF)

# PDF target
$(PDF): $(TEXFILE) $(BIB)
	pdflatex $(TEXFILE)
	bibtex $(basename $(TEXFILE))
	pdflatex $(TEXFILE)
	pdflatex $(TEXFILE)

# Clean target
clean:
	rm -f $(PDF) *.aux *.log *.out *.toc *.bbl *.blg

# Phony targets
.PHONY: all clean

