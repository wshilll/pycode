#!/usr/bin/env python
#coding=utf-8


import serial.tools.list_ports

port_list = list(serial.tools.list_ports.comports())

if len(port_list) <= 0:
    print(u"串口没有找到")
else:
    port_list_0 = list(port_list[0])
    port_serial = port_list_0[0]
    ser = serial.Serial(port_serial,9600,timeout= 60)
    print("Content-Type:text/html\n")
    print(u"当前端口为：",ser.name)
