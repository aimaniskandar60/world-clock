from WorldTimeAPI import service
from datetime import datetime
import countries


def get_timezone():
    client = service.Client('timezone')
    country = None
    location = None
    states = None
    continent = None

    while not country:
        country_input = str(input("Provide a country to lookup its timezone: "))
        country = countries.get_country_data(country_input)
    
    print(f"\nYou chose {country.name}!")

    states = countries.get_states_data(country.alpha_2)
    states_uppercase = [state.upper() for state in states]
    print(f"\nHere are the available states in {country.name}: "+", ".join(states))

    valid_location = False
    while not valid_location:
        location = str(input("\nSelect one of the above states to include in your timezone lookup: "))
        try:
            if location.upper() not in states_uppercase:
                raise ValueError
            valid_location = True
        except ValueError:
            print("Please select a valid state.")

    continent = countries.get_continent(country.alpha_2)

    # Area is the continent
    # Location is the state
    payload = {
        "area": continent,
        "location": location
    }

    response = client.get(**payload)
    current_date_time = datetime.strptime(response.datetime, "%Y-%m-%dT%H:%M:%S.%f%z")
    print(current_date_time.strftime("%B"))


    print(f"\nIt is currently {current_date_time.strftime("%A, %B %-d")} in {country.name}")
    print(f"\nThe time is {current_date_time.strftime("%I:%M %p")}")

if __name__ == "__main__":
    get_timezone()





