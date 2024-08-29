from PIL import Image, ImageDraw

for i in range(5):
    image = Image.new("RGB", (100, 100), "white")
    draw = ImageDraw.Draw(image)
    draw.rectangle([(10 + i*5, 10 + i*5), (90 - i*5, 90 - i*5)], outline="black", fill="blue")
    draw.ellipse([(30, 30), (70, 70)], outline="red", fill="green")
    
    filename = f"/mnt/DCIM/test_image_{i}.bmp"
    image.save(filename)
    print(f"BMP文件已生成：{filename}")

