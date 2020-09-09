#!/usr/bin/env python3

import memory
import processor
import json

def main():
    # Create a new memory
    mem = memory.LinearMemory(32)

    # Load instructions to memory

    # Start executing instructions using the processor
    processor.SuperSimpleComputer(mem)

    # Save memory to file
    # mem_f = open("output_memory.json")
    # json.dump(mem.memory, mem_f)


if __name__ == "__main__":
    main()