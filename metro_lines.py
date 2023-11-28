class train(object):
	# Defines and initializes the train objects
	# when the user adds a train to the system
	def __init__(self, id, line_name, start):
		self.id = id
		self.line = line_name
		self.pos = start
		self.dir = 1


def plan_trip(start, stop, stations, visited):
	# Recursively searches through the stations dictionary
	# and outputs a list of destinations, that must be filtered
	# by another function before display
	for item in stations[start]:
		if item == stop:
			
			visited.append(item)

		if item not in visited:
			
			visited.append(item)
			
			plan_trip(item, stop, stations, visited)

			if stop not in stations[item] and stop not in visited:
				visited.remove(item)

	if stop not in visited:
		visited = []

	return visited

	
def display_lines(dict):
	# displays the line names
	for line in dict.keys():
		print('\t {}'.format(line))



def filter_trip(trip, start, destination):
	# Filters the list provided by the plan_trip function into a final trip
	# that gets displayed to the user

	for i in range(10):
		flag = False
		strip = False
		for stop in trip:

			if stop != start and flag == False:
				trip.remove(stop)
			elif stop == start:
				flag = True
			elif stop == destination:
				strip = True
			elif strip == True:
				trip.remove(stop)

	return trip


def display_stations(dict):
	# Displays station names
	for station in dict.keys():
		print('\t {}'.format(station))
	

def display_trains(list):
	# This function accesses all of the train objects within the passed list
	# and displays their attributes
	for train in list:

		print('*** Information for Train {} ***'.format(train.id))
		print('\t Line: {}'.format(train.line))
		print('\t Current position: {}'.format(train.pos))

def sort_line(line, color):
	# sorts the stations on a given line in order to be passed to 
	# the step function
	connections = []
	count = 0
	for i in range(len(line[color])):

		for key in line[color].keys():

			if len(line[color][key])== 1 and key not in connections and \
			count % 2 == 0:

				connections.append(key)
				connections.append(line[color][key][0])
				count += 1

			elif len(line[color][key]) == 2:

				for x in range(2):

					if key in connections:

						if line[color][key][x] not in connections:

							connections.append(line[color][key][x])
	return connections

def step(trains, lines):

	for train in trains:

		stops = sort_line(lines, train.line)

		if stops.index(train.pos) + 1 == len(stops):
			train.dir = 0
		elif stops.index(train.pos) == 0:
			train.dir = 1

		if train.dir == 1:
			new_pos = stops[stops.index(train.pos) + 1]
		elif train.dir == 0:
			new_pos = stops[stops.index(train.pos) - 1]

		print('{} has moved from {} to {}'.format(train.id, train.pos, new_pos))
		
		train.pos = new_pos

def run_metro_system(name):
	# This function serves as the main loop that the user uses
	# The function handles user input and displays or calls ouput functions
	turn = input('[{}] >>> '.format(name))
	trains = []
	stations = {}
	lines = {}

	while turn != 'exit':

		command = turn.split()

		if command[0] == 'create':

			if command[1] == 'train':
				
				trains.append(train(command[2], command[3], command[4]))

			elif command[1] == 'station':

				if command[2] in stations.keys():

					print('This station has already been created')

				else:

					stations[command[2]] = []

		elif command[0] == 'connect':
			color = command[4]
			stations[command[2]].append(command[3])
			stations[command[3]].append(command[2])

			if color not in lines.keys():
				lines[color] = {}

			if command[2] not in lines[color].keys():
				lines[color][command[2]] = [command[3]]

			else:
				lines[color][command[2]].append(command[3])

			if command[3] not in lines[color].keys():
				lines[color][command[3]] = [command[2]]

			else:
				lines[color][command[3]].append(command[2])
			
				
		elif command[0] == 'step':

			step(trains, lines)

			

		elif command[0] == 'display':

			if command[1] == 'stations':
				display_stations(stations)

			elif command[1] == 'trains':
				display_trains(trains)

			elif command[1] == 'lines':
				display_lines(lines)


		elif command[0] == 'plan':

			init_trip = plan_trip(command[2], command[3], stations, [command[2]])

			final_trip = filter_trip(init_trip, command[2], command[3])

			for key in lines.keys():

				if command[2] in lines[key]:

					begin = 'Start on the {} --> '.format(key)

			itinerary = begin + ' --> '.join(final_trip)

			print(itinerary)

		turn = input('[{}] >>> '.format(name))

if __name__ == '__main__':
	system_name = input('>>> ')
	run_metro_system(system_name)
