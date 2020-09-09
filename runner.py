#!/usr/bin/env python3

import memory
import processor
import loader
import json
import sys
from loguru import logger

def main():
    # Create a new memory
    mem = memory.LinearMemory(32)

    # Load instructions to memory
    if len(sys.argv) > 1:
        logger.info(f"Loading {sys.argv[1]} into memory")
        loader.SimpleLoader(sys.argv[1], mem, offset=0)
    else:
        logger.info("No machine code specified to be loaded")

    # Show memory state before execution
    mem.show()

    # Start executing instructions using the processor
    processor.SuperSimpleComputer(mem)

    # Show memory state after execution
    mem.show()


if __name__ == "__main__":
    main()