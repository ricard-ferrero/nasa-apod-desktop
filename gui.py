import tkinter
import requests
from PIL import ImageTk, Image
from platform import system

def transform_size(size):
	"""
	Returns the correct size in a tupple (x,y) in case that 
	the size of the original image is too big
	"""
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
	image = Image.open(response.raw)

	# Manipulating the image: adapting the size
	size = image.size
	if size != transform_size(size):
		image = image.resize((transform_size(size)))


	# Creating the GUI
	PAD = 20
	window = tkinter.Tk()
	window.configure(bg='black')
	window.title('NASA APOD')
	
	# Icon from Google Fonts
	if system()=='Windows':
		window.iconbitmap('icons/icon.ico')
	elif system()=='Darwin':
		window.iconbitmap('icons/icon.icns')
	else:
		window.iconbitmap('@icons/icon.xbm')

		# Firts the frames
	frame_image = tkinter.Frame(window, bg='black')
	frame_text = tkinter.Frame(window, bg='black')
	frame_image.grid(row=0, column=0, padx=PAD, pady = PAD)
	frame_text.grid(row=0, column=1, padx=PAD, pady = PAD)

		# Create the correct image from TK
	new_image = ImageTk.PhotoImage(image)
	label_image = tkinter.Label(frame_image, image=new_image, bg='black')
	label_image.pack()

		# Create the text content
	label_title = tkinter.Label(frame_text, text=title, font='times 20 bold', fg='white', bg='black')
	label_title.pack()
	if copyright: # Not all the images have a copyright
		cp = 'Copyright: ' + copyright
		label_copyright = tkinter.Label(frame_text, text=cp, font='san-serif 8 italic', fg='white', bg='black')
		label_copyright.pack()
	label_description = tkinter.Message(frame_text, text=description, font='san-serif 10', fg='white', bg='black')
	label_description.pack()
	
	window.mainloop()