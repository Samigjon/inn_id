import requests
from bs4 import BeautifulSoup

def fetch_org_info(tin):
    url = f"https://orginfo.uz/search/all/?q={tin}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извлечение необходимых данных
        details = {'TIN': tin}

        tin_element = soup.find('span', class_='bg-success bg-opacity-25 text-success px-2 py-1 rounded-5')
        if tin_element:
            details['TIN'] = tin_element.text.strip()

        name_element = soup.find('h6', class_='card-title')
        org_name = name_element.text.strip() if name_element else 'Not Found'
        details['Name'] = org_name

        date_element = soup.find('span', class_='text-body-tertiary ms-1 text-nowrap')
        registration_date = date_element.text.strip() if date_element else 'Not Found'
        details['RegistrationDate'] = registration_date

        address_element = soup.find('p', class_='text-body-tertiary mb-0')
        address = address_element.text.strip() if address_element else 'Not Found'
        details['Address'] = address

        return details
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def fetch_org_info_and_send_to_gas(tin):
    org_info = fetch_org_info(tin)
    if org_info:
        url = 'https://script.google.com/macros/s/AKfycbx5PhUW9rWlksAzO3p3bNg1FC1qap9WSibFCh7k2VnTt7f1CYTX5CNeZnx6xRisi5CUhw/exec'
        response = requests.post(url, json=org_info)
        
        if response.status_code == 200:
            print('Data sent successfully!')
        else:
            print(f'Failed to send data. Status code: {response.status_code}')
            
            
import requests

def send_to_google_sheets(org_info):
    url = 'https://script.google.com/macros/s/AKfycbx5PhUW9rWlksAzO3p3bNg1FC1qap9WSibFCh7k2VnTt7f1CYTX5CNeZnx6xRisi5CUhw/exec'
    response = requests.post(url, json=org_info)
    
    if response.status_code == 200:
        print('Data sent successfully!')
    else:
        print(f'Failed to send data. Status code: {response.status_code}')

# if __name__ == "__main__":
    # tin = "310013168"
    # fetch_org_info_and_send_to_gas(tin)