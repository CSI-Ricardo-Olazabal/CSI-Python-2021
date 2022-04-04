import requests
import bs4
res = requests.get('https://forecast.weather.gov/MapClick.php?lat=18.01165000000003&lon=-66.61441999999994#.YkroCyjMKUk')
res.raise_for_status()
Weather = bs4.BeautifulSoup(res.content, 'html.parser')
sevenDay = Weather.find(id="seven-day-forecast")
forecast_items = sevenDay.find_all(class_="tombstone-container")
tonight = forecast_items[1]
period = tonight.find(class_="period-name").get_text()
img = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp temp-low").get_text()
print(period+": "+img+", "+temp)