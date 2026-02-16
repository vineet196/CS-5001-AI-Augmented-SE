# Flask To-do Application

A basic Flask to-do application with routes for '/' and '/about'.

## Setup Instructions

1. Create a virtual environment:
   bash
   python -m venv venv
   

2. Activate the virtual environment:
   - On Windows:
     bash
     venv\Scripts\activate
     
   - On macOS/Linux:
     bash
     source venv/bin/activate
     

3. Install dependencies:
   bash
   pip install -r requirements.txt
   

4. Run the application:
   bash
   python app.py
   

5. Open your browser and navigate to:
   - http://localhost:5000/
   - http://localhost:5000/about

## Project Structure


.
├── app.py                # Main Flask application
├── static/
│   └── style.css         # CSS styles
├── templates/
│   ├── index.html        # Homepage template
│   ├── about.html        # About page template
│   └── base.html         # Base template
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation


## Features

- Add new to-do items
- Mark to-do items as complete
- Simple navigation between pages
- Basic styling with CSS

## Running with Gunicorn

To run the application with Gunicorn for production:

bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app


This will start the application with 4 worker processes on port 5000.