import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw

from PIL import Image
image = Image.open('images.jpeg')
logo = Image.open('yuhbruh.jpeg')
image_copy = image.copy()
position =((image_copy.width), (image_copy.height - logo.height))
image_copy.paste(logo, position)
image_copy.save('modified.jpeg')

def frame(original_image, color, frame_width):
    """ Put frame around a PIL.Image
    
    original_image must be a PIL.Image
    Returns a new PIL.Image with a frame, where
    0 < frame_width < 1
    is the border as a portion of the shorter dimension of original_image
    """
    #set the radius of the rounded corners
    width, height = original_image.size
    thickness = int(frame_width * min(width, height)) # thickness in pixels
    
    ###
    #create a mask
    ###
    
    #start with transparent mask
    r,g,b = color
    frame_mask = PIL.Image.new('RGBA', (width, height), (0,0,0,0))
    drawing_layer = PIL.ImageDraw.Draw(frame_mask)
    
    drawing_layer.rectangle((0,0, width, thickness), fill=(r,g,b,255))#top
    drawing_layer.rectangle((width, 0, width-thickness, height), fill=(r,g,b,255))#right
    drawing_layer.rectangle((0,0, thickness-width, height), fill=(r,g,b,255)) #left
    drawing_layer.rectangle((0,0, width, thickness), fill=(r,g,b,255)) 
    # Make the new image, starting with all transparent
    result = original_image.copy()
    result.paste(frame_mask, (0,0), mask=frame_mask)
    return result
    
    def get_images(directory=None):
    #""" Returns PIL.Image objects for all the images in directory.if directory is not specified, uses current directory.Returns a 2-tuple containing a list with a  PIL.Image object for each image file in root_directory, anda list with a string filename for each image file in root_directory 
        if directory == None:
            directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

    