# !/usr/bin/env python
# coding=utf-8
# __author__:wshill
# Email:wshill@126.com

# 求一个数字内所有奇偶数，并求和

while True:
    oulist = []
    jilist = []
    n = int(input("请输入一个数字："))
    try:
        for i in range(1, n + 1):
            if i % 2 == 0:
                oulist += [i]
            else:
                jilist += [i]
        print("偶数是：", oulist)
        print("奇数是：", jilist)
        print("偶数和是：", sum(oulist))
        print("奇数和是：", sum(jilist))

    except Exception as e:
        raise e


