
import datetime
import random
import time

print("La paradoja del cumpleaños")

birthdays = {}


def bday_collision_test(num_people) -> bool:
    birthdays.clear()
    iteration_runner = 0
    for i in range(num_people):
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 12, 31)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        if f'{random_date}' in birthdays:
            return True
        else:
            birthdays[f'{random_date}'] = iteration_runner

        iteration_runner += 1

    return False


def experiment(num_experiments: int, num_people: int):
    collisions = 0
    for i in range(num_experiments):
        if bday_collision_test(num_people):
            collisions += 1

    print(f'for {num_people} num of people and a {num_experiments} experiments, collision fraction: {float(collisions) / float(num_experiments)}')


def main():
    experiment(100, 20)
    experiment(100, 30)
    experiment(100, 45)


main()
