#!/usr/bin/env python3

make_multiplier = __import__('8-make_multipler').make_multiplier
print(make_multiplier.__annotations__)
fun = make_multipler(2.22)
print("{}".format(fun(2.22)))
