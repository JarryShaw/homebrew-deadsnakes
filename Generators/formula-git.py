# -*- coding: utf-8 -*-

import os
import posixpath
import re
import urllib.parse


def key(item):
    return os.path.splitext(item)[0].split('_')[1]


for path in sorted(os.listdir('temp'), key=key):
    with open(os.path.join('temp', path)) as file:
        content = file.read()

    version = None
    for line in content.splitlines():
        if not line.strip().startswith('url'):
            continue

        url = line.split()[1][1:-1]
        uri = urllib.parse.urlsplit(url).path
        name = posixpath.split(uri)[1]

        match = re.match(r'Python-(?P<version>[23].\d\.\d{1,2})(\.tar\.xz|\.tgz|\.tar\.bz2)', name)
        if match is None:
            continue
        version = match.group('version')
        break

    if version is None:
        print('-', path, 'no version')
        continue
    print('+', path, '->', version)

    dst = os.path.join('..', 'Formula', f'python@{version}.rb')
    if os.path.isfile(dst):
        # print('Existed:', path)
        continue

    with open(dst, 'w') as file:
        file.write(content)
