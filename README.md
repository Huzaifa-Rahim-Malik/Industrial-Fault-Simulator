# Industrial Test Rig Simulator

A bench-scale rig for reproducing common industrial machine faults (unbalance, abnormal load, flow/level faults, overcurrent) under controlled, repeatable conditions, with a multi-sensor data-acquisition pipeline for predictive-maintenance research.

<p align="center">
  <img src="Old Design/images/Fault_Simulator.jpg" alt="Test rig" width="700">
</p>

## Features
- Induction motor driven shaft with worm gearbox and adjustable mechanical load
- Fault injection: load (weight plates, magnetic clutch/brake), flow/level (pump and water tank), electrical (current)
- Sensors: accelerometers, current sensors, tachometer, temperature/humidity, water level
- Data acquisition with NI USB DAQ and Arduino, logged through LabVIEW

## Repository structure
| Folder | Contents |
|---|---|
| `data/sample_datasets/` | Sample `.lvm` and `.csv` recordings (no fault, 2/5/7/10 kg load) |
| `docs/` | Hardware, sensor, LabVIEW and test rig design documents |
| `firmware/` | Arduino accelerometer code |
| `hardware/altium/` | Schematics and block diagrams |
| `images/` | Photos and diagrams of the rig |
| `software/labview/` | LabVIEW data acquisition VI |
| `software/python/` | Data loading and plotting scripts |

## Getting started
1. Clone the repository.
2. Open `software/labview/Sensor_data.vi` in LabVIEW to acquire data.
3. Run the Python scripts in `software/python/` to plot the datasets.

## Author
Huzaifa Rahim Malik
