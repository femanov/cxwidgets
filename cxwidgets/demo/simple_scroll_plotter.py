#!/usr/bin/env python3

from PyQt5.QtWidgets import QApplication
import sys
import pyqtgraph as pg
from cxwidgets import CXScrollPlotDataItem, TimeAxisItem, AgeAxisItem, CXScrollAgePlotDataItem


app = QApplication(sys.argv)

pen = (0, 255, 0)

graph = pg.GraphicsLayoutWidget()
graph.resize(700, 700)
plt = graph.addPlot(title="simple scroll demo",
                    labels={'left': ('Beam current', 'mA'), 'bottom': ('Age', 's')})
# plt = graph.addPlot(title="simple scroll demo",
#                     axisItems={'bottom': TimeAxisItem(orientation='bottom', format="%H:%M:%S")})
# plt = graph.addPlot(title="simple scroll demo",
#                     axisItems={'bottom': AgeAxisItem(orientation='bottom', format="%H:%M:%S")})

plt.showGrid(x=True, y=True)
#plt.gcf().autofmt_xdate()

#curv = CXScrollPlotDataItem(cname='canhw:21.ring_current', pen=pen, length=2000)
#curv = CXScrollPlotDataItem(cname='cxhw:0.dcct.beamcurrent', pen=pen, length=2000, utime=200)
#curv = CXScrollAgePlotDataItem(cname='cxhw:0.dcct.beamcurrent', pen=pen, length=10000, utime=200)
curv = CXScrollAgePlotDataItem(cname='cxhw:5.out1.t', pen=pen, length=10000, utime=200)


plt.addItem(curv)
plt.setXRange(0, 200, padding=0.02)
# text='Age,s'
plt.invertX(True)

graph.show()


sys.exit(app.exec_())
