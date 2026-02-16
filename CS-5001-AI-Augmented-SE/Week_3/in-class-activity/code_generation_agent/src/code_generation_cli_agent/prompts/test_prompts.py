
import yaml
import sys
import os
import json
from openai import OpenAI

# --- CONFIGURATION ---
CLIENT = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
MODEL_NAME = "devstral-small-2:24b-cloud" # Ensure this matches 'ollama list'

# Get the folder where this script is located
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# New folder for multi-file projects
OUTPUT_DIR = os.path.join(SCRIPT_DIR, "Quiz")

def load_yaml(filepath):
    try:
        with open(filepath, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        print(f"Error: Could not find {filepath}")
        sys.exit(1)

def call_ollama(prompt):
    print(f"\n🤖 Calling Ollama ({MODEL_NAME})...")
    try:
        response = CLIENT.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1, # Keep low to ensure valid JSON
            max_tokens=4000,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❌ API Error: {e}")
        return ""

def save_project_files(json_content):
    """Parses JSON response and saves multiple files."""
    try:
        # 1. Clean up markdown if the model accidentally added it
        clean_json = json_content.replace("```json", "").replace("```", "").strip()
        
        # 2. Parse the JSON
        project_files = json.loads(clean_json)
        
        # 3. Create Base Directory
        if os.path.exists(OUTPUT_DIR):
            print(f"\n⚠️  Warning: Overwriting files in {OUTPUT_DIR}")
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        print(f"\n📂 Project Directory: {OUTPUT_DIR}")

        # 4. Loop through files and save
        for filename, content in project_files.items():
            # Handle subdirectories (e.g. src/main.py)
            file_path = os.path.join(OUTPUT_DIR, filename)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  └── 💾 Saved: {filename}")
            
    except json.JSONDecodeError as e:
        print(f"\n❌ JSON Error: The model didn't return valid JSON.\nError: {e}")
        print("Raw Output Snippet:", clean_json[:200])

def run_scaffold_flow(language, description):
    print(f"\n{'='*60}")
    print(f"🚀 SCAFFOLDING PROJECT: {language}")
    print(f"{'='*60}")
    
    planner_cfg = load_yaml('planning.yaml')
    codegen_cfg = load_yaml('code_generation.yaml')

    # --- STEP 1: PLAN ---
    print("\n📝 Planning Architecture...")
    # We use the 'detailed' planner for multi-file projects
    planner_tmpl = planner_cfg['variants']['detailed']['template']
    plan_prompt = planner_tmpl.format(
        language=language,
        module_path="Full Project Structure",
        desc=description
    )
    plan_output = call_ollama(plan_prompt)
    print("✅ Plan created.")

    # --- STEP 2: SCAFFOLD (JSON Generation) ---
    print("\n🏗️  Generating Files...")
    # We use the new 'scaffold' variant here
    codegen_tmpl = codegen_cfg['variants']['scaffold']['template']
    
    code_prompt = codegen_tmpl.format(
        language=language,
        desc=description,
        plan=plan_output
    )
    
    json_output = call_ollama(code_prompt)
    
    # --- STEP 3: SAVE ---
    save_project_files(json_output)

if __name__ == "__main__":
    # Example: Python Data Analysis Project
    run_scaffold_flow(
        # project_name="react_quiz_app",
        language="React",
        description="""
        A modern React application that runs a 5-question trivia quiz.
        
        Required File Structure & Logic:
        1. 'package.json':
           - Standard React dependencies (react, react-dom, react-scripts).
           - Scripts for "start" and "build".
        
        2. 'src/data/questions.js':
           - Export an array of 5 objects.
           - Each object has: id, questionText, answerOptions (array of texts), and correctAnswer.
        
        3. 'src/components/QuestionCard.js':
           - A functional component that displays the current question and a set of answer buttons.
           - It should accept props for the question data and an 'onAnswerClick' callback.
        
        4. 'src/App.js':
           - Manage state: 'currentQuestion' (index), 'score', and 'showScore' (boolean).
           - Logic: When an answer is clicked, check if it is correct, update score, and move to the next question.
           - If it is the last question, set 'showScore' to true.
           - Render the 'QuestionCard' OR a "Result Screen" based on 'showScore'.
        
        5. 'src/index.js':
           - The standard React entry point to mount <App /> to the DOM.
           
        6. 'public/index.html':
           - Basic HTML template with <div id="root"></div>.
           
        7. 'src/App.css':
           - Modern styling. Use a centered card layout, nice gradients for buttons, and a dark theme.
        """
    )
    # run_scaffold_flow(
    #     language="Python",
    #     description="""
    #     A basic Flask To-do application structure.
    #     Required files:
    #     1. 'app.py': The main Flask application with routes for '/' and '/about'.
    #     2. 'templates/index.html': A simple HTML homepage using Jinja2 inheritance.
    #     3. 'static/style.css': A basic CSS file to style the body background.
    #     4. 'requirements.txt': Flask and Gunicorn.
    #     5. 'README.md': Instructions to run the app.
    #     """
    # )
    # Test Case: Node.js Weather App Scaffolding
    # run_scaffold_flow(
        
    #     language="Node.js",
    #     description="""
    #     A simple Weather Dashboard using Express.js and OpenWeatherMap.
        
    #     Required structure:
    #     1. 'server.js': Main Express server. 
    #        - Serve static files from 'public'.
    #        - Route '/api/weather' (POST) that fetches real data from OpenWeatherMap using axios.
    #        - Use a placeholder API key.
    #     2. 'public/index.html': 
    #        - Input field for city name.
    #        - "Get Weather" button.
    #        - A div to display the results.
    #        - Fetch data from '/api/weather' using fetch() API.
    #     3. 'public/style.css':
    #        - Clean, modern styling.
    #        - Card layout for the weather display.
    #     4. 'package.json':
    #        - Dependencies: express, axios, body-parser, cors.
    #        - Start script: "node server.js"
    #     5. 'README.md': Setup instructions.
    #     """
    # )
    # Test Case: Modern Calculator App

    # run_scaffold_flow(
    #     # project_name="modern_calculator",
    #     language="JavaScript",
    #     description="""
    #     A modern, fully functional Calculator Web App.
        
    #     Required Files:
    #     1. 'index.html': 
    #        - A clean structure with a 'display' screen at the top.
    #        - A grid layout for buttons (0-9, +, -, *, /, =, C, .).
    #        - Link the CSS and JS files.
    #     2. 'style.css': 
    #        - Modern 'Dark Mode' UI.
    #        - Use CSS Grid for the button layout.
    #        - Rounded corners, nice shadows, and hover effects on buttons.
    #        - Responsive design (works on mobile and desktop).
    #     3. 'script.js': 
    #        - Handle all click events.
    #        - Support keyboard input (typing numbers/operators works).
    #        - Logic for addition, subtraction, multiplication, division.
    #        - 'C' clears the screen.
    #        - Handle errors (e.g., dividing by zero displays "Error").
    #     4. 'README.md': 
    #        - Instructions on how to open the app.
    #     """
    # )




# import yaml
# import sys
# import os  
# from openai import OpenAI

# # --- CONFIGURATION ---
# CLIENT = OpenAI(
#     base_url="http://localhost:11434/v1",
#     api_key="ollama"
# )

# MODEL_NAME = "devstral-small-2:24b-cloud"

# # Define where you want to save the files
# OUTPUT_DIR = "outputs" 

# def load_yaml(filepath):
#     try:
#         with open(filepath, 'r') as f:
#             return yaml.safe_load(f)
#     except FileNotFoundError:
#         print(f"Error: Could not find {filepath}")
#         sys.exit(1)

# def call_ollama(prompt):
#     print(f"\n🤖 Calling Ollama ({MODEL_NAME})...")
#     try:
#         response = CLIENT.chat.completions.create(
#             model=MODEL_NAME,
#             messages=[{"role": "user", "content": prompt}],
#             temperature=0.1,
#             max_tokens=2000,
#         )
#         return response.choices[0].message.content.strip()
#     except Exception as e:
#         print(f"❌ API Error: {e}")
#         return ""

# def save_file(filename, content):
#     """Creates the directory and saves the file."""
#     # 1. Ensure the directory exists
#     os.makedirs(OUTPUT_DIR, exist_ok=True)
    
#     # 2. Clean up markdown fences if the model accidentally added them
#     clean_content = content.replace("```python", "").replace("```javascript", "").replace("```", "").strip()
    
#     # 3. Create the full path
#     full_path = os.path.join(OUTPUT_DIR, filename)
    
#     # 4. Write the file
#     with open(full_path, "w", encoding="utf-8") as f:
#         f.write(clean_content)
        
#     print(f"\n💾 FILE SAVED: {full_path}")
#     return full_path

# def run_test_flow(language, framework, description, file_path):
#     print(f"\n{'='*60}")
#     print(f"🚀 GENERATING: {file_path} ({language})")
#     print(f"{'='*60}")
    
#     planner_cfg = load_yaml('planning.yaml')
#     codegen_cfg = load_yaml('code_generation.yaml')

#     # --- STEP 1: PLAN ---
#     print("\n📝 Planning...")
#     planner_tmpl = planner_cfg['variants']['default']['template']
#     plan_prompt = planner_tmpl.format(
#         language=f"{language} with {framework}",
#         module_path=file_path,
#         desc=description
#     )
#     plan_output = call_ollama(plan_prompt)
#     print(f"✅ Plan created.")

#     # --- STEP 2: CODE ---
#     print("\n💻 Coding...")
#     codegen_tmpl = codegen_cfg['variants']['default']['template']
#     code_prompt = codegen_tmpl.format(
#         language=f"{language} with {framework}",
#         module_path=file_path,
#         desc=description,
#         plan=plan_output
#     )
#     code_output = call_ollama(code_prompt)
    
#     # --- STEP 3: SAVE ---
#     save_file(file_path, code_output)

# if __name__ == "__main__":

    
#     # Example: Generating the Calculator App
#     # run_test_flow(
#     #     language="Python",
#     #     framework="Flask",
#     #     description="""
#     #     A single-file Flask web application that acts as a calculator.
#     #     1. Use 'render_template_string' to serve a simple HTML page at '/'.
#     #     2. The page should have a form with two inputs (number A, number B) and a dropdown for operation (Add, Sub, Mul, Div).
#     #     3. When submitted, display the result on the same page.
#     #     """,
#     #     file_path="app.py" 
#     # )



#     # run_test_flow(
#     #     language="Node.js",
#     #     framework="Express",
#     #     description="""
#     #     A single-file Node.js Express server that acts as a Weather App using the OpenWeatherMap API.
        
#     #     Requirements:
#     #     1. Setup an Express server on port 3000.
#     #     2. Dependencies: Use 'express' for the server and 'axios' for making HTTP requests.
#     #     3. Config: Create a variable 'const API_KEY' and set it to a placeholder string "YOUR_API_KEY_HERE".
#     #     4. Root route '/': Serve an HTML string containing a clean form to input a 'City Name'.
#     #     5. Route '/get-weather': 
#     #        - Handle the POST request.
#     #        - Use 'axios' to fetch data from: https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric
#     #        - Extract the temperature and weather description from the JSON response.
#     #     6. Response: Return the HTML string with the real weather data injected (Server-Side Rendering).
#     #     7. Error Handling: If the city is invalid or the API key is missing, display a friendly error message on the page.
#     #     """,
#     #     file_path="weather_app.js"
#     # )



# #     run_test_flow(
# #     language="Python",
# #     framework="Flask",
# #     description="""
# #     A simple Flask blog application.
# #     1. Store blog posts as a list of dictionaries (title, content, date) in memory.
# #     2. Route '/': Display all blog post titles as clickable links.
# #     3. Route '/post/<int:id>': Display the full content of a specific post.
# #     4. Use the 'markdown' library to render the post content as HTML.
# #     5. Includes a 'New Post' page with a form to add a new entry.
# #     """,
# #     file_path="blog_app.py"



#     # run_test_flow(
#     #     language="Node.js",
#     #     framework="Express",
#     #     description="""
#     #     A URL Shortener service API.
#     #     1. POST '/shorten': Accepts a long URL and returns a shortened 6-character ID.
#     #     2. Store the mapping (ID -> Long URL) in a simple in-memory object/dictionary.
#     #     3. GET '/<id>': Looks up the ID and redirects the user to the original Long URL.
#     #     4. If the ID is not found, return a 404 error page.
#     #     5. Use the 'crypto' module to generate random IDs.
#     #     """,
#     #     file_path="url_shortener.js"
#     # ) 


# #     run_test_flow(
# #     language="Python",
# #     framework="Streamlit",
# #     description="""
# #     A simple single-room chat application.
# #     1. Use 'st.session_state' to store a list of messages.
# #     2. Provide a text input box for the user to type a message.
# #     3. When the user hits 'Send', append the message to the list and clear the input.
# #     4. Display the chat history above the input box.
# #     5. Add a 'Clear Chat' button to reset the history.
# #     6. Simulate a "bot" response that echoes the user's message after 1 second.
# #     """,
# #     file_path="chat_app.py"
# # )



# #     run_test_flow(
# #     language="React",
# #     framework="Create React App",
# #     description="""
# #     A product dashboard component.
# #     1. Create a functional component named 'ProductDashboard'.
# #     2. Use hardcoded sample data for 5 products (id, name, price, category, image_url).
# #     3. Display the products in a CSS Grid layout.
# #     4. Implement a 'Filter' dropdown to filter products by category.
# #     5. Implement a 'Sort' button to toggle between Price: Low-to-High and High-to-Low.
# #     6. Use standard CSS for styling (no external libraries like Tailwind).
# #     """,
# #     file_path="ProductDashboard.js"
# # )


# #     run_test_flow(
# #     language="Python",
# #     framework="Flask",
# #     description="""
# #     A secure file upload service.
# #     1. HTML Form: Allow users to upload .png or .jpg files only.
# #     2. Security: Validate the file extension before saving.
# #     3. Storage: Save uploaded files to a folder named 'uploads'.
# #     4. Display: After upload, show a list of all uploaded files with 'Delete' buttons next to them.
# #     5. Route '/uploads/<filename>': Serve the uploaded file so it can be viewed in the browser.
# #     """,
# #     file_path="file_server.py"
# # )


