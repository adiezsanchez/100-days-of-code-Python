from PIL import Image, ImageFilter # for reading image files

def erode(cycles, image):
    for _ in range(cycles):
         image = image.filter(ImageFilter.MinFilter(3))
    return image

def dilate(cycles, image):
    for _ in range(cycles):
         image = image.filter(ImageFilter.MaxFilter(3))
    return image

# Load the logo that will become the watermark
logo = "./image/3d.jpg" # Filepath for the logo image file

with Image.open(logo) as img_logo: # open() to read from the file
    img_logo.load() # Write the image into memory so that the file can be closed

# Obtaining the outer shape of the glasses
img_logo = Image.open(logo)
outer_shape = img_logo.convert("L") # Convert to grayscale
threshold = 250
outer_shape = outer_shape.point(lambda x: 255 if x > threshold else 0)
outer_shape = erode(1,outer_shape) # Filling in by eroding white pixels
outer_shape = dilate(1,outer_shape) # Return to original size afte filling
outer_shape = outer_shape.filter(ImageFilter.GaussianBlur(1)) #Blurring to get rid of serrated edges
outer_shape = outer_shape.filter(ImageFilter.SHARPEN) #Sharpen to obtain a thinner line
outer_shape = outer_shape.filter(ImageFilter.EDGE_ENHANCE_MORE)
outer_shape = outer_shape.filter(ImageFilter.CONTOUR) #Select just the contour of the shape
# To use this as a watermark, you’ll need to reverse the colors so that the background is black and only the outline
# that you want to keep is white
outer_shape = outer_shape.point(lambda x: 0 if x == 255 else 255)

# Obtaining the inner shape of the glasses (eye holes)
img_gray = img_logo.convert("L")
img_gray_smooth = img_gray.filter(ImageFilter.SMOOTH) # Smoothing before finding edges leads to a better result
edges_smooth = img_gray_smooth.filter(ImageFilter.FIND_EDGES)
edge_enhance = edges_smooth.filter(ImageFilter.EDGE_ENHANCE)
threshold = 180
inner_shape = edge_enhance.point(lambda x: 255 if x > threshold else 0)

# Combine into one by pasting inner shape into outer shape
outer_shape.paste(inner_shape,(0,0),inner_shape)
watermark = outer_shape
