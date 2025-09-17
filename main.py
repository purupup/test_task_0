import asyncio
from function.console import get_argument_values
from function.files import combining_files
from function.reports import reporting


if __name__ == '__main__':
    files, report = get_argument_values().values()
    print(files, report)
    asyncio.run(combining_files(files), debug=True)
    asyncio.run(reporting(report), debug=True)
