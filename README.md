
# Illegal Radio Transmission Detector
This project scans radio wave spectra within
the FM Radio (88 MHz -108 MHz) and TV (UHF, VHF) bandwidths, with the use of software defined radio,
specifically using a RTL-SDR Blog V3 device. The data are processed in Python with the use of the Pandas
and Numpy Python libraries. These elements together constitute the infrastructure that processes and analyzes
the data with the goal of discerning between legal and illegal radio transmissions. Necessary for this process
was the use of statistical operators such as correlation as well as signal comparators like the root mean square
error, to serve as metrics of the similarity between a scanned signal and a reference signal. All this information
is presented through a web browser interface by way of a web interface programmed in Python, HTML and
CSS. Within the web interface a user first needs to create an account. Once logged in, the user then selects the
scanning bandwidth (FM or TV) in which the system will detect any undesired signals. The web application runs
on a Raspberry Pi 3 which acts as the web server. This server then initiates the scanning and data processing
commands, as well as connect to a Google Cloud Storage database in order to store any alerts of illegal radio
transmissions in the cloud.
## Authors

- [@NeoGeoXL](https://github.com/NeoGeoXL)


## Licenses
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)

## Installation

To install RTL-SDR, follow the installation guide at: https://www.rtl-sdr.com/rtl-sdr-quick-start-guide/, 
and also install Raspbian Buster on the Raspberry Pi 3. You can read the radio spectrum using the command:

```bash
  rtl_test
```
If the RTL-SDR device has been installed correctly in the system, the following message will be displayed:

![rtl_test](https://user-images.githubusercontent.com/76502399/206020068-3d14139d-84cb-4e0b-924f-79540be62350.png)

Once installed, you can continue with the installation of the project using git clone or downloading the ZIP file,
and then configure the environment variables.
## Environment Variables

To run this project, you will need to configure the following environment variables

`FLASK_APP = main.py`

`FLASK_DEBUG = 1 `

`FLASK_ENV = development `




## Guide

The objective of this project is analyze the radio spectrum and process the radio waves 
to determine illegal transmissions, for this purpose it is necessary to use the RTL-SDR Blog v3 device, 
which allows read the radio spectrum then with Python’s libraries creates a pandas dataframe that will 
be compared with a reference signal using statistical operators such as RMSE or correlation. This project 
works on a Raspberry Pi 3 B+ as a server. 

![RTL -SDR](https://user-images.githubusercontent.com/76502399/205982004-3fe0ab49-73ba-46eb-9da7-2af032c320a6.png)

To test the detection system, an experiment is performed using Rohde Schwarz SMC100A signal generator in the telecommunications laboratory of the Universidad de Cuenca.
Which will broadcast an illegal signal on the FM spectrum at 89.3 [MHz]. The detection system is located 1.5 meters from the transmitter as shown in the following figure.

![laboratorio](https://user-images.githubusercontent.com/76502399/206036729-121e0105-576e-42bd-b711-ff3d7cd34e59.jpg)

In the user interface, if there is an illegal transmission, a message will be displayed in red indicating an alert and specifying the frequency and power of the illegal signal. 
If there is no illegal transmission, the user interface will show a message in yellow indicating that there are no illegal signals.

![example](https://user-images.githubusercontent.com/76502399/206037431-38274c54-324d-4cfe-bda8-507ce485c8c2.jpg)

To initialize this detection system, it is necessary register the user and click the options for scanning the FM or TV radio spectrum. When detecting an illegal transmission, 
the system stores the information of the frequency, power, radio service, and date of detection in a Google Cloud Platform database, which is connected through the API created 
in flask for this project.

![a1](https://user-images.githubusercontent.com/76502399/206038547-3ca74768-ee01-4441-bbc9-c689be2b42e0.jpg)

![a13](https://user-images.githubusercontent.com/76502399/206038592-f1ee9236-e06f-4f15-8ba0-06412add2904.jpg)


## Feedback

If you have any feedback, please reach out to my at ggarcia9539@gmail.com

