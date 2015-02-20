#!/usr/bin/env python
# encoding: utf-8
"""
"""

import string

module_variable = 0


def functionName(self, int):
    local = 5 + 5
    module_variable = 5*5
    return module_variable


class my_class(object):

    def __init__(self, arg1, string):
        self.value = True
        return

    def method1(self, str):
        self.s = str
        return self.value

    def method2(self):
        return
        print 'How did we get here?'

    def method1(self):
        return self.value + 1
	method2 = method1

class my_subclass(my_class):

    def __init__(self, arg1, string):
        self.value = arg1
        return
