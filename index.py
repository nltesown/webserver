import cgi
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

nom = form.getvalue("name")
send = form.getvalue("send")

html = f"""<!DOCTYPE html>
<head>
    <title>Mon programme</title>
</head>
<body>
<h1>Bonjour {nom}</h1>
<p>Il est {current_time}</p>
<p id="heure"></p>
    <form action="/index.py" method="post">
        <input type="text" name="name" value="Votre nom" />
        <input type="submit" name="send" value="Envoyer information au serveur">
    </form> 
<script>
let elHeure = document.getElementById("heure");
window.setInterval(() => {{
    elHeure.innerHTML = new Date();
  }}, 1000);
</script>
</body>
</html>
"""

print(html)
