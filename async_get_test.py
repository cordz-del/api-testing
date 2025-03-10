# async_get_test.py
import asyncio
import httpx

async def async_get_request():
    # Sample API endpoint for asynchronous GET testing
    url = "https://jsonplaceholder.typicode.com/posts/1"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        # Assert that the response is successful
        assert response.status_code == 200, f"Expected 200, got {response.status_code}"
        print("Async GET test passed.")

if __name__ == "__main__":
    asyncio.run(async_get_request())
