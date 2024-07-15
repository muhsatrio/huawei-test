from fastapi import HTTPException
import requests
from constant import weather_mapping, mapping_province_url
import xmltodict

def get(province, city):
    if mapping_province_url[province] is None:
        raise HTTPException(status_code=404, detail="province is Not Found")

    api_url = mapping_province_url[province]

    results = requests.get(api_url)

    parsed_results = xmltodict.parse(results.content)

    converted_data = convert_weather_data(parsed_results['data']['forecast']['area'])

    if (city is None):
        return converted_data

    for data in converted_data:
        if data['key'] == city:
            return data
        
    raise HTTPException(status_code=404, detail="city is Not Found")

def get_list_provinces():
    result = []
    for province in mapping_province_url:
        result.append(province)

    return result

def convert_weather_data(list_of_area):
    result = []
    for area in list_of_area:
        new_dict = {}
        new_dict['city'] = area['@description']
        description = area['@description'].replace(".", "")
        new_dict['key'] = "-".join(description.lower().split())
        if "parameter" in area:
            for parameter in area['parameter']:
                if parameter['@id'] == 'weather':
                    time_ranges = []
                    for time_range in parameter['timerange']:
                        temp_dict = {}
                        year = time_range['@datetime'][:4]
                        month = time_range['@datetime'][4:6]
                        date = time_range['@datetime'][6:8]
                        hour = time_range['@datetime'][8:10]
                        temp_dict['date_time'] = f"{year}-{month}-{date} {hour}:00:00"
                        temp_dict['weather'] = weather_mapping[time_range['value']['#text']]
                        time_ranges.append(temp_dict)
                    new_dict['weather'] = time_ranges
                if parameter['@id'] == 'tmax':
                    time_ranges = []
                    for time_range in parameter['timerange']:
                        temp_dict = {}
                        year = time_range['@datetime'][:4]
                        month = time_range['@datetime'][4:6]
                        date = time_range['@datetime'][6:8]
                        temp_dict['date_time'] = f"{year}-{month}-{date} 00:00:00"
                        temp_dict["temperature_in_celcius"] = int(time_range['value'][0]['#text'])
                        time_ranges.append(temp_dict)
                    new_dict['max_temperature'] = time_ranges
            result.append(new_dict)
    return result