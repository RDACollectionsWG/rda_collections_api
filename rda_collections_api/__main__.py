from rda_collections_api import app, redis_store

def main():

    redis_store.init_app(app.app)
    app.run(host='0.0.0.0', port=8080, debug=True)

if __name__ == '__main__':
    main()
