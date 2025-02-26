# CARLA-SUMO-OMNET++ Co-Simulation Platform

## Running the Cosimulation

Step 1: Run Carla

Step 2: Launch `sumo_launchd.py` script. Run command: `./sumo_launchd.py -vv -c sumo-gui`

Step 3: Launch `omnetpp.ini` from the project (`opp_run` command or from OMNeT++ IDE)

Step 4: Change into `carla-scripts` directory. Run the `run_synchronization.py` script. The command is given below.

```
python3 run_synchronization.py --carla-host 10.116.48.5 --sumo-host localhost --sumo-port 49286 --step-length 0.1 --client-order 2 --town-map Town05 --tls-manager sumo examples/Town05.sumocfg --debug
```

Note: `--carla-host` command is followed by the IP address of the computer where CARLA is running. 

Please use the Github Issues or reach out to [Minhaj Ahmad](https://minhaj6.github.io).



This co-simulation platform uses a lot of open-source work done by Carla developers (Carla-Sumo Co-SIM) and Dr. Christoph Sommer (Veins)

