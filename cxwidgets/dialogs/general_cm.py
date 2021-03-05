from cxwidgets import BaseGridW, PSpinBox, PCheckBox
from cxwidgets.aQt.QtWidgets import QLabel, QLineEdit, QTextEdit, QMenu,QWidgetAction
from cxwidgets.aQt.QtCore import Qt
from pycx4.qcda import rflags_meanings

class CXGeneralCM(BaseGridW):
    def __init__(self, source_w=None, parent=None):
        super().__init__(parent)
        self.source_w = source_w
        self.grid.addWidget(QLabel("handle info"), 0, 0, 1, 2, Qt.AlignHCenter)

        self.grid.addWidget(QLabel("name"), 1, 0)
        self.name_line = QLineEdit()
        self.grid.addWidget(self.name_line, 1, 1)
        self.name_line.setText(self.source_w.cname)
        self.name_line.setReadOnly(True)

        self.grid.addWidget(QLabel("flags"), 2, 0, 1, 2, Qt.AlignHCenter)
        self.flags_te = QTextEdit()
        self.grid.addWidget(self.flags_te, 3, 0, 1, 2, Qt.AlignHCenter)
        if source_w.chan is not None:
            ft = source_w.chan.rflags_text()
            self.flags_te.setText('\n'.join(ft))
        else:
            self.flags_te.setText('channel not defined')



class CXFlagsMenu(QMenu):
    def __init__(self, flags):
        super().__init__()
        self.setTitle('rflags')
        self.items = {}
        self.widgets = {}
        for k in rflags_meanings.keys():
            self.widgets[k] = PCheckBox(k)
            self.widgets[k].setEnabled(False)
            #self.widgets[k].setAttribute(Qt.WA_TransparentForMouseEvents, True)
            self.items[k] = QWidgetAction(self)
            self.items[k].setDefaultWidget(self.widgets[k])
            self.addAction(self.items[k])
        k = list(rflags_meanings.keys())[0]
        self.widgets[k].setValue(1)

