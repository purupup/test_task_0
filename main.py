import asyncio
from function.console import get_argument_values
from function.files import combining_files


if __name__ == '__main__':
    files, report = get_argument_values().values()
    asyncio.run(combining_files(files))
