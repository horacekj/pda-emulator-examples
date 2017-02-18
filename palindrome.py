#!/usr/bin/env python2
import sys
sys.path.insert(0, '../pda/')

from pda import PDA

# This PDA checks for palindromes of 'a', 'b' and 'c' words.

pda = PDA(
    states={'q0', 'q1', 'q2'},
    input_symbols={'a', 'b', 'c'},
    stack_symbols={'a', 'b', 'c', 'x'},
    transitions={
        'q0': {
            'a': [{
                    # Add 'a' to stack.
                    'x': ('q0', ('a', 'x')),
                    'a': ('q0', ('a', 'a')),
                    'b': ('q0', ('a', 'b')),
                    'c': ('q0', ('a', 'c')),
                  }],
            'b': [{
                    # Add 'b' to stack.
                    'x': ('q0', ('b', 'x')),
                    'a': ('q0', ('b', 'a')),
                    'b': ('q0', ('b', 'b')),
                    'c': ('q0', ('b', 'c')),
                  }],
            'c': [{
                    # Add 'c' to stack.
                    'x': ('q0', ('c', 'x')),
                    'a': ('q0', ('c', 'a')),
                    'b': ('q0', ('c', 'b')),
                    'c': ('q0', ('c', 'c')),
                  }],
            '' : [{
                    # Guess the middle of the word, keep the stack.
                    'x': ('q1', ('x',)),
                    'a': ('q1', ('a',)),
                    'b': ('q1', ('b',)),
                    'c': ('q1', ('c',)),
                  },
                  {
                    # Guess the middle of the word, remove last word from stack
                    #  (to match palindromes of odd length).
                    'x': ('q1', ''),
                    'a': ('q1', ''),
                    'b': ('q1', ''),
                    'c': ('q1', ''),
                  }],
        },

        'q1': {
            # Unwind the stack and check for matching letters.
            'a': [{ 'a': ('q1', '') }],
            'b': [{ 'b': ('q1', '') }],
            'c': [{ 'c': ('q1', '') }],

            # Stack empty -> go to final state.
            # Final state has to transitions -> it fails if some letters are left.
            '' : [{'x': ('q2', ('x',))}]
        },
    },
    initial_state='q0',
    initial_stack_symbol='x',
    final_states={'q2'}
)

tests = ['abba', 'a', 'caca', 'acca', 'abccba', 'aca', 'cbbca', '']

for test in tests:
    print "Testing " + test + " :",
    print(pda.validate_input(test))
