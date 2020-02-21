# auxiliary widgets common for some programs

from cxwidgets.aQt.QtWidgets import QWidget, QGridLayout, QFrame


class HLine(QFrame):
    def __init__(self, *args):
        super().__init__(*args)
        self.setFrameShape(QFrame.HLine)
        self.setFrameShadow(QFrame.Raised)
        self.setLineWidth(3)
        self.setMidLineWidth(3)


class BaseGridW(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(2, 2, 2, 2)
        self.grid = QGridLayout()
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(1)
        self.setLayout(self.grid)


class BaseFrameGridW(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setContentsMargins(2, 2, 2, 2)
        self.grid = QGridLayout()
        self.grid.setContentsMargins(0, 0, 0, 0)
        self.grid.setSpacing(1)
        self.setLayout(self.grid)

        self.setFrameStyle(QFrame.Sunken | QFrame.StyledPanel)
        self.setLineWidth(3)
        self.setMidLineWidth(3)
