import csv

async def combining_files(files: list[str], output_file = './out.csv') -> None:
    
    with open(output_file, 'w+', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
    
        for file in files:
            await io_files(file, writer)


async def io_files(file, writer) -> None:
    try:
        with open(file, newline='', encoding='utf-8') as input_file:
            reader = csv.reader(input_file)

            for row in reader:
                if 'student_name' in row: continue
                writer.writerow(row)
    except (FileNotFoundError, FileExistsError):
            print('Для аргумента --files не указанно ни одного файла, ' \
            'либо пути указаны не верно')

