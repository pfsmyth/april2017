REM This script installs pip, then installs matplotlib, ipython, pandas
PATH=C:\Python27\ArcGIS10.2;C:\Python27\ArcGIS10.2\Scripts;%HOME%\AppData\Roaming\Python\Scripts;%PATH%
python -c "import urllib; urllib.urlretrieve('https://bootstrap.pypa.io/get-pip.py', 'get-pip.py')"
pip install --user ipython matplotlib pandas jupyter
