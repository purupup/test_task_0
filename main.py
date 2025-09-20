import asyncio
from function.console import get_argument_values
from function.files import combining_files
from function.reports import reporting

async def main():
    files, report = get_argument_values().values()
    await combining_files(files)
    await reporting(report)


if __name__ == '__main__':
    asyncio.run(main())
