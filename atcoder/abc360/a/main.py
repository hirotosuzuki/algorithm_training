#!/usr/bin/env python3
"""
R: ご飯
M: 味噌汁
S: サラダ

R < Mかどうかを判定する
"""

S = input()

r_index = S.find('R')
m_index = S.find('M')

if r_index < m_index:
    print('Yes')
else:
    print('No')
