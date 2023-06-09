"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student ID: 151317891
Name:       Nguyen The Long
Email:      long.nguyen@tuni.fi

Project 3: Road Trip Optimizer
This program is to find the shortest route between two cities. The program
will read the distance information from a file and store it in a suitable
data structure. Then, it will find the shortest route between two cities
using Dijkstra's algorithm (Prediction based on the template code). 
Finally, it will print out the route and the total distance of the route.
"""


def find_route(data, departure, destination):
    """
    This function tries to find a route between <departure>
    and <destination> cities. It assumes the existence of
    the two functions fetch_neighbours and distance_to_neighbour
    (see the assignment and the function templates below).
    They are used to get the relevant information from the data
    structure <data> for find_route to be able to do the search.

    The return value is a list of cities one must travel through
    to get from <departure> to <destination>. If for any
    reason the route does not exist, the return value is
    an empty list [].

    :param data: dict[str, dict[str, int]], A data structure of an unspecified type (you decide)
           which contains the distance information between the cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or
           an empty list if the route can not be found. If the departure
           and the destination cities are the same, the function returns
           a two element list where the departure city is stores twice.
    """
    if departure not in data:
        return []

    elif departure == destination:
        return [departure, destination]

    greens = {departure}
    deltas = {departure: 0}
    came_from = {departure: None}

    while True:
        if destination in greens:
            break

        red_neighbours = []
        for city in greens:
            for neighbour in fetch_neighbours(data, city):
                if neighbour not in greens:
                    delta = deltas[city] + distance_to_neighbour(data, city, neighbour)
                    red_neighbours.append((city, neighbour, delta))

        if not red_neighbours:
            return []

        current_city, next_city, delta = min(red_neighbours, key=lambda x: x[2])

        greens.add(next_city)
        deltas[next_city] = delta
        came_from[next_city] = current_city

    route = []
    while True:
        route.append(destination)
        if destination == departure:
            break
        destination = came_from.get(destination)

    return list(reversed(route))


def read_distance_file(file_name):
    """
    Reads the distance information from <file_name> and stores it
    in a suitable data structure (you decide what kind of data
    structure to use). This data structure is also the return value,
    unless an error happens during the file reading operation.

    :param file_name: str, The name of the file to be read.
    :return: dict[str, dict[str, int]] | None: A data structure containing the information
             read from the <file_name> or None if any kind of error happens.
             The data structure to be chosen is completely up to you as long
             as all the required operations can be implemented using it.
    """
    try:
        file_name = open(file_name, mode="r", encoding="utf-8")
        data = {}

        for row in file_name:
            row = row.rstrip().split(";")

            if row[0] not in data:
                data[row[0]] = {row[1]: int(row[2])}
            else:
                data[row[0]][row[1]] = int(row[2])

        file_name.close()
        return data

    except FileNotFoundError:
        return None


def fetch_neighbours(data, city):
    """
    Returns a list of all the cities that are directly
    connected to parameter <city>. In other words, a list
    of cities where there exist an arrow from <city> to
    each element of the returned list. Return value is
    an empty list [], if <city> is unknown or if there are no
    arrows leaving from <city>.

    :param data: dict[str, dict[str, int]], A data structure containing the distance
           information between the known cities.
    :param city: str, the name of the city whose neighbours we
           are interested in.
    :return: list[str], the neighbouring city names in a list.
             Returns [], if <city> is unknown (i.e. not stored as
             a departure city in <data>) or if there are no
             arrows leaving from the <city>.
    """
    if city not in data:
        return []
    return list(data[city].keys())


def distance_to_neighbour(data, departure, destination):
    """
    Returns the distance between two neighbouring cities.
    Returns None if there is no direct connection from
    <departure> city to <destination> city. In other words
    if there is no arrow leading from <departure> city to
    <destination> city.

    :param data: dict[str, dict[str, int]], A data structure containing the distance
           information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: int | None, The distance between <departure> and
           <destination>. None if there is no direct connection
           between the two cities.
    """
    if departure == destination:
        return 0

    # Check if departure is in destination and return the distance
    if departure in data and destination in data[departure]:
        return int(data[departure][destination])

    return 0


def display(distance_data):
    """
    Displays the contents of the data structure <distance_data> in
    alphabetical order according to the departure cities. The display
    format is as the description of the assignment specifies.

    :param distance_data: dict[str, dict[str, int]], A data structure containing the distance
              information between the known cities.
    :return: None
    """

    # Create a copy of distance_data for printing
    print_data = distance_data.copy()

    # Sort the dictionary according to the departure cities
    print_data = sorted(print_data.items())

    # Print the data
    for departure, destinations in print_data:
        # Sort the destinations according to the destination cities
        destinations = sorted(destinations.items())

        for destination, distance in destinations:
            print(f"{departure:<14}{destination:<14}{distance:>5}")


def add(distance_data, dptcity, dttcity, distance):
    """
    Adds a new road segment between <dptcity> and <dttcity> with
    the length <distance> to the data structure <distance_data>.
    If <dptcity> or <dttcity> is not a known city, adds the city
    to the data structure. If there already exists a road segment
    between <dptcity> and <dttcity>, updates the length of the
    road segment to the new value <distance>.

    :param distance_data: dict[str, dict[str, int]], A data structure containing the distance
                information between the known cities.
    :param dptcity: str, the name of the departure city.
    :param dttcity: str, the name of the destination city.
    :param distance: int, the length of the road segment between
                <dptcity> and <dttcity>.
    :return: None
    """
    if dptcity not in distance_data:
        distance_data[dptcity] = {dttcity: distance}
    else:
        distance_data[dptcity][dttcity] = distance


def remove(distance_data, dptcity, dttcity):
    """
    Removes the road segment between <dptcity> and <dttcity>
    from the data structure <distance_data>. If <dptcity> or
    <dttcity> is not a known city or if there is no road
    segment between the two cities, does nothing.

    :param distance_data: dict[str, dict[str, int]], A data structure containing the distance
                information between the known cities.
    :param dptcity: str, the name of the departure city.
    :param dttcity: str, the name of the destination city.
    :return: None
    """

    if dptcity not in distance_data:
        print(f"Error: '{dptcity}' is unknown.")
    elif dttcity not in distance_data[dptcity]:
        print(f"Error: missing road segment between '{dptcity}' and '{dttcity}'.")
    else:
        del distance_data[dptcity][dttcity]


def check_departure(distance_data, dptcity):
    """
    Checks if <dptcity> is a departure city in <distance_data>.
    If <dptcity> is not a departure city, prints an error message
    and returns False. Otherwise returns True.

    :param distance_data: dict[str, dict[str, int]], A data structure containing the distance
                information between the known cities.
    :param dptcity: str, the name of the departure city.
    :return: bool, True if <dptcity> is a departure city in <distance_data>,
                False otherwise.
    """
    dptcity_in_data = False
    # Check if dptcity is in distance_data
    if dptcity not in distance_data:
        for departure, destinations in distance_data.items():
            if dptcity in destinations:
                dptcity_in_data = True
                break

        if not dptcity_in_data:
            print(f"Error: '{dptcity}' is unknown.")
    else:
        dptcity_in_data = True

    return dptcity_in_data


def neighbours(distance_data, dptcity):
    """
    Prints all the cities that are directly connected to
    <dptcity>. In other words, prints all the cities where
    there exist an arrow from <dptcity> to the city in question.
    If <dptcity> is not a known city, prints an error message.

    :param distance_data: dict[str, dict[str, int]], A data structure containing the distance
                information between the known cities.
    :param dptcity: str, the name of the city whose neighbours we
                are interested in.
    """

    dptcity_in_data = check_departure(distance_data, dptcity)

    # Print the neighbours
    if dptcity_in_data:
        print_data = distance_data.copy()

        # Sort the dictionary according to the departure cities
        print_data = sorted(print_data.items())

        for departure, destinations in print_data:
            if departure == dptcity:
                # Sort the destinations according to the destination cities
                destinations = sorted(destinations.items())

                # Print the data
                for destination, distance in destinations:
                    print(f"{departure:<14}{destination:<14}{distance:>5}")


def print_route(distance_data, dptcity, dttcity):
    """
    Prints the route from <dptcity> to <dttcity> if such a route
    exists. The route is printed as a sequence of city names
    separated by a dash "-". If there is no route between the
    cities, prints an error message.

    :param distance_data: dict[str, dict[str, int]], A data structure containing the distance
                information between the known cities.
    :param dptcity: str, the name of the departure city.
    :param dttcity: str, the name of the destination city.
    :return: None
    """
    route_found = find_route(distance_data, dptcity, dttcity)
    
    if not route_found:
        print(f"No route found between '{dptcity}' and '{dttcity}'.")
    else:
        # Calculate the total distance
        total_distance = 0
        
        for i in range(1, len(route_found)):
            total_distance += distance_to_neighbour(
                distance_data, route_found[i - 1], route_found[i]
            )

        # Print the route
        route = "-".join(route_found)
        print(f"{route} ({total_distance} km)")


def main():
    input_file = input("Enter input file name: ")
    distance_data = read_distance_file(input_file)

    if distance_data is None:
        print(f"Error: '{input_file}' can not be read.")
        return

    while True:
        action = input("Enter action> ")

        if action == "":
            print("Done and done!")
            return
        elif "display".startswith(action):
            display(distance_data)

        elif "add".startswith(action):
            dptcity = input("Enter departure city: ")
            dttcity = input("Enter destination city: ")
            distance = input("Distance: ")

            try:
                int(distance)
                add(distance_data, dptcity, dttcity, distance)
            except ValueError:
                print(f"Error: '{distance}' is not an integer.")

        elif "remove".startswith(action):
            dptcity = input("Enter departure city: ")
            
            if dptcity not in distance_data:
                print(f"Error: '{dptcity}' is unknown.")
            else:
                dttcity = input("Enter destination city: ")
                remove(distance_data, dptcity, dttcity)

        elif "neighbours".startswith(action):
            dptcity = input("Enter departure city: ")
            neighbours(distance_data, dptcity)

        elif "route".startswith(action):
            dptcity = input("Enter departure city: ")
            dptcity_in_data = check_departure(distance_data, dptcity)
            
            if dptcity_in_data:
                dttcity = input("Enter destination city: ")
                print_route(distance_data, dptcity, dttcity)

        else:
            print(f"Error: unknown action '{action}'.")


if __name__ == "__main__":
    main()
