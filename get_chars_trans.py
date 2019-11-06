import os
"""
This file get separate audio files of characters from different TTS services:

The TTS sercvices including:

- Google Translate
- Yandex (there is a script detection so failed)

See get_8C_google_translate_trans.py for more info.

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


def code_to_word(code):
    return num_to_eng[code] if code in num_to_eng else code


def download_char_audio(code, engine='google', path='./char_mp3/'):
    cmd = 'trans -download-audio-as ' + path + code + '-' + engine + '.mp3' + \
            ' -no-translate ' + '"' + code_to_word(code) + '"' \
            + ' -e ' + engine
    print(code, ':', cmd)
    os.system(cmd)


for code in symbols:
    download_char_audio(code)
    # download_char_audio(code, engine='yandex')
