"""文字檔字串__doc__"""

def getMax(x, y):
    """文字檔字串實例
    建議x、y是整數
    這個函數將回傳較大值"""
    if y>x:
        return y
    else:
        return x
    
#呼叫
print(getMax(3, 7))
print(getMax.__doc__)