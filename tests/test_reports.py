import pytest
from function.reports import *


class TestReports:
    @pytest.mark.asyncio
    async def test_student_performance(self, set_test_data):
        test_file = './test_task_0/tests/test_report_file.csv'
        func_result = await student_performance(test_file)
        data_dict, data_list = set_test_data
        data = (
            {key:list(map(lambda x: float(x), values)) for key, values in data_dict.items()},
            data_list
        )
        assert data == func_result


    @pytest.mark.asyncio
    async def test_build_table(self, capsys, set_test_data, set_output_data):
        await build_table(set_test_data)
        captured = capsys.readouterr()
        assert captured.out == set_output_data

    @pytest.mark.asyncio
    async def test_reporting(self, capsys, set_output_data):
        reports_list = ['student-performance',]
        await reporting(
            reports=reports_list,
            file=r'./test_task_0/tests/test_out.csv'
        )
        captured = capsys.readouterr()
        assert captured.out == set_output_data

