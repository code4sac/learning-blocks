import json
import requests
import csv

import numpy as np
import matplotlib.pyplot as plt
import addcopyfighandler


def make_url(school_code, student_id, cert):
    url = 'https://demo.aeries.net/aeries/api/v5/schools/%d/students' % school_code
    if student_id is not None:
        url += '/%d' % student_id
    url += '?cert=%s' % cert
    return url


def get_data_from_url(url):
    response = requests.get(url)
    return json.loads(response.text)


def write_json_file(data, filename):
    file = open(filename, 'w')
    json.dump(data, file)
    file.close()
    return file


def write_csv_file(data, filename):
    file = open(filename, 'w', newline='')
    writer = csv.writer(file)
    writer.writerow(data[0].keys())         # Todo: This is assuming all entries have the same keys
    for student in data:
        writer.writerow(student.values())
    file.close()
    return file


# Todo: Generalize to not need the z_field (i.e the user just wants 1 histogram)
def count_fields(data, x_field, y_field, z_field):
    # Find all the keys for counting
    z_keys = set()
    y_keys = set()
    x_keys = set()
    for entry in data:
        z_keys.add(entry[z_field])
        y_keys.add(entry[y_field])
        x_keys.add(entry[x_field])
    z_keys = list(z_keys)
    y_keys = list(y_keys)
    x_keys = list(x_keys)

    # Init some arrays
    arrays = {}
    for z_key in z_keys:
        arrays[z_key] = np.zeros((len(y_keys), len(x_keys)))

    # Count the data
    for entry in data:
        z_key = entry[z_field]
        y_index = y_keys.index(entry[y_field])
        x_index = x_keys.index(entry[x_field])
        arrays[z_key][y_index][x_index] += 1

    return arrays, (x_keys, y_keys, z_keys)


def plot_histograms(histograms, keys):
    for z_key in histograms:
        plt.imshow(histograms[z_key])
        for (j, i), value in np.ndenumerate(histograms[z_key]):
            plt.text(i, j, int(value), ha='center', va='center')

        plt.title('z key = %s' % z_key)
        plt.xticks(np.arange(len(keys[0])), keys[0])
        plt.yticks(np.arange(len(keys[1])), keys[1])
        plt.xlabel('x key')
        plt.ylabel('y key')
        plt.show()


def main(
        school_code=994,
        student_id=None,
        cert='477abe9e7d27439681d62f4e0de1f5e1',
        json_filename='data.json',
        csv_filename='data.csv',
        histogram_csv_filename='histograms.csv',
        x_field='AttendanceProgramCodePrimary',
        y_field='Grade',
        z_field='InactiveStatusCode'
):

    # Make the url
    url = make_url(school_code, student_id, cert)

    # Get the data
    data = get_data_from_url(url)

    # Write the data to a json file
    json_file = write_json_file(data, json_filename)

    # Write the data to a csv file
    csv_file = write_csv_file(data, csv_filename)

    # Histogram the data
    histograms, keys = count_fields(data, x_field, y_field, z_field)

    # Todo: Make into a function
    histogram_csv_file = open(histogram_csv_filename, 'w', newline='')
    writer = csv.writer(histogram_csv_file)
    for z_key in histograms:
        writer.writerow(['%s = %s' % (z_field, z_key)])
        writer.writerow(['%s / %s' % (y_field, x_field)] + keys[0])
        for i, row in enumerate(histograms[z_key]):
            writer.writerow([keys[1][i]] + row.tolist())
        writer.writerow('')
    histogram_csv_file.close()

    # Sanity check
    plot_histograms(histograms, keys)

    return json_file, csv_file, histogram_csv_file


if __name__ == '__main__':
    main()
