from app import gmaps

legal_event_types = ['leisure', 'active', 'food', 'other']

class Event:
	def __init__(self, name, location, event_type):
		self.name = name
		self.location = location

		if event_type in legal_event_types:
			self.event_type = event_type
		else:
			raise Exception('Illegal event type')

	def __str__(self):
		return 'Name: {0}\nLocation: {1}\nEvent Type: {2}'.format(self.name, self.location, self.event_type)

def get_events(location):
	pass