import functools

MINING_REWARD = 10

genesis_block = {
    "previous_hash": "",
    "index": 0,
    "transactions": [],
}
blockchain = [genesis_block]
open_transactions = []
owner = "Max"
participants = {"Max"}


def hash_block(block):
    return "-".join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [
        [tx["amount"] for tx in block["transactions"] if tx["sender"] == participant]
        for block in blockchain
    ]
    open_tx_sender = [
        [tx["amount"] for tx in open_transactions if tx["sender"] == participant]
    ]
    tx_sender = tx_sender + open_tx_sender
    amount_sent = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
        tx_sender,
        0,
    )

    tx_recipient = [
        [tx["amount"] for tx in block["transactions"] if tx["recipient"] == participant]
        for block in blockchain
    ]
    amount_received = functools.reduce(
        lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0,
        tx_recipient,
        0,
    )

    return amount_received - amount_sent


def get_last_blockchain_value():
    """Returns the last value of the current blockchain"""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction["sender"])
    return sender_balance >= transaction["amount"]


def add_transaction(recipient, sender=owner, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain.

    Arguments:
        :sender: The sender of the coins
        :recipient: The recipient of the coins
        :amount: The amount of coins sent with the transactions (default = 1.0)
    """
    transaction = {"sender": sender, "recipient": recipient, "amount": amount}
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_blocked = hash_block(last_block)
    reward_transaction = {
        "sender": "Mining",
        "recipient": owner,
        "amount": MINING_REWARD,
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        "previous_hash": hashed_blocked,
        "index": len(blockchain),
        "transactions": copied_transactions,
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    """Returns the input of the user(a new transaction amount) as a float."""
    tx_recipient = input("Enter the sender of the transaction:")
    tx_amount = float(input("Your transaction amount please: "))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input("Your choice: ")
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print("Outputting Block")
        print(block)


def verify_chain():
    """Verify the current blockchain and return True if it's valid, False otherwise"""
    for index, block in enumerate(blockchain):
        if index == 0:
            continue
        if block["previous_hash"] != hash_block(blockchain[index - 1]):
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    print("Please choose")
    print("1: Add a new transaction value")
    print("2: Mine a new Block")
    print("3: Output the blockchain blocks")
    print("4: Output participants")
    print("5: Check transaction validity")
    print("h: Manipulate the chain")
    print("q: Quit")
    user_choice = get_user_choice()
    if user_choice == "1":
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add the transaction amount to the blockchain
        if add_transaction(recipient, amount=amount):
            print("Added transaction!")
        else:
            print("Transactions failed!")
        print(open_transactions)
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":
        print_blockchain_elements()
    elif user_choice == "4":
        print(participants)
    elif user_choice == "5":
        if verify_transactions():
            print("All transactions are valid")
        else:
            print("There are invalid transactions!")
    elif user_choice == "h":
        # Make sure that you don't try to "hack" the bockchain if it's empty
        if len(blockchain) >= 1:
            blockchain[0] = {
                "previous_hash": "",
                "index": 0,
                "transactions": [
                    {"sender": "Chris", "recipient": "Max", "amount": 100.00}
                ],
            }
    elif user_choice == "q":
        waiting_for_input = False
        # break
    else:
        print("Input was invalid, please pick a value from the list!")
    if not verify_chain():
        print_blockchain_elements()
        print("Invalid blockchain!")
        break
    print("Balance of {}:{:6.2f}".format("Max", get_balance("Max")))
else:
    print("User left")
print("Done!")
