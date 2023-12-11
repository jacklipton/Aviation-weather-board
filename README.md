# Aviation Weather Board

This project contains a Python script designed to be run on an ESP32 microcontroller. The script serves retreives the weather for a number of airports in southern ontario and colours a a series of LEDs based on the severity of the weather at each location.

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Overview

[Provide a more detailed overview of what your script does, its purpose, and any important features.]

## Prerequisites

Before you begin, ensure you have met the following requirements:

Ensure you have flashed the ESP32 with Micropython and have the following libraries installed:

network
import urequests 
machine
neopixel
json
import time
sys
esp

## Installation

Use a micropython IDE (such as UpyCraft) to upload the script. Ensure to call it in the ESP boot up script

## Usage

[Explain how users can use your script on the ESP32. Include examples and any important considerations.]

## Configuration

Ensure in the script you add the name of your own wifi SSID and password at line 39 and 40. You can choose your own airports at line 89. Lastly, checkout the output port on the microcontroller

## Contributing

Contributions are welcome! If you have any improvements, bug fixes, or feature suggestions, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). [Include a link to your license file.]

