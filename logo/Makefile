

.PHONY: all
all: logo.svg logo.png logo.eps logo.pdf

logo.svg: logo_svg_minsk_hackerspace_generator.py
	./$< > $@

%.pdf: %.svg
	convert $< $@

%.eps: %.svg
	convert $< $@

%.png: %.svg
	convert $< $@


.PHONY: clean
clean:
	rm -f *.png *.pdf *.eps logo.svg

