def fix_message_data(data: bytes) -> bytes:
    """
    Implement this function to return the "fixed" message content. This message
    should have minimal differences from the original message, but should pass
    the check of `msgcheck`.

    :param data: The source message data.
    :return: The fixed message data.
    """
    #this is a special edge case, where the message is two bytes or less. 
    if len(data)<3:
        return bytes([0x8c,0x8c])
    data_list= list(data)
    # the first bytes is indcating the number of bytes were gonna check (excluding the first two bytes), but this cannot exceed the len of the message itself. 
    length = min(len(data_list),data_list[0]+2)
    expected_xor = 0x8c
    #here were xoring each byte in the message (in the given length above), and xoring this whith 0x8c 
    for i in range(2, length):
        expected_xor = expected_xor ^ data_list[i]
    #checking if the result we got is equal to the second byte in the message. if not, we are going to fix it by changing the second byte to be as expected.
    if(data_list[1] != expected_xor):
        data_list[1]= expected_xor
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
