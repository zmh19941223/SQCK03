"""
@author: haiwen
@date: 2021/11/9
@file: utils.py
"""
def filter_data(data):
    # 准备HR3格式模板，用来比对数据
    template = {
        'config': {
            'name': str,
            'base_url': str,
            'variables': dict,
            'parameters': dict,
            'verify': bool,
            'export': list
        },
        'teststeps': [{
            'name': str,
            'variables': list,
            'extract': dict,
            'validate': list,
            'setup_hooks': list,
            'teardown_hooks': list,
            'request': {
                'method': str,
                'url': str,
                'params': list,
                'headers': dict,
                'cookies': dict,
                'data': dict,
                'json': dict
            },
        }]
    }
    return merge_dict(template,data)

def merge_dict(left,right):
    '''
    合并字典同类项，删除空的数据
    '''
    # 覆盖左侧模板同类项
    for k in right:
        if k in left:
            if isinstance(left[k],dict) and isinstance(right[k],dict):
                merge_dict(left[k],right[k])
            elif isinstance(left[k],list) and isinstance(right[k],list):
                for one in right[k]:
                    merge_dict(left[k][0],one)
            # 合并条件:right[k]不为空（也包含空字符串，空列表，空字典）
            elif right[k]:
                left[k]=right[k]
            elif not right[k]:
                left.pop(k) # 删除左侧对应右侧为空的数据
    # 删除左侧多余项
    for k in list(left.keys()):
        if k not in right:
            left.pop(k)

    return left  # left为处理好的数据。