from model import ImagePreprocessor, ONNXModel
import torch

def test_model(image_path, expected_class_id):
    preprocessor = ImagePreprocessor()
    model = ONNXModel()

    input_data = preprocessor.preprocess(image_path)
    output = model.predict(input_data)
    predicted_class = int(torch.tensor(output).argmax())

    print(f"Predicted class ID: {predicted_class}")
    assert predicted_class == expected_class_id, f"Expected {expected_class_id}, got {predicted_class}"
    print("Test passed.")

if __name__ == "__main__":
    test_model("n01440764_tench.jpeg", 0)
    test_model("n01667114_mud_turtle.JPEG", 35)
