"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 151317891
Name:       Nguyen The Long
Email:      long.nguyen@tuni.fi

Student Id: 151394898
Name:       Vu Dinh Thi
Email:      thi.vu@tuni.fi
Project 3: Road Trip Optimizer
Examine distances and routes between cities through Finnish highway network

Tom gon lai nhung gi minh can sua lai:
- Đổi tên biến cho phù hợp với nội dung và yêu cầu
- Thêm comment + docstring vào trong bài, chú thích vào trong function, biến,...
- Giải thích phương pháp sắp xếp mảng (nghĩa là sắp xếp các phần tử theo thứ tự) bằng docstring (T có thể dùng phương
 pháp khác, nhưng nói chung là làm vậy thì nó sẽ có trật tự trong biến dictionary hơn, nên t thích dùng phương pháp này)
- Rút ngắn function nếu cảm thấy quá dài, nói chung file t đưa m là nguyên mẫu, nếu trong trường hợp có thể rút ngắn
theo cách kết hợp thì cứ áp dụng
- Có thể xem xét lại phương pháp xác định điều kiện True/False (bởi vì t chỉ dùng biến để xác định điều kiện cho 1 số
hàm while/if nếu có, miễn không thay đổi giá trị nội dung là được)
-... Còn cái gì tự nghĩ ra thì nhớ làm luôn

Lưu ý:
+ M không cần phải tác động vào def find_route (từ dòng 24 đến dòng 91), cứ giữ nguyên như vậy mà không cần thay đổi
+ Nhớ đọc lại file thứ 2 (file 20 điểm đầu tiên) của bài project 6.2 để tham khảo - Nếu muốn có thể tham khảo luôn file
20 điểm cuối cùng
+ Có thể dùng chức năng replace để sửa file, nhưng nhớ cẩn thận
+ Nhớ xem thử nội dung mà assistant chấm cho project 1 của m và t, project 2 để đối chiếu
+ Khi đổi tên biến nhớ lưu ý những biến có sẵn trong template thì không đổi
+ Làm xong rồi thì nhớ xóa mấy cái này
+ Làm xong rồi nhớ test file lại bằng submit only, đừng chọn graded là được

+++ Lỡ m des mà có hư nội dung file này thì file test.py luôn đợi m ở đó
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

    :param data: ?????, A data structure of an unspecified type (you decide)
           which contains the distance information between the cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: list[str], a list of cities the route travels through, or
           an empty list if the route can not be found. If the departure
           and the destination cities are the same, the function returns
           a two element list where the departure city is stores twice.
    """

    # +--------------------------------------+
    # |                                      |
    # |     DO NOT MODIFY THIS FUNCTION!     |
    # |                                      |
    # +--------------------------------------+

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
    :return: ????? | None: A data structure containing the information
             read from the <file_name> or None if any kind of error happens.
             The data structure to be chosen is completely up to you as long
             as all the required operations can be implemented using it.
    """

    # +----------------------------------------------------------------+
    # |                                                                |
    # |  TODO: Implement your own version of read_distance_file here.  |
    # |                                                                |
    # +----------------------------------------------------------------+\
    try:
        file_name = open(file_name, mode='r', encoding="utf-8")
        data = {}
        k = []
        for row in file_name:
            k.append(row.rstrip().split(";"))  # split ";" each row from the file into the list
        for i in range(0, len(k), 1):  # call each list in list k
            listtosmalllist = [[k[i][1]]]
            listtosmalllist[0].append(k[i][2])  # append value of list of list k to list of listtosmallist
            if k[i][0] not in data:
                data[k[i][0]] = listtosmalllist
            else:
                data[k[i][0]] += listtosmalllist
                for u in range(0, len(data[k[i][0]]) - 1):
                    for v in range(u + 1, len(data[k[i][0]])):
                        if data[k[i][0]][u][0] > data[k[i][0]][v][0]:
                            # Change the position of the list of the list of a value of key of dictionary
                            a = data[k[i][0]][u]
                            data[k[i][0]][u] = data[k[i][0]][v]
                            data[k[i][0]][v] = a
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

    :param data: ?????, A data structure containing the distance
           information between the known cities.
    :param city: str, the name of the city whose neighbours we
           are interested in.
    :return: list[str], the neighbouring city names in a list.
             Returns [], if <city> is unknown (i.e. not stored as
             a departure city in <data>) or if there are no
             arrows leaving from the <city>.
    """

    # +--------------------------------------------------------------+
    # |                                                              |
    # |  TODO: Implement your own version of fetch_neighbours here.  |
    # |                                                              |
    # +--------------------------------------------------------------+
    k = []
    if city not in data:
        k = []
    else:
        for i in range(0, len(data[city]), 1):
            k.append(data[city][i][0])
    return k


def distance_to_neighbour(data, departure, destination):
    """
    Returns the distance between two neighbouring cities.
    Returns None if there is no direct connection from
    <departure> city to <destination> city. In other words
    if there is no arrow leading from <departure> city to
    <destination> city.

    :param data: ?????, A data structure containing the distance
           information between the known cities.
    :param departure: str, the name of the departure city.
    :param destination: str, the name of the destination city.
    :return: int | None, The distance between <departure> and
           <destination>. None if there is no direct connection
           between the two cities.
    """

    # +-------------------------------------------------------------------+
    # |                                                                   |
    # |  TODO: Implement your own version of distance_to_neighbour here.  |
    # |                                                                   |
    # +-------------------------------------------------------------------+
    k = None
    for i in range(0, len(data[departure])):
        if data[departure][i][0] == destination:
            k = int(data[departure][i][1])
            break
    if k is None:
        k = 0
    return k


def display(distance_data):
    """Docstring first, m nho sua lai docstring nay cho phu hop"""
    u = []
    for k, v in sorted(distance_data.items()):
        for i in v:
            u.append(f"{k:14}{i[0]:14}{i[1]:>5}")
    return u


def add(distance_data, dptcity, dttcity, distance):
    """Docstring first, m nho sua lai docstring nay cho phu hop"""
    a = []
    k = []
    b = []
    j = []
    b.append(dttcity)
    b.append(distance)
    j.append(b)
    if dttcity not in distance_data:
        distance_data[dttcity] = []

    a.append(dttcity)
    a.append(distance)
    k.append(a)
    if dptcity not in distance_data:
        distance_data[dptcity] = k
    else:
        a = 0
        for i in range(0, len(distance_data[dptcity]), 1):
            if distance_data[dptcity][i][0] == dttcity:
                distance_data[dptcity][i][1] = k[0][1]
                a = 1
                break
        if a == 0:
            distance_data[dptcity] += k
            for u in range(0, len(distance_data[dptcity]) - 1):
                for v in range(u + 1, len(distance_data[dptcity])):
                    if distance_data[dptcity][u][0] > distance_data[dptcity][v][0]:
                        # Change the position
                        a = distance_data[dptcity][u]
                        distance_data[dptcity][u] = distance_data[dptcity][v]
                        distance_data[dptcity][v] = a


def remove(distance_data, dptcity, dttcity):
    """Docstring first, m nho sua lai docstring nay cho phu hop"""
    a = True
    for i in range(0, len(distance_data[dptcity]) - 1):
        if distance_data[dptcity][i][0] == dttcity:
            distance_data[dptcity].remove(distance_data[dptcity][i])
            a = False
    if a:
        print(f"Error: missing road segment between '{dptcity}' and '{dttcity}'.")


def neighbours(distance_data, dptcity):
    """Docstring first, m nho sua lai docstring nay cho phu hop"""
    u = []
    if dptcity not in distance_data:
        u.append(f"Error: '{dptcity}' is unknown.")
    else:
        for i in distance_data[dptcity]:
            u.append(f"{dptcity:14}{i[0]:14}{i[1]:>5}")
    return u


def main():
    input_file = input("Enter input file name: ")
    # input_file = "distances1.txt"
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
            # +----------------------------------------+
            # |                                        |
            # |  TODO: Implement "display" action.     |
            # |                                        |
            # +----------------------------------------+
            ...
            u = display(distance_data)
            print("\n".join(u))
        elif "add".startswith(action):
            # +----------------------------------------+
            # |                                        |
            # |  TODO: Implement "add" action.         |
            # |                                        |
            # +----------------------------------------+
            ...
            dptcity = input("Enter departure city: ")
            dttcity = input("Enter destination city: ")
            distance = input("Distance: ")
            try:
                int(distance)
                add(distance_data, dptcity, dttcity, distance)
            except ValueError:
                print(f"Error: '{distance}' is not an integer.")
        elif "remove".startswith(action):
            # +----------------------------------------+
            # |                                        |
            # |  TODO: Implement "remove" action.      |
            # |                                        |
            # +----------------------------------------+
            ...
            dptcity = input("Enter departure city: ")
            if dptcity not in distance_data:
                print(f"Error: '{dptcity}' is unknown.")
            else:
                dttcity = input("Enter destination city: ")
                remove(distance_data, dptcity, dttcity)
        elif "neighbours".startswith(action):
            # +----------------------------------------+
            # |                                        |
            # |  TODO: Implement "neighbours" action.  |
            # |                                        |
            # +----------------------------------------+
            ...
            dptcity = input("Enter departure city: ")
            u = neighbours(distance_data, dptcity)
            print("\n".join(u))
        elif "route".startswith(action):
            # TODO: Implement "route" action.
            # +----------------------------------------+
            # |                                        |
            # |  TODO: Implement "route" action.       |
            # |                                        |
            # +----------------------------------------+
            ...
            dptcity = input("Enter departure city: ")
            if dptcity not in distance_data:
                print(f"Error: '{dptcity}' is unknown.")
            else:
                dttcity = input("Enter destination city: ")

                c = find_route(distance_data, dptcity, dttcity)

                if not c:
                    print(f"No route found between '{dptcity}' and '{dttcity}'.")
                elif c[0] == c[1]:
                    t = "-".join(c)
                    print(f"{t} (0 km)")
                else:
                    totaldistance = 0
                    for i in range(1, len(c)):
                        for t in range(0, len(distance_data[c[i - 1]])):
                            if distance_data[c[i - 1]][t][0] == c[i]:
                                totaldistance += int(distance_data[c[i - 1]][t][1])
                    t = "-".join(c)
                    print(f"{t} ({totaldistance} km)")

        else:
            print(f"Error: unknown action '{action}'.")


if __name__ == "__main__":
    main()
