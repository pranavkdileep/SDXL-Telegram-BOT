from truecallerpy import search_phonenumber

def get_truecaller_info(phone_number):
    api_key = "a1i0v--gGYtPu-hVIu09Kf1xr1w8zKP51SbuabstmmWAqYf4yvpCntqhc6rEm1Np"
    country_code = "IN"
    data = search_phonenumber(phone_number, country_code, api_key)
    print(data)
    

    # Extracting and returning the desired information
    if 'data' in data and len(data['data']) > 0:
        result = data['data'][0]
        name = result.get('name')
        email = result['internetAddresses'][0]['id'] if result['internetAddresses'] else None
        country = result['addresses'][0].get('countryCode')
        city = result['addresses'][0].get('city')
        info = f"Name: {name}\nEmail: {email}\nCountry: {country}\nCity: {city}"
        return info
    else:
        return None

