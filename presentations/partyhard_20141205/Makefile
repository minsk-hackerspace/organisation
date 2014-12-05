
NAME=slides

.PHONY: all
all: $(NAME).pdf

%.pdf: %.tex logo.eps
	pdflatex $<

logo.eps:
	make -C ../../logo logo.eps
	cp ../../logo/logo.eps ./

.PHONY: clean
clean:
	rm -f *.aux *.out *.log *.pdf *.snm *.toc *.nav *.dvi logo.eps

