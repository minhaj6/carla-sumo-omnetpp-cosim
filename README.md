# CARLA-SUMO-OMNET++ Co-Simulation Platform

This environment is tested and verified in Linux and Windows systems. 

## Version: 

- Carla : 0.9.15
- InstantVeins: instant-veins-5.2-i1

## Note

We are using [InstantVeins](https://veins.car2x.org/documentation/instant-veins/) as a component of the cosimulation, for quick setup. Please make sure the instantveins and Carla in the same network. One way to do that is using the "Bridged Adapter" network mode in VirtualBox.

Go to VirtualBox -> Settings -> Networks -> Attached to : Bridged Adapter. 

## Running the Cosimulation

The following videos go through the installation process - 
1. https://youtu.be/FmYy6aTucpQ?si=BtcY1etnvzGCWUxR
2. https://youtu.be/E0PoBPkh720?si=QJvpPN7iW1jc-n7R

Or, 

Step 1: Run Carla in your host computer (Tested using Carla 0.9.15)

Note: If host computer is resource constrained older computer, running carla with `./CarlaUE4.sh -quality-level=Low` might help

Step 2: Launch the InstantVeins VM. 

Step 3: Define `SUMO_HOME` environment variable. Run `echo 'export SUMO_HOME="$HOME/src/sumo"' >> ~/.zshrc`

Step 4: Clone this github repository in your omnet++ workspace. 

Step 5: Launch OMNeT++ IDE. 

Step 6: Import this github repository as a OMNeT++ project. 

Step 7: Launch `sumo_launchd.py` script. Run command: `./sumo-launchd.py -vv -c sumo-gui`. If you want to connect additional SUMO clients for any experimentation or data collection, use the flag `-n` or `--number-of-clients`. If the number of clients is not mentioned, SUMO starts with expectation of two clients (Carla and OMNeT++). Example for starting with 3 clients - `./sumo-launchd.py -vv -c sumo-gui -n 3`.

Step 8: Run simulation on `omnetpp.ini` from the IDE. 

Step 9: Press the run button on the OMNeT++ simulation GUI.

Step 10: Go to `carla-scripts` directory. Run the `run_synchronization.py` script with the following arguments. Change the IP address of `--carla-host` option according to your set-up. 

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
