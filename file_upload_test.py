# file_upload_test.py
import requests

def test_file_upload():
    # Use httpbin.org to simulate file upload testing
    url = "https://httpbin.org/post"
    file_content = b"Hello, this is a test file."
    files = {"file": ("test.txt", file_content, "text/plain")}
    
    response = requests.post(url, files=files)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Validate that the uploaded file content is echoed back by the API
    response_data = response.json()
    uploaded_file = response_data["files"].get("file")
    assert uploaded_file == file_content.decode(), "Uploaded file content mismatch."
    print("File upload test passed.")

if __name__ == "__main__":
    test_file_upload()
