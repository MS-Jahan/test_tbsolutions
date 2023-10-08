# Web Scraping Demo Project

This repository contains a Python web scraping project that utilizes both Selenium and Playwright for web automation. It provides options for configuring web scraping with Selenium and Playwright, along with installation instructions and details on how to run the project.

## Prerequisites

Before running the project, ensure that you have the following prerequisites installed on your system:

- [Python](https://www.python.org/downloads/): Tested on 3.12, but should run on any Python 3 version which supports selenium.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/MS-Jahan/test_tbsolutions
   ```

2. Navigate to the project directory:

   ```bash
   cd test_tbsolutions
   ```

3. Install the required Python packages using `setup.bat`:

   ```bash
   setup.bat
   ```

   This script will ensure that you have the latest version of pip and install the necessary packages listed in `requirements.txt`.

## Running the Project

### Option 1: Selenium

1. Ensure that you have the Chrome browser installed on your system.

2. Create a `secrets.ini` file with your proxy settings. You can use the provided `secrets_sample.ini` as a template.

3. Edit the `config.py` file to configure your scraping settings, such as the URL, input, and other options if needed.

4. To run the Selenium web scraper, execute `run.bat`:

   ```bash
   run.bat
   ```

### Option 2: Playwright (Prerequisite)

Before running the Playwright option, please note that it requires Microsoft Visual C++ 14.0 or greater. You can get it with [Microsoft C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/). This is why Playwright is not included as the primary script.

Otherwise, all the steps for installation and running are the same as for selenium.

## Contributing

If you encounter issues or have suggestions for improvement, feel free to open an issue or submit a pull request. Your contributions are welcome!
