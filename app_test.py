import pytest
from mock import Mock, patch

import app

class TestCalc():
    def new_sum(self, a, b):
        return a + b
        
    def new_connect_github():
        print 200
        
    @patch('app.sum')
    def test_calc(self, mock_sum):
        mock_sum.side_effect = self.new_sum
        print app.calc(1,2)
        
    def test_sum(self):
        a = 1
        b = 3
        result = app.sum(a, b)
        assert result == 4
        
    def test_true(self):
        self = True
        assert self == True
        
    def test_false(self):
        self = False
        assert self == False
        
    @patch('app.connect_github')
    def test_connect_github(self, mock_connect_github):
        mock_connect_github.return_value = '200'
        response = app.connect_github()
        assert response == '200'