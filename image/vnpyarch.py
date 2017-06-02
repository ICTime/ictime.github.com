#!/usr/bin/env python
#coding:utf-8
# Author:  mozman
# Purpose: svg examples
# Created: 07.11.2010
# Copyright (C) 2010, Manfred Moitzi
# License: MIT License

try:
    import svgwrite
except ImportError:
    # if svgwrite is not 'installed' append parent dir of __file__ to sys.path
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.split(os.path.abspath(__file__))[0]+'/..'))

import svgwrite
from svgwrite import cm, mm   


def basic_shapes(name):
    dwg = svgwrite.Drawing(filename=name, size=('35cm', '25cm'), debug=True)
    hlines = dwg.add(dwg.g(id='hlines', stroke='green'))
    for y in range(5):
        # hlines.add(dwg.line(start=(2*cm, 5*(y)*cm), end=(30*cm, 5*y*cm)))
 	pass 		

    shapes = dwg.add(dwg.g(id='shapes', fill='red'))

    # 4 strategy 
    for i in [5,10,15,22.5]:
    	shapes.add(dwg.rect(insert=( i*cm, 20*cm), size=(45*mm, 45*mm), fill='none', stroke='black', stroke_width=1))

    # 2 Engine 
    shapes.add(dwg.rect(insert=(5*cm, 15*cm), size=(15*cm, 45*mm), fill='none', stroke='black', stroke_width=1))
    shapes.add(dwg.rect(insert=(20.5*cm, 15*cm), size=(9.5*cm, 45*mm), fill='none', stroke='black', stroke_width=1))

    # 1 Risk 
    shapes.add(dwg.rect(insert=(5*cm, 10*cm), size=(25*cm, 45*mm), fill='none', stroke='black', stroke_width=1))

    # Gate 
    shapes.add(dwg.rect(insert=(5*cm, 5*cm), size=(12.25*cm, 45*mm), fill='none', stroke='black', stroke_width=1))
    shapes.add(dwg.rect(insert=(18*cm, 5*cm), size=(12*cm, 45*mm), fill='none', stroke='black', stroke_width=1))

    for i in [5,8, 11, 14, 18, 21, 24,27 ]:
    	shapes.add(dwg.rect(insert=(i*cm, 1*cm), size=(2.5*cm, 35*mm), fill='none', stroke='black', stroke_width=1))

    text_style = "font-size:%ipx; font-family:%s" % (22, "Courier New")
    text1 = dwg.text("策略", insert=(2*cm, 22*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("引擎", insert=(2*cm, 17*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("风控", insert=(2*cm, 12*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("接口", insert=(2*cm, 7*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("交易所", insert=(2*cm, 3*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("T", insert=(7*cm, 22*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("B", insert=(12*cm, 22*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("V", insert=(17*cm, 22*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("F", insert=(24*cm, 22*cm), fill="black", style=text_style)
    shapes.add(text1)

    text1 = dwg.text("CTA", insert=(10*cm, 17*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("PAIR", insert=(24*cm, 17*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("RISK", insert=(16*cm, 12*cm), fill="black", style=text_style)
    shapes.add(text1)

    text1 = dwg.text("CTP", insert=(10*cm, 7*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("IB", insert=(24*cm, 7*cm), fill="black", style=text_style)
    shapes.add(text1)

    text1 = dwg.text("SHFE", insert=(5.5*cm, 3*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("DCE", insert=(8.5*cm, 3*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("CZCE", insert=(11.5*cm, 3*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("CFFEX", insert=(14*cm, 3*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("HKFE", insert=(18.5*cm, 3*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("OSE.JPN", insert=(21*cm, 3*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("GLOBEX", insert=(24*cm, 3*cm), fill="black", style=text_style)
    shapes.add(text1)
    text1 = dwg.text("CME", insert=(27*cm, 3*cm), fill="black", style=text_style)
    shapes.add(text1)

    dwg.save()

if __name__ == '__main__':
    basic_shapes('base.svg')
