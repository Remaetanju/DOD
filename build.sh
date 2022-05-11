#!/bin/bash
pyinstaller --onefile --hidden-import tkinter App/src/main.py && ./dist/main