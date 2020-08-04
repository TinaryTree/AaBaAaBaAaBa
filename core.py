import morse
from pypinyin import lazy_pinyin


def main():
    strings = input('请输入的内容：')
    res = ''
    for cur_word in lazy_pinyin(strings):
        if cur_word.isalpha():
            res += ''.join(morse.string_to_morse(cur_word)) + ' '
        else:
            res += cur_word
    res = res.replace('.', '啊').replace('-', '吧')
    print('小智障说：', res)


if __name__ == '__main__':
    while True:
        main()
