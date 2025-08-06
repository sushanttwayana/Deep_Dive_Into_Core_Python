import asyncio

#  A shared varibale
shared_resource = 0

#  an asyncio lock
lock = asyncio.Lock()

async def modify_shared_resource():

    global shared_resource

    async with lock:
        # Critical section starts

        print(f"Resource before modification: {shared_resource}")
        shared_resource += 1 # modify the shared resource

        await asyncio.sleep(1) # simulate an IO operation
        print(f"Resource after modifications: {shared_resource}")

        # Critical section ends


async def main():
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))

asyncio.run(main())

        