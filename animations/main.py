from google.colab import files
from PIL import Image
import torch
import IPython
uploaded = files.upload()

# load models
model_facev1 = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="face_paint-512_v1")
model_facev2 = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="face_paint-512_v1")
model_paprika = torch.hub.load("bryandlee/animegan2-pytorch:main", "generator", pretrained="paprika")

face2paint = torch.hub.load("bryandlee/animegan2-pytorch:main", "face2paint", size=512)

for INPUT_IMG in ['photo_test1.jpg', 'photo_test2.jpg']:
    img = Image.open(INPUT_IMG).convert("RGB")

    out_facev1 = face2paint(model_facev1, img)
    out_facev2 = face2paint(model_facev2, img)
    out_paprika = face2paint(model_paprika, img)

    display(img)
    display(out_facev1)
    display(out_facev2)
    display(out_paprika)

    # save images
    out_facev2.save(f'out_facev2_{INPUT_IMG}.jpg')

