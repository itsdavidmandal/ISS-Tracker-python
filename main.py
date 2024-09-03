import webbrowser
import urllib.request
import time
import json
import turtle
import geocoder
import os
import socket
import logging
import threading

# Set up logging
logging.basicConfig(filename='iss_tracking.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Fetch the list of astronauts currently on the ISS
url = "http://api.open-notify.org/astros.json"  # API endpoint for the number of people in space

def fetch_astronauts_data():
    global result
    try:
        response = urllib.request.urlopen(url, timeout=10)  # Send a request to the API with a timeout
        result = json.loads(response.read())  # Parse the JSON response
        logging.info("Successfully fetched astronauts data.")
    except urllib.error.URLError as e:
        logging.error(f"Network error: {e.reason}")
        result = None
    except socket.timeout:
        logging.error("Request timed out.")
        result = None
    except json.JSONDecodeError:
        logging.error("Failed to parse JSON response.")
        result = None

    if result:
        try:
            # Open a text file to save the information about astronauts
            with open("iss.txt", "w") as file:
                # Write the number of astronauts currently on the ISS to the file
                file.write(f"There are currently {result['number']} astronauts on the ISS:\n\n")

                people = result["people"]  # Extract the list of people on the ISS

                # Write each astronaut's name to the file
                for p in people:
                    file.write(f"{p['name']} - on board\n")

                try:
                    # Get the current geographic coordinates of the user based on their IP address
                    g = geocoder.ip("me")
                    if g.latlng:
                        file.write(f"\nYour current lat/long is: {g.latlng}")
                    else:
                        file.write("\nCould not determine your current location.")
                except Exception as e:
                    file.write(f"\nFailed to get geolocation: {e}")
                    logging.error(f"Failed to get geolocation: {e}")

        except IOError as e:
            logging.error(f"File error: {e}")

        # Attempt to open the text file using the default text editor (works on Windows)
        try:
            os.startfile("iss.txt")
            logging.info("Text file opened successfully.")
        except Exception as e:
            logging.error(f"Failed to open the file: {e}")

# Set up the Turtle graphics screen for displaying the map
screen = turtle.Screen()
screen.title("ISS Tracker")
screen.setup(1280, 720)  # Set the screen size
screen.setworldcoordinates(-180, -90, 180, 90)  # Set the coordinate system to match global lat/long

# Load the background image of the world map and ISS image for Turtle
try:
    screen.bgpic("map.gif")  # Set the background image to a world map
    screen.register_shape("iss.gif")  # Register the ISS image as a shape
    logging.info("Background and ISS images loaded successfully.")
except turtle.TurtleGraphicsError:
    # Error handling if the required image files are not found
    logging.error("Required image files not found: 'map.gif' and 'iss.gif'.")

# Create a turtle to represent the ISS
iss = turtle.Turtle()
iss.shape("iss.gif")  # Use the ISS image for the turtle
iss.penup()  # Lift the pen so the turtle doesn't draw lines as it moves

def fetch_iss_position():
    while True:
        # Fetch the current position of the ISS
        url = "http://api.open-notify.org/iss-now.json"  # API endpoint for ISS location
        try:
            response = urllib.request.urlopen(url, timeout=10)  # Send a request to the API with a timeout
            result = json.loads(response.read())  # Parse the JSON response
            logging.info("Successfully fetched ISS position data.")
        except urllib.error.URLError as e:
            logging.error(f"Network error: {e.reason}")
            continue
        except socket.timeout:
            logging.error("Request timed out.")
            continue
        except json.JSONDecodeError:
            logging.error("Failed to parse JSON response.")
            continue

        location = result["iss_position"]  # Extract the ISS position (latitude and longitude)
        try:
            lat = float(location["latitude"])  # Convert latitude to a float
            lon = float(location["longitude"])  # Convert longitude to a float

            # Log the current ISS location
            logging.info(f"Current ISS position - Latitude: {lat}, Longitude: {lon}")
            iss.dot(10, "red")
            # Move the ISS turtle to the current position on the map
            iss.goto(lon, lat)
        except (ValueError, KeyError) as e:
            logging.error(f"Error processing ISS location data: {e}")

        # Wait for 15 seconds before updating the position again
        time.sleep(5)

# Run the fetch_iss_position function in a separate thread
iss_thread = threading.Thread(target=fetch_iss_position)
iss_thread.daemon = True
iss_thread.start()

# Run the fetch_astronauts_data function
fetch_astronauts_data()

# Keeps the turtle window open until the user closes it
turtle.done()