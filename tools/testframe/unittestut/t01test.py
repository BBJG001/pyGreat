# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2020/11/30 5:15 下午
# @Author  : 百变金刚
# @Content : test frame unittest learn
import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self) -> None:
        print('Test begin')

    def tearDown(self) -> None:
        print('Test over')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    # unittest.main()

    # suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    # unittest.TextTestRunner(verbosity=2).run(suite)

    testcase = unittest.FunctionTestCase(TestStringMethods("test_split"))
    testcase.run()
    # unittest.main()