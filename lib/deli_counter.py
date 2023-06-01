katz_deli = []

def line(queue):
    if len(queue) == 0:
        print("The line is currently empty.")
    else:
        message = 'The line is currently:'
        for index, person in enumerate(queue):
            customer = f" {index + 1}. {person}"
            message = message + customer
        print(message)

def take_a_number(queue, new_customer):
    queue.append(new_customer)
    print(f"Welcome, {new_customer}. You are number {len(queue)} in line.")

def now_serving(queue):
    if len(queue) == 0:
        print ("There is nobody waiting to be served!")
    else:
        print (f"Currently serving {queue[0]}.")
        del queue[0]