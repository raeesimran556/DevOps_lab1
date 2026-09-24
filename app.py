def show_services():
    services = ["Student Portal", "Library", "Transport", "IT Help Desk"]

    print("Campus Service Portal")
    print("Available Services:")

    for number, service in enumerate(services, start=1):
        print(f"{number}. {service}")


if __name__ == "__main__":
    show_services()
