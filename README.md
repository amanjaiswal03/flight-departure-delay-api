# Running the Python Flask App

This guide will help you set up and run the Python Flask app, and test it using an HTML page.

## Prerequisites

- Python 3.12
- pip (Python package installer)

## Setup

1. Clone the repository to your local machine.

2. Navigate to the project directory.

3. Create a virtual environment:

```sh
python3 -m venv venv
```

4. Activate the virtual environment:

    On Windows:
  
    ```sh
    .\venv\Scripts\activate
    ```
  
    On Unix or MacOS:
    ```sh
    source venv/bin/activate
    ```

5. Install the required dependencies:
```sh
  pip install -r requirements.txt
```

## Running the app
1. Start the Flask app:
```sh
python main.py
```
This will start the Flask server, typically accessible at http://127.0.0.1:5000.

## Testing the App with an HTML Page
1. Open the index.html file in your web browser.

2. The HTML page should have a form or JavaScript code to make requests to the Flask app. Ensure the requests are pointed to the correct endpoint, e.g., http://127.0.0.1:5000/flights.

3. Submit the form to trigger the JavaScript code to make the request.

4. The Flask app should process the request, displaying the response on your HTML page.


## Running Tests
To run tests for the Flask app, use the following command:

```sh
pytest test_main.py
```
This assumes you have pytest installed, which should be included if you've installed dependencies from requirements.txt.



