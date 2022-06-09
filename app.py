from flask import Flask, render_template, request
import os
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


def GetDownloadPath():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')


@app.route('/download', methods=["POST", "GET"])
def download():
    url = request.form["url"]
    os.chdir(GetDownloadPath())
    os.popen(f"spotdl {url}")
    return home()


if __name__ == '__main__':
    app.run()
