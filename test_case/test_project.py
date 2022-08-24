# @Project : pythonwork
# @File    : test_project.py
# @Author  : zhangjing
# @Time    : 2022/8/24 14:07
# @Software : Pycharm
# @Description :
import json
import os
import sys

import pytest

from tools.xlsController import get_excel_data


file_path = os.path.abspath("E:/study/pythonwork/test_case/test_project.py")
print(file_path)
# 获取当前文件所在的目录
cur_path = os.path.dirname(file_path)
print(cur_path)
# 获取项目所在路径
project_path = os.path.dirname(cur_path)
print(project_path)
# 把项目路径加入python搜索路径
sys.path.append(project_path)

@pytest.mark.project
class Test_project:

    @pytest.mark.project_list
    @pytest.mark.parametrize('inData,expData',get_excel_data('../data/inData.xlsx', '我的项目列表',
                         'project', '请求参数','响应预期结果',runCase=['all']))
    def test_project_list(self,inData,expData,project_init):
        result = project_init.project_list(inData)
        assert result['meta']['current_page'] == expData['meta']['current_page']

    @pytest.mark.project_update
    @pytest.mark.parametrize('inData', get_excel_data('../data/inData.xlsx', '项目列表',
                                                              'update', '请求参数', runCase=['all']))
    def test_project_update(self,inData,project_update_init):
        url = project_update_init[0]
        project_init = project_update_init[1]
        inData = json.dumps(str(inData))
        project_init.project_update(url,inData)
        assert 1==1





if __name__ == '__main__':
    pytest.main(['test_project.py', '-s', '--alluredir', '../report/tmp'])
    os.system("allure serve ../report/tmp")


