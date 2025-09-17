import csv


async def reporting(reports, file=r"./out.csv"):
    funcs = list()
    if "student-performance" in reports:
        await student_performance(file)
        funcs.append(student_performance(file))

    # for func in funcs:
    #     await func(file)


async def student_performance(file):
    result_data = dict()
    with open(file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            try:
                result_data[row[0]].append(int(row[-1]))
            except KeyError:
                result_data[row[0]] = list(row[-1])
    print(result_data)
