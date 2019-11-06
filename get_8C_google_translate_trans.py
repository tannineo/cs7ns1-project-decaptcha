from random import choice
import os
"""
This file is for generating the training data (audio captchas) from Google
Translate.

The API of Google Translate is free and has no limitations of Requests.
So we can actually run this script in multiple consoles to accelerate the
downloading.

Sometimes I could get captchas 'translated' into contiguous words, so I
transformed the numbers into words and used '-' to devide them, and the
division did not affect the audio output.

The tool used is:
https://github.com/soimort/translate-shell
"""

symbols = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3',
    '4', '5', '6', '7', '8', '9'
]

num_to_eng = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}


def gen_captcha_code(length=4):
    result = ''
    for i in range(length):
        result += choice(symbols)
    return result


def get_sentence_gapped(code):
    result = ''
    for ch in code:
        tmp_ch = num_to_eng[ch] if ch in num_to_eng else ch
        result += tmp_ch if result == '' else ('-' + tmp_ch)
    return result


def download_captcha_code_voices(num=4):
    for i in range(num):
        code = gen_captcha_code(8)
        sentence = get_sentence_gapped(code)
        cmd = 'trans -download-audio-as ' + code + '.mp3' + \
            ' -no-translate ' + '"' + sentence + '"'
        print(i, ':', cmd)
        os.system(cmd)


download_captcha_code_voices(5000)
