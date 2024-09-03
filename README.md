# ISS Tracker

This project is a Python application that tracks the International Space Station (ISS) in real-time and provides information about astronauts currently on the ISS. It uses various libraries and APIs to fetch data and visualize the ISS's position on a world map using Turtle graphics.

## Features

- Fetches and displays the list of astronauts currently on the ISS.
- Tracks the real-time location of the ISS and updates its position on a world map.
- Logs important events and errors for debugging and informational purposes.
- Displays the user's current geographic location based on their IP address.

## Requirements

- Python 3.x
- Required Python libraries: `webbrowser`, `urllib`, `time`, `json`, `turtle`, `geocoder`, `os`, `socket`, `logging`, `threading`

You can install the necessary Python packages using pip:

```bash
pip install geocoder
```

Note: `turtle` is included with Python's standard library, so you don't need to install it separately.

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/iss-tracker.git
   ```

2. Navigate to the project directory:

   ```bash
   cd iss-tracker
   ```

3. Ensure you have the required images in your project directory:
   - `map.gif` (World map image)
   - `iss.gif` (Image representing the ISS)

   These images should be placed in the same directory as the script.

## Usage

1. Run the script using Python:

   ```bash
   python iss_tracker.py
   ```

2. The script will:
   - Fetch and save the list of astronauts currently on the ISS to a text file (`iss.txt`).
   - Attempt to open `iss.txt` with the default text editor.
   - Display a Turtle graphics window with a world map and a representation of the ISS.
   - Continuously update the ISS's position on the map every 5 seconds.

## Code Explanation

### `fetch_astronauts_data()`

- Fetches data from the `http://api.open-notify.org/astros.json` API to get the list of astronauts on the ISS.
- Saves the information to `iss.txt` and attempts to open the file.
- Uses `geocoder` to get the user's current location and includes this information in `iss.txt`.

### `fetch_iss_position()`

- Continuously fetches the ISS's current position from the `http://api.open-notify.org/iss-now.json` API.
- Updates the ISS's position on the Turtle graphics map every 5 seconds.

### Logging

- Logs events and errors to `iss_tracking.log`.
- Records successful data fetches, errors, and other significant events.

### Turtle Graphics

- Uses Turtle to display a world map and represent the ISS.
- Updates the ISS's position on the map based on data fetched from the API.

## Troubleshooting

- Ensure the required image files (`map.gif` and `iss.gif`) are in the same directory as the script.
- Check the log file `iss_tracking.log` for detailed error messages if something goes wrong.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The ISS Tracker uses data from the Open Notify API for ISS tracking and astronaut information.
- The Turtle graphics library is used for visualization.
