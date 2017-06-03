"""
Runs tests on python script file passing to it STDIN and reading STDOUT and matching this to expected result.
Usage:

    from test import Tester
    t = Tester(__file__)
    t.test(
'''INPUT''',
'''EXPECTED RESULT''')


"""

import subprocess

def shorten(s):
    MAXLINES = 30
    lines = s.split('\n')
    if len(lines) <= MAXLINES:
        return s
    return '\n'.join(lines[:MAXLINES//2] + ['..(' + str(len(lines) - MAXLINES) + ' lines)..'] + lines[-MAXLINES//2:])

class Tester:
    def __init__(self, file_):
        self.file_ = file_
        self.count = 0

    def test(self, input_, expected):
        whitespacechars = "\n \t"
        input_ = input_.strip(whitespacechars)
        expected = expected.strip(whitespacechars)
        # cp - CompleteProcess
        cp = subprocess.run(['python', self.file_], input = input_, encoding = 'utf-8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if cp.returncode > 0:  # error
            print('TEST FAILED')
            print(cp.stderr)
            return

        output = cp.stdout.strip(whitespacechars)

        if output != expected:
            output = shorten(output)
            expected = shorten(expected)
            input_ = shorten(input_)
            print('TEST FAILED')
            print('                            INPUT')
            print(input_)
            print('                            OUTPUT')
            print(output)
            print('                            EXPECTED')
            print(expected)
        else:
            self.count += 1
            print('TEST ' + str(self.count) + ' SUCCESS')


