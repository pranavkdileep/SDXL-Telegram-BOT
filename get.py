from truecallerpy import search_phonenumber

def get_truecaller_info(phone_number):
    api_key = "a1i0u--gFEQ8K-D-vzYJeE8wvTQhcKEFbXpERdfDZChE1Y4mcY1LvG7hK6r9V8HV"
    country_code = "IN"
    data = search_phonenumber(phone_number, country_code, api_key)
    

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

# Example usage
