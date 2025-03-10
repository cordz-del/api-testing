# json_schema_validation_test.py
import requests
from jsonschema import validate, ValidationError

def test_json_schema():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200
    data = response.json()
    
    # Define the expected JSON schema
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": "number"},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
        "required": ["userId", "id", "title", "body"]
    }
    
    try:
        validate(instance=data, schema=schema)
        print("JSON schema validation test passed.")
    except ValidationError as e:
        raise AssertionError(f"JSON schema validation failed: {e}")

if __name__ == "__main__":
    test_json_schema()
