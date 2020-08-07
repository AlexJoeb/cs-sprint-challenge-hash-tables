#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    result = []
    first_ticket = None

    for ticket in tickets:
        if ticket.source == "NONE":
            first_ticket = ticket
            result.append(ticket.destination)
        else: continue

    def next_flight(ticket):
        for poss in tickets:
            if poss.source == ticket.destination and poss is not ticket:
                if poss.destination != "NONE":
                    result.append(poss.destination)
                    return next_flight(poss)
                else:
                    result.append("NONE")
                    break
                
    next_flight(first_ticket)
    return result