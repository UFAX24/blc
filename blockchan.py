# initializing our blockchain list
blockchain = []


def get_last_blockchain_value():
    """ returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    return float(input('Your transaction amount please: '))


def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-'*20)


def verify_chain():
    block_index = 0
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            block_index += 1
            continue
        if blockchain[block_index][0] == blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


waiting_for_input = True


while waiting_for_input:

    print('Please Choose: ')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()

    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input invalid')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break

    # print('Choice Registered')

else:
    print('User Left')

print('Done')