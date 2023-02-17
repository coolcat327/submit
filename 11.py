import pyperclip
import time


def save(filename, u_list, mode):
    f = open(filename, mode, encoding='utf-8')
    f.write(str(u_list))
    f.write("\n")
    f.close()


if __name__ == '__main__':
    # 内容放到剪切板
    pyperclip.copy('good')
    # 读取剪切板内容
    last_paste = pyperclip.paste()
    while True:
        # 检测频率
        try:
            time.sleep(0.5)
            now_paste: str = pyperclip.paste()  # 读取剪切板内容
            # 复制到新内容就提交
            if now_paste != last_paste:

                if now_paste.find('优惠') != -1 or now_paste.find('超级星期五') != -1:
                    print(now_paste)
                    save(f'闲鱼.txt', now_paste, 'a')
                last_paste = now_paste

        except Exception as e:
            print(e, '复制的内容不符合格式')
            last_paste = now_paste
