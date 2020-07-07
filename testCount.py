from testEmulator import *
em=Emulator()
em.loadProgram("count.asm")  # this is our program we want to test
em.pc = 17 # this is just an arbitrary starting location
em.step(38)
assert(em.output_stream[0]=='001')
assert(em.output_stream[1]=='002')
assert(em.output_stream[2]=='003')
assert(em.output_stream[3]=='004')
assert(em.output_stream[4]=='005')
assert(em.output_stream[5]=='006')
assert(em.output_stream[6]=='007')
assert(em.output_stream[7]=='008')
assert(em.output_stream[8]=='009')
assert(em.output_stream[9]=='010')

