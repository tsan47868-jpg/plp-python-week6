from safe_tools import safe_divide, safe_number, get_field


def main():
    print(safe_divide(12, 3))
    print(safe_divide(12, 0))
    print(safe_number("7"))
    print(safe_number("oops"))

    learner = {"name": "Amina", "score": 82}
    print(get_field(learner, "score"))
    print(get_field(learner, "email"))


if __name__ == "__main__":
    main()
