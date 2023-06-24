from truecallerpy import search_phonenumber

def get_truecaller_info(phone_number, country_code, api_key):
    data = search_phonenumber(phone_number, country_code, api_key)

    # Extracting and returning the desired information
    if 'data' in data and len(data['data']) > 0:
        result = data['data'][0]
        name = result['name']
        email = result['internetAddresses'][0]['id']
        country = result['addresses'][0]['countryCode']
        city = result['addresses'][0]['city']

        return name, email, country, city
    else:
        return None

# Example usage
api_key = "a1i0u--gFEQ8K-D-vzYJeE8wvTQhcKEFbXpERdfDZChE1Y4mcY1LvG7hK6r9V8HV"
phone_number = "+919544047655"
country_code = "IN"

info = get_truecaller_info(phone_number, country_code, api_key)

if info:
    name, email, country, city = info
    print("Name:", name)
    print("Email:", email)
    print("Country:", country)
    print("City:", city)
else:
    print("No information available for the provided phone number.")
