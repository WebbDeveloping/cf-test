

def get_temperature_by_city(city: str = "Provo"):
    # is there a better way of doing this?
    if city == "Springville":
        return 'unknown!'
    if city == 'pleasant grove':
        return 80    
    if city != 'Pleasant Grove':    
        temperature = temperature_data.get(city.capitalize(), 76)
    else:
        temperature = temperature_data.get(city, 76)  


    print('temp', temperature)
    return temperature


def convert_fahrenheit_to_celsius(ftemp):
    return round((ftemp - 32) * 5 /9)


temperature_data = {
    "Provo": 72,
    "Orem": 78,
    "Lindon": 66,
    "Pleasant Grove": 80
}