import cv2

path = 'Automation/image_processing/'

def calculate_size(scale_percentage, width, height):
    new_width = int(width * scale_percentage / 100)
    new_height = int(height * scale_percentage / 100)
    return (new_width, new_height)



def resize(image_path, scale_percentage, resized_path):
    image = cv2.imread(image_path)
    new_dim = calculate_size(scale_percentage, image.shape[1], image.shape[0])
    resized_image = cv2.resize(image, new_dim)
    cv2.imwrite(resized_path, resized_image)



#Load the 2 images
image = cv2.imread(path+'elfs.jpeg')

resize(path+'barca.png', 30, path+'resized-barca.png')

watermark = cv2.imread(path+'resized-barca.png')

print(image.shape)
print(watermark.shape)


x = image.shape[1] - watermark.shape[1]
y = image.shape[0] - watermark.shape[0]

watermark_place = image[y:, x:]
cv2.imwrite(path+'watermark_place.jpeg', watermark_place)
print(watermark_place.shape)

blend = cv2.addWeighted(watermark_place, 0.5, watermark, 0.5, 0)
cv2.imwrite(path+'blend.jpeg', blend)

image[y:, x:] = blend
cv2.imwrite(path+'elfs-watermarked.jpeg', image)






resize(path+'galaxy.jpeg', 10, path+'resized-galaxy.jpeg')