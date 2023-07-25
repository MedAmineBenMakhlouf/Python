import random
from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = "65165_è-_è"  

def generate_random_number():
    return random.randint(1, 100)

guesses_list = []

@app.route("/", methods=["GET", "POST"])
def numberGuessing():
    if "random_number" not in session:
        # Generate a random number between 1 and 100 and store it in the session
        session["random_number"] = generate_random_number()

    if request.method == "POST":
        guess = int(request.form.get("guess", 0))
        random_number = session["random_number"]
        guesses_list.append(guess)  # Add the user's guess to the guesses list

        if guess < random_number:
            message = "Too low!"
        elif guess > random_number:
            message = "Too high!"
        else:
            message = "Congratulations! You guessed the right number!"
            session.pop("random_number")  # Remove the stored number after guessing correctly

    else:
        message = ""

    # Pass the entire guesses list to the template
    return render_template("index.html", message=message, guesses=guesses_list)


@app.route("/newgame")
def new_game():
    # Start a new game by generating a new random number and clearing the guesses list
    session["random_number"] = generate_random_number()
    guesses_list.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=5001)