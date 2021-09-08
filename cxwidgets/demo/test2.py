#!/usr/bin/env python3

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


class CompeseHistPlotter:
    def __init__(self, *args, **kwargs):
        self.chunk_size = kwargs.get("chankSize", 100)
        self.max_chunks = kwargs.get("max_chunks", 20)
        self.curves = []
        self.data = np.empty((2, chunkSize))
        self.ind = 0
        self.chunk_ind = 0

    def add_point(self, x, y):
        pass

    def update(self):
        for c in curves:
            c.setPos(-(now - startTime), 0)


def update3():
    i = ptr5 % chunkSize
    if i == 0:
        curve = p5.plot()
        curves.append(curve)
        last = data5[-1]
        data5 = np.empty((chunkSize + 1, 2))
        data5[0] = last
        while len(curves) > maxChunks:
            c = curves.pop(0)
            p5.removeItem(c)
    else:
        curve = curves[-1]
    data5[i + 1, 0] = now - startTime
    data5[i + 1, 1] = np.random.normal()
    curve.setData(x=data5[:i + 2, 0], y=data5[:i + 2, 1])
    ptr5 += 1



startTime = pg.ptime.time()

win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('pyqtgraph example: Scrolling Plots')
p = win.addPlot()
p.setLabel('bottom', 'Time', 's')
p.setXRange(-20, 0)

timer = pg.QtCore.QTimer()
timer.timeout.connect(update3)
timer.start(50)

## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    QtGui.QApplication.instance().exec_()
