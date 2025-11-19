import json
from dataclasses import dataclass


# 1. Model the data
@dataclass
class Activity:
    activity: str
    activity_type: str
    cost: int
    people: int


# 2. Load the data
def load_data() -> list[Activity]:
    activities: list[Activity] = []
    with open('activities.json') as f:
        for activity in json.load(f):
            activities.append(
                Activity(
                    activity['activity'],
                    activity['type'],
                    activity['cost'],
                    activity['people'],
                )
            )

        return activities


# 3. Generate activities
def generate_activities(activities: list[Activity]) -> None:
    try:
        people: int = int(input('How many people are you? '))
        cost: int = int(input('How much are you willing to spend per person ($)? '))
    except ValueError:
        print('Error: Please only enter numerical values.')
        return

    # Gather the activities that meet the criteria and display them
    matched_activities: list[Activity] = []
    for activity in activities:
        activity_cost: int = activity.cost
        activity_people: int = activity.people

        if activity_cost <= cost and activity_people <= people:
            matched_activities.append(activity)

    if matched_activities:
        for i, matched in enumerate(matched_activities, 1):
            print(f'{i}: {matched.activity}: {matched.cost}$ per person [{people}p: {people * matched.cost}$]')
    else:
        print('No activities matched your criteria...')


# 4. Put it all together
def main() -> None:
    activities: list[Activity] = load_data()
    generate_activities(activities)


if __name__ == '__main__':
    main()

# Homework:
# 1. Add more activities to the script.
# 2. Create an option that allows the user to specify activities that should be indoor
# or outdoor, in case it's raining or something.
