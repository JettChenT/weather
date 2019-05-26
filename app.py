# Weather API
import fire,requests,json

class Weather():
    def __init__(self,config='config.json'):
        with open(config,'r') as f:
            data = json.load(f)
        self.area = data['area']
        self.api_key = data['api_key']
        self.lang = data['lang']
        self.url = "https://free-api.heweather.net/s6/weather/{weather}?location={location}&key={key}"
    def now(self):
        weather_data = requests.get(self.url.format(weather='now',location=self.area,key=self.api_key)).json()
        return weather_data
    def print_now(self):
        weather_data = self.now()
        if self.lang == 'zh-CN':
            n = weather_data['HeWeather6'][0]['now']
            txt = "你好，现在的温度为{temp}度,风向为{wind_dir},天气为{cond_txt}."
            return txt.format(temp = n['tmp'],wind_dir = n['wind_dir'],cond_txt = n['cond_txt'])
        else:
            return "对不起，目前不支持这个语言。"
        
if __name__ == '__main__':
    fire.Fire(Weather)