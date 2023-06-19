
#在n字符串里面查找以x开始  以y结束的字符串
#输入 查找字符串， x，y
def findstr(n,x,y):
    if n.find(x)>=0:
        s=n[n.find(x)+len(x):]
        if s.find(y)>=0:
            # print(s[:s.find(y)])
            return True,s[:s.find(y)]
        else:return False,""
    else:return False,""
#---------------------------示例-----------------------------------------
# 字符串='<img  data-original="https://www.umei.cc/d/file/20230616/small3657219dfe2aa3a7eddb229274b1c6561686877093.jpg"/>'
# 开始字符串='data-original="'
# 结束字符串='"/>'
# print(findstr(字符串,开始字符串,结束字符串))
# 结果=(True, 'https://www.umei.cc/d/file/20230616/small3657219dfe2aa3a7eddb229274b1c6561686877093.jpg')
