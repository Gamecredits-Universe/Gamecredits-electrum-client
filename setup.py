#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: Electrum requires Python version >= 2.7.0...")

data_files = []

if platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    usr_share = os.path.join(sys.prefix, "share")
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum-gmc.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum-gmc.png'])
    ]

setup(
    name="Electrum-GMC",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'ltc_scrypt',
        'protobuf',
        'dnspython',
    ],
    package_dir={
        'electrum_gmc': 'lib',
        'electrum_gmc_gui': 'gui',
        'electrum_gmc_plugins': 'plugins',
    },
    packages=['electrum_gmc','electrum_gmc_gui','electrum_gmc_gui.qt','electrum_gmc_plugins'],
    package_data={
        'electrum_gmc': [
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    scripts=['electrum-gmc'],
    data_files=data_files,
    description="Lightweight Gamecredits Wallet",
    author="Thomas Voegtlin",
    author_email="thomasv@electrum.org",
    license="GNU GPLv3",
    url="http://electrum-gmc.org",
    long_description="""Lightweight Gamecredits Wallet"""
)
