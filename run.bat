cd ./test_case
pytest -s --alluredir ../report/tmp
allure serve ../report/tmp