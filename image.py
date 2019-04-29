from PIL import Image, ImageFilter

filename ="test.png"
orig_pic=Image.open(filename)

print("format ",orig_pic.format)
print("Width ",orig_pic.size[0])
print("Higth ",orig_pic.size[1])

thumbnail_size=(100,100)
blur_pic=orig_pic.filter(ImageFilter.BLUR)
blur_pic.thumbnail(thumbnail_size)
new_filename=filename.split(".")[0]
blur_pic.convert('RGB').save(new_filename + ".jpeg")