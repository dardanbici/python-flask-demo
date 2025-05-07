# SECURITY VULNERABILITY: Arbitrary code execution
def insecure_input():
    user_input = input("Enter something: ")
    eval(user_input)  # Dangerous: eval on user input


# RELIABILITY BUG: Invalid exception being raised
def raise_wrong_exception():
    raise "This should be an Exception object, not a string"


# CODE SMELL: Deep nesting and redundant logic
def nested_smell(x):
    if x > 0:
        if x < 100:
            if x % 2 == 0:
                print("Even number")
            else:
                print("Odd number")
        else:
            print("Too large")
    else:
        print("Negative")


# DUPLICATED CODE: This function is duplicated on purpose
def duplicate_logic():
    print("This is duplicate code")
    print("This is duplicate code")
    print("This is duplicate code")
    print("This is duplicate code")
    print("This is duplicate code")


# Exact duplicate of the above function
def duplicate_logic_2():
    print("This is duplicate code")
    print("This is duplicate code")
    print("This is duplicate code")
    print("This is duplicate code")
    print("This is duplicate code")


# UNTESTED LOGIC: This function will reduce your coverage
def risky_untested_logic():
    result = 42 / 0  # Division by zero error
    return result


if __name__ == "__main__":
    print("Running sonar demo issues...")
    # Do not call risky_untested_logic() so it's untested
    insecure_input()
    try:
        raise_wrong_exception()
    except:
        pass

    nested_smell(42)
    duplicate_logic()
    duplicate_logic_2()
