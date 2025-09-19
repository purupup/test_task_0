import csv
from tabulate import tabulate


async def reporting(reports: list, file: str = r"./out.csv") -> None:
    funcs = list()

    if "student-performance" in reports:
        report_data = await student_performance(file)
        print(report_data)
        funcs.append(build_table(report_data))


    for func in funcs:
        await func


async def student_performance(file: str) -> tuple[dict[str, list[str]], list[str]]:
    result_data = dict()
    headers =['student_name', 'grade']

    with open(file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:

            try:
                result_data[row[0]].append(int(row[-1]))
            except KeyError:
                result_data[row[0]] = list([int(row[-1])])

    for key, value in result_data.items():
        result_data[key] = [sum(value) / len(value)]

    result_data = dict(
        sorted(result_data.items())
        )
    result_data = dict(
        sorted(
            result_data.items(),
            key = lambda item: item[1],
            reverse=True
            )
        )
    return (result_data, headers)


async def build_table(
        report_data: tuple[dict[str, list[str]],list[str]]) -> None:
    table_data, headers = report_data
    table = [[key, *values] for key, values in table_data.items()]
    print(tabulate(
        table,
        headers = headers,
        tablefmt = 'psql',
        showindex = range(1, len(table)+1)
        )
    )
