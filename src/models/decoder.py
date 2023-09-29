from torchvision.models import resnet34
import torch.nn as nn
from torch import load, device
import torchvision.transforms as transforms

model = resnet34()
in_features = model.fc.in_features
model.fc = nn.Linear(in_features, 114)
model.load_state_dict(load('.\src\models\myshroomweights114.pth'))
device = device("cpu")
model.to(device)
model.eval()
data_transforms = transforms.Compose([
        transforms.Resize((300,300)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])

def analize(image):
    clean_image = data_transforms(image)
    return model(clean_image)