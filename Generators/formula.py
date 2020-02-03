# -*- coding: utf-8 -*-

import multiprocessing
import os
import subprocess

import pkg_resources

ROOT = os.path.dirname(os.path.realpath(__file__))

downloads = os.path.join(ROOT, '..', 'Downloads')
with multiprocessing.Pool() as pool:
    for implementation in sorted(os.listdir(downloads)):
        for version in sorted(os.listdir(os.path.join(downloads, implementation)), key=pkg_resources.parse_version):
            print(f'+ {implementation} {version}')

            args_list = list()
            if implementation == 'cpython':
                args_list.append([
                    'brew', 'extract', '--version', version, 'homebrew/core/python', 'jarryshaw/deadsnakes'
                ])
                args_list.append([
                    'brew', 'extract', '--version', version, 'homebrew/core/python@2', 'jarryshaw/deadsnakes'
                ])
                args_list.append([
                    'brew', 'extract', '--version', version, 'homebrew/core/python@3', 'jarryshaw/deadsnakes'
                ])
                args_list.append([
                    'brew', 'extract', '--version', version, 'homebrew/core/python@3.8', 'jarryshaw/deadsnakes'
                ])
            elif implementation == 'pypy':
                args_list.append([
                    'brew', 'extract', '--version', version, 'homebrew/core/pypy', 'jarryshaw/deadsnakes'
                ])
                args_list.append([
                    'brew', 'extract', '--version', version, 'homebrew/core/pypy3', 'jarryshaw/deadsnakes'
                ])
            else:
                args_list.append([
                    'brew', 'extract', '--version', version, f'homebrew/core/{implementation}', 'jarryshaw/deadsnakes'
                ])
            pool.map(subprocess.run, args_list)
