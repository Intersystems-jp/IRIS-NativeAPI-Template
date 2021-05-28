@echo off
rm -rf wheel

bitsadmin /transfer myDownloadJob /download /priority normal https://github.com/Intersystems-jp/IRISModules/raw/master/python/wheel/intersystems_irispython-3.2.0-py3-none-any.whl %CD%/wheel/intersystems_irispython-3.2.0-py3-none-any.whl
pip install ./wheel/intersystems_irispython-3.2.0-py3-none-any.whl

pip install matplotlib
pip install networkx