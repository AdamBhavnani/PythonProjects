import random
import argparse
import functools

from PIL import Image

# Colors for dungeon cells
COLOR_EMPTY = (28, 15, 0)
COLOR_TUNNEL = (185, 168, 125)
COLOR_TREASURE = (217, 217, 217)
COLOR_MONSTER = (164, 8, 2)

def constrained(f, min_value=None, max_value=None):
	"""Helper function to constrain a castin function (e.g. int, float, etc.) to a given range

	Args:
		f (function): casting function
		min_value=None: Optional minimum value to constrain to
		max_value=None: Optional maximum value to constrain to
	"""

	@functools.wraps(f)
	def wrapper(value):
		value = f(value)

		if not min_value is None and value < min_value:
			raise ValueError('%s <= %s' % (min_value, value))
		if not max_value is None and value > max_value:
			raise ValueError('%s <= %s' % (value, max_value))

		return value

	return wrapper

def get_cli_arguments():
	"""Parse the command-line arguments

	Returns:
		(namespace)
	"""

	parser = argparse.ArgumentParser()

	parser.add_argument(
		'-s', '--seed',
		type=int,
		default=None,
		help=''
	)

	parser.add_argument(
		'-W', '--width',
		type=constrained(int, min_value=2),
		default=50,
		help=''
	)
	parser.add_argument(
		'-H', '--height',
		type=constrained(int, min_value=2),
		default=50,
		help=''
	)

	parser.add_argument(
		'-t', '--tunnels',
		type=constrained(int, min_value=1),
		default=20,
		help=''
	)
	parser.add_argument(
		'--max-tunnel',
		type=constrained(int, min_value=2),
		default=float('+inf'),
		help=''
	)
	parser.add_argument(
		'-T', '--treasures',
		type=constrained(int, min_value=1),
		default=1,
		help=''
	)

	parser.add_argument(
		'-M', '--monsters',
		type=constrained(float, min_value=0.0, max_value=1.0),
		default=0,
		help=''
	)

	parser.add_argument(
		'-o', '--output',
		type=str,
		default=None,
		help=''
	)

	return parser.parse_args()

def can_move(x, y, width, height, direction):
	"""Determine if you can move in a direction from a starting location given the bounds of the map

	Args:
		x (int): Starting x position
		y (int): Starting y position
		width (int): Map width
		height (int): Map height
		direction (tuple): The direction of movement
	"""

	return (0 <= x + direction[0] < width) and (0 <= y + direction[1] < height)

def generate_tunnels(width, height, tunnels, max_tunnel_length):
	"""Generate the coordinates of

	Args:
		width (int): Width of the map
		height (int): Height of the map
		tunnels (int): How many tunnels to make
		max_tunnel_length (int): Maximum length of a tunnel

	Returns:
		(bool) False if moving in this direction would put you outside of the map True otherwise
	"""

	# Direction definitions
	NORTH = (0, -1)
	EAST = (1, 0)
	SOUTH = (0, 1)
	WEST = (-1, 0)

	# Direction state change lookup table
	STATES = {
		NORTH: [EAST, WEST],
		EAST: [NORTH, SOUTH],
		SOUTH: [EAST, WEST],
		WEST: [NORTH, SOUTH],
		None: [NORTH, EAST, SOUTH, WEST],
	}

	# Function lookup table for calculating maximum possible travel distance in a direction
	max_length = {
		NORTH: lambda x, y: y,
		EAST: lambda x, y: width - x - 1,
		SOUTH: lambda x, y: height - y - 1,
		WEST: lambda x, y: x
	}

	# Initialize starting state
	direction = None
	x = random.randrange(width)
	y = random.randrange(height)

	# Yield the starting position
	yield (x, y)

	# Produce the specified number of tunnels
	for tunnel in range(tunnels):
		# Choose a random direction from the available directions given the previous direction
		direction = random.choice([dir for dir in STATES[direction] if can_move(x, y, width, height, dir)])

		# Calculate the length of the tunnel to be dug
		tunnel_length = min(max_length[direction](x, y), max_tunnel_length)
		if tunnel_length > 1:
			tunnel_length = random.randrange(1, tunnel_length)

		# Yield the positions of the tunnel
		for offset in range(tunnel_length):
			x += direction[0]
			y += direction[1]

			yield (x, y)

def render(image, positions, color):
	"""Fill a list of pixels with a given color value

	Args:
		image (PIL.Image): Image to render to
		positions (iterable): List of positions
		color (tuple): Color to use for rendering
	"""

	for p in positions:
		image.putpixel(p, color)

def main():
	args = get_cli_arguments()

	random.seed(args.seed)

	positions_tunnels = set(generate_tunnels(args.width, args.height, args.tunnels, args.max_tunnel))

	positions_treasures = random.choices(list(positions_tunnels), k=args.treasures)
	positions_tunnels.difference_update(positions_treasures)

	monster_count = max(1, int(args.monsters * len(positions_tunnels)))

	positions_monsters = random.choices(list(positions_tunnels), k=monster_count)
	positions_tunnels.difference_update(positions_monsters)

	image = Image.new('RGB', size=(args.width, args.height), color=COLOR_EMPTY)

	render(image, positions_tunnels, COLOR_TUNNEL)
	render(image, positions_treasures, COLOR_TREASURE)
	render(image, positions_monsters, COLOR_MONSTER)

	if args.output is None:
		image.show()
	else:
		image.save(args.output)

if __name__ == '__main__':
	main()
