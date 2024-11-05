from flask import Flask, render_template, request
from stories import stories  # Import the stories dictionary

app = Flask(__name__)
app.config['SECRET_KEY'] = "ooogabooga"

@app.route('/')
def choose_story():
    """Homepage to choose a story template."""
    return render_template('choose_story.html', stories=stories.values())

@app.route('/form')
def display_form():
    """Display form with prompts for the chosen story."""
    story_code = request.args.get("story_code")
    story = stories.get(story_code)

    prompts = story.prompts

    return render_template("form.html",
                           story = story,
                           prompts=prompts)

    

@app.route('/story', methods=['POST'])
def display_story():
    """Generate and display the story from form inputs."""
    story_code = request.form["story_code"]
    story = stories[story_code]

    # Get the user's answers from the form
    answers = {prompt: request.form[prompt] for prompt in story.prompts}

    # Generate the story using the answers
    text = story.generate(answers)

    return render_template("story.html",
                           text=text)


    

