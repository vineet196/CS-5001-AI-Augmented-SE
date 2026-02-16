from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
</head>
<body>
    <h1>Calculator</h1>
    <form method="POST">
        <input type="number" name="numberA" placeholder="Number A" required>
        <input type="number" name="numberB" placeholder="Number B" required>
        <select name="operation" required>
            <option value="Add">Add</option>
            <option value="Sub">Subtract</option>
            <option value="Mul">Multiply</option>
            <option value="Div">Divide</option>
        </select>
        <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
        <h2>Result: {{ result }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            numberA = float(request.form['numberA'])
            numberB = float(request.form['numberB'])
            operation = request.form['operation']

            if operation == 'Add':
                result = numberA + numberB
            elif operation == 'Sub':
                result = numberA - numberB
            elif operation == 'Mul':
                result = numberA * numberB
            elif operation == 'Div':
                if numberB == 0:
                    result = "Error: Division by zero"
                else:
                    result = numberA / numberB
        except ValueError:
            result = "Error: Invalid input"

    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)