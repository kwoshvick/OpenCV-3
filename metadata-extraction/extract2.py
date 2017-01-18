from PIL import Image, ExifTags
img = Image.open("images/data2.jpg")
exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }

for x,y in exif.items():
    print(x,' -> ',y)