import asyncio

async def brew_chai(chai_type):
    print(f"brewing {chai_type} chai wait for a second...")
    await asyncio.sleep(2)
    print(f"{chai_type} chai is ready.")

async def main():
    await asyncio.gather(
        brew_chai("masala"),
        brew_chai("lemon"),
        brew_chai("black"),
    )

asyncio.run(main())