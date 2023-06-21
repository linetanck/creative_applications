from PIL import Image
img = Image.open('portrait.jpg')
width, height = img.size
pixels = img.load()

def sort_row(row):
    min = 255*3
    min_index = 0
    #find the darkest pixel in the row
    for i in range(len(row)):
        # each pixel has an RPG value, for instance (255, 255, 255)
        temp = row[i][0] + row[i][1] + row[i][2]
        if temp < min:
            min = temp
            min_index = i
# sort the row up the brightest pixel
    sorted_row = row[:min_index]
    sorted_row.sort()
    return sorted_row + row[min_index:]

new_img = Image.new('RGB',(width, height))

# to make a new image, we'll need to conver the data to a list
sorted_pixels = []
for y in range(height):
       for x in range(width):
           sorted_pixels.append(pixels[x,y])
new_img.putdata(sorted_pixels)
new_img.show()
new_img.save('portrait_sorted.jpg')
