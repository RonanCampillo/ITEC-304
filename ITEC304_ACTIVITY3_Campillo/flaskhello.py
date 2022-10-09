from os import link

from flask import Flask, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return ("\n"
            "<html><body>\n"
            "<h2>Welcome to Hephaestus Dungeon</h2>\n"
            "<h3> Your Goal is to Find the Cursed Blade \n "
            "\n"
            "<h3> Choose a path to take "
            "<form action=\"/left\">\n"
            "<input type ='submit' value='Left Path"
            ""
            "'>\n"
            "</form>"

            "<form action=\"/right\">\n"
            "<input type ='submit' value='Right Path'>\n"
            "</form>"

            "</body></html>\n")


@app.route('/right')
def right():
    return ("\n"
            "<html><body>\n"
            "<h3> You see a Locked Door </br>"
            "You take a closer look and sees a stone tablet </br>"
            "In the Tablet a Riddle is written</br>"
            "Insert Riddle Here</br>"
            "Type in your answer </h3>"
            "<form action=\"/correct_ans\">\n"
            "<input type =  'text' name='answer'></br>"
            "</br>"
            "<input type = 'Submit' value='Submit Answer'>"

            "</form>"

            "</body></html>\n")


@app.route('/correct_ans')
def correct_ans():
    answer = request.args.get('answer')
    if answer == 'Rick and Morty':
        return """
                <html><body>
                Yey Congratulation
                </body>
                </html>
        """
    else:
        return redirect("/wrong_ans", code=302)


@app.route("/wrong_ans")
def wrong_ans():
    return ("\n"
            "<html><body>\n"
            "<h2>You see yourself in a cave lit up with glowing crystal</h2>\n"
            "<h3>you can find a straight  path</h3> \n "
            "<h3> you can see a faint light at the end of the path</h3> "
            "<h3> as you further and closer to the light </h3> "
            "<h3> you now have a clear view of an entrance </h3> "

            "Insert Riddle Here</br>"
            "Type in your answer </h3>"
            "<form action=\"/left\">\n"
            "<input type =  'text' name='ans'></br>"
            "</br>"
            "<input type = 'Submit' value='Submit Answer'>"

            "</form>"



            "</body></html>\n")


@app.route("/left")
def left():
    ans = request.args.get('ans')
    if ans == 'EFF':
        return ("\n"
                "<html><body>\n"
                "<h2>You see yourself in a cave lit up with glowing crystal</h2>\n"
                "<h3>you can find a straight  path</h3> \n "
                "<h3> you can see a faint light at the end of the path</h3> "
                "<h3> as you further and closer to the light </h3> "
                "<h3> you now have a clear view of an entrance </h3> "

                "\n"
                "<h3> </h3> "
                "<h3> Choose a path to take</h3> "
                "<form action=\"/L1\">\n"
                "<input type ='submit' value='Left Path"
                ""
                "'>\n"
                "</form>"

                "<form action=\"/L2\">\n"
                "<input type ='submit' value='Right Path'>\n"
                "</form>"

                "</body></html>\n")

    else:
        return redirect("/RR")


@app.route('/L1')
def L1():
    return ("\n"
            "<html><body>\n"

            "<h3> Choose a path to take "
            "<form action=\"/right\">\n"
            "<input type ='submit' value='Left Path"
            ""
            "'>\n"
            "</form>"

            "<form action=\"/wrong_ans\">\n"
            "<input type ='submit' value='Right Path'>\n"
            "</form>"

            "</body></html>\n")


@app.route('/L2')
def L2():
    return ("\n"
            "<html><body>\n"

            "<h3> Choose a path to take "
            "<form action=\"/RR\">\n"
            "<input type ='submit' value='Left Path"
            ""
            "'>\n"
            "</form>"

            "<form action=\"/home\">\n"
            "<input type ='submit' value='Right Path'>\n"
            "</form>"

            "</body></html>\n")


@app.route('/RR')
def RR():
    return redirect('/https://www.youtube.com/watch?v=dQw4w9WgXcQ', code=302)


# Launch the FlaskPy dev server
app.run(host="localhost", debug=True)
