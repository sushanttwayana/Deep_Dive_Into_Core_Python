import asyncio
# from copyreg import constructor


# Define a coroutine that simulates a long-running task
async def fetch_data(delay):
    print("Fetching data...")
    await asyncio.sleep(delay) # simulate an I/O operation with a sleep
    print("Data fetched successfully.")
    return {"data": "some data"} # Return some data

# coroutine function

# define another coroutine that calls the first coroutine
async def main():
    # print("Start of main coroutine.")
    # task = fetch_data(5)

    # # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    # result = await task
    # print(f"Result: {result}")
    # print("Main coroutine completed.")

    print("Start of main coroutine.")
    task = fetch_data(2)

    # Await the fetch_data coroutine, pausing execution of main until fetch_data completes
    print("Main coroutine completed.")
    result = await task
    print(f"Result: {result}")


# normal function
# main() -> Coroutine object 
# print(main())


# Run the main coroutine
asyncio.run(main())

