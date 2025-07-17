# call_visualizer_q12.py
from graphviz import Digraph

class CallGraphQ12:
    def __init__(self):
        self.graphQ12 = Digraph(comment="Function Call Graph Q12")
        self.prevFuncQ12 = None

    def traceCallsQ12(self, frameQ12, eventQ12, argQ12):
        if eventQ12 == "call":
            currFuncQ12 = frameQ12.f_code.co_name
            if self.prevFuncQ12:
                self.graphQ12.edge(self.prevFuncQ12, currFuncQ12)
            self.prevFuncQ12 = currFuncQ12
        elif eventQ12 == "return":
            self.prevFuncQ12 = None
        return self.traceCallsQ12

    def renderGraphQ12(self, filenameQ12="call_graph_q12"):
        self.graphQ12.render(filenameQ12, view=False, format="png")