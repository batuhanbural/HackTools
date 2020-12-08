from zipfile import ZipFile

if __name__ == '__main__':
    input_files = [
        r"C:\Users\ibatu\PycharmProjects\HackTools\Keyloggers\Resources\Screenshots\image'd'.png",
        r"C:\Users\ibatu\PycharmProjects\HackTools\Keyloggers\Resources\Screenshots\image'i'.png"
    ]
    with ZipFile('files.zip', mode='w') as zf:
        for f in input_files:
            zf.write(f)