from AbstractGraph import *
from AGraphPySide.Settings import *
from AGraphPySide import BaseNode


class FloatNode(BaseNode.Node, AGNode):
    def __init__(self, name, graph):
        super(FloatNode, self).__init__(name, graph, spacings=Spacings)
        self.spin_box = QtGui.QDoubleSpinBox()
        self.spin_box.setRange(-999999999.99999999, 999999999.99999999)
        self.spin_box.valueChanged.connect(self.set_data)

        self.output = self._add_port(AGPortTypes.kOutput, AGPortDataTypes.tFloat, 'out')

        # hack! overload the output's port 'set_data' method to update lineEdit
        def set_data_overloads(data, dirty_propagate=True):
            self.spin_box.setValue(float(data))
        self.output.set_data_overload = set_data_overloads

        spin_box_proxy = QtGui.QGraphicsProxyWidget()
        spin_box_proxy.setWidget(self.spin_box)
        self.inputsLayout.insertItem(0, spin_box_proxy)
        self.compute()

    @staticmethod
    def get_category():
        return 'GenericTypes'

    def set_data(self):

        self.output.set_data(self.spin_box.value(), True)

    def compute(self):

        self.output.set_data(self.spin_box.value(), False)
