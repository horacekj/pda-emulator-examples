#!/usr/bin/env python2
import sys
sys.path.insert(0, '../pda/')

from pda import PDA

# This pda loop infinitely.

pda = PDA(
    states={'q0', 'q1'},
    input_symbols={'a', 'b'},
    stack_symbols={'0'},
    transitions={
        'q0': {
            '': [{'0': ('q0', ('0',))}]
        },
    },
    initial_state='q0',
    initial_stack_symbol='0',
    final_states={'q1'}
)

print(pda.validate_input('ab'))
