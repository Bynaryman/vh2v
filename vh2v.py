#!/usr/bin/env python

import os
import argparse

analysis_cmd = "ghdl -a --ieee=standard -fsynopsys -fexplicit --std=93 --work=tmp {input_file}"
vhdl2verilog_cmd = 'yosys -m ghdl -p "ghdl --std=93 --ieee=standard -fsynopsys -fexplicit {input_file} -e {entity} ; write_verilog {output_dir}/{entity}.v"'

def parse_args():
        parser = argparse.ArgumentParser(description='Converter help')
        parser.add_argument('--input_file', metavar="<foo.vhdl>", required=True, type=str)
        parser.add_argument('--output_dir', metavar="<output_dir>", required=True, type=str)
        return parser.parse_args()

def verilog2vhdl(input_file, output_dir):

        os.system(analysis_cmd.format(input_file=input_file))
        entities = []

        # get entities from the input file
        with open("./tmp-obj93.cf", "r") as analysis:
                analysis_lines = analysis.readlines()
                for str_line in analysis_lines:
                        str_line_split = str_line.split()
                        if str_line_split[0]=="entity":
                                print("found entity {}".format(str_line_split[1]))
                                entities.append(str_line_split[1])

        # remove temporary ghdl file
        os.system("rm ./tmp-obj93.cf")

        # write each entity as a verilog file to output folder
        for entity in entities:
                os.system(vhdl2verilog_cmd.format(input_file=input_file, entity=entity, output_dir=output_dir))

def main():
        args = parse_args()
        verilog2vhdl(args.input_file, args.output_dir)

if __name__ == "__main__":
        main()
