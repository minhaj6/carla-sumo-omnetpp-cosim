import carla
import math

def get_sumo_transform(in_carla_transform, extent):
    """
    Returns sumo transform based on carla transform.
    """
    offset = (270.80, 200.32) 
    
    in_location = in_carla_transform.location
    in_rotation = in_carla_transform.rotation

    # From center to front-center-bumper (carla reference system).
    yaw = -1 * in_rotation.yaw
    pitch = in_rotation.pitch
    out_location = (
        in_location.x + math.cos(math.radians(yaw)) * extent.x,
        in_location.y - math.sin(math.radians(yaw)) * extent.x,
        in_location.z - math.sin(math.radians(pitch)) * extent.x
    )
    out_rotation = (in_rotation.pitch, in_rotation.yaw, in_rotation.roll)

    # Applying offset carla-sumo net (not needed here)
    out_location = (out_location[0] + offset[0], out_location[1] - offset[1], out_location[2])

    # Transform to sumo reference system.
    out_transform = carla.Transform(
        carla.Location(out_location[0], -out_location[1], out_location[2]),
        carla.Rotation(out_rotation[0], out_rotation[1] + 90, out_rotation[2])
    )

    return out_transform

def generate_sumo_poly_file():
    client = carla.Client("10.116.48.5", 2000)
    client.set_timeout(10.0)
    world = client.load_world('Town05')

    buildings = world.get_environment_objects(carla.CityObjectLabel.Buildings)

    xml_content = '''<?xml version="1.0" encoding="UTF-8"?>
<additional xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://sumo.dlr.de/xsd/additional_file.xsd">
'''

    for idx, building in enumerate(buildings):
        transform = building.transform
        bb = building.bounding_box
        extent = bb.extent

        # Get SUMO transform for the building
        sumo_transform = get_sumo_transform(transform, extent)

        # Calculate building corners in SUMO coordinates
        corners_local = [
            carla.Location(x=extent.x, y=extent.y),
            carla.Location(x=-extent.x, y=extent.y),
            carla.Location(x=-extent.x, y=-extent.y),
            carla.Location(x=extent.x, y=-extent.y)
        ]

        # Transform corners to SUMO coordinates
        sumo_corners = [sumo_transform.transform(corner) for corner in corners_local]

        # Format shape string
        shape_str = " ".join([f"{corner.x:.2f},{corner.y:.2f}" for corner in sumo_corners])

        xml_content += f'    <poly id="building_{idx}" type="building" color="1.00,0.00,0.00" fill="1" layer="4" shape="{shape_str}"/>\n'

    xml_content += "</additional>"

    with open("network.poly.xml", "w") as f:
        f.write(xml_content)
    print("SUMO network.poly.xml generated successfully!")

if __name__ == "__main__":
    generate_sumo_poly_file()