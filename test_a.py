import pytest
import yaml


def func(a):
    return a + 1


@pytest.fixture()
def login():
    username = "Jack"
    return username


class TestDemo:

    # @pytest.mark.parametrize("a,b", [(1, 2), (2, 3), (4, 5)])
    # def test_answer(a,b):
    #     assert func(a) == 5

    @pytest.mark.parametrize('re1,re2', [(1, 2), (2, 3), (4, 5)])
    def test_ask(self, re1, re2):
        assert func(re1) == re2

    def test_result(self, login):
        print(f"your username is {login}")


class TestData:
    @pytest.mark.parametrize(("a", "b"), yaml.safe_load(open("./data.yaml")))
    def test_data(self, a, b):
        print(a + b)


class TestCase:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_case(self, env):
        print(yaml.safe_load(open("./env.yml")))
        if "env" in env:
            print(f"测试环境：{env['env']}")
        else:
            print(f"测试环境：env['test']")
    # def test_yaml(self):
    #     print(yaml.safe_load(open("./env.yml",encoding='utf-8')))

#
# if __name__ == '__main__':
#     pytest.main(["test_a.py::TestDemo", "-v"])
