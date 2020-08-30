from termcolor import colored
import pandas as pd
import datetime

activity = []
activity.insert(0, "")
activity.insert(1, 1)
activity.insert(2, 1)

activity_pd = pd.Series([1, 3, 2], index=['start', 'end', 'duration'])

activities = []
activities_data = {'name': [],
                   'start': [],
                   'end': [],
                   'duration': []
                   }

activities_df = pd.DataFrame(activities_data, columns=['name', 'start', 'end', 'duration'])


def write_csv(d):
    d.to_csv("log.csv", sep=";")


def append_activities(name, start, end, duration):
    new_data = {'name': [name],
                'start': [start],
                'end': [end],
                'duration': [duration]
                }
    new_df = pd.DataFrame(new_data, columns=['name', 'start', 'end', 'duration'])
    return activities_df.append(new_df, ignore_index=True)


def start_activity():
    print("criar uma nova atividade")
    activity.insert(0, input("Choose a name for the activity: "))
    activity.insert(1, datetime.datetime.now())
    activity.insert(2, activity[1])


def end_activity():
    activity.insert(1, datetime.datetime.now())
    print("Terminate actual activity")
    return append_activities(activity[0], activity[1], activity[2], activity[2] - activity[1])


def actual_activity():
    print(f"Started in: {activity[1]}\n Ended in: {activity[2]} \n duration: {activity[2] - activity[1]}")


if __name__ == '__main__':
    while True:
        choice = str(input("1. to start a new activity \n2. end actual activity \n10. write to csv \nquit. to quit \n :"))
        if choice == "1":
            if activity[0]=="":
                start_activity()
            else:
                print(f"the activity {activity[0]} was not terminated.")
        elif choice == "2":
            if activity[0] != "":
                activities_df = end_activity()
                activity[0] = ""
                activity[1] = 0
                activity[2] = 0
            else:
                print("The activity was not initiated.")
        elif choice == "10":
            write_csv(activities_df)
        elif choice=="quit":
            exit()
        else:
            print(colored(f"{choice} is not an option.", "red"))
