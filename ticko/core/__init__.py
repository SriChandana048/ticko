from dataclasses import dataclass,field
from typing import List

# @dataclass
# class Ticket:
#     id: int
#     title: str
#     description: str
#     tickets: List[List] = field(default_factory=list)
#     def createTicket(self,title:str,description:str):
#         if not any(ticket[1] == title for ticket in self.tickets):
#             new_id = len(self.tickets)+1
#             self.tickets.append([new_id, title, description])
#             print("New Ticket Created")
#         else:
#             print("Ticket Already Exists")
    
#     def ListTickets(self):
#         for ticket in self.tickets:
#             print(ticket)
    
#     def deleteTicket(self,nid):
#         for ticket in self.tickets:
#             if ticket[0]==nid: 
#                 self.tickets.remove(ticket)
#                 print(f'Ticket(id={nid}) is deleted')
#                 return
#         print(f'Ticket(id={nid}) not found')

# ticko1=Ticket(0,"Angry Birds: Skeletons","Build bird skeletons")
# ticko1.createTicket("Angry Birds: Skeletons","Build bird skeletons")
# ticko1.createTicket("Angry Birds: Animation","Build animations")
# ticko1.createTicket("Angry Birds: Effects","Create Effects")
# ticko1.deleteTicket(3)
# ticko1.ListTickets()


import dataclasses as dc

@dc.dataclass(slots=True, kw_only=True)
class Ticket:
    id: int | None = None
    title: str
    description: str

_id_counter = 0
tickets = []

def create(title: str, description: str) -> Ticket:
    global _id_counter
    _id_counter += 1
    ticket = Ticket(id=_id_counter, title=title, description=description)
    tickets.append(ticket)
    return ticket

def list_() -> list[Ticket]:
    return tickets

def delete(id: int) -> Ticket:
    global tickets
    deleted_ticket = next(filter(lambda ticket: ticket.id == id, tickets), None)
    _ = filter(lambda ticket: ticket.id != id, tickets)
    tickets = list(_)
    return deleted_ticket