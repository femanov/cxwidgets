#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import QApplication
import pyqtgraph as pg
from cxwidgets import CXPlotDataItem


app = QApplication(sys.argv)


graph = pg.GraphicsLayoutWidget()
graph.resize(700, 700)
plt = graph.addPlot(title="simple demo")
plt.showGrid(x=True, y=True)

curv = CXPlotDataItem(cname='cxhw:15.adc250_8a.line0', pen=(0, 255, 0))
plt.addItem(curv)

curv1 = CXPlotDataItem(cname='cxhw:15.adc250_8a.line1', pen=(255, 0, 0), max_nelems=2000)
plt.addItem(curv1)


graph.show()


sys.exit(app.exec_())
