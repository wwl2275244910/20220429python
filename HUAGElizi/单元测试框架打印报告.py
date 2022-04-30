from  Lib import HTMLTestRunnerCN
import unittest

#文件路径
Testcase_dir = 'D:\\pythonwenjian\\20220423UI_AUTO_Test\\UI_Auto_Testcase'
#覆盖该文件路径下的文件
dis = unittest.defaultTestLoader.discover(Testcase_dir,'YMW_UI_Auto_Testcase.py')
# 定义报告存放路径
filename = "D:\\pythonwenjian\\20220423UI_AUTO_Test\\Report\\20220430_Ymw.html"
    # 定义报告存放路径，如果没有，创建
fp = open(filename, 'wb')
    # 定义测试报告
runner = HTMLTestRunnerCN.HTMLTestRunner(stream=fp, title='测试', description="description='描述：登录，搜索模块'")
    # 运行测试用例
runner.run(dis)
#关闭报告文件
#fp.close()
