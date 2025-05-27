import imageio.v3 as img

filenames = [
    r"C:\Users\PC\OneDrive - Hanoi University of Science and Technology\Desktop\DinhDucManh\My Repositories\Study_DinhDucManh\Python\GIF_Project\khanh_pic1.jpg",
    r"C:\Users\PC\OneDrive - Hanoi University of Science and Technology\Desktop\DinhDucManh\My Repositories\Study_DinhDucManh\Python\GIF_Project\khanh_pic2.jpg"
]

images = []

for filename in filenames:
    images.append(img.imread(filename))

img.imwrite("khanh.gif", images, duration=500, loop=0)
