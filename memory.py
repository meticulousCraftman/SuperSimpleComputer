#!/usr/bin/env python3

from loguru import logger

class LinearMemory:
    
    def __init__(self, size):
        
        # Create a fixed size array
        self.memory = []

        # Append all zeros in memory
        for x in range(size):
            self.memory.append(0)
        
        logger.debug(f"Created memory of size {len(self.memory)}")
    
    def __setitem__(self, key, value):
        self.memory[key] = value
    
    def __getitem__(self, key):
        return self.memory[key]
    
    def show(self):
        print(f"State of memory -> {self.memory}")