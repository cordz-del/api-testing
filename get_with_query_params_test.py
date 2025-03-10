# get_with_query_params_test.py
import requests

def test_get_with_query_params():
    # Endpoint returning comments; filtering by query parameter 'postId'
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": 1}
    response = requests.get(url, params=params)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    data = response.json()
    # Validate all returned comments correspond to the specified postId
    for comment in data:
        assert comment["postId"] == 1, "Comment postId does not match the query parameter"
    print("GET with query parameters test passed.")

if __name__ == "__main__":
    test_get_with_query_params()
