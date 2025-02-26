from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        issue = request.form.get("issue")

        template = f"""
        <h2>Support Ticket Submitted</h2>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Issue:</strong> {issue}</p>
        <hr>
        <p>We will get back to you soon.</p>
        """

        return render_template_string(template)

    return """
    <html>
    <head>
        <title>Support Ticket System</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background: linear-gradient(283deg, #0471FF 0%, #0BE8DD 99.8%);
                font-family: Arial, sans-serif;
                flex-direction: column;
                color: white;
            }
            .ticket-box {
                background: rgba(255, 255, 255, 0.2);
                padding: 30px;
                border-radius: 10px;
                text-align: center;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
                width: 380px;
            }
            input, textarea {
                display: block;
                margin: 10px auto;
                padding: 12px;
                width: 250px;
                border-radius: 5px;
                border: none;
                outline: none;
                text-align: center;
            }
            button {
                background: #0471FF;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                width: 270px;
                margin-top: 10px;
                font-size: 16px;
            }
            button:hover {
                background: #0356d6;
            }
        </style>
    </head>
    <body>
        <div class="ticket-box">
            <h2>Submit a Support Ticket</h2>
            <form method="POST">
                <input type="text" name="name" placeholder="Your Name" required>
                <textarea name="issue" placeholder="Describe your issue" required></textarea>
                <button type="submit">Submit</button>
            </form>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
