#!/usr/bin/env python3

from loguru import logger

class SuperSimpleComputer:

    def __init__(self, memory):
        self.memory = memory
        self.memory_size = len(self.memory.memory)
        self.pc = 0     # Program Counter

        # Keep incrementing the program counter to execute next instructions
        while(self.pc < self.memory_size):
            self.execute()

            # Increment program counter with 4 to get the next word.
            self.pc += 4
            logger.debug("Incremented program counter by 4")
    
    def execute(self):
        # Fetch the word from memory
        opcode = self.memory[self.pc]
        dest_addr = self.memory[self.pc + 1]
        op1_addr = self.memory[self.pc + 2]
        op2_addr = self.memory[self.pc + 3]
        

        # Executing whatever is the command
        # No instruction
        if opcode == 0:
            logger.debug(f"No instruction at PC {self.pc}")
        
        # Perform addition
        elif opcode == 1:
            op1 = self.memory[op1_addr]
            op2 = self.memory[op2_addr]
            result = self.add(op1, op2)

            # Need to perform bounds check here for memory address
            self.memory[dest_addr] = result
            logger.success(f"Performed addition operation. Result saved at memory location {dest_addr}")
        
        elif opcode == 2:
            op1 = self.memory[op1_addr]
            op2 = self.memory[op2_addr]
            result = self.subtract(op1, op2)

            # Need to perform bounds check here for memory address
            self.memory[dest_addr] = result
            logger.success(f"Performed subtraction operation. Result saved at memory location {dest_addr}")
        
        else:
            logger.error("Unknown opcode encountered. Skipping")


    def add(self, op1, op2):
        # Need todo something about the overflow condition
        return op1 + op2
    
    def subtract(self, op1, op2):
        # Need todo something about the overflow condition
        # 2's complement representation of the number has to be done in memory
        return op1 - op2
