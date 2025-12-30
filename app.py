from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Hummingbird</title>
    <!-- Load Tailwind CSS from CDN for instant styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-50 flex items-center justify-center min-h-screen p-4">
    <div class="text-center">
        <h1 class="text-6xl md:text-8xl font-extrabold text-indigo-700
                   hover:scale-105 transition duration-300 ease-in-out">
            Welcome to Project Hummingbird
        </h1>
        <p class="mt-4 text-xl text-gray-500">
            Your simple Flask application is running!
        </p>
        <p class="mt-5 text-xl text-gray-400">
	    ....everybody loves hummingbirds
        </p>
    </div>
</body>
</html>
    """

if __name__ == "__main__":
    # Listen on all interfaces (0.0.0.0) on port 8080
    app.run(host="0.0.0.0", port=8080)
