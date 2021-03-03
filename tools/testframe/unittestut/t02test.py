# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 6:02 下午
# @Author  : 百变金刚
# @Content : unittest for mathfunc.Operate
import unittest
from mathfunc import Operate
import sys

SHOWF = 0

def showFun(flag):
    def show(func):
        def inner(Operate):
            if flag:
                print(func.__name__)
                ret = func(Operate)
                return ret
            else:
                ret = func(Operate)
                return ret
        return inner
    return show

class TestOperateCase(unittest.TestCase):
    def setUp(self) -> None:
        '''
        测试前的准备操作
        :return:
        '''
        self.operator = Operate(3,2)
        # print('Test begin')

    def tearDown(self) -> None:
        '''
        测试结束后的收尾工作
        :return:
        '''
        # print('Test over')
        pass

    @classmethod
    def setUpClass(cls):
        print("This setUpClass() method only called once before all cases.")

    @classmethod
    def tearDownClass(cls):
        print("This tearDownClass() method only called once after all cases.")

    @showFun(SHOWF)
    def test_add(self):
        '''
        test_xxx，unittest会检测这些方法执行，一个test_xxx是一个测试用例
        :return:
        '''
        operator = Operate(1,2)
        self.assertEqual(3, operator.add())

    @showFun(SHOWF)
    def test_minus(self):
        operator = Operate(3,2)
        self.assertEqual(1, operator.minus())
        self.assertNotEqual(1, operator.minus())    # 错误case（注意是NotEqual）

    @showFun(SHOWF)
    def test_multi(self):
        # operator = Operate(3,2)
        self.assertEqual(6, self.operator.multi())

    @showFun(SHOWF)
    def test_divide(self):
        operator = Operate(5,2)
        self.assertEqual(2, operator.divide())  # 错误case

if __name__ == '__main__':
    unittest.main()

    # 通过TestSuite执行
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestOperateCase)
    # unittest.TextTestRunner(verbosity=2).run(suite)
'''
.FF.
======================================================================
FAIL: test_divide (__main__.TestOperateCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "t02test.py", line 20, in inner
    ret = func(Operate)
  File "t02test.py", line 65, in test_divide
    self.assertEqual(2, operator.divide())  # 错误case
AssertionError: 2 != 2.5

======================================================================
FAIL: test_minus (__main__.TestOperateCase)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "t02test.py", line 20, in inner
    ret = func(Operate)
  File "t02test.py", line 55, in test_minus
    self.assertNotEqual(1, operator.minus())    # 错误case（注意是NotEqual）
AssertionError: 1 == 1

----------------------------------------------------------------------
Ran 4 tests in 0.001s

FAILED (failures=2)

不确定执行顺序的依据
在第一行给出了每一个用例执行的结果的标识，成功是 .，失败是 F，出错是 E，跳过是 S。
'''