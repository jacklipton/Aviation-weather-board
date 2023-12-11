<div id="top"></div>

<h3 align="center">Aviation Weather Map</h3>

  <p align="center">
    A weather dependant light up aviation map.
    <br />
    <a href="https://github.com/jacklipton/Aviation-weather-board"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</div>


https://github.com/jacklipton/Aviation-weather-board/assets/83594679/f8df7533-afa8-4296-8fbb-ba53487697fc

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#configuration">Configuration</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<br/>


## About The Project

This project aimed to ad live weather data to a standard souther ontario VNC (VFR Navigation Chart) from NavCanada. Each airport has an LED at its location on the map and the colour of the LED corresponds to the current weather at that airport. It is designed to mimic the flight catagory feature on the maps tab in foreflight.

The board flashes either green or red when initially booted-up to indicate a successful or failed wifi connection. Each light corresponds to a specfic weather status:

* Green = VFR (Visusal Flight Rules): <i> Ceiling greater than 3000' and/or visibility greater than 5 miles</i>
* Blue = MVFR (Marginal Visual Flight Rules): <i> Ceiling between 1000' - 3000' and/or visibility between 3 - 5 miles</i>
* Red = IFR (Instrument Flight Rules): <i> Ceiling between 500' - 1000' and/or visibility between 1 - 3 miles</i>
* Pink = LIFR (Low Instrument Flight Rules): <i> Ceiling less than 500' and/or visibility less than 1</i>


### Built With

* [Micropython](https://micropython.org/)
* [CheckWX API](https://www.checkwxapi.com/)


## Prerequisites

Before you begin, ensure you have met the following requirements:

* Create an account with CheckWX and obtain an Auth Key
* Download the micropython firmware for your microcontroller and flash it

## Installation

Use a micropython IDE (such as UpyCraft) to upload the script. Ensure to call it in the ESP boot up script

## Configuration

Ensure in the script you add the name of your own wifi SSID and password at line 39 and 40. You can choose your own airports at line 89 by modifying the ICAO airport codes. Lastly, ensure you have added your API auth key.

## Contributing

Contributions are welcome! If you have any improvements, bug fixes, or feature suggestions, feel free to fork the repository and submit a pull request.


