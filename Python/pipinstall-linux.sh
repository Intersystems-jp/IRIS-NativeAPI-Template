#!/bin/bash

# サンプルで使うライブラリのインポート
pip3 install matplotlib
pip3 install networkx

rm -rf wheel/*.whl
# NativeAPI用whlファイルのGET（Linux用）
wget -P wheel https://github.com/Intersystems-jp/IRISModules/raw/master/python/wheel/intersystems_irispython-3.2.0-py3-none-any.whl
pip3 install ./wheel/intersystems_irispython-3.2.0-py3-none-any.whl

# 日本語フォントのインストール（Takaoフォントを利用しています）
#sudo apt-get update
#sudo sudo apt install fontconfig
#sudo apt-get install -y fonts-ipaexfont

# fontList.cache を削除
echo -e "\nfontList.cacheを削除します（存在しない時は No such file or directory と出ます）"
CACHEDIR=`python3 -c "import matplotlib as plt; print(plt.get_cachedir())"`
rm ${CACHEDIR}/fontList.cache
rm ${CACHEDIR}/fontList.py3k.cache