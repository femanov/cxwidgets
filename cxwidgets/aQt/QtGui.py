from . import PYQT4, PYQT5

if PYQT5:
    from PyQt5.QtGui import *


elif PYQT4:
    from PyQt4.QtGui import *

