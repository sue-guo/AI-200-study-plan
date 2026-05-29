import asyncio
import time


async def fake_network_call(name: str, delay_seconds: float) -> str:
    print(f"{name}: started")
    await asyncio.sleep(delay_seconds)
    print(f"{name}: finished after {delay_seconds} seconds")
    return name


async def main() -> None:
    started_at = time.perf_counter()

    results = await asyncio.gather(
        fake_network_call("model request", 2.0),
        fake_network_call("database lookup", 1.0),
        fake_network_call("cache lookup", 0.5),
    )

    elapsed = time.perf_counter() - started_at
    print("Results:", results)
    print(f"Total elapsed: {elapsed:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main())

