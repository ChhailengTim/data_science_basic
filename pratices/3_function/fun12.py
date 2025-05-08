def print_info(**kwargs):
    if kwargs:
        print("\n--- Info --")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    else:
        print("No info provided.")


print_info(name="Alice", age=30, city="New York")
print_info(job="Engineer", salary=70000)
print_info(country="USA", state="NY", city="New York")
print_info()