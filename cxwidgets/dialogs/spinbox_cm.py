from cxwidgets import BaseGridW, PSpinBox
from cxwidgets.aQt.QtWidgets import QLabel, QLineEdit
from cxwidgets.aQt.QtCore import Qt


class CXSpinboxCM(BaseGridW):
    def __init__(self, source_w=None, parent=None):
        super().__init__(parent)
        self.source_w = source_w
        self.grid.addWidget(QLabel("handle settings"), 0, 0, 1, 4, Qt.AlignHCenter)

        self.grid.addWidget(QLabel("name"), 1, 0)
        self.name_line = QLineEdit()
        self.grid.addWidget(self.name_line, 1, 1)
        self.name_line.setText(self.source_w.cname)
        self.name_line.setReadOnly(True)

        self.grid.addWidget(QLabel("step"), 2, 0)
        self.step_sb = PSpinBox()
        self.grid.addWidget(self.step_sb, 2, 1)

        self.grid.addWidget(QLabel("min"), 3, 0)
        self.min_sb = PSpinBox()
        self.grid.addWidget(self.min_sb, 3, 1)

        self.grid.addWidget(QLabel("max"), 4, 0)
        self.max_sb = PSpinBox()
        self.grid.addWidget(self.max_sb, 4, 1)

        source_w.chan.get_range()
        source_w.chan.get_strings()
        print(source_w.chan.quant)