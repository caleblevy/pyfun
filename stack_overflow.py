'''
Writes a python file that, when executed, will produce a stack overflow by sheer number of function calls.
'''

N = 2048
prog_start = '''a = 2


def double0(x):
    return x+x

'''
def_list = []
for I in range(N):
    string = '''
def double%s(N):
    return double%s(N)

''' %(str(I+1),str(I))
    def_list.append(string)

prog = [prog_start]
prog.extend(def_list)

prog_end = '''
b = double%s(a)
'''%str(I+1)
prog.append(prog_end)
prog_text = ''.join(prog)

if __name__ == '__main__':
    with open('rec.py','w') as f:
        f.write(prog_text)