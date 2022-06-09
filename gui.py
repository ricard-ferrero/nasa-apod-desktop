import webbrowser
import tkinter
import requests
from PIL import ImageTk, Image
from platform import system

def transform_size(size):
	MAX_WIDTH = 600
	MAX_HEIGTH = 400

	x = size[0]
	y = size[1]
	pr = size[0]//size[1]

	if x > MAX_WIDTH:
		pr = x / MAX_WIDTH
		x = MAX_WIDTH
		y = y / pr
	if y > MAX_HEIGTH:
		pr = y / MAX_HEIGTH
		y = MAX_HEIGTH
		x = x / pr
	return (int(x), int(y))


def gui(title, description, image_url, copyright=None):
	
	# Getting the image from the URL
	response = requests.get(image_url, stream=True)
	# If is an image:
	try:
		image = Image.open(response.raw)
		# Manipulating the image: adapting the size
		size = image.size
		if size != transform_size(size):
			image = image.resize((transform_size(size)))
	# But somptimes is a Youtube Video
	except:
		image = "Today is not an image."



	# Creating the GUI and using the image with the correct size
	PAD = 20
	window = tkinter.Tk()
	window.configure(bg='black')
	window.title('NASA APOD')
	window.iconbitmap('@/etc/nasa-apod/icon.xbm')

		# Firts the frames
	frame_image = tkinter.Frame(window, bg='black')
	frame_text = tkinter.Frame(window, bg='black')
	frame_image.grid(row=0, column=0, padx=PAD, pady = PAD)
	frame_text.grid(row=0, column=1, padx=PAD, pady = PAD)

		# Create the correct image from TK
	if isinstance(image, str):
		label_image = tkinter.Label(frame_image, text=image, bg='black', font='san-serif 10', fg='white').pack()
		link_image = tkinter.Label(frame_image, text=image_url, bg='black', font='san-serif 10', fg='white', cursor="hand1")
		link_image.bind('<Button-1>', lambda x: webbrowser.open_new_tab(image_url))
		link_image.pack()
	else:
		new_image = ImageTk.PhotoImage(image)
		label_image = tkinter.Label(frame_image, image=new_image, bg='black').pack()

		# Create the text content
	label_title = tkinter.Label(frame_text, text=title, font='times 20 bold', fg='white', bg='black')
	label_title.pack()
	if copyright:
		cp = 'Copyright: ' + copyright
		label_copyright = tkinter.Label(frame_text, text=cp, font='san-serif 8 italic', fg='white', bg='black')
		label_copyright.pack()
	label_description = tkinter.Message(frame_text, text=description, font='san-serif 10', fg='white', bg='black')
	label_description.pack()
	
	window.mainloop()
