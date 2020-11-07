import asyncio
import sys
import os


async def get_date():
    code = 'import datetime; print(datetime.datetime.now());a=input("input:");print(a)'

    # Create the subprocess; redirect the standard output
    # into a pipe.
    # cwd = os.path.abspath('.')
    # file = os.path.join(cwd, 'code.py')
    # with open(file, 'w') as f:
    #     f.write(code)
    proc = await asyncio.create_subprocess_exec(
        # sys.executable, '-c', code,
        *['python', '-sB', 'code.py'],
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )

    # Read one line of output.
    data = await asyncio.wait_for(
        proc.stdout.readline(), 2  # type: ignore
    )
    print(data)
    proc.stdin.write('======='.encode('u8') + b'\n')
    data = await asyncio.wait_for(
        proc.stdout.readline(), 2  # type: ignore
    )
    line = data.decode('u8')  # .rstrip()

    proc.stdin.write('======='.encode('u8') + b'\n')

    # Wait for the subprocess exit.
    print(line)

    line1 = data.decode('ascii').rstrip()
    print(line1)

    await proc.wait()
    return line


if sys.platform == "win32":
    asyncio.set_event_loop_policy(
        asyncio.WindowsProactorEventLoopPolicy())

date = asyncio.run(get_date())
print(f"Current date: {date}")
