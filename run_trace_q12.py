# run_trace_q12.py
import sys
from call_visualizer_q12 import CallGraphQ12
import demo_target_q12

if __name__ == "__main__":
    tracerQ12 = CallGraphQ12()
    sys.settrace(tracerQ12.traceCallsQ12)
    demo_target_q12.mainQ12()
    sys.settrace(None)
    tracerQ12.renderGraphQ12()
    