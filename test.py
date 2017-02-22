#!/usr/bin/env python2
import sys
sys.path.insert(0, '../pda/')

from pda import PDA

pda = PDA(
    states={'q0', 'q1', 'q2', 'q3'},
    input_symbols={'0', '1'},
    stack_symbols={'1', '0'},
    transitions={
        'q0': {
            '0': [{'1': ('q1', ('1', '0'))}],
            '': [{'1': ('q1', ('1', '0'))}]
        },
        'q1': {
            '0': [{'1': ('q1', ('1', '1'))}],
            '1': [{'1': ('q2', '')}]
        },
        'q2': {
            '0': [{'1': ('q2', '')}],
            '': [{'0': ('q3', ('0',))}]
        }
    },
    initial_state='q0',
    initial_stack_symbol='0',
    final_states={'q3'}
)

print(pda.validate_input('1100'))
