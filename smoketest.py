import contextlib
import os
import sys

from infosec import core


TEST_COMMAND = 'echo "I am g`whoami`!"; exit'
COMMAND_RESULT = 'I am groot!'


@core.smoke.smoke_check
def check_q1():
    with core.in_directory('q1'):
        command = f'`python q1.py {repr(TEST_COMMAND)}`'
        result = core.execute([sys.executable, 'q1.py', TEST_COMMAND])
        if COMMAND_RESULT not in result.stdout:
            core.smoke.error(f'Failed running a root command shell with {command}')
        else:
            core.smoke.success(f'{command} seems cool')


@core.smoke.smoke_check
def check_q2a():
    with core.in_directory('q2'):
        if os.path.isfile('core'):
            os.remove('core')
        core.execute([sys.executable, 'q2a.py'])
        if not os.path.exists('core'):
            core.smoke.error('Running q2a.py did not generate a `core` file')
        else:
            core.smoke.success('Generated a `core` file with q2a.py')


@core.smoke.smoke_check
def check_q2b():
    with core.in_directory('q2'):
        command = f'`echo {repr(TEST_COMMAND)} | python q2b.py`'
        result = core.execute(
            [sys.executable, 'q2b.py'], TEST_COMMAND.encode())
        if COMMAND_RESULT not in result.stdout:
            core.smoke.error(f'Failed running a root command shell with {command}')
        else:
            core.smoke.success(f'{command} seems cool')


@contextlib.contextmanager
def question_context(name):
    try:
        core.smoke.highlight(name)
        yield
    except Exception as e:
        core.smoke.error(e)
    finally:
        # Add a new-line after each question
        print()


def smoketest():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    with question_context('Question 1'):
        check_q1()
        core.smoke.check_if_nonempty('q1/q1.txt')

    with question_context('Question 2A'):
        check_q2a()
        core.smoke.check_if_nonempty('q2/q2a.txt')

    with question_context('Question 2B'):
        check_q2b()
        core.smoke.check_if_nonempty('q2/q2b.txt')
        core.smoke.check_if_nonempty('q2/shellcode.asm')


if __name__ == '__main__':
    smoketest()
