# See LICENSE.vyoma for details

TOPLEVEL_LANG ?= verilog

PWD=$(shell pwd)

VERILOG_SOURCES = $(PWD)/UniversalShiftRegister.v               # provide your design path

TOPLEVEL := UniversalShiftRegister          # design file
MODULE   :=test_UniversalShiftRegister     # test file

include $(shell cocotb-config --makefiles)/Makefile.sim

clean_all: clean
	rm -rf *.xml sim_build __pycache__ 
