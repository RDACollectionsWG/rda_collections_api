import connexion
from connexion.resolver import RestyResolver
from flask_redis import FlaskRedis

app = connexion.App(__name__)
app.app.config["REDIS_URL"] = "redis://localhost:6379/0"
redis_store = FlaskRedis()

app.add_api('swagger.yaml', arguments={"app_name": __name__})
