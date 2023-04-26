import random

class BankQueue:
    def __init__(self):
        self.queue = []

    def add_customer(self, customer):
        self.queue.append(customer)

    def remove_customer(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def print_queue(self):
        print("Bank Queue:")
        for i, customer in enumerate(self.queue):
            print(f"{i+1}. {customer.name} ({customer.business})")

class Customer:
    def __init__(self, name, business):
        self.name = name
        self.business = business

customers = [
    Customer("Alice", "Deposit"),
    Customer("Bob", "Withdrawal"),
    Customer("Charlie", "Loan"),
    Customer("Dave", "Deposit"),
    Customer("Eve", "Withdrawal")
]

queue = BankQueue()

# Randomly add customers to the queue
for i in range(10):
    customer = random.choice(customers)
    queue.add_customer(customer)

# Print the initial queue
queue.print_queue()

# Simulate serving customers
while len(queue.queue) > 0:
    print("Now serving:")
    customer = queue.remove_customer()
    print(f"{customer.name} ({customer.business})")
    queue.print_queue()
