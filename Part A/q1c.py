def fix_message_data(data: bytes) -> bytes:
    """
    Implement this function to return the "fixed" message content. This message
    should have minimal differences from the original message, but should pass
    the check of `msgcheck`.

    The fix in this file should be *different* than the fix in q1b.py.

    :param data: The source message data.
    :return: The fixed message data.
    """
    #this is a special edge case, where the message is two bytes or less. 
    if len(data)<3:
        return bytes([0x0,0x8c])
    data_list= list(data)
    #if well change the number of bytes were gonna check to zero, and the respected result of the xor to 0x8c, we'll always get a valid message
    data_list[0]=0
    data_list[1]=0x8c
    return bytes(data_list)


def fix_message(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    fixed_data = fix_message_data(data)
    with open(path + '.fixed', 'wb') as writer:
        writer.write(fixed_data)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    fix_message(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
