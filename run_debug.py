import app


def main():
    server = app.create_app()
    server.run(debug=True)


if __name__ == "__main__":
    main()
