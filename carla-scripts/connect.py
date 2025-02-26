import carla

client = carla.Client("10.116.48.5", 2000)

world = client.get_world()

themap = world.get_map()
