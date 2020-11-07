#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication
import sys
from cxwidgets import CXProcPlot


app = QApplication(sys.argv)

w = CXProcPlot('cxhw:15.adc250_8a.line0')
w.show()


sys.exit(app.exec_())
