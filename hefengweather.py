#!/usr/bin/env python3
# encoding : utf-8
'''和风天气API'''

import requests
import UART

cion_list = ['100','101','102','103','104',
             '200','201','202','203','204','205','206','207','208','209','210','211','212','213',
             '300','301','302','303','304','305','306','307','308','309','310','311','312','313',
             '400','401','402','403','404','405','406','407',
             '500','501','502','503','504','507','508',
             '900','901','999']

hefeng_url = 'https://free-api.heweather.com/v5/weather'
hefeng_now_url = 'https://free-api.heweather.com/v5/now'
hefeng_payload = {  'key':'yourkey',  '''add your key here'''
                    'city':'shenzhen'
}

def hefeng_weather():
    '''获取天气'''
    r = requests.get(hefeng_url, params=hefeng_payload)
    if r.status_code == 200:
        #print(r.json())
        print('天气：'+ r.json()['HeWeather5'][0]['now']['cond']['txt'] + 'code：'+ r.json()['HeWeather5'][0]['now']['cond']['code'])
        UART.UART_send('p0.pic=' + str(cion_list.index(r.json()['HeWeather5'][0]['now']['cond']['code'])))
        UART.UART_send('t2.txt=' + '"' + '天气:' + r.json()['HeWeather5'][0]['now']['cond']['txt'] + '"')
        #print(r.json()['HeWeather5'][0]['now']['cond']['code'])

        print('体感温度：'+ r.json()['HeWeather5'][0]['now']['fl'])

        print('温度：'+ r.json()['HeWeather5'][0]['now']['tmp'])
        UART.UART_send('t1.txt=' + '"' + '温度:' + r.json()['HeWeather5'][0]['now']['tmp'] + '"')

        print('湿度：'+ r.json()['HeWeather5'][0]['now']['hum'])
        UART.UART_send('t3.txt=' + '"' + '湿度:' + r.json()['HeWeather5'][0]['now']['hum'] + '"')

        print('风向：'+ r.json()['HeWeather5'][0]['now']['wind']['dir'] + r.json()['HeWeather5'][0]['now']['wind']['sc'])
        UART.UART_send('t4.txt=' + '"' + '风向:' + r.json()['HeWeather5'][0]['now']['wind']['dir'] + r.json()['HeWeather5'][0]['now']['wind']['sc'] + '"')

        print('空气质量：'+ r.json()['HeWeather5'][0]['aqi']['city']['qlty'] + ',PM2.5:' + r.json()['HeWeather5'][0]['aqi']['city']['pm25'])
        UART.UART_send('t7.txt=' + '"' + '空气质量:' + r.json()['HeWeather5'][0]['aqi']['city']['qlty'] + '"')
        UART.UART_send('t8.txt=' + '"' + 'PM2.5:' + r.json()['HeWeather5'][0]['aqi']['city']['pm25'] + '"')

        print('更新时间：'+ r.json()['HeWeather5'][0]['basic']['update']['loc'])
        UART.UART_send('t19.txt=' + '"' + '更新时间:' + r.json()['HeWeather5'][0]['basic']['update']['loc'] + '"')

        print('未来三天预报')

        for i in range(0,3):
            print('-------------------')
            print(r.json()['HeWeather5'][0]['daily_forecast'][i]['date'])
            #print('白天')
            print('白天：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['cond']['txt_d'] +
                  ',夜间：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['cond']['txt_n'])
            print('最高气温：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['tmp']['max'] +
                  '，最低气温：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['tmp']['min'])
            print('风向：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['wind']['dir'] + r.json()['HeWeather5'][0]['daily_forecast'][i]['wind']['sc'])
            print('湿度：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['hum'])
            print('能见度：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['vis'] + 'km')
            print('日出时间：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['astro']['sr'] + '\r\n'
                + '日落时间：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['astro']['ss'] + '\r\n'
                + '月出时间：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['astro']['mr'] + '\r\n'
                + '月落时间：' + r.json()['HeWeather5'][0]['daily_forecast'][i]['astro']['ms']
                )
            
            if(i==0):
                UART.UART_send('t5.txt=' + '"' + '白天:' + r.json()['HeWeather5'][0]['daily_forecast'][i]['cond']['txt_d'] + '"')
                UART.UART_send('t6.txt=' + '"' + '夜间:' + r.json()['HeWeather5'][0]['daily_forecast'][i]['cond']['txt_n'] + '"')
                UART.UART_send('t9.txt=' + '"' + '最低气温:' + r.json()['HeWeather5'][0]['daily_forecast'][i]['tmp']['min'] + '"')
                UART.UART_send('t10.txt=' + '"' + '最高气温:' + r.json()['HeWeather5'][0]['daily_forecast'][i]['tmp']['max'] + '"')
                UART.UART_send('t11.txt=' + '"' + '湿度:' + r.json()['HeWeather5'][0]['daily_forecast'][i]['hum'] + '"')
                UART.UART_send('t12.txt=' + '"' + '能见度:' + r.json()['HeWeather5'][0]['daily_forecast'][i]['vis'] + 'km' + '"')
                UART.UART_send('t13.txt=' + '"' + 'srT:' + r.json()['HeWeather5'][0]['daily_forecast'][i]['astro']['sr'] + '"')
                UART.UART_send('t14.txt=' + '"' + 'ssT:' + r.json()['HeWeather5'][0]['daily_forecast'][i]['astro']['ss'] + '"')
                UART.UART_send('t15.txt=' + '"' + 'mrT:' + r.json()['HeWeather5'][0]['daily_forecast'][i]['astro']['mr'] + '"')
                UART.UART_send('t16.txt=' + '"' + 'msT:' + r.json()['HeWeather5'][0]['daily_forecast'][i]['astro']['ms'] + '"')

            print('-------------------')

        
        print('空气指数：'+ r.json()['HeWeather5'][0]['suggestion']['air']['brf'] + ':' + r.json()['HeWeather5'][0]['suggestion']['air']['txt'])
        print('舒适度指数：'+ r.json()['HeWeather5'][0]['suggestion']['comf']['brf'] + ':' + r.json()['HeWeather5'][0]['suggestion']['comf']['txt'])
        UART.UART_send('t17.txt=' + '"' + '舒适度指数:' + r.json()['HeWeather5'][0]['suggestion']['comf']['brf'] + '"')
        UART.UART_send('t18.txt=' + '"' + r.json()['HeWeather5'][0]['suggestion']['comf']['txt'] + '"')

        print('洗车指数：'+ r.json()['HeWeather5'][0]['suggestion']['cw']['brf'] + ':' + r.json()['HeWeather5'][0]['suggestion']['cw']['txt'])
        print('穿衣指数：'+ r.json()['HeWeather5'][0]['suggestion']['drsg']['brf'] + ':' + r.json()['HeWeather5'][0]['suggestion']['drsg']['txt'])
        print('感冒指数：'+ r.json()['HeWeather5'][0]['suggestion']['flu']['brf'] + ':' + r.json()['HeWeather5'][0]['suggestion']['flu']['txt'])
        print('运动指数：'+ r.json()['HeWeather5'][0]['suggestion']['sport']['brf'] + ':' + r.json()['HeWeather5'][0]['suggestion']['sport']['txt'])
        print('旅游指数：'+ r.json()['HeWeather5'][0]['suggestion']['trav']['brf'] + ':' + r.json()['HeWeather5'][0]['suggestion']['trav']['txt'])
        print('紫外线指数：'+ r.json()['HeWeather5'][0]['suggestion']['uv']['brf'] + ':' + r.json()['HeWeather5'][0]['suggestion']['uv']['txt'])

    else:
        print(r.status_code)
        print(r)

if __name__ == '__main__':
    try:
        hefeng_weather()

    except Exception as ex:
        print(ex)
        raise


