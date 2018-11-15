#!/usr/bin/env python3

import sys
import setuptools
from distutils.core import setup



def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


if sys.version_info < (3, 3):
    print("THIS MODULE REQUIRES PYTHON 3.3+. YOU ARE CURRENTLY\
    USING PYTHON {0}".format(sys.version))
    sys.exit(1)


exec(open('model_streamer/version.py').read())

setup(
    name="model_streamer",
    version=__version__,
    include_package_data=True,
    author="Stanislav Arnaudov",
    author_email="stanislv_ts@abv.bg",
    description=" ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    license="GNU General Public License v3.0",
    keywords=" ",
    url="https://github.com/palikar/model_streamer",
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    # entry_points={
    #     'console_scripts': [
    #         'model_streamer = model_streamer.'
    #     ]
    # },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
