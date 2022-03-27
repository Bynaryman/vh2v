# vh2v

## Introduction

vh2v stands for VHDL to verilog. It is a python3 script that outputs the verilog modules as different files when given one vhdl file cotaining several entities.
Example below:  
```
python3 vh2v.py --input_file SystolicArray.vhdl --output_dir /tmp
```  
or, like following to  get prompted the basic help from the script:  
```
user@linux:~/vh2v$ python3 vh2v.py 
usage: vh2v.py [-h] --input_file <foo.vhdl> --output_dir <output_dir>
vh2v.py: error: the following arguments are required: --input_file, --output_dir
```

## Installation Instructions

The python itself is self contained, and therefore, does not require libraries to be installed with "pip". However, the script needs 3 tools to be installed in order to work:  
* [Yosys](https://github.com/YosysHQ/yosys): Yosys Open SYnthesis Suite, a framework for RTL synthesis tools for [verilog](https://en.wikipedia.org/wiki/Verilog).
* [GHDL](https://github.com/ghdl/ghdl): the open-source analyzer, compiler, simulator and (experimental) synthesizer for [VHDL](https://en.wikipedia.org/wiki/VHDL).
* [ghdl-yosys-plugin](https://github.com/ghdl/ghdl-yosys-plugin): VHDL synthesis (based on GHDL and Yosys).

Once these 3 tools installed, the python script can be executed as showed in [Introduction](#introduction). All the listed github links of the tools contain installation procedures. However, I (gratefully 😄 ) summarize and flatten all the instructions here:
```

```

## Achievments

This script has generated verilog in the context of [MPW5](https://platform.efabless.com/open_shuttle_program/5) [ASIC](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit) [submission](https://github.com/Bynaryman/wrapped_teras).

## Issues

Despite the abovementioned successful vhdl->verilog tapeout, VHDL synthesis with GHDL is still Experimental or incomplete. In fact, I encountered once a weird corner-case feature that was not developped in GHDL, and there might be more ! However, the GHDL team could solve my [issue](https://github.com/ghdl/ghdl/issues/1951) after less than 24h.

## Authors
Ledoux Louis (Binaryman)