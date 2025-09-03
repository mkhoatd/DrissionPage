# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="DrissionPage",
    version="4.1.1.2",
    author="g1879",
    author_email="g1879@qq.com",
    description="Python based web automation tool. It can control the browser and send and receive data packets.",
    keywords="DrissionPage",
    url="https://DrissionPage.cn",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'lxml',
        'requests',
        'cssselect',
        'DownloadKit>=2.0.7',
        'websocket-client',
        'click',
        'tldextract>=3.4.4',
        'psutil'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        # "License :: OSI Approved :: BSD License",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'dp = DrissionPage._functions.cli:main',
        ],
    },
)
