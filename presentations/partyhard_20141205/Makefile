
NAME=slides

.PHONY: all images
all: $(NAME).pdf

%.pdf: %.tex
	pdflatex $<

%.pdf: %.eps
	epstopdf $<

$(NAME).tex: logo.pdf images

images: imget.sh
	bash imget.sh

logo.pdf:
	make -C ../../logo logo.pdf
	cp ../../logo/logo.pdf ./

.PHONY: clean
clean:
	rm -f *.aux *.out *.log *.pdf *.snm *.toc *.nav *.dvi logo.eps

