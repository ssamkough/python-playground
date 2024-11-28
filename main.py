import csv

import requests

from shapes import Circle


def main():
    # class
    circle = Circle((2, 3), 2)
    print(circle)
    
    print(circle.center)
    print(circle.distance)
    
    circle.center = (4, 6)
    print(circle.center)
    print(circle.distance)

    # requests
    r = requests.get('https://dog.ceo/api/breed/hound/images/random/3')
    print(r.status_code)
    r_dict = r.json()

    for key in r_dict:
        print(key)

    if r_dict['message'] is not None:
        print('\nmessage key: ', r_dict['message'])
        print('\namt of messages: ', len(r_dict['message']))

    payload = {'key1': 'value1', 'key2': 'value2'}
    r2 = requests.get('https://httpbin.org/get', params=payload)
    print('\n', r2.status_code)

    # reading / writing files
    with open('requirements.txt') as f:
        content = f.read()
    
    print('\n', content)

    with open('people.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['Name'] + ['Bday'])
        writer.writerow(['Sammy', '1998-03-17'])
        writer.writerow(['Timaf', '1998-07-16'])
        
    print('\n')

    with open('people.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            print(', '.join(row))

    with open('people.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        print('\nheadings line', next(reader))
        print('first line', next(reader))



if __name__ == '__main__':
    main()