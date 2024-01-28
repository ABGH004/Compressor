from tkinter import *
import heapq
from tkinter import filedialog
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = ".",
										title = "Select a File",
										filetypes = (("Text files",
														"*.txt*"),
													("all files",
														"*.*")))


def compress():
	pass


def decompress():
	pass
																								
window = Tk()

window.title('Compressor')

window.geometry("400x400")

photo = PhotoImage(file = 'images/zip_icon.png')
window.wm_iconphoto(False, photo)

window.resizable(0, 0)

window.config(background = "white")
	
button_explore = Button(window, text = "Browse Files", command = browseFiles,
						height = 1, width = 10) 

button_compress = Button(window, text = "Compress", command = compress, 
						height = 1, width = 10) 

button_decompress = Button(window, text = "Decompress", command = decompress, 
						height = 1, width = 10) 


button_explore.place(relx=0.5, rely=0.05, anchor=CENTER)
button_compress.place(relx=0.5, rely=0.15, anchor=CENTER)
button_decompress.place(relx=0.5, rely=0.25, anchor=CENTER)

window.mainloop()


