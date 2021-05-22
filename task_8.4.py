class Ticket:
    def __init__(self, price, destination):
        self.price = price
        self.destination = destination


class Passenger:
    def __init__(self, name, money, need_to_go, tickets):
        self.name = name
        self.money = money
        self.need_to_go = need_to_go
        self.tickets = []

    def show_info(self):
        print(f'passenger {self.name}, money: {self.money}, tickets: {",".join(self.tickets)}')

    def buy_ticket(self, ticket):
        if self.money >= ticket.price:
            self.tickets.append(ticket.destination)
            self.money -= ticket.price
            print('new ticket: to ' + ticket.destination + ', balance: ' + str(self.money))
        else:
            print(f'{self.name}, not enough money to buy a ticket to {ticket.destination}')

    def return_ticket(self, ticket):
        if ticket.destination in self.tickets:
            self.tickets.remove(ticket.destination)
            self.money += ticket.price
            print(f'{self.name}, you returned the ticket to {ticket.destination}, balance: {self.money}')
        else:
            print('error 404...')


pass1 = Passenger('Alice', 5000, 'Novosibirsk', [])
pass2 = Passenger('Daniel', 2400, 'Moscow', [])
pass1.show_info()
pass2.show_info()
tick1 = Ticket(3000, 'Novosibirsk')
tick2 = Ticket(1000, 'Tomsk')
tick3 = Ticket(2000, 'Moscow')
pass1.buy_ticket(tick1)
pass2.buy_ticket(tick2)
pass2.return_ticket(tick2)
pass2.buy_ticket(tick3)
pass1.show_info()
pass2.show_info()
