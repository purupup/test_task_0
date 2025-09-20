import pytest
from function.files import *


class TestFilesOperation():
    @pytest.mark.asyncio
    async def test_files_1(self, set_pathfile):
        files_list = [
            './test_task_0/tests/test_data_file1.csv',
            './test_task_0/tests/test_data_file2.csv',
        ]
        test_output_file, comparison_file = set_pathfile
        await combining_files(
            files = files_list,
            output_file = test_output_file
        )
        with open(test_output_file, 'r', encoding='utf-8') as t_file:
            with open(comparison_file, 'r', encoding='utf-8') as c_file:
                assert t_file.readlines() == c_file.readlines()


    @pytest.mark.asyncio
    async def test_files_2(self, set_pathfile, capsys):
        files_list = [
            './test_task_0/tests/sdfdfsdfsdf.xml',
            'fffsdfwefds',
            'hello'
        ]
        result_text = 'Для аргумента --files не указанно ни одного файла, ' \
            'либо пути указаны не верно'
        test_output_file, _ = set_pathfile

        await combining_files(
            files = files_list,
            output_file = test_output_file
        )
        captured = capsys.readouterr()
        assert result_text in captured.out
