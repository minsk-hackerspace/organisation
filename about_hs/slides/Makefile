
NAME=slides

.PHONY: all images
all: $(NAME).pdf

%.pdf: %.tex 
	pdflatex $<

$(NAME).tex: logo.pdf images

images: get_img.sh
	bash get_img.sh

logo.pdf:
	make -C ../../logo logo.pdf
	cp ../../logo/logo.pdf ./

.PHONY: clean
clean:
	rm -f *.aux *.out *.log *.pdf *.snm *.toc *.nav *.dvi *.jpg

