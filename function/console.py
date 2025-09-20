from argparse import ArgumentParser

def get_argument_values() -> dict[str, list[str]]:
    """
    Возвращает значения аргументов, переданных при вызове функции в консоли.
    """
    parser = ArgumentParser()

    parser.add_argument(
        '-f', '--files',
        help='str: Добавляет исходные файлы для отчета',
        type=str,
        nargs='+'
        )
    
    parser.add_argument(
        '-r',
        '--report',
        help='str: Определяет формат отчета. По умолчанию равен\
              student-performance',
        type=str,
        nargs='+',
        default='student-performance'
        )
    
    data = parser.parse_args()
    return data.__dict__