#!/usr/bin/env python2
import sys
sys.path.insert(0, '../pda/')

from pda import PDA
# PDA which which matches zero or more 'a's, followed by the same
# number of 'b's (accepting by final state)

pda = PDA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'a', 'b'},
    stack_symbols={'0', '1'},
    transitions={
        'q0': {
            'a': [{'0': ('q1', ['1', '0'])}],  # transition pushes '1' to stack
            '': [{'0': ('q3', ['0'])}]
        },
        'q1': {
            'a': [{'1': ('q1', ['1', '1'])}],
            'b': [{'1': ('q2', [])}]  # transition pops from stack
        },
        'q2': {
            'b': [{'1': ('q2', [])}],
            '': [{'0': ('q3', ['0'])}]  # transition does not change stack
        }
    },
    initial_state='q0',
    initial_stack_symbol='0',
    final_states={'q3'}
)

print(pda.validate_input('ab'))
