# -*- coding: utf-8 -*-

import hashlib
import multiprocessing
import os
import re
import shutil
import subprocess
import sys

import bs4
import requests

ROOT = os.path.dirname(os.path.realpath(__file__))


def download(version: str):
    print(f'Downloading [{version}]...')

    path = os.path.join(ROOT, '..', 'Downloads', 'cpython', version)
    os.makedirs(path, exist_ok=True)

    tarball = os.path.join(path, f'Python-{version}.tgz')
    if shutil.which('aria2c') is None:
        if os.path.isfile(tarball):
            return

        try:
            page = requests.get(f'https://www.python.org/ftp/python/{version}/Python-{version}.tgz')
            with open(tarball, 'wb') as file:
                file.write(page.content)

            sha256 = hashlib.sha256(page.content).hexdigest()
            with open(os.path.join(ROOT, 'sha256.txt'), 'a') as file:
                print(f'Python-{version}.tgz', sha256, file=file)
        except BaseException:
            os.remove(tarball)
    else:
        if os.path.isfile(tarball) and (not os.path.isfile(f'{tarball}.aria2')):
            return

        try:
            subprocess.check_call(['aria2c',
                                   f'--dir={path}', f'--out=Python-{version}.tgz',
                                   f'--max-connection-per-server={os.cpu_count() or 4}', '--min-split-size=1M',
                                   f'https://www.python.org/ftp/python/{version}/Python-{version}.tgz'])

            with open(tarball, 'rb') as file:
                content = file.read()
            sha256 = hashlib.sha256(content).hexdigest()
            with open(os.path.join(ROOT, 'sha256.txt'), 'a') as file:
                print(f'Python-{version}.tgz', sha256, file=file)
        except BaseException:
            os.remove(tarball)


def main():
    page = requests.get('https://www.python.org/downloads/source/')
    soup = bs4.BeautifulSoup(page.text, 'html5lib')

    versions = list()
    column = soup.find_all('div', class_='column')[0]
    for link in column.find_all('a'):
        href: str = link.attrs.get('href')
        if href is None or not href.endswith('.tgz'):
            continue

        version = href.rsplit('/', maxsplit=1)[1]
        match = re.match(r"Python-(?P<version>\d\.\d\.\d{1,2}).tgz", version)
        if match is None:
            continue
        versions.append(match.group('version'))
    multiprocessing.Pool().map(download, sorted(versions))


if __name__ == "__main__":
    sys.exit(main())
