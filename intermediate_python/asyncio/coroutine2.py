import asyncio

# Define a coroutine that simulates a long-running task

async def fetch_data(delay, id):
    print(f"Fetching data for ID: {id}")
    await asyncio.sleep(delay) # simulate an I/O operation with a sleep
    print(f"Data fetched for ID: {id}")
    # await asyncio.sleep(dela)
    return {"data": f"Some data for ID: {id}"}


# Define another coroutine that calls the first coroutine
async def main():

    task1 = fetch_data(2, 1)
    task2 = fetch_data(3, 2)

    result1 = await task1
    print(f"Result 1: {result1}")

    result2 = await task2
    print(f"Result 2: {result2}")


# run the main coroutine
asyncio.run(main())