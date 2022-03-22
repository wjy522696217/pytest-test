import pytest
import allure


@allure.feature("登录模块")
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        with allure.step("步骤1:打开应用"):
            print("打开应用")

        with allure.step("步骤2:进入登录页面"):
            print("登录页面")
        print("这是登录 成功的测试用例")

    @allure.story("登录失败")
    @allure.title("登录成功")
    def test_login_fail(self):
        print("这是登录失败的：测试用例")


@allure.feature("菜单模块")
class MenuLogin():
    @allure.story("菜单显示成功")
    def test_login_success(self):
        with allure.step("步骤1:打开菜单"):
            print("打开菜单")


if __name__ == '__main__':
    pytest.main()
