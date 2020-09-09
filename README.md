# Super Simple Computer
This project simulates the Instruction Set of a hypothetical computer.

## How to run this project?
```
$ pip3 install -r requirements.txt
$ python3 runner.py
```

Basic components that are required:
  1. Processor
  2. Memory
  3. Loader -> Load instructions from file to memory
  4. Assembler -> Converts program written in text format to binary
  5. Runner -> Setup different parts of the program and run the processor.


Currently this project only has one processor and that is **SuperSimpleComputer**, here is some more information about the same:
  - Instruction Size = 32 bit (4 Byte)
  - Word Size = 32 bit (4 Byte)
  - Uses Linear Memory
  - Byte Addressable Memory, each address only stores 1 Byte of information

## Instruction Format

Each instruction is 32 bit long.

```
|  0000 0000 |     0000 0000     |      0000 0000     |      0000 0000     |
|--------------------------------------------------------------------------|
|   OP Code  | Dest. Memory Addr | Operand 1 Mem Addr | Operand 2 Mem Addr |
```

Instruction opcode table:
  - No instruction: 0
  - ADD : 1
  - SUB : 2
  - MUL : 3
  - DIV : 4

## Super Simple Assembly (.ssa files)
These are simple text files that contain assembly instructions for Super Simple Computer. These instructions are processed by the assembler to generate machine code that can be executed by the computer.

Each instruction takes 1 line

## Filenames
  - **.ssa** -> Super Simple Assemnbly file. Text file that contains assmebly instructions for Super Simple Computer (SSC).