# post_request_test.py
import requests

def test_post_request():
    # API endpoint that accepts POST requests
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(url, json=payload)
    # Expecting a 201 Created response
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"
    data = response.json()
    # Validate that the response contains the sent payload data
    assert data["title"] == "foo", "Title in response does not match payload"
    print("POST request test passed.")

if __name__ == "__main__":
    test_post_request()
