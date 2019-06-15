
def createPage(sections):
    html = """
    <!doctype html>
    <html>
    <head>
        <title>Basic Template</title>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">

        <!-- Kube CSS -->
        <link rel="stylesheet" href="css/kube.min.css">
        <link rel="stylesheet" href="css/main.css">

    </head>
    <body>
    <div class="container">
    """
    for section in sections:
        html += section
    html +="""
    </div>
    </body>
    </html>
    """
    return html