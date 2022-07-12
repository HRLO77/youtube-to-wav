import re
import os
import pathlib

download = '/tmp'
# if not os.path.isdir(download):
#     os.mkdir(download)



def copy(file: str, path: str):
    if not os.path.isdir(path):
        os.mkdir(path)
    with open(file, 'rb') as f:
        b = f.read()
        name = os.path.basename(file)
    path = os.path.join(path, name)
    if not os.path.isfile(path):
        with open(path, 'x') as f:
            pass
        with open(path, 'wb') as f:
            f.write(b)

# regex
pattern = '(((https?://)?(m\.)?)|((https?://)?(www\.)?))?youtu\.?be\.com((/watch\?v=[a-zA-Z0-9]{11}){1}|(/([a-zA-Z0-9]){11}){1})?'
while True:
    try:
        s = input('Enter a youtube url to download: ')
        r = re.search(pattern, s)
        assert not r is None
    except AssertionError:
        print('Enter a valid youtube url.')
    else:
        s = s[r.span()[0]:r.span()[1]]  # filtering purposes
        break

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
    }],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url_list=[s])

for file in os.listdir("./"):
    if file.endswith(".wav"):
        copy(file, download)
        os.remove(file)


print('Done!')
