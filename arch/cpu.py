"""CPU functionality."""

import sys

LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.pc = 0
        self.reg = [0] * 8
        self.ram = [0] * 256

        self.running = False

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        pass
        # running loop
        self.running = True

        while self.running:
            # fetch
            inst = self.ram[self.pc]
            opa = self.ram[self.pc + 1]
            opb = self.ram[self.pc + 2]

            # decode instruction size
            opcode_size = (inst >> 6) + 1

            
            # decode
            if inst == HLT:
                # execute
                self.running = False
            
                # decode
            elif inst == LDI:
                # execute
                # get the reg index.
                reg_index = opa
                # get the num.
                num = opb
                # put the number in the registers list at the index of reg_index
                self.reg[reg_index] = num
                

            # decode
            elif inst == PRN:
                # execute
                # get reg index.
                reg_index = opa
                print(self.reg[reg_index])
           

            # decode
            else:
                print(f"Unknown instruction {inst}")
                self.running = False


            self.pc += opcode_size

if __name__ == "__main__":
    
    """Main."""

    import sys

    cpu = CPU()

    cpu.load()
    cpu.run()