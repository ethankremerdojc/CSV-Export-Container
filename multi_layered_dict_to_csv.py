import csv
# Read a dictionary, and convert it into a readable csv file. Can contain any number of lists or dicts.

my_test_container = {"stuff": ['thing', 'thing2', None, ['a','b']], "Other Stuff":['Meh', {"thing":[1, 2, 3, ["End!"]]}]}

test_container = {"stuff":[1, 2, 3], "things":[1, [1, 2], [1, 2]]}

def get_depth(container):

    if type(container) not in [dict, list] or container in [{}, []]:
        return 0

    max_depth = 1

    for item in container:
        if type(container) == dict:
            item = container[item]

        depth = get_depth(item) + 1

        if depth > max_depth:
            max_depth = depth

    # print(f"Max depth of {container}: {max_depth}")
    return max_depth

get_depth(test_container)

def csv_export_container(container, file):

    with open(file, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([container])

        def write_container(container, column):

            c_depth = get_depth(container)

            row = ['' for _ in range(column)]

            if c_depth == 0:
                csv_writer.writerow(row + [container])
            else:
                if type(container) == list:
                    csv_writer.writerow(row + ["list: [["])

                    for item in container:
                        write_container(item, column + 1)

                    csv_writer.writerow(row + ["]]"])

                if type(container) == dict:
                    csv_writer.writerow(row + ["dict: {{"])
                    for item in container:
                        csv_writer.writerow(row + ["", item + ":"])
                        item = container[item]
                        write_container(item, column + 2)

                    csv_writer.writerow(row + ["}}"])

        write_container(container, 0)

csv_export_container(my_test_container, 'test.csv')

#* Depth 1: Single object "hello", 1, None, [], {} etc.
#* Depth 2: [1](container with an object)
#* Depth 3: [1, [1, 2]] container containing a container containing objects