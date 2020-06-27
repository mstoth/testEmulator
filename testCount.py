from testEmulator import *
em=Emulator()
em.loadProgram("count.asm")  # this is our program we want to test
em.pc = 17 # this is just an arbitrary starting location
em.memory[17]='500'
em.step(1)
assert(em.output_stream[0]=='001')
