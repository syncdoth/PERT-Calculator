from scipy import stats


def get_inputs():
    inputs = input("write value of to, tm, tp, separated by comma: ").split(
        ',')
    return [float(x) if float(x) != int(x) else int(x) for x in inputs]


def get_all():
    n_activity = int(input("how many activities? "))
    path_total = 0
    variance_path = 0
    path_stack = []

    for i in range(n_activity):
        to, tm, tp = get_inputs()
        path_stack.append(f'{to}-{tm}-{tp}')
        path_total += (to + tm * 4 + tp) / 6
        variance_path += ((tp - to)**2) / 36

    SD_path = (variance_path)**(1 / 2)
    print("\nActivity path:\n", "\t".join(path_stack))
    print("\n\npath_total (path mean):", path_total)
    print("variance:", variance_path)
    print("SD:", SD_path)

    proceed = input(
        "Do you wish to proceed and get Z score of specified time? (y/n): ")

    if proceed.lower() == "y":
        specific_event = float(input("What is specified time? "))
        get_project_time(specific_event, path_total, SD_path)


def get_project_time(specific_event, path_total, SD_path):
    Z = (specific_event - path_total) / SD_path
    print("Z score:", Z)
    prob = stats.norm(0, 1).cdf(Z)
    print(
        f"probability of project taking less than {specific_event} is {prob}")


def run():
    print("\n\nWhat do you wish to calculate?")
    print("1. \tPath total, Variance, SD")
    print("2. \tZ score with specified time\n")
    choice = input("1 or 2?\t\t")
    if choice == "1":
        get_all()

    elif choice == "2":
        specific_event = float(input("What is specified time? "))
        path_total = float(input("What is the path total (path mean)? "))
        SD_path = float(input("What is the variance? "))**(1 / 2)
        get_project_time(specific_event, path_total, SD_path)

    else:
        print("Wrong input! Try again.")
        run()

    cont = input("Analyze another path?\t").lower() == "y"
    if cont:
        run()
    print("done")


if __name__ == "__main__":
    run()
