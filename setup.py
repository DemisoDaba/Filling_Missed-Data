# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 14:18:09 2023

@author: Demiso
"""

import setuptools

setuptools.setup(
    name="data_filler",
    version="1.0",
    author="Demiso",
    description="GUI application to fill missing data",
    py_modules=["__main__"],
    entry_points={
        "console_scripts": [
            "data_filler = __main__:main",
        ]
    },
    install_requires=[
        "numpy",
        "tkinter"
    ],
)
