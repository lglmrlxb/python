import pyautogui as pyg

# 参考网址https://blog.csdn.net/qq_57099024/article/details/122125304
'''     ==============鼠标===================='''
# print(pyg.size())#屏幕大小
# pyg.moveTo(100, 100, 0.1)# 移动
# pyg.moveRel(100, 100, 1)#相对移动
# print(pyg.position())  # 获取鼠标位置
# pyg.click(116, 51, button='left', duration=0.3)  # 点击
# pyg.doubleClick(116, 51, button='left', duration=0.3)  # 双击

'''     ==============键盘===================='''
# pyg.press('3')  # 按下立即释放
# pyg.keyDown('1')  # 按下等待释放
# pyg.keyUp('1')  # 释放按键
# pyg.hotkey('1', '2')  # 组合键
# pyg.typewrite('sdadaf', 0.1)  # 连续打字  可输入列表  0.1表示输入的每个按键间隔时间
'''     ==============标签控件===================='''
# print(pyg.alert(text='一个测试', title='test'))  # 点击确定后将返回OK
# print(pyg.confirm('请选择性别', buttons=['男', '女']))# 将输出你的点击项
# print(pyg.prompt('请输入你的账号'))  # 将返回刚才输入的内容
# print(pyg.password('请输入你的密码'))  # 返回输入的密码
'''     =================================='''
