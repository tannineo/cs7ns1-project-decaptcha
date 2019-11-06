# cs7ns1-project-decaptcha

This is a course work of CS7NS1 Scalable Computing.

## TODO

## Decaptcha - Picture Captcha

## Decaptcha - Audio Captcha

### generate audio files

#### generate the n-char captcha directly from TTS (e.g. Google Translate)

For Google Translate (no limitation on API calls), we use [trans](https://github.com/soimort/translate-shell)

#### generate the n-char captach from multiple TTS services

26 alphabets and 10 digit so 10

### generate spectrograms

two ways to generate the spectrograms:

- `sox`: see [sox official website](http://sox.sourceforge.net/)
  - the command: `sox ${i} -n spectrogram -m -r -x 500 -y 500 -a -o ${filename}.png`
- `lobrosa`: see [librosa.feature.melspectrogram](https://librosa.github.io/librosa/generated/librosa.feature.melspectrogram.html)
