

def lambda_handler(event, context):
    message = """
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width,
        initial-scale=1.0" />
    <title> Final Project</title>
    <link rel="stylesheet" href="main.css" />
</head>

<body>
    <nav>
        <div class="logo">EDM</div>
        <div class="nav-items">
            <a href="index.html">Home </a>
            <a href="data.html"> Data </a>
            <a href="form.html">Survey</a>
        </div>
    </nav>
    <section class="hero">
        <div class="hero-container">
            <div class="column-left">
                <h1>Climate Change</h1>
                <p>Where we are and what we can do.</p>
                <button> <a href="data.html"> Get Started </a> </button>
            </div>
        </div>
    </section>
</body>

</html>