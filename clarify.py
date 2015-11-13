#!/usr/bin/env python
import sys

# Simple string matching, does not consider substring issues, e.g. str vs strh
def main():
    # Pipe in Data
    data = sys.stdin.readlines()
    # Iterate through Data
    for line in data:
        # Strip newline characters
        line = line.rstrip('\n')
        for operation in get_instruction_set():
            if (operation[0] in line.upper()):
                print line + ' ' + operation[1]
                # Break loop to avoid second instance of matching command
                break

# Incomplete instruction set, does not consider thumb, arguments etc
def get_instruction_set():
    instruction_set = [("WFS", "Write FP status register"),
                       ("ADC", "Add with carry"),
                       ("ADD", "Add"),
                       ("B", "Branch"),
                       ("BIC", "Bit Clear"),
                       ("BL", "Branch with Link"),
                       ("BX", "Branch and Exchange"),
                       ("CDP", "Coprocessor Data Processing"),
                       ("CMN", "Compare Negative"),
                       ("CMP", "Compare"),
                       ("EOR", "Exclusive Or"),
                       ("LDC", "Load Coprocessor from memory"),
                       ("LDM", "Load multiple registers"),
                       ("LDR", "Load registers from memory"),
                       ("MCR", "Move CPU register to coprocessor register"),
                       ("MLA", "Multiply accumulate"),
                       ("MOV", "Move register or constant"),
                       ("MRC", "Move from coprocessor to register to CPU register"),
                       ("MRS", "Move PSR status flags to register"),
                       ("MUL", "Multiply"),
                       ("MVN", "Move negative register"),
                       ("ORR", "Or"),
                       ("RSB", "Reverse subtract"),
                       ("RSC", "Reverse subtract with carry"),
                       ("SBC", "Subtract with carry"),
                       ("STC", "Store coprocessor register to memory"),
                       ("STM", "Store Multiple"),
                       ("STR", "Store register to memory"),
                       ("SUB", "Subtract"),
                       ("SWI", "Software Interrupt"),
                       ("SWP", "Swap register with memory"),
                       ("TEQ", "Test bitwise equality"),
                       ("TST", "Test bits")]
    return instruction_set


if __name__=="__main__":
    main()


