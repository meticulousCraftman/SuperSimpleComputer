#!/usr/bin/env python3

import json
from loguru import logger

class SimpleLoader:

    def __init__(self, ssmc_file, memory, offset=0):
        
        with open(ssmc_file) as machine_code_file:
            # Load the machine code from file
            machine_code = json.load(machine_code_file)

            # Insert machine code in memory
            i = 0
            for abyte in machine_code:
                memory.memory[offset + i] = machine_code[i]
                i += 1
            
        logger.success(f"Loaded machine code from {ssmc_file} into memory.")
