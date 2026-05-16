def add(a: int, b: int) -> int:
    """Return the sum of two numbers."""
    return a + b


def main() -> None:
    """Application entry point used by the wheel console command."""
    result = add(10, 20)

    print("Application started successfully!")
    print("Welcome to Jenkins CI/CD Demo using Python Wheel")
    print(f"10 + 20 = {result}")


if __name__ == "__main__":
    main()
