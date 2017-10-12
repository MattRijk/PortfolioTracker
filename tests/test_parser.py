import pytest
from api.parser import TextParser

class TestParser:

    def test_open_returned_list_of_lists(self):
        path = '/Users/matthewrijk/PycharmProjects/PortfolioTracker/files/FundOne-Qtr1-16.txt'
        self.text = TextParser()
        assert self.text.splitbylines(path)[0][0] == 'AMERICAN AIRLINES GROUP INC'
        assert self.text.splitbylines(path)[1][0] == 'APPLE INC'
        assert self.text.splitbylines(path)[2][0] == 'AMERISOURCEBERGEN CORP'
        assert self.text.splitbylines(path)[-1][-1] == '0'

    def test_get_column_returned_first_column_text(self):
        path = '/Users/matthewrijk/PycharmProjects/PortfolioTracker/files/FundOne-Qtr1-16.txt'
        self.text = TextParser()
        rows = self.text.splitbylines(path)
        assert self.text.first_column(rows) == ['AMERICAN AIRLINES GROUP INC','APPLE INC','AMERISOURCEBERGEN CORP']

    # compare columns of two files
    def test_compare_two_columns(self):
        path1 = '/Users/matthewrijk/PycharmProjects/PortfolioTracker/files/FundOne-Qtr1-16.txt'
        qtr1 = self._columns_helper(path1)
        assert qtr1 == ['AMERICAN AIRLINES GROUP INC', 'APPLE INC', 'AMERISOURCEBERGEN CORP']
        path2 = '/Users/matthewrijk/PycharmProjects/PortfolioTracker/files/FundOne-Qtr4-16.txt'
        qtr4 = self._columns_helper(path2)
        assert qtr4 == ['AMERICAN AIRLINES GROUP INC', 'APPLE INC', 'AMERISOURCEBERGEN CORP','ACCENTURE PLC', 'ADOBE SYSTEMS INC',
                                                         'AUTOMATIC DATA PROCESSING']
        assert self.text.add_to_map(qtr1) == {0: 'AMERICAN AIRLINES GROUP INC', 1: 'APPLE INC', 2: 'AMERISOURCEBERGEN CORP'}
        assert self.text.compare(qtr1, qtr4) == ['ACCENTURE PLC', 'ADOBE SYSTEMS INC', 'AUTOMATIC DATA PROCESSING']


    def _columns_helper(self, path):
        self.text = TextParser()
        rows = self.text.splitbylines(path)
        columns = self.text.first_column(rows)
        return columns









