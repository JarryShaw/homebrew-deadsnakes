# -*- coding: utf-8 -*-

import hashlib
import os
import re
import sys

import bs4
import requests

ROOT = os.path.dirname(os.path.realpath(__file__))


def download(bottle: str, version: str, implementation: str):
    print(f'Downloading [{implementation}-{version}] {bottle}...')

    path = os.path.join(ROOT, '..', 'Downloads', implementation, version)
    os.makedirs(path, exist_ok=True)

    page = requests.get(f'https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/bottles/{bottle}')
    if os.path.isfile(os.path.join(path, bottle)):
        return

    try:
        with open(os.path.join(path, bottle), 'wb') as file:
            file.write(page.content)

        sha256 = hashlib.sha256(page.content).hexdigest()
        with open(os.path.join(ROOT, 'sha256.txt'), 'a') as file:
            print(bottle, sha256, file=file)
    except BaseException:
        os.remove(os.path.join(path, bottle))


def main():
    page = requests.get('https://mirrors.tuna.tsinghua.edu.cn/homebrew-bottles/bottles/')
    soup = bs4.BeautifulSoup(page.text, 'html5lib')

    for item in soup.find_all('td', class_='link'):
        name: str = list(item.stripped_strings)[0]
        if not name.endswith('.tar.gz'):
            continue

        if name.startswith('python-2.'):
            # Python 2.x
            match = re.match(r"python-(?P<version>[.0-9]+)(_\d)?\..+\.tar\.gz", name)
            download(name, match.group('version'), 'cpython')

        if name.startswith('python-3.'):
            # Python 3.x
            match = re.match(r"python-(?P<version>[.0-9]+)(_\d)?\..+\.tar\.gz", name)
            download(name, match.group('version'), 'cpython')

        if name.startswith('python3-3.'):
            # Python 3.x
            match = re.match(r"python3-(?P<version>[.0-9]+)(_\d)?\..+\.tar\.gz", name)
            download(name, match.group('version'), 'cpython')

        if name.startswith('python@2-2.'):
            # Python 2.x
            match = re.match(r"python@2-(?P<version>[.0-9]+)(_\d)?\..+\.tar\.gz", name)
            download(name, match.group('version'), 'cpython')

        if name.startswith('python@3.8-3.'):
            # Python 3.8.x
            match = re.match(r"python@3.8-(?P<version>[.0-9]+)(_\d)?\..+\.tar\.gz", name)
            download(name, match.group('version'), 'cpython')

        if name.startswith('cython-'):
            # Cython 0.x
            match = re.match(r"cython-(?P<version>[.0-9]+)(_\d)?\..+\.tar\.gz", name)
            download(name, match.group('version'), 'cython')

        if name.startswith('jython-'):
            # Jython 2.x
            match = re.match(r"jython-(?P<version>[.0-9]+)(_\d)?\..+\.tar\.gz", name)
            download(name, match.group('version'), 'jython')

        if name.startswith('micropython-'):
            # MicroPython 2.x
            match = re.match(r"micropython-(?P<version>[.0-9]+)(_\d)?\..+\.tar\.gz", name)
            download(name, match.group('version'), 'micropython')

        if name.startswith('pypy-'):
            # PyPy 2.x
            match = re.match(r"pypy-(?P<version>[.0-9]+)(_\d)?\..+\.tar\.gz", name)
            download(name, match.group('version'), 'pypy')

        if name.startswith('pypy3-'):
            # PyPy 3.x
            match = re.match(r"pypy3-(?P<version>[.0-9]+)(_\d)?\..+\.tar\.gz", name)
            download(name, match.group('version'), 'pypy')


if __name__ == "__main__":
    sys.exit(main())
