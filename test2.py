import asyncio
import time

async def test(sec):
    print(f"{sec}秒待ちます")
    await asyncio.sleep(sec)
    print(f"{sec}秒終わり")

async def main ():
    print(f"main開始 {time.strftime('%X')}")
    asyncio.create_task(test(2))
    await test(1)
    print(f"main終了 {time.strftime('%X')}")

if __name__ == "__main__":
    asyncio.run(main())