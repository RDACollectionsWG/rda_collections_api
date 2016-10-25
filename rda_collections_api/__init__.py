import connexion
from connexion.resolver import RestyResolver

app = connexion.App(__name__)
app.add_api('swagger.yaml', arguments={"app_name": __name__})

app.run(port=8080)
