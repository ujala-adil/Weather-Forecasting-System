import requests
from tkinter import *
import pyglet
import datetime


def time_converter(time):
        converted_time = datetime.datetime.fromtimestamp(
            int(time)
        ).strftime('%I:%M %p')
        return converted_time


class Weather:
    '''Displays welcome page of the system'''

    def welcome(self):

        print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t WEATHER APPLICATION")
        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t-----------------------------\n\n')
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t |  Check the weather, anytime,anywhere!  |\n")


    def login(self):
        '''User login function'''

        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t==============================')
        print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLOGIN")
        print('\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t==============================\n\n')

        #FILING
        fw = open('User_records.txt', 'a')
        fw.write(input('Enter your name:  ') + '\n')
        fw.write(input('Enter your e-mail:  ') + '\n\n')
        fw.close()

        password = input('Enter password: ')
        admin_password: str = '12345'

        if admin_password == password:
            return 1
        else:
            return 0




    def url_builder(self, cityName):
        '''Builds a complete url'''

        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + cityName + '&units=metric'
        return url



    def data_fetch(self, url):
        '''Fetches data from server which is in json format'''

        json_data = requests.get(url).json()
        return json_data



    def data_organizer(self, main_weather):
        print('==============================');

        for key in main_weather:
            print('-------------------------\n')
            print(key,main_weather[key]);
            print('-------------------------')

        print('==============================')



    def data_organizer2(self, json_data):
        '''Organizes data into separate variables'''

        data = dict(
            city=json_data.get('name'),
            country=json_data.get('sys').get('country'),
            temp=json_data.get('main').get('temp'),
            temp_max=json_data.get('main').get('temp_max'),
            temp_min=json_data.get('main').get('temp_min'),
            humidity=json_data.get('main').get('humidity'),
            pressure=json_data.get('main').get('pressure'),
            sky=json_data['weather'][0]['main'],
            sunrise=time_converter(json_data.get('sys').get('sunrise')),
            sunset=time_converter(json_data.get('sys').get('sunset')),
            wind=json_data.get('wind').get('speed'),
            wind_deg=json_data.get('deg'),
            dt=time_converter(json_data.get('dt')),
            cloudiness=json_data.get('clouds').get('all'),
            typeid=json_data['weather'][0]['id'],
            wtype=json_data['weather'][0]['description'],
            longitude=json_data['coord'] ['lon'],
            latitude=json_data['coord'] ['lat'],
            visibility=json_data['visibility'],
            icon=json_data['weather'][0]['icon']
        )
        return data



    def data_output(self, data):
        '''Prints formatted data as output'''

        m_symbol = '\xb0' + 'C'
        l_symbol = '\xb0'
        print('')
        print('---------------------------------------')
        print('Current weather in: {}, {}:'.format(data['city'], data['country']))
        print('')
        print('Temperature: ', data['temp'], m_symbol)
        print('Sky: ', data['sky'])
#       print('Maximum Temperature: {}, Minimum Temperature {}'.format(data['temp_max'], data['temp_min']))
        print('')
        print('Maximum Temperature: ', data['temp_max'], m_symbol)
        print('Minimum Temperature: ', data['temp_min'], m_symbol)
        print('')
        print('Wind Speed: {} m/s, Degree: {} \xb0'.format(data['wind'], data['wind_deg']))
        print('Humidity: {}'.format(data['humidity']), '%')
        print('Visibilty: ', data['visibility'], 'meter')
        print('Clouds: {}'.format(data['cloudiness']), '%')
        print('Pressure: {}'.format(data['pressure']), 'hPa')
        print('Sunrise at: {}'.format(data['sunrise']))
        print('Sunset at: {}'.format(data['sunset']))
        print('')
        print('Longitude: ', data['longitude'], l_symbol)
        print('Latitude: ', data['latitude'], l_symbol)
        print('')
        print('Weather ID: {}'.format(data['typeid']))
        print('Last update from the server: {}'.format(data['dt']))
        print('---------------------------------------')
        print('')
        global weatherid
        weatherid=('{}'.format(data['typeid']))
        weathertype=('{}'.format(data['wtype']))
        print('Weather ID: ' + weatherid)
        print('Weather Type: ' + weathertype.title())



    def load_icon(self, icon_id, w_desc, org):

                # create the canvas, size in pixels
        canvas = Canvas(width = 1050, height = 900, bg = 'light blue')

        # pack the canvas into a frame/form
        canvas.pack(expand = YES, fill = BOTH)

        # load the .gif image file
        # put in your own gif file here, may need to add full path
        # like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
        gif1 = PhotoImage(file = icon_id + '.png')

        # put gif image on canvas
        # pic's upper left corner (NW) on the canvas is at x=50 y=10
        canvas.create_image(650, 50, image = gif1, anchor = NW)
        canvas.create_text(680, 150, text=w_desc.title(), font=('Times New Roman', -40,))
        canvas.create_text(650, 220, text='Current weather in: {}, {}:'.format(org['city'] , org['country']), font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 250, text='Sky: ' + str(org['sky']), font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 280, text='Maximum Temperature: ' +  str(org['temp_max']) + '\xb0', font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 310, text='Minimum Temperature: ' +  str(org['temp_min']) + '\xb0', font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 340, text='Wind Speed: {} m/s, Degree: {} \xb0'.format(org['wind'], org['wind_deg']), font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 370, text='Humidity: {}'.format(org['humidity']) + '%', font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 400, text='Visibilty: ' + str(org['visibility']) + 'meter', font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 430, text='Clouds: {}'.format(org['cloudiness']) + '%', font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 460, text='Pressure: {}'.format(org['pressure']) + 'hPa', font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 490, text='Sunrise at: {}'.format(org['sunrise']), font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 510, text='Sunset at: {}'.format(org['sunset']), font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 540, text='Longitude: ' + str(org['longitude']) + '\xb0', font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 570, text='Latitude: ' + str(org['latitude']) + '\xb0', font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 600, text='Weather ID: {}'.format(org['typeid']), font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 630, text='Last update from the server: {}'.format(org['dt']), font=('Calibri', -20, 'bold'))
        canvas.create_text(650, 660, text='Weather Type: {}'.format(org['wtype']), font=('Calibri', -20, 'bold'))

         # run it ...
        mainloop()



    def gif(self, gif_name):
        '''Loads GIF'''

        animation = pyglet.image.load_animation(gif_name + '.gif')
        animSprite = pyglet.sprite.Sprite(animation)

        w = animSprite.width
        h = animSprite.height

        window = pyglet.window.Window(width=w, height=h)

        r,g,b,alpha = 0.5, 0.5, 0.8, 0.5


        pyglet.gl.glClearColor(r,g,b,alpha)

        @window.event
        def on_draw():
            window.clear()
            animSprite.draw()


        pyglet.app.run()



w=Weather()

w.welcome()

log_in = w.login()

if log_in == 1:
    print('\t\t\t\t\t\tCongratulations!  You have successfully logged in.')

else:
    print('\t\t\t\t\t\t\tINVALID PASSWORD!\n\t\t\t\t\tPlease try again.\n')
    w.login()


cityName=input('\n\nEnter city name: ')

url=w.url_builder(cityName)
fetched_data=w.data_fetch(url)
org=w.data_organizer2(fetched_data)
w.data_output(org)
weatherid=('{}'.format(org['typeid']))
icon_id = ('{}'.format(org['icon']))
w_desc=('{}'.format(org['wtype']))
#w.load_icon(icon_id, w.data_output(org))
w.load_icon(icon_id, w_desc, org)

