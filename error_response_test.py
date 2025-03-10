# error_response_test.py
import requests

def test_404_response():
    # Intentionally using an invalid endpoint to trigger a 404 Not Found error
    url = "https://jsonplaceholder.typicode.com/invalid_endpoint"
    response = requests.get(url)
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"
    print("404 response test passed.")

if __name__ == "__main__":
    test_404_response()
