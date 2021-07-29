maps = {"name": "stiven", "lastname": "perez", "age": 12, "city": "bogota"}

# for key, value in maps.items():
#     print(key, value)
numbers = [1, 2, 3, 4, 5, 6]

ipAddress = {"R1": " 10.1.1.1", "R2": "10.2.2.1", "R3": " 10.3.1"}

ipAddress["S2"] = "23.42.34"


def iter_map(map: dict):
    for key, value in map.items():
        print(f"The key is: {key} and the value is: {value}")

    for key, value in ipAddress.items():
        print(f"the router: {key}, have the ip: {value}")

    print(f'the router "R1" has the ip : {ipAddress["R1"]}')

    for key in numbers:
        print(key)


iter_map(maps)
