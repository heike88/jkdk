from jkdk import Jkdk
import os
# import argparse

# parser = argparse.ArgumentParser(description='填入学号和密码')
# parser.add_argument('-c', '--credit', required=True, help='学号')
# parser.add_argument('-p', '--password', required=True, help='密码')

# outputs = parser.parse_args()
# print(f'credit={outputs.credit}, password={outputs.password}')

username = os.environ.get('username')
password = os.environ.get('password')
key = os.environ.get('key')
province = os.environ.get('province')
city = os.environ.get('city')
position = os.environ.get('position')
city = province+city
myvs_26 = os.environ.get('myvs_26', 2)
jingdu = os.environ.get('jingdu', '115.31018')
weidu = os.environ.get('weidu', '34.26915')


print(f'username={username}')
print(f'password={password}')
print(f'SCKEY={key}')
print(f'province={province}')
print(f'city={city}')
print(f'position={position}')
print(f'longitude={jingdu}')
print(f'gratitude={weidu}')

if key == '':
    key = None
m = Jkdk(username, password, key, province=province,
         city=city, position=position, myvs_26=myvs_26, jingdu=jingdu, weidu=weidu)
m.jkdk()
