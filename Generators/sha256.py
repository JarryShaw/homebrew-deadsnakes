# -*- coding: utf-8 -*-

import collections
import json
import os
import re

BOTTLE = re.compile(
    r'(?P<formula>python|pypy|cython|jython|micropython)(3|@2|@3.8)?-(?P<version>[.0-9]+)(_(?P<revision>\d))?\.(?P<macos>yosemite|el_capitan|sierra|high_sierra|mojave|catalina)\.bottle\.((?P<rebuild>\d)\.)?tar\.gz')  # pylint: disable=line-too-long
TARBALL = re.compile(r"Python-(?P<version>\d\.\d\.\d{1,2})\.tgz", re.VERBOSE)

database = dict(
    bottle=dict(
        python=collections.defaultdict(list),
        jython=collections.defaultdict(list),
        pypy=collections.defaultdict(list),
        cython=collections.defaultdict(list),
        micropython=collections.defaultdict(list),
    ),
    tarball=dict(
        python=dict(),
        jython=dict(),
        pypy=dict(),
        cython=dict(),
        micropython=dict(),
    ),
)

ROOT = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(ROOT, 'sha256.txt')) as file:
    for line in file:
        if not line.strip():
            continue
        filename, checksum = line.strip().split()

        tarball = TARBALL.match(filename)
        if tarball is not None:
            version = tarball.group('version')
            database['tarball']['python'][version] = checksum
            continue

        bottle = BOTTLE.match(filename)
        if bottle is not None:
            formula = bottle.group('formula')
            version = bottle.group('version')
            data = bottle.groupdict()
            data['checksum'] = checksum
            database['bottle'][formula][version].append(data)
            continue

        raise ValueError(filename)

with open(os.path.join(ROOT, 'sha256.json'), 'w') as file:
    json.dump(database, file, indent=2, sort_keys=True)
