# -*- coding: utf-8 -*-

import contextlib
import os
import subprocess

os.makedirs('temp', exist_ok=True)
repo = subprocess.check_output(
    ['brew', '--repo', 'homebrew/core']
).strip().decode()

with contextlib.suppress(subprocess.CalledProcessError):
    rev_list_1 = subprocess.check_output(
        ['git', '-C', repo, 'rev-list', 'HEAD', '--', 'Formula/python.rb']
    ).strip().decode().splitlines()
    for index, revision in enumerate(rev_list_1):
        with contextlib.suppress(subprocess.CalledProcessError):
            context = subprocess.check_output(
                ['git', '-C', repo, 'show', f'{revision}:Formula/python.rb']
            )
        with open(os.path.join('temp', f'python_{index}.rb'), 'wb') as file:
            file.write(context)

with contextlib.suppress(subprocess.CalledProcessError):
    rev_list_2 = subprocess.check_output(
        ['git', '-C', repo, 'rev-list', 'HEAD', '--', 'Formula/python@2.rb']
    ).strip().decode().splitlines()
    for index, revision in enumerate(rev_list_2):
        with contextlib.suppress(subprocess.CalledProcessError):
            context = subprocess.check_output(
                ['git', '-C', repo, 'show', f'{revision}:Formula/python@2.rb']
            )
        with open(os.path.join('temp', f'python@2_{index}.rb'), 'wb') as file:
            file.write(context)

with contextlib.suppress(subprocess.CalledProcessError):
    rev_list_3 = subprocess.check_output(
        ['git', '-C', repo, 'rev-list', 'HEAD', '--', 'Formula/python@3.rb']
    ).strip().decode().splitlines()
    for index, revision in enumerate(rev_list_3):
        with contextlib.suppress(subprocess.CalledProcessError):
            context = subprocess.check_output(
                ['git', '-C', repo, 'show', f'{revision}:Formula/python@3.rb']
            )
        with open(os.path.join('temp', f'python@3_{index}.rb'), 'wb') as file:
            file.write(context)

with contextlib.suppress(subprocess.CalledProcessError):
    rev_list_4 = subprocess.check_output(
        ['git', '-C', repo, 'rev-list', 'HEAD', '--', 'Formula/python@3.8.rb']
    ).strip().decode().splitlines()
    for index, revision in enumerate(rev_list_4):
        with contextlib.suppress(subprocess.CalledProcessError):
            context = subprocess.check_output(
                ['git', '-C', repo, 'show', f'{revision}:Formula/python@3.8.rb']
            )
        with open(os.path.join('temp', f'python@3.8_{index}.rb'), 'wb') as file:
            file.write(context)
