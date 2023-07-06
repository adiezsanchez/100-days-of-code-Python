from PIL import Image, ImageTk
from tkinter import Tk, PhotoImage, Button, Label
from tkinter.filedialog import askopenfilename, asksaveasfilename
from watermark import watermark


def choose_picture():
    # Create a Tkinter window to select the image file
    Tk().withdraw()
    filename = askopenfilename()
    # Load the image file and store it in a variable
    img = Image.open(filename)

    # Get image size and then generate the coordinates where the watermark would be pasted (bottom right)
    size = img.size  # This tuple contains the image size
    coordinates = list(size)  # Change the tuple into a list in order to modify its values
    watermark_size = watermark.size
    watermark_size = list(watermark_size)
    coordinates[0] = coordinates[0] - (watermark_size[0] + 100)
    coordinates[1] = coordinates[1] - (watermark_size[1] + 100)
    coordinates = tuple(coordinates)  # Back to tuple so it can be used a paste argument

    # Paste the watermark on top
    img.paste(watermark, coordinates, watermark)

    # Convert the watermarked image to a Tkinter PhotoImage and display it in the window
    img_tk = ImageTk.PhotoImage(img)
    img_label = Label(image=img_tk)
    img_label.image = img_tk
    img_label.grid(column=1, row=5, columnspan=2)

    # Create a Tkinter button to save the watermarked image
    save_button = Button(text="Save Watermarked Image", width=44, command=lambda: save_picture(img))
    save_button.grid(column=1, row=6, columnspan=2)


def save_picture(img):
    # Create a Tkinter window to save the watermarked image
    save_filename = asksaveasfilename(defaultextension='.png')

    # Save the watermarked image in the selected location
    img.save(save_filename)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Watermark your images!")
window.config(padx=50, pady=20, bg="white")

# Create buttons
add_button = Button(text="Choose your image to watermark", width=44, command=choose_picture)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()