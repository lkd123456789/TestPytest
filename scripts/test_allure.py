import allure
import pytest


class TestAllure:
    @allure.step(title="第一个测试")
    def test_Allure(self):
        assert 1

