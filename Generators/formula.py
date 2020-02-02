# -*- coding: utf-8 -*-

import os
import subprocess

ROOT = os.path.dirname(os.path.realpath(__file__))

downloads = os.path.join(ROOT, '..', 'Downloads')
for implementation in sorted(os.listdir(downloads)):
    for version in sorted(os.listdir(os.path.join(downloads, implementation))):
        print(f'+ {implementation} {version}')
        if implementation == 'cpython':
            subprocess.run([  # pylint: disable=subprocess-run-check
                'brew', 'extract', '--version', version, 'homebrew/core/python', 'jarryshaw/deadsnakes'
            ])
            subprocess.run([  # pylint: disable=subprocess-run-check
                'brew', 'extract', '--version', version, 'homebrew/core/python@2', 'jarryshaw/deadsnakes'
            ])
            subprocess.run([  # pylint: disable=subprocess-run-check
                'brew', 'extract', '--version', version, 'homebrew/core/python@3', 'jarryshaw/deadsnakes'
            ])
            subprocess.run([  # pylint: disable=subprocess-run-check
                'brew', 'extract', '--version', version, 'homebrew/core/python@3.8', 'jarryshaw/deadsnakes'
            ])
        elif implementation == 'pypy':
            subprocess.run([  # pylint: disable=subprocess-run-check
                'brew', 'extract', '--version', version, 'homebrew/core/pypy', 'jarryshaw/deadsnakes'
            ])
            subprocess.run([  # pylint: disable=subprocess-run-check
                'brew', 'extract', '--version', version, 'homebrew/core/pypy3', 'jarryshaw/deadsnakes'
            ])
        else:
            subprocess.run([  # pylint: disable=subprocess-run-check
                'brew', 'extract', '--version', version, f'homebrew/core/{implementation}', 'jarryshaw/deadsnakes'
            ])
