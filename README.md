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
  
First of all, create a convenient place (folder) to gather all these tools
```
mkdir translation_tools
cd translation_tools
TRANSLATION_DIR=$("pwd")
```

then, clone all repositories (including this one):
```
git clone https://github.com/YosysHQ/yosy
git clone https://github.com/ghdl/ghdl
git clone https://github.com/ghdl/ghdl-yosys-plugin
git clone https://github.dev/Bynaryman/vh2v
```

At this point, you should see such folders:
```
user@linux:~/translation_tools$ ls $TRANSLATION_DIR 
ghdl  ghdl-yosys-plugin  vh2v  yosys
```

Now, we have to install each of these tools one by one, let's start with yosys:
```
cd yosys
make config-gcc
make
sudo make install
cd $TRANSLATION_DIR
```
If you encounter some errors, your system may lack some tools. For instance, for ubuntu, the dependencies can be installed as following:
```
$ sudo apt-get install build-essential clang bison flex \
	libreadline-dev gawk tcl-dev libffi-dev git \
	graphviz xdot pkg-config python3 libboost-system-dev \
	libboost-python-dev libboost-filesystem-dev zlib1g-dev
```
Please, refer to [Yosys installation](https://github.com/YosysHQ/yosys#building-from-source) for more details.

Let's proceed with GHDL installation:  
Important note /!\: GHDL is written in [ada](https://en.wikipedia.org/wiki/Ada_(programming_language)) and therefore needs an ada compiler. The latter can be installed on ubuntu as such:
```
sudo apt install gnat-gps
```

Then, the installation:
```
cd ghdl
./configure --prefix=/usr/local
make
sudo make install
cd $TRANSLATION_DIR
```

We continue with ghdl-yosys-plugin:
```
cd ghdl-yosys-plugin
make
sudo make install
cd $TRANSLATION_DIR
```

Finally, testing vh2v:
```
cd vh2v
python3 vh2v.py --input_file my_top_vhdl.vhd --output_dir /tmp
cd /tmp
ls -l *.v  # observe result files
cd $TRANSLATION_DIR
```
## Achievements

This script has generated verilog in the context of [MPW5](https://platform.efabless.com/open_shuttle_program/5) [ASIC](https://en.wikipedia.org/wiki/Application-specific_integrated_circuit) [submission](https://github.com/Bynaryman/wrapped_teras).

## Issues

Despite the abovementioned successful vhdl->verilog tapeout, VHDL synthesis with GHDL is still Experimental or incomplete. In fact, I encountered once a weird corner-case feature that was not developped in GHDL, and there might be more ! However, the GHDL team could solve my [issue](https://github.com/ghdl/ghdl/issues/1951) after less than 24h.

# Future

If you like it ..

## Authors
Ledoux Louis (Binaryman)