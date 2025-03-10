# chained_api_calls_test.py
import requests

def test_chained_api_calls():
    # First API call to retrieve a post
    url_post = "https://jsonplaceholder.typicode.com/posts/1"
    response_post = requests.get(url_post)
    assert response_post.status_code == 200
    post_data = response_post.json()
    
    # Use the post's userId from the first call to fetch user details
    user_id = post_data["userId"]
    url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response_user = requests.get(url_user)
    assert response_user.status_code == 200
    user_data = response_user.json()
    
    # Validate that the user details include the expected key (e.g., "name")
    assert "name" in user_data, "User name not found in response"
    print("Chained API calls test passed.")

if __name__ == "__main__":
    test_chained_api_calls()
