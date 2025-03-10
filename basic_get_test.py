# basic_get_test.py
import requests

def test_basic_get():
    # Define a sample API endpoint (using a public placeholder API)
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    # Validate that the status code is 200 (OK)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    print("Basic GET test passed.")

if __name__ == "__main__":
    test_basic_get()
