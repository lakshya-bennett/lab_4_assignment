class FlightTable:
    def __init__(self):
        self.matches = []

    def add_match(self, location, team1, team2, timing):
        self.matches.append({
            "Location": location,
            "Team 01": team1,
            "Team 02": team2,
            "Timing": timing
        })

    def search_by_team(self, team_name):
        team_matches = []
        for match in self.matches:
            if team_name in [match["Team 01"], match["Team 02"]]:
                team_matches.append(match)
        return team_matches

    def search_by_location(self, location_name):
        location_matches = []
        for match in self.matches:
            if location_name == match["Location"]:
                location_matches.append(match)
        return location_matches

    def search_by_timing(self, timing_type):
        timing_matches = []
        for match in self.matches:
            if timing_type == match["Timing"]:
                timing_matches.append(match)
        return timing_matches

def main():
    flight_table = FlightTable()
    flight_table.add_match("Delhi", "India", "England", "DAY")
    flight_table.add_match("Mohali", "India", "Australia", "DAY-NIGHT")
    flight_table.add_match("Delhi", "India", "Australia", "DAY-NIGHT")
    flight_table.add_match("Chennai", "India", "England", "DAY")
    flight_table.add_match("Indore", "Australia", "South Africa", "DAY-NIGHT")
    flight_table.add_match("Mumbai", "Sri Lanka", "Australia", "DAY")

    while True:
        print("Search Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            team_name = input("Enter team name: ")
            team_matches = flight_table.search_by_team(team_name)
            for match in team_matches:
                print(match)
        elif choice == 2:
            location_name = input("Enter location name: ")
            location_matches = flight_table.search_by_location(location_name)
            for match in location_matches:
                print(match)
        elif choice == 3:
            timing_type = input("Enter timing type (DAY/DAY-NIGHT): ")
            timing_matches = flight_table.search_by_timing(timing_type)
            for match in timing_matches:
                print(match)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
