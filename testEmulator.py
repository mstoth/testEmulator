import unittest

class Emulator:
    pc = 0
    acc = 0 # accumulator
    inst = '000' # instruction register
    memory = ['000' for i in range(100)]
    output_stream = []
    istream = 0 # points to next input value
    # input_stream = ['004', '005']
    input_stream = ['002','002','002','002','002','002']
    meaning = {0:"copy input card       ",
               1:"clear and add         ",
               2:"add                   ",
               3:"test accumulator      ",
               4:"shift                 ",
               5:"copy to output        ",
               6:"store acc into cell   ",
               7:"subtract              ",
               8:"jump                  ",
               9:"halt                  "}
    
    
    def __init__(self):
        # use for simple addition program
##        self.pc = 19
##        self.memory = ['000' for i in range(19)]
##        self.memory.extend(['034','035','134','235','636','536','900'])
##        self.memory.extend(['000' for i in range(100-len(self.memory))])
##        self.istream = 0
##        self.memory[0]='001'
        # use for improved Nim game
        self.pc = 52
        self.output_stream = []
        self.memory = ['001','001','002','003','000','000','000','000','000','000',
                       '003','002','002','003','013','000','000','013','004','100',
                       '001','001','001','003','000','000','000','000','000','000',
                       '001','001','002','002','000','000','000','000','000','000',
                       '000','000','000','000','000','000','000','000','000','000',
                       '000','000']
        self.memory.extend(['015','114','715','614','617','514','718','362','617',
                            '858','115','410','217','219','667','100','616',
                            '516','114','716','614','514','952'])
        self.memory.extend(['000' for i in range(100-len(self.memory))])
        self.istream = 0
        self.memory[0]='001'
        self.inst = '000'
        self.acc = 0
        self.input_stream = ['002','002','002','002','002','002']


    def reset(self):
        # use for simple addition program
##        self.pc = 19
##        self.memory = ['000' for i in range(19)]
##        self.memory.extend(['034','035','134','235','636','536','900',])
##        self.memory.extend(['000' for i in range(100-len(self.memory))])
##        self.istream = 0
##        self.output_stream=[]
##        self.inst = '000'
##        self.acc = 0
        # use for improved Nim game
        self.pc = 52
        self.memory = ['001','001','002','003','000','000','000','000','000','000',
                       '003','002','002','003','013','000','000','013','004','100',
                       '001','001','001','003','000','000','000','000','000','000',
                       '001','001','002','002','000','000','000','000','000','000',
                       '000','000','000','000','000','000','000','000','000','000',
                       '000','000']
        self.memory.extend(['015','114','715','614','617','514','718','362','617',
                            '858','115','410','217','219','667','100','616',
                            '516','114','716','614','514','952'])
        self.memory.extend(['000' for i in range(100-len(self.memory))])
        self.istream = 0
        self.output_stream = []
        self.memory[0]='001'
        self.inst = '000'
        self.acc = 0
        self.input_stream = ['002','002','002','002','002','002']

    def dump(self):
        print(self.pc,'\t',self.acc,'\t',self.inst,'\t',self.meaning[(int(self.inst[0]))],'\t',
              self.input_stream[self.istream % len(self.input_stream)],'\t',self.output_stream,'\n')
        for i in range(10):
            if i==0:
                line="00: "
            else:
                line=str(i*10)+": "
            for j in range(10):
                line=line+ ' '+self.memory[i*10+j]
            print(line)


    def read(self):
        if self.istream < len(self.input_stream):
            inst = self.input_stream[istream]
            self.istream = self.istream + 1
            return true
        else:
            return false

    def copy_cell_to_output(self,adr):
        # copies contents of memory cell 'adr' to output
        self.output_stream.append(self.memory[adr])

    def copy_input_to_cell(self,cell):
        # copies input to memory cell
        self.memory[cell]=self.input_stream[self.istream]
        self.istream = self.istream + 1 

    def clear_and_add(self,cell):
        # clears accumulator and adds contents of cell to accumulator
        self.acc = int(self.memory[cell])

    def add(self,cell):
        # adds contents of cell to accumulator
        self.acc += int(self.memory[cell])

    def move(self,cell):
        # moves bug to cell (program counter)
        self.pc = int(cell)

    def shift(self,left,right):
        # shifts left then right
        self.acc = self.acc * pow(10,left)
        self.acc = int(self.acc % 1000)
        self.acc = self.acc / pow(10,right)
        self.acc = int(self.acc % 1000)

    def copy_to_output(self,cell):
        self.output_stream.append(self.memory[cell])

    def copy_acc_into_cell(self,cell):
        self.memory[cell] = str(self.acc).zfill(3)

    def subtract_contents_of_cell(self,cell):
        self.acc = self.acc - int(self.memory[cell])

    def call(self,cell):
        self.memory[99]=str(800+self.pc)
        self.pc = cell

    def fetch(self):
        self.inst = self.memory[self.pc]
        self.pc = self.pc + 1

    def decode(self):
        op = int(self.inst[0])
        adr = int(self.inst[1])*10 + int(self.inst[2])
        
        if op == 0:
            # copy input card
            self.copy_input_to_cell(adr)
        elif op == 1:
            # clear and add
            # print(adr)
            self.clear_and_add(adr)
        elif op == 2:
            # add
            self.add(adr)
        elif op == 3:
            # test accumulator (jump)
            # print(op,adr)
            if self.acc < 0:
                self.pc=adr
                print("set pc to ",adr)
        elif op == 4:
            # shift
            self.shift(int(adr/10),adr % 10)
        elif op == 5:
            # output
            self.copy_to_output(adr)
        elif op == 6:
            # store acc into cell
            self.copy_acc_into_cell(adr)
        elif op == 7:
            # subtract
            self.subtract_contents_of_cell(adr)
        elif op == 8:
            # jump (subroutine)
            self.call(adr)
        elif op == 9:
            # stop
            self.pc=adr
            # print("done")
        else:
            # error
            print("error")

    def step1(self,first = False):
        self.fetch()
        self.decode()
        if self.istream >= len(self.input_stream):
            self.istream = len(self.input_stream) - 1
        if first:
            print(self.pc-1,'\t',self.acc,'\t',self.inst,'\t',self.meaning[(int(self.inst[0]))],'\t',
              self.input_stream[0],'\t',self.output_stream)
        else:
            print(self.pc-1,'\t',self.acc,'\t',self.inst,'\t',self.meaning[(int(self.inst[0]))],'\t',
              self.input_stream[self.istream],'\t',self.output_stream)

    def step(self,n):
        print("\npc\tacc\tinst\tmeaning                 \tinput\toutput")
        for i in range(n):
            self.step1(i==0)
            
        
        
class TestEmulator(unittest.TestCase):

    def test_PC(self):
        em = Emulator()
        # self.assertEqual(em.pc,19,"pc incorrect") ## for simple addition program
        self.assertEqual(em.pc,52,"pc incorrect") ## for improved Nim program

    def test_read(self):
        # reads the next input value
        em = Emulator()
        self.assertTrue(em.read)
        self.assertTrue('034',em.inst)

    def test_copy_cell_to_output(self):
        # write memory cell to output
        em = Emulator()
        self.assertEqual(0,len(em.output_stream))
        em.copy_cell_to_output(0)
        self.assertEqual(1,len(em.output_stream))
        self.assertEqual('001',em.output_stream[0])

    def test_copy_input_to_cell(self):
        # write input to cell
        em = Emulator()
        em.copy_input_to_cell(19) # input has '002'
        self.assertEqual('002',em.memory[19])
        
    def test_clear_and_add(self):
        em = Emulator()
        em.memory[19]=1
        em.clear_and_add(19)
        self.assertEqual(1,em.acc)

    def test_add(self):
        em = Emulator()
        em.add(0)
        self.assertEqual(1,em.acc)

    def test_move(self):
        em = Emulator()
        em.move(19)
        self.assertEqual(19,em.pc)

    def test_shift(self):
        em = Emulator()
        em.acc = 1
        em.shift(1,0)
        self.assertEqual(10,em.acc)
        em.shift(0,1)
        self.assertEqual(1,em.acc)
        em.shift(4,0)
        self.assertEqual(0,em.acc)
        
    def test_copy_to_output(self):
        em = Emulator()
        em.copy_to_output(0)
        self.assertEqual('001',em.output_stream[0])

    def test_copy_acc_into_cell(self):
        em = Emulator()
        em.acc = 2
        em.copy_acc_into_cell(2)
        self.assertEqual('002',em.memory[2])

    def test_subtract_contents_of_cell(self):
        em = Emulator()
        em.acc = 2
        em.subtract_contents_of_cell(0)
        self.assertEqual(1,em.acc)

    def test_accumulator(self):
        print("test accumulator")
        em = Emulator()
        em.inst='361'
        em.acc=-1
        em.decode()
        self.assertEqual(61,em.pc)
        
    def test_call(self):
        em = Emulator()
        em.pc = 1
        em.call(12)
        self.assertEqual(em.pc,12)
        self.assertEqual(em.memory[99],'801')

    def test_fetch(self):
        em = Emulator()
        em.fetch()
        # self.assertEqual(em.inst,'034') ## for simple addition program
        self.assertEqual(em.inst,'015')  ## for improved Nim program


    def test_length_of_memory(self):
        em = Emulator()
        self.assertEqual(100,len(em.memory))

    def test_input(self):
        em = Emulator()
        # self.assertEqual(em.input_stream[em.istream],'004')
        self.assertEqual(em.input_stream[em.istream],'002')
                
    def test_step(self):
        em = Emulator()
        #  self.assertEqual(em.pc,19)  ## for simple addition program
        self.assertEqual(em.pc,52)  ## for improved Nim program
        em.step1()
        # self.assertEqual(em.pc,20) ## for simple addition program
        self.assertEqual(em.pc,53) ## for improved Nim program
        self.assertEqual(em.inst,'015')
        self.assertEqual(em.memory[0],'001')
        em.reset()
        self.assertEqual(em.pc,52) ## for improved Nim program

        em.dump()
        print("\n")
        em.step(75)
        em.dump()

if __name__ == '__main__':
    unittest.main()
