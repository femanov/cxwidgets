from cxwidgets.aQt.QtCore import pyqtSlot, pyqtProperty, Qt
from cxwidgets.aQt.QtWidgets import QMenu, QWidgetAction
import pycx4.qcda as cda
from .pspinbox import PSpinBox
from .dialogs.spinbox_cm import CXSpinboxCM
from .dialogs.general_cm import CXFlagsMenu

class CXSpinBox(PSpinBox):
    def __init__(self, parent=None, **kwargs):
        super().__init__(parent, **kwargs)
        self._cname = kwargs.get('cname', None)
        self.chan = None

        self.cx_connect()
        self.done.connect(self.cs_send)

    def contextMenuEvent(self, event):
        global w
        w = CXSpinboxCM(self)
        contextMenu = QMenu(self)
        act_prt = contextMenu.addAction("print")
        fl_menu = CXFlagsMenu(0)
        contextMenu.addMenu(fl_menu)
        act_all = QWidgetAction(contextMenu)
        act_all.setDefaultWidget(w)

        contextMenu.addAction(act_all)

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == act_prt:
            print("hello")

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            print("Left Button Clicked")
        elif QMouseEvent.button() == Qt.RightButton:
            #do what you want here
            print("Right Button Clicked")

    def cx_connect(self):
        if self._cname is None or self._cname == '':
            return
        self.chan = cda.IChan(self._cname, private=True)
        self.chan.valueChanged.connect(self.cs_update)

    @pyqtSlot(int)
    def cs_send(self, value):
        if self.chan is None:
            return
        if int(value) == self.chan.val:
            return
        self.chan.setValue(value)

    def cs_update(self, chan):
        if int(self.value()) == chan.val:
            return
        self.setValue(chan.val)
        if chan.rflags != 0:
            print(chan.rflags_text())
            pass

    @pyqtSlot(str)
    def set_cname(self, cname):
        if self._cname == cname:
            return
        self._cname = cname
        self.cx_connect()

    def get_cname(self):
        return self._cname

    cname = pyqtProperty(str, get_cname, set_cname)

