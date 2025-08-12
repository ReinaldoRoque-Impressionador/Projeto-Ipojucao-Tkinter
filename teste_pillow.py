from PIL import Image

img = Image.new("RGB", (100, 100), color="green")
img.save("imagem_teste.png")
print("Imagem criada com sucesso!")