from fastapi import FastAPI, UploadFile, File
from model import ImagePreprocessor, ONNXModel
import torch

app = FastAPI()
preprocessor = ImagePreprocessor()
model = ONNXModel()

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image = await file.read()
    with open("temp_image.jpg", "wb") as f:
        f.write(image)
    input_data = preprocessor.preprocess("temp_image.jpg")
    output = model.predict(input_data)
    predicted_class = int(torch.tensor(output).argmax())
    return {"predicted_class_id": predicted_class}
