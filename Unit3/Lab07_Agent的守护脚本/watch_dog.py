import time

with open('testquit.log') as f:
    text = f.read()
if 'Error' in text:
    print('请立即修复！')
