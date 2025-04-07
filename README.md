# CARLA-SUMO-OMNET++ Co-Simulation Platform

## Note

We are using [InstantVeins](https://veins.car2x.org/documentation/instant-veins/) as a component of the cosimulation. Please make sure the instantveins and Carla in the same network. One way to do that is using the "Bridged Adapter" network mode in VirtualBox. 

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


# Frequent issues
## Increasing InstantVeins VM size

[InstantVeins](https://veins.car2x.org/documentation/instant-veins/) uses 20GB of virtual storage, which might not be sufficient as you are developing new things. We can extend the virtual disk space as our project need grows. 

It is a two step process. 

### Increase VirtualBox virtual drive space

1. Navigate to **Tools -> Media** in the VirtualBox Manager interface.

2. Select the _instant-veins*.vdi_ file in **Hard disks** tab. 

3. Increase the size from the **Attributes** tab and apply. 

Note: _the size slider will be grayed out if the VM is already running. You need to power off the VM completely to make this change._

### Extend the filesystem to utilize the increased space

1. Now run the InstantVeins virtual machine and log-in.

2. Use **cfdisk** tool to extend the free space. [what is cfdisk](https://cfdisk.com/#:~:text=Example%203%3A%20Resizing%20a%20Partition)

```
sudo cfdisk

resize

write

quit
```

3. Install _lvm2_ package. We need a tool `resize2fs`. Command - `sudo apt install lvm2`

4. Run `sudo resize2fs /dev/sda1` 

Check that the disk is extended. Command - `df -h`
