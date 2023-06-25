#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import time
from pprint import pprint

with open('data.json', 'r') as f:
    data = json.load(f)


def find_next(prev_list):
    l, s, t = 0,1,0
    nums = [[], []]
    for i in range(len(prev_list)):
        num = prev_list[i]
        double = num * 2
        nums[0].append(double)
        nums[1].append(num)

        if i==0:
            l=double
            s=double
        if double>l:
            l = double
        if double<s:
            s = double
        t += 1

        if num%2==0 and (num - 1) / 3 == (num - 1) // 3 and (num-1)/3 > 1:
            small = int((num - 1) / 3)
            nums[0].append(small)
            nums[1].append(num)
            if small<s:
                s = small
            t += 1
    return {
        'nums': nums,
        'l': l,
        's': s,
        't': t,
        }


def create_next(prev_iter):
    new_iter = find_next(prev_iter['nums'][0])
    new_iter['d'] = prev_iter['d'] + 1
    return new_iter

for i in range(10):
    new_iter = create_next(data['calcs'][data['I']])
    
    if(new_iter['l'] > data['L']):
        data['L'] = new_iter['l']
    if(new_iter['s'] > data['S']):
        data['S'] = new_iter['s']  
    data['T'] += new_iter['t']
    data['I']+=1
    new_iter['f'] = data['F'] = data['T']/data['L']
    
    data['calcs'].append(new_iter)
    
    if i%5==0:
      time.sleep(1)
    
pprint(data)

