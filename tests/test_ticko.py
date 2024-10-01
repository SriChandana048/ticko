
from ticko import core

def test_create_ticket():
    title = 'feat: build bird skeleton'
    description = "Design the birds' skeletons and rig the models"
    ticket = core.create(title, description)
    assert core.tickets[0] == ticket


def test_delete_ticket():
    title = 'feat: build bird skeleton'
    description = "Design the birds' skeletons and rig the models"
    ticket = core.create(title, description)
    n_tickets = len(core.tickets)
    deleted_ticket = core.delete(ticket.id)
    n_tickets_after_deletion = len(core.tickets)
    assert deleted_ticket == ticket
    assert n_tickets_after_deletion == n_tickets - 1
