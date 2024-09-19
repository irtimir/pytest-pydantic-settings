from tests.functional.settings import SomeSettings

# load_dotenv("/tests/functional/.env") 


DSN = SomeSettings().model_dump()

if __name__ == "__main__":
    print(f">>> KEY {DSN.get("key")}")
    if DSN.get("KEY") == "tests/functional/.env":
        print("Подтянулась то что нужно, венв который в тесте")
    else:
        print("подтянуто не то что нужно")
