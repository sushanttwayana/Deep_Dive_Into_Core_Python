import asyncio

async def fetch_data(id, slep_time):
    print(f"Coroutine {id} starting to fetch data!!!")
    await asyncio.sleep(slep_time)
    return {"id": id, "data": f"Data for ID: {id}"}


# async def main():

#     # Create tasks for running coroutines concurrently
#     task1 = asyncio.create_task(fetch_data(1, 2))
#     task2 = asyncio.create_task(fetch_data(2, 3))
#     task3 = asyncio.create_task(fetch_data(3, 1))

#     result1 = await task1
#     result2 = await task2
#     result3 = await task3

#     print(result1, result2, result3)


# using gather function

# async def main():

#   # run coroutines concurrently and gather their return values
#   results = await asyncio.gather(fetch_data(1, 2), fetch_data(2, 3), fetch_data(3, 1))
  
#   # process the results 
#   for result in results:
#     print(f"Recieved Result: {result}")

    
# TaskGroup 
async def main():

    tasks = []

    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start = 1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)
 
    #  After the Task Group block, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f"Recieved result: {result}")

asyncio.run(main())
