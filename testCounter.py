from testEmulator import *
em = Emulator()
em.loadProgram("counter.asm")
em.step(10)
assert(em.output_stream[0]=='001')
