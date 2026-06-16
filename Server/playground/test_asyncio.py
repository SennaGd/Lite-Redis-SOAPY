import asyncio, time


async def say_hello(delay, what):
	await asyncio.sleep(delay)
	print(what)

async def main():
	task1 = asyncio.create_task(
			say_hello(1, "hello"))
	task2 = asyncio.create_task(
			say_hello(1, "bye"))

	print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
	await task1
	await task2

	print(f"finished at {time.strftime('%X')}")
with asyncio.Runner() as runner:
	runner.run(main())
	runner.close()
