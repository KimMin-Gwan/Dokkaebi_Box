from fastapi import FastAPI



def main():
    app = FastAPI()
    app.run("main:app",)


if __name__ == "__main__":
    main()