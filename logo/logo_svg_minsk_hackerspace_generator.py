#!/usr/bin/python


X_color = '#000000'
M_color = 'blue'
pcb_track_color = '#D0D0D0'
drill_color = '#FFFFFF'
highlight_track_color = '#FFD700'


W = 800
H = 5/6 * W
w1 = 1/5 * W # ширина треугольного бокового проема в букве Х
h1 = 1/3 * H # высота треугольного бокового проема в букве Х
w2 = 1/3 * W # ширина прямоугольного проема в букве Х
h2 = 1/5 * H # высота прямоугольного проема в букве Х

w3 = w2 # ширина буквы М
h3 = 4/9 * H # высота буквы М
w4 = 1/5 * w3 # ширина полосы которой рисуется буква М
h4 = 4/5 * h3 # высота верхнего проема в букве М
h5 = 1/2 * h3 # высота нижних проемов в букве М

r1 = 1/15 * h2 # радиус больших отверстий
r2 = 1/4 * w4 # радиус площадок
r3 = 1/2 * r2 # радиус малых отверстий

d1 = 4/5 * r3 # половина ширины дорожки
l1 = 1/6 * w3 # длина горизонтального участка дорожки ("нога" буквы М)
dl1 = 3/4 * d1 # выступ для наклона соединения горизонтальной и диагональной дорожек
l2 = 1/2 * h2 # длина вертикального участка дорожки
dl2 = 3/4 * d1 # выступ для наклона соединения вертикальной и диагональной дорожек

# координаты большого отверстия:
xR1 = 3 * r1
yR1 = 3 * r1

yM1 = (H - h3)/2 # расстояние от верха до начала буквы М
xX1 = (W-w2)/2 # расстояние до верхнего проема в букве Х
yX1 = (H - h1)/2 # расстояние до бокового проема в букве Х

# координата первого малого отверстия на букве Х:
xR2 = 1/5 * xX1
yR2 = 4/5 * h2
dxR2 = 4 * r2 # расстояние между отверситями на букве Х

# координата первого малого отверстия на букве М:
xR3 = xX1 + 1/2 * w4
yR3 = yM1 + 1/16 * h3
dyR3 = 1/8 * h3 # расстояние между отверстиями на букве М

X_poly_points = [
	(0, 	 0),
	(xX1, 	 0),
	(xX1, 	 h2),
	(xX1+w2, h2),
	(xX1+w2, 0),
	(W, 	 0),
	(W, 	 yX1),
	(W-w1, 	 H/2),
	(W, 	 yX1+h1),

	(W, 	 H),

	(W-xX1,	 H),
	(W-xX1,  H-h2),
	(xX1, 	 H-h2),
	(xX1, 	 H),
	(0, 	 H),
	(0, 	 H-yX1),
	(w1, 	 H/2),
	(0, 	 yX1)
]

M_poly_points = [
	(xX1,		 yM1),
	(xX1+w4,	 yM1),
	(xX1+w3/2,	 yM1+h4),
	(xX1+w3-w4,	 yM1),
	(xX1+w3,	 yM1),

	(xX1+w3,	 yM1+h3 ),
	(xX1+w3-w4,	 yM1+h3),
	(xX1+w3-w4,	 yM1+h3-h5),
	(xX1+(w3-w4)/2+w4, 	 yM1+h3),
	(xX1+(w3-w4)/2, 	 yM1+h3),
	(xX1+w4,	 yM1+h3-h5),
	(xX1+w4,	 yM1+h3),
	(xX1,		 yM1+h3)
]


import svgwrite
from svgwrite import cm, mm 

svg_document = svgwrite.Drawing(filename = "logo.svg",
                                size = ("%dpx" % W, "%dpx" % H))

svg_document.add(svgwrite.shapes.Polygon(points=X_poly_points, fill=X_color))
svg_document.add(svgwrite.shapes.Polygon(points=M_poly_points, fill=M_color))

svg_document.add(svgwrite.shapes.Circle(center=(xR1, yR1), r=r1, fill=drill_color))
svg_document.add(svgwrite.shapes.Circle(center=(W - xR1, yR1), r=r1, fill=drill_color))
svg_document.add(svgwrite.shapes.Circle(center=(W - xR1, H - yR1), r=r1, fill=drill_color))
svg_document.add(svgwrite.shapes.Circle(center=(xR1, H - yR1), r=r1, fill=drill_color))


def create_pcb_track (dwg, pM, pX):
	
	dwg.add(svgwrite.shapes.Circle(center=pM, r=r2, fill=pcb_track_color))
	dwg.add(svgwrite.shapes.Circle(center=pM, r=r3, fill=M_color))
	
	dwg.add(svgwrite.shapes.Circle(center=pX, r=r2, fill=pcb_track_color))
	dwg.add(svgwrite.shapes.Circle(center=pX, r=r3, fill=X_color))
	
	
	isLeft = pM[0] > pX[0]
	isUp = pM[1] > pX[1]

	d1x = d1 if isLeft else -d1
	d1y = d1 if isUp else -d1
	r3x = r3 if isLeft else -r3
	r3y = r3 if isUp else -r3
	L1 = l1 if isLeft else -l1
	dL1 = dl1 if isLeft else -dl1
	L2 = l2  if isUp else -l2
	dL2 = dl2 if isUp else -dl2

	track_poly_points = [
		(pX[0] - d1x, 		pX[1] + r3y),
		(pX[0] + d1x, 		pX[1] + r3y),

		(pX[0] + d1x, 		pX[1] + r3y + L2),
		(pM[0] - (r3x + L1), 		pM[1] - d1y),

		(pM[0] - r3x, 		pM[1] - d1y),
		(pM[0] - r3x, 		pM[1] + d1y),

		(pM[0] - (r3x + L1 + dL1), 	pM[1] + d1y),
		(pX[0] - d1x, 		pX[1] + r3y + L2 + dL2)
	]
	
	dwg.add(svgwrite.shapes.Polygon(points=track_poly_points, fill=pcb_track_color))


def create_pcb_bus (root, p1, p2, dx1, dy2) :
	
	create_pcb_track(root, p1, (p2[0]+3*dx1, p2[1]));
	create_pcb_track(root, (p1[0], p1[1]+dy2), (p2[0]+2*dx1, p2[1]));
	create_pcb_track(root, (p1[0], p1[1]+2*dy2), (p2[0]+dx1, p2[1]));
	create_pcb_track(root, (p1[0], p1[1]+3*dy2), p2);


create_pcb_bus(svg_document, (xR3, yR3), (xR2, yR2), dxR2, dyR3);
create_pcb_bus(svg_document, (xR3 + w3 - w4, yR3), (W - xR2, yR2), -dxR2, dyR3);
create_pcb_bus(svg_document, (xR3 + w3 - w4, yR3 + h3 - h3/8), (W - xR2, H - yR2), -dxR2, -dyR3);
create_pcb_bus(svg_document, (xR3, yR3 + h3 - h3/8), (xR2, H - yR2), dxR2, -dyR3);



print(svg_document.tostring())
























