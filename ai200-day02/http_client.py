import asyncio

import httpx


async def main() -> None:
    async with httpx.AsyncClient(base_url="http://127.0.0.1:8000", timeout=10) as client:
        health_response = await client.get("/health")
        health_response.raise_for_status()
        print("Health:", health_response.json())

        chat_response = await client.post(
            "/fake-chat",
            json={"prompt": "Why do Azure AI apps need configuration management?"},
        )
        chat_response.raise_for_status()
        print("Fake chat:", chat_response.json())


if __name__ == "__main__":
    asyncio.run(main())

