# -*- coding: utf-8 -*-

#バブルソート
    #昇順
def buble_sort_asc(list):
    k = len(list)
    for i in range(k - 1):
        for j in range(k,i,-1):
            if list[j - 1] > list[j]:
                list[j - 1],list[j] = list[j],list[j - 1]
    return list

    #降順
def buble_sort_desc(list):
    k = len(list)
    for i in range(k - 1):
        for j in range(k,i,-1):
            if list[j - 1] < list[j]:
                list[j - 1],list[j] = list[j],list[j - 1]
    return list

#挿入ソート
    #昇順
def insert_sort_asc(list):
    k = len(list)
    for i in range(1,k):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
    return list

    #降順
def insert_sort_desc(list):
    k = len(list)
    for i in range(1,k):
        temp = list[i]
        j = i - 1
        while j >= 0 and temp > list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = temp
    return list

#選択ソート
    #昇順
def select_sort_asc(list):
    k = len(list)
    for i in range(k - 1):
        n = i
        for j in range(i + 1, k):
            if list[j] < list[i]:
                list[i],n,list[n] = list[j],j,list[i]
    return list

    #降順
def select_sort_desc(list):
    k = len(list)
    for i in range(k - 1):
        n = i
        for j in range(i + 1, k):
            if list[j] > list[i]:
                list[i],n,list[n] = list[j],j,list[i]
    return list

#マージソート
    #昇順
def merge_sort_asc(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    left = merge_sort_asc(left)
    right = merge_sort_asc(right)
    return merge_asc(left, right)

def merge_asc(left, right):
    merged = []
    li, ri = 0, 0
    while li < len(left) and ri < len(right):
        if left[li] <= right[ri]:
            merged.append(left[li])
            li += 1
        else:
            merged.append(right[ri])
            ri += 1
    if li < len(left):
        merged.extend(left[li:])
    if ri < len(right):
        merged.extend(right[ri:])
    return merged

    #降順
def merge_sort_desc(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]
    left = merge_sort_desc(left)
    right = merge_sort_desc(right)
    return merge_desc(left, right)

def merge_desc(left, right):
    merged = []
    li, ri = 0, 0
    while li < len(left) and ri < len(right):
        if left[li] >= right[ri]:
            merged.append(left[li])
            li += 1
        else:
            merged.append(right[ri])
            ri += 1
    if li < len(left):
        merged.extend(left[li:])
    if ri < len(right):
        merged.extend(right[ri:])
    return merged

