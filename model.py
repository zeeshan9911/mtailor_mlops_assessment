import onnxruntime as ort
import numpy as np
from PIL import Image
from torchvision import transforms

class ImagePreprocessor:
    def __init__(self):
        self.transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.CenterCrop((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406],
                                 [0.229, 0.224, 0.225])
        ])

    def preprocess(self, image_path):
        image = Image.open(image_path).convert("RGB")
        return self.transform(image).unsqueeze(0).numpy()

class ONNXModel:
    def __init__(self, model_path="model.onnx"):
        self.session = ort.InferenceSession(model_path)

    def predict(self, input_data):
        inputs = {self.session.get_inputs()[0].name: input_data}
        outputs = self.session.run(None, inputs)
        return outputs[0]
