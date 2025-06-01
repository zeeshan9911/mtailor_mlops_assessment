import requests

def test_server(image_path):
    url = "http://localhost:8000/predict/"
    with open(image_path, "rb") as f:
        files = {"file": f}
        response = requests.post(url, files=files)
    print(response.json())

if __name__ == "__main__":
    test_server("n01440764_tench.jpeg")
    test_server("n01667114_mud_turtle.JPEG")
