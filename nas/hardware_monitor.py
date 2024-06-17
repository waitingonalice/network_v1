import asyncio
import platform
import os


"""
NOTE: This script only works on Linux systems.
This script is used to monitor the CPU and RAM usage of the system.
"""


async def main():
    try:
        while True:
            device_name = platform.node()
            cpu_name = platform.processor()
            cpu_count = os.popen(
                """
                lscpu | grep "^CPU(s):" | awk '{print $2}'
                """
            ).read()
            cpu_usage_percent = os.popen(
                """
                top -bn1 | sed -n '/Cpu/p' | awk '{print $2}' | sed 's/..,//'
                """
            ).read()
            min = os.popen(
                """
                lscpu | grep "CPU min MHz:" | awk '{print $4}'
                """
            ).read()
            max = os.popen(
                """
                lscpu | grep "CPU max MHz:" | awk '{print $4}'
                """
            ).read()

            cpu = {
                "name": cpu_name,
                "count": cpu_count.replace("\n", ""),
                "min": min.replace("\n", "").split(",")[0],
                "max": max.replace("\n", "").split(",")[0],
                "usage": cpu_usage_percent.replace(",", ".").replace("\n", ""),
            }

            total_mem = os.popen(
                """
                free -m | grep Mem | awk '{print $2}'
                """
            ).read()
            available_mem = os.popen(
                """
                free -m | grep Mem | awk '{print $4}'
                """
            ).read()

            ram = {
                "total": int(total_mem.replace("\n", "")) * 1024 * 1024,
                "available": int(available_mem.replace("\n", "")) * 1024 * 1024,
            }
            print(f"Device Name: {device_name}")
            print(f"CPU: {cpu}")
            print(f"Memory: {ram}")

            await asyncio.sleep(delay=5)
    except KeyboardInterrupt:
        print("Exiting...")
        return

    except Exception as e:
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    asyncio.run(main())
