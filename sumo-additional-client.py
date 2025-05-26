import sys
import os

# ==================================================================================================
# -- find traci module -----------------------------------------------------------------------------
# ==================================================================================================

if 'SUMO_HOME' in os.environ:
    sys.path.append(os.path.join(os.environ['SUMO_HOME'], 'tools'))
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")


import traci
import time

sumo_binary = "sumo-gui"

traci.init(host="localhost", port=49286)

traci.setOrder(3)

veh_id = "0"

while veh_id not in traci.vehicle.getIDList():
    traci.simulationStep()

try: 
    # Disable all safety constraints and stop sign behavior
    traci.vehicle.setSpeedMode(veh_id, 0b0000000)                 # Disable all safety checks
    # traci.vehicle.setIgnoreJunctionBlocks(veh_id, True)           # Don't stop for blocked intersections
    traci.vehicle.setSpeed(veh_id, 10)                            # Force speed to move forward

    # Run simulation for N steps
    while True:
        traci.simulationStep()

finally:
    traci.close()

