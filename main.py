import pyperclip
import time
import re
import requests
import pandas as pd


def submit(submit_url, s, tempurl):
    chaoshi_url = f'{submit_url}/?url={tempurl}%20%B3%AC%CA%D0%BF%A8&code=12'
    youhui_url = f'{submit_url}/?url={tempurl}%20%D3%C5%BB%DD&code=5'

    headers = {
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    }
    if s == 'chaoshi':
        response = requests.get(chaoshi_url, headers=headers, verify=False)
    if s == 'youhui':
        response = requests.get(youhui_url, headers=headers, verify=False)

    print()
    return response.content.decode('gbk')


pattern = re.compile(r'http[s]?://(?:[a-za-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fa-f][0-9a-fa-f]))+')  # 匹配模式

if __name__ == '__main__':
    # 内容放到剪切板
    pyperclip.copy('good')
    # 读取剪切板内容
    last_paste = pyperclip.paste()
    submit_url = input('请输入提交地址，(回车)：')
    while True:
        # 检测频率
        try:
            time.sleep(0.2)
            now_paste: str = pyperclip.paste()  # 读取剪切板内容
            # 复制到新内容就提交
            if now_paste != last_paste and now_paste != '提交成功':
                # print([string])
                # print(now_paste.split())
                text_list = now_paste.split()
                username = text_list[0]
                url = re.findall(pattern, now_paste)[0]
                # print(url)
                ret = ''
                if now_paste.find('优惠') != -1:
                    ret = submit(submit_url, 'youhui', url)
                    num = 5
                    log = [[url, ret, num]]
                    print(log)
                    if ret.find('成功') != -1:
                        df = pd.DataFrame(log)
                        df.to_csv("C:\提交记录.csv", mode='a', header=False, index=False, encoding='utf_8_sig')
                        pyperclip.copy('提交成功')

                if now_paste.find('超市卡') != -1:
                    ret = submit(submit_url, 'chaoshi', url)
                    num = 12
                    log = [[url, ret, num]]
                    print(log)
                    if ret.find('成功') != -1:
                        df = pd.DataFrame(log)
                        df.to_csv("C:\提交记录.csv", mode='a', header=False, index=False, encoding='utf_8_sig')
                        pyperclip.copy('提交成功')
                last_paste = now_paste
                #

        except Exception as e:
            print(e, '复制的内容不符合格式')
            last_paste = now_paste
