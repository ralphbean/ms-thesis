#!/usr/bin/python
import sys
sys.path.append('/home/ralph/thesis/pga/chaos_control_ga')
import metrics as mtr


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print "Usage:   ./ga.py <ID> <step> <max_steps>"
        sys.exit(1)

    ID = sys.argv[1]
    i = float(sys.argv[2])
    n = float(sys.argv[3])
    if ID[0] == str(1):
        step = ((i/n) * 15)**1.5 - 29
    else:
        step = (i/n) * 4 - 2

    i_str = mtr.get_inverse_string(ID)(step)
    #i_str = i_str.replace('*', '\*')
    print i_str
