from torchvision.models import mobilenet_v2
import torch.nn as nn
from torch import load, device, unsqueeze
import torchvision.transforms as transforms
import requests
from PIL import Image
from io import BytesIO

class IdentifierBinaryModel:
    def __init__(self):
        model = mobilenet_v2()
        num_classes = 2 # Suposición
        in_features = model.classifier[1].in_features
        model.classifier = nn.Sequential(
            nn.Dropout(0.2),
            nn.Linear(in_features, num_classes))
        dev = device("cpu")
        model.to(dev)
        model.load_state_dict(load('./src/files/binary_weights.pth',map_location=device('cpu')))
        model.eval()
        self.mod = model
        self.data_transforms = transforms.Compose([
                transforms.Resize((150,150)),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])
        dicti = {'Mushroom':0, 'Other':1}
        keys = dicti.values()
        values = dicti.keys()
        self.class_mapping = dict(zip(keys, values))
        
    def predict (self, url):
        resp= requests.get(url)
        img = Image.open(BytesIO(resp.content))
        img = img.convert("RGB")
        clean_image = self.data_transforms(img)
        clean_image = unsqueeze(clean_image,dim=0)
        prediction = self.mod(clean_image)
        predicted_index = int(prediction[0].argmax(0))
        predicted = self.class_mapping[predicted_index]
        return predicted