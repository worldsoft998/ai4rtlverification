**What are the best Python-HDL/HLS/HVL Bridges/Interfaces/Communications Modules?**

What are the best (and easiest to implement) Python-HDL/HLS/HVL bridges/interfaces/communications modules for existing, non-Python, HDL/HLS/HVL RTL design such as (System)Verilog, VHDL, SystemC and testbenches based on popular verification methodologies such as UVM, UVVM, OSVVM, ABV(SVA,PSL) and others, while Python will be applied for Hardware Verification Optimization based on AI (Artificial Intelligence) & ML (Machine Learning) algorithms?

I have conducted some kind of investigations into this subject, and have tried several of them, and as a result, I've compiled a list of them organized in the order of their importance to me. Here below is a simple listing without detailed explanation, which you can find with me if you're interested in particular or you may find more information about some of the particular modules by searching on search engines or by asking AI boots such as ChatGPT or grok.

**FIRST PRIORITY**

cocotb / PyUVM - GPI (Generic Procedural Interface)

(Requires significant TB porting)

PyHDL-IF

Py-HPI (Procedural HDL Python Integration)

tblink-rpc

DPI / VPI + TCP sockets

(TCP Sockets) + (Python embedding), (DPI-C + Shared Memory), (DPI-C + Python C API Wrapper), (DPI-C + C shim)

TCP Sockets IPC (Inter-Process Communication)

PyMTL / PyMTL3 (Mamba)

**VENDOR-SPECIFIC / COMMERCIAL TOOLS WITH PYTHON APIs** / vendor-specific socket API

Questa Python API

Synopsys Verdi Python

HLS Tools From Xilinx

FLI (Foreign Language Interface) - C/C++> Verilog Simulators

PyVerilator / Verilator

VHPIDirect for GHDL

**VHDL RELEVANT**

VUnit (VHPI/FLI)

VHPI (VHDL Procedural Interface) / PyVHPI

VHPIDirect for GHDL

**PYTHON - C++**

pybind11 to Create Python Bindings of Existing C++ Code

Python/C API for Python- C++ Interaction

**COMPILED PYTHON MODULES**

pysv: Running Python Code in SystemVerilog

systemverilog-python

**RUNNING PYTHON TESTBENCHES WITH HARDWARE EMULATION**

PyDVE: Open-Source Python-Based Design Verification

**HARDWARE DESCRIPTION IN PYTHON AND CONVERSION TO VERILOG/VHDL**

MyHDL and Amaranth

**OTHERS**

Named Pipes (FIFOS)

Shared Files

Shared Memory

pystim - Call Python within the SystemVerilog by Embedding Python Interpreter

PyVHDL: A Hardware Simulation Environment Integrating Python and VHDL

Python Subprocess

I have not yet tried all of them, it's also not necessary nor feasible. But I am wondering if the subject is of some kinds of interests among the verification community, and if yes, I am curious of any comments on my topics and we may continue to follow up the development trends in this area, because it's a new area and is changing very rapidly. I have noticed that there is no special forums which is dedicated either to Python-HDL interfaces or to AI/ML applications to RTL verification, quite astonished.

The Python - HDL/HSL/HVL interface topic is an important subject and is still at its early stage of development and to my understanding, it will be becoming even more and more important as AI/ML are being developed rapidly over the next years and Python as you know, is the de facto language of AI/ML.

I am a verification guy with particular interest in AI/ML applications to RTL verification optimization, in particular the stimulus optimization aimed at test time reduction. I wish to gather a group of same-flavored people to exchange views and info, so that we can grow together for that mission. Thank you!