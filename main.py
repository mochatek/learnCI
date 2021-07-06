from requests import get
import logging


def predict_age(name):
    response = get('https://api.agify.io/', params={'name': name})
    data = response.json()
    age = data.get('age', None)

    return age


if __name__ == '__main__':
    logging.basicConfig(filename='error.log', filemode='w',
                        format='%(name)s: %(levelname)s %(message)s', level=logging.ERROR)

    print('AGE PREDICTOR -new'.center(30))
    print('-'*30)

    name = 'Mocha'
    age = predict_age(name)

    if age:
        print(f'Your age is: {age}')
    else:
        logging.error(f'Could not predict age for {name}')
