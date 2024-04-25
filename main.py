from flask import Flask, render_template, session, request, redirect, url_for


# Press Mayús+F1pip search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

@app.route('/')
def home():
    return render_template("index.html")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
