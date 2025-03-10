# response_time_test.py
import requests
import time

def test_response_time():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    elapsed = end_time - start_time
    # Assert that the API responds within 1 second (adjust threshold as needed)
    assert elapsed < 1, f"Response time too high: {elapsed} seconds"
    print(f"Response time test passed in {elapsed:.2f} seconds.")

if __name__ == "__main__":
    test_response_time()
