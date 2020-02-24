global lastTicket


def is_ticket_lucky(ticket):
    ticket = str(ticket)

    if len(ticket) < 6:
        ticket = ticket.rjust(6, "0")

    first_triad = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
    second_triad = int(ticket[3]) + int(ticket[4]) + int(ticket[5])

    if first_triad == second_triad:

        return True

    else:

        return False


def lucky(ticket):

    if is_ticket_lucky(ticket) and is_ticket_lucky(lastTicket):

        return 'Счастливый'

    else:

        return 'Несчастливый'
