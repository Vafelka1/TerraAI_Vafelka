import torch
import albumentations as A
from albumentations.pytorch import ToTensorV2
import numpy as np
from PIL import Image
#from tqdm import tqdm

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
BATCH_SIZE = 4
NUM_WORKERS = 6
PIN_MEMORY = True
LOAD_MODEL = True
LEARNING_RATE = 3e-5

test_transforms_512 = A.Compose(
    [
        A.Resize(height=512, width=512),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.5),
        A.RandomRotate90(p=0.5),
        A.ColorJitter(brightness=(0.9, 1.1), contrast=(0.9, 1.1), saturation=(0.9, 1.1), hue=(0, 0), p=0.5),
        A.GaussianBlur(blur_limit=(3, 7), sigma_limit=0, always_apply=True, p=1),
        A.Normalize(
            mean=[0.3199, 0.2240, 0.1609],
            std=[0.3020, 0.2183, 0.1741],
            max_pixel_value=255.0,
        ),
        ToTensorV2(),
    ]
)
test_transforms_628 = A.Compose(
    [
        A.Resize(height=628, width=628),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.5),
        A.RandomRotate90(p=0.5),
        A.ColorJitter(brightness=(0.9, 1.1), contrast=(0.9, 1.1), saturation=(0.9, 1.1), hue=(0, 0), p=0.5),
        A.GaussianBlur(blur_limit=(3, 7), sigma_limit=0, always_apply=True, p=1),
        A.Normalize(
            mean=[0.3199, 0.2240, 0.1609],
            std=[0.3020, 0.2183, 0.1741],
            max_pixel_value=255.0,
        ),
        ToTensorV2(),
    ]
)
test_transforms_428 = A.Compose(
    [
        A.Resize(height=428, width=428),
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.5),
        A.RandomRotate90(p=0.5),
        A.ColorJitter(brightness=(0.9, 1.1), contrast=(0.9, 1.1), saturation=(0.9, 1.1), hue=(0, 0), p=0.5),
        A.GaussianBlur(blur_limit=(3, 7), sigma_limit=0, always_apply=True, p=1),
        A.Normalize(
            mean=[0.3199, 0.2240, 0.1609],
            std=[0.3020, 0.2183, 0.1741],
            max_pixel_value=255.0,
        ),
        ToTensorV2(),
    ]
)
from efficientnet_pytorch import EfficientNet
from torch import nn

EffNetB5_512_model = EfficientNet.from_name('efficientnet-b5')
EffNetB5_512_model._fc = nn.Linear(2048, 1)

EffNetB6_428_model = EfficientNet.from_name('efficientnet-b6')
EffNetB6_428_model._fc = nn.Linear(2304, 1)

EffNetB3_512_model = EfficientNet.from_name('efficientnet-b3')
EffNetB3_512_model._fc = nn.Linear(1536, 1)

EffNetB3_628_model = EfficientNet.from_name('efficientnet-b3')
EffNetB3_628_model._fc = nn.Linear(1536, 1)

EffNetB5_512_model.load_state_dict(torch.load('EffNetB5_512acc78kap78.pth.tar',map_location=torch.device('cpu'))["state_dict"])
EffNetB6_428_model.load_state_dict(torch.load('EffNetB6_428acc77kap76.pth.tar',map_location=torch.device('cpu'))["state_dict"])
EffNetB3_512_model.load_state_dict(torch.load('EffNetB3_512_acc79_kap76.pth.tar',map_location=torch.device('cpu'))["state_dict"])
EffNetB3_628_model.load_state_dict(torch.load('EffNetB3_628_acc79_kap72.pth.tar',map_location=torch.device('cpu'))["state_dict"])

EffNetB5_512_model.eval()
EffNetB6_428_model.eval()
EffNetB3_512_model.eval()
EffNetB3_628_model.eval()

def predict_img_ensamble(path):
  x = np.array(Image.open(path))
  predict = []

  #512 models
  for i in range(4):
    image = test_transforms_512(image=x)["image"]
    image = image.unsqueeze(0)
    with torch.no_grad():
      pred = EffNetB5_512_model(image)
      predict.append(pred)
      pred = EffNetB3_512_model(image)
      predict.append(pred)

  #428 model
  for i in range(4):
    image = test_transforms_428(image=x)["image"]
    image = image.unsqueeze(0)
    with torch.no_grad():
      pred = EffNetB6_428_model(image)
      predict.append(pred)

  #628 model
  for i in range(4):
    image = test_transforms_628(image=x)["image"]
    image = image.unsqueeze(0)
    with torch.no_grad():
      pred = EffNetB3_628_model(image)
      predict.append(pred)

  predict = np.squeeze(np.array(predict),(-1,-2))

  mean_predict = predict.mean()

  if mean_predict < 0.5: predict = 'You have no DR'#0
  elif mean_predict >= 0.5 and mean_predict < 1.5: predict = 'You have mild stage DR'#1
  elif mean_predict >= 1.5 and mean_predict < 2.5: predict = 'You have moderate stage DR'#2
  elif mean_predict >= 2.5 and mean_predict < 3.5: predict = 'You have severe stage DR'#3
  elif mean_predict >= 3.5: predict = 'You have Proliferative DR'#4

  return(predict)

