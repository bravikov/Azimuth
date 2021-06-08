from geographiclib.geodesic import Geodesic

'''
Возвращает азимут по направлению от координаты 1 к координате 2 
и расстояние между этими координатами.

Результат помещается в словарь с полями:
    'distance' (расстояние),
    'azimuth' (азимут).
Поля содержат значения типа float.

Возвращает None, если азимут и расстоние недоступны.

Проверить работу функции можно с помощью вызова:
    get_azimuth_and_distance(55.751052, 37.623968, 50.45, 30.524166)
который должен вернуть:
    {'distance': 755.092, 'azimuth': 221.693}.
'''


def get_azimuth_and_distance(latitude1, longitude1, latitude2, longitude2):
    result = Geodesic.WGS84.Inverse(latitude1, longitude1, latitude2, longitude2)
    
    distance_km = result['s12'] / 1000
    azimuth = result['azi1']

    if azimuth < 0:
        azimuth = 360 + azimuth

    distance_km = round(distance_km, 3)
    azimuth = round(azimuth, 3)
    
    return {'distance': distance_km, 'azimuth': azimuth}
