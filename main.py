from templates import app

app.config.from_object('configurations.DevelopmentConfig')

port = 5000

if __name__ == '__main__':
    app.run(port=port)