from flask import Flask, request, render_template_string, redirect, url_for
import markdown
from datetime import datetime

app = Flask(__name__)

posts = []

def get_post(id):
    for post in posts:
        if post['id'] == id:
            return post
    return None

def generate_date():
    return datetime.now().strftime("%Y-%m-%d")

@app.route('/')
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Blog</title>
        </head>
        <body>
            <h1>Blog Posts</h1>
            <a href="/new">New Post</a>
            <ul>
                {% for post in posts %}
                <li><a href="/post/{{ post.id }}">{{ post.title }}</a> ({{ post.date }})</li>
                {% endfor %}
            </ul>
        </body>
        </html>
    ''', posts=posts)

@app.route('/post/<int:id>')
def post(id):
    post = get_post(id)
    if post is None:
        return "Post not found", 404
    content_html = markdown.markdown(post['content'])
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>{{ post.title }}</title>
        </head>
        <body>
            <h1>{{ post.title }}</h1>
            <p>Date: {{ post.date }}</p>
            <div>{{ content_html|safe }}</div>
            <a href="/">Back to all posts</a>
        </body>
        </html>
    ''', post=post, content_html=content_html)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        if title and content:
            new_post = {
                'id': len(posts) + 1,
                'title': title,
                'content': content,
                'date': generate_date()
            }
            posts.append(new_post)
            return redirect(url_for('index'))
        return "Title and content are required", 400
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>New Post</title>
        </head>
        <body>
            <h1>New Post</h1>
            <form method="POST">
                <label for="title">Title:</label><br>
                <input type="text" id="title" name="title" required><br>
                <label for="content">Content:</label><br>
                <textarea id="content" name="content" required></textarea><br>
                <button type="submit">Submit</button>
            </form>
            <a href="/">Cancel</a>
        </body>
        </html>
    ''')

if __name__ == '__main__':
    app.run(debug=True)