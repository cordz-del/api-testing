# get_with_auth_test.py
import requests

def test_get_with_authentication():
    # This example uses httpbin to simulate basic authentication
    url = "https://httpbin.org/basic-auth/user/passwd"
    response = requests.get(url, auth=("user", "passwd"))
    # Validate that authentication was successful
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    assert data.get("authenticated") is True, "Authentication failed"
    print("GET with authentication test passed.")

if __name__ == "__main__":
    test_get_with_authentication()
