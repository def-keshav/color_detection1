import pandas as pd 
import cv2

image = "pic_3.jpg"
csv_file = "colors.csv"

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_file, names=index, header=None)

img = cv2.imread(image)
img = cv2.resize(img, (800,600))

clicked = False
red = green = blue = xposn = yposn = 0

def get_color_name(R,G,B):
	minimum = 1000
	for i in range(len(df)):
		d = abs(R - int(df.loc[i,'R'])) + abs(G - int(df.loc[i,'G'])) + abs(B - int(df.loc[i,'B']))
		if d <= minimum:
			minimum = d
			cname = df.loc[i, 'color_name']

	return cname

def draw_function(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global blue, green, red, xposn, yposn, clicked
		clicked = True
		xposn = x
		yposn = y
		blue, green, red = img[y,x]
		blue = int(blue)
		green = int(green)
		red = int(red)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
	cv2.imshow('image', img)
	if clicked:
		cv2.rectangle(img, (20,20), (600,60), (blue, green, red), -1)
		text = get_color_name(red, green ,blue) + ' R=' + str(red) + ' G=' + str(green) + ' B=' + str(blue)
		cv2.putText(img, text, (50,50), 2,0.8, (255,255,255),2,cv2.LINE_AA)

		if red + green + blue >=600:
			cv2.putText(img, text, (50,50), 2,0.8, (0,0,0),2,cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()
