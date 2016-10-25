import connexion
from connexion.resolver import RestyResolver

app = connexion.App(__name__)
app.add_api('swagger.yaml', arguments={"app_name": __name__})

def main():
	app.run(port=8080)

if __name__ == '__main__':
	main()
