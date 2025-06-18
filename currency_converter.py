import json
import requests
import tkinter as tk
from tkinter import ttk, messagebox
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_exchange_rates():
    api_key = os.getenv('EXCHANGE_RATE_API_KEY')
    if not api_key:
        messagebox.showerror("Error", "API key not found. Set EXCHANGE_RATE_API_KEY in .env file.")
        return
    base_currency = base_currency_var.get().split(":")[0].strip().upper()
    target_currency = target_currency_var.get().split(":")[0].strip().upper()
    url = f'https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        
        if data.get('result') == 'error':
            result_label.config(text=f"API Error: {data.get('error-type', 'Unknown error')}")
            return
            
        exchange_rate = data['rates'][target_currency]
        amount = float(amount_entry.get())
        converted_amount = amount * exchange_rate
        result_label.config(text=f'{amount} {base_currency} = {converted_amount:.2f} {target_currency}')
    except requests.RequestException as e:
        result_label.config(text=f'Network Error: {str(e)}')
    except KeyError:
        result_label.config(text='Invalid currency code')
    except ValueError:
        result_label.config(text='Invalid amount')

def read_favorites():
    try:
        with open('favorites.json', 'r') as file:
            favorites = json.load(file)
    except FileNotFoundError:
        favorites = []
    return favorites

def write_favorites(favorites):
    with open('favorites.json', 'w') as file:
        json.dump(favorites, file)

def display_favorites():
    favorites_listbox.grid()
    favorites_listbox.delete(0, tk.END)
    favorites = read_favorites()
    for favorite_pair in favorites:
        favorites_listbox.insert(tk.END, favorite_pair)

def add_to_favorites():
    base_currency = base_currency_var.get().split(":")[0].strip().upper()
    target_currency = target_currency_var.get().split(":")[0].strip().upper()
    favorite_pair = f'{base_currency} to {target_currency}'
    favorites = read_favorites()
    if favorite_pair not in favorites:
        favorites.append(favorite_pair)
        write_favorites(favorites)
        messagebox.showinfo("Success", "Pair added to favorites")
    else:
        messagebox.showinfo("Info", "Pair already in favorites")

def select_favorite_pair(event):
    selected_index = favorites_listbox.curselection()
    if selected_index:
        selected_pair = favorites_listbox.get(selected_index[0])
        base_currency_var.set(selected_pair.split(" to ")[0])
        target_currency_var.set(selected_pair.split(" to ")[1])

def close_favorites_listbox():
    favorites_listbox.grid_remove()

# Initialize Tkinter app
app = tk.Tk()
app.title('Currency Converter')
app.geometry('400x500')

# GUI Elements
amount_label = tk.Label(app, text='Amount:')
amount_label.grid(row=0, column=0, padx=10, pady=5)
amount_entry = tk.Entry(app)
amount_entry.grid(row=0, column=1, padx=10, pady=5)

base_currency_label = tk.Label(app, text='Base Currency:')
base_currency_label.grid(row=1, column=0, padx=10, pady=5)
base_currency_var = tk.StringVar(app)
base_currency_combobox = ttk.Combobox(app, textvariable=base_currency_var, state='normal', width=30)
base_currency_combobox.grid(row=1, column=1, padx=10, pady=5)

target_currency_label = tk.Label(app, text='Target Currency:')
target_currency_label.grid(row=2, column=0, padx=10, pady=5)
target_currency_var = tk.StringVar(app)
target_currency_combobox = ttk.Combobox(app, textvariable=target_currency_var, state='normal', width=30)
target_currency_combobox.grid(row=2, column=1, padx=10, pady=5)

convert_button = tk.Button(app, text='Convert', command=get_exchange_rates)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

result_label = tk.Label(app, text='')
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

favorites_listbox = tk.Listbox(app, width=30)
favorites_listbox.grid(row=5, column=0, columnspan=2, padx=10, pady=5)
favorites_listbox.grid_remove()
favorites_listbox.bind('<<ListboxSelect>>', select_favorite_pair)

add_to_favorites_button = tk.Button(app, text='Add to Favorites', command=add_to_favorites)
add_to_favorites_button.grid(row=6, column=0, padx=10, pady=5)

display_favorites_button = tk.Button(app, text='Show Favorite Pairs', command=display_favorites)
display_favorites_button.grid(row=6, column=1, padx=10, pady=5)

close_favorites_button = tk.Button(app, text='Close Favorite Pairs', command=close_favorites_listbox)
close_favorites_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

# Currency list
currencies = [
    'AED: United Arab Emirates Dirham', 'AFN: Afghan Afghani', 'ALL: Albanian Lek', 'AMD: Armenian Dram',
    'ANG: Netherlands Antillean Guilder', 'AOA: Angolan Kwanza', 'ARS: Argentine Peso', 'AUD: Australian Dollar',
    'AWG: Aruban Florin', 'AZN: Azerbaijani Manat', 'BAM: Bosnia-Herzegovina Convertible Mark',
    'BBD: Barbadian or Bajan Dollar', 'BDT: Bangladeshi Taka', 'BGN: Bulgarian Lev', 'BHD: Bahraini Dinar',
    'BIF: Burundian Franc', 'BMD: Bermudian Dollar', 'BND: Bruneian Dollar', 'BOB: Bolivian Boliviano',
    'BRL: Brazilian Real', 'BSD: Bahamian Dollar', 'BTN: Bhutanese Ngultrum', 'BWP: Botswana Pula',
    'BYN: Belarusian Ruble', 'BZD: Belizean Dollar', 'CAD: Canadian Dollar', 'CDF: Congolese Franc',
    'CHF: Swiss Franc', 'CLP: Chilean Peso', 'CNY: Chinese Yuan Renminbi', 'COP: Colombian Peso',
    'CRC: Costa Rican Colon', 'CUC: Cuban Convertible Peso', 'CUP: Cuban Peso', 'CVE: Cape Verdean Escudo',
    'CZK: Czech Koruna', 'DJF: Djiboutian Franc', 'DKK: Danish Krone', 'DOP: Dominican Peso',
    'DZD: Algerian Dinar', 'EGP: Egyptian Pound', 'ERN: Eritrean Nakfa', 'ETB: Ethiopian Birr', 'EUR: Euro',
    'FJD: Fijian Dollar', 'FKP: Falkland Island Pound', 'FOK: Faroese Króna', 'GBP: British Pound Sterling',
    'GEL: Georgian Lari', 'GGP: Guernsey Pound', 'GHS: Ghanaian Cedi', 'GIP: Gibraltar Pound',
    'GMD: Gambian Dalasi', 'GNF: Guinean Franc', 'GTQ: Guatemalan Quetzal', 'GYD: Guyanese Dollar',
    'HKD: Hong Kong Dollar', 'HNL: Honduran Lempira', 'HRK: Croatian Kuna', 'HTG: Haitian Gourde',
    'HUF: Hungarian Forint', 'IDR: Indonesian Rupiah', 'ILS: Israeli New Shekel', 'IMP: Isle of Man Pound',
    'INR: Indian Rupee', 'IQD: Iraqi Dinar', 'IRR: Iranian Rial', 'ISK: Icelandic Krona', 'JEP: Jersey Pound',
    'JMD: Jamaican Dollar', 'JOD: Jordanian Dinar', 'JPY: Japanese Yen', 'KES: Kenyan Shilling',
    'KGS: Kyrgyzstani Som', 'KHR: Cambodian Riel', 'KID: Kiribati Dollar', 'KMF: Comoran Franc',
    'KPW: North Korean Won', 'KRW: South Korean Won', 'KWD: Kuwaiti Dinar', 'KYD: Caymanian Dollar',
    'KZT: Kazakhstani Tenge', 'LAK: Lao Kip', 'LBP: Lebanese Pound', 'LKR: Sri Lankan Rupee',
    'LRD: Liberian Dollar', 'LSL: Lesotho Loti', 'LYD: Libyan Dinar', 'MAD: Moroccan Dirham',
    'MDL: Moldovan Leu', 'MGA: Malagasy Ariary', 'MKD: Macedonian Denar', 'MMK: Burmese Kyat',
    'MNT: Mongolian Tughrik', 'MOP: Macau Pataca', 'MRU: Mauritanian Ouguiya', 'MUR: Mauritian Rupee',
    'MVR: Maldivian Rufiyaa', 'MWK: Malawian Kwacha', 'MXN: Mexican Peso', 'MYR: Malaysian Ringgit',
    'MZN: Mozambican Metical', 'NAD: Namibian Dollar', 'NGN: Nigerian Naira', 'NIO: Nicaraguan Cordoba',
    'NOK: Norwegian Krone', 'NPR: Nepalese Rupee', 'NZD: New Zealand Dollar', 'OMR: Omani Rial',
    'PAB: Panamanian Balboa', 'PEN: Peruvian Sol', 'PGK: Papua New Guinean Kina', 'PHP: Philippine Peso',
    'PKR: Pakistani Rupee', 'PLN: Polish Zloty', 'PYG: Paraguayan Guarani', 'QAR: Qatari Riyal',
    'RON: Romanian Leu', 'RSD: Serbian Dinar', 'RUB: Russian Ruble', 'RWF: Rwandan Franc',
    'SAR: Saudi Arabian Riyal', 'SBD: Solomon Islander Dollar', 'SCR: Seychellois Rupee',
    'SDG: Sudanese Pound', 'SEK: Swedish Krona', 'SGD: Singapore Dollar', 'SHP: Saint Helenian Pound',
    'SLL: Sierra Leonean Leone', 'SOS: Somali Shilling', 'SRD: Surinamese Dollar', 'SSP: South Sudanese Pound',
    'STN: Sao Tomean Dobra', 'SVC: Salvadoran Colon', 'SYP: Syrian Pound', 'SZL: Swazi Lilangeni',
    'THB: Thai Baht', 'TJS: Tajikistani Somoni', 'TMT: Turkmenistani Manat', 'TND: Tunisian Dinar',
    'TOP: Tongan Pa\'anga', 'TRY: Turkish Lira', 'TTD: Trinidadian Dollar', 'TVD: Tuvaluan Dollar',
    'TWD: Taiwan New Dollar', 'TZS: Tanzanian Shilling', 'UAH: Ukrainian Hryvnia', 'UGX: Ugandan Shilling',
    'USD: United States Dollar', 'UYU: Uruguayan Peso', 'UZS: Uzbekistani Som', 'VES: Venezuelan Bolivar',
    'VND: Vietnamese Dong', 'VUV: Vanuatu Vatu', 'WST: Samoan Tala', 'XAF: Central African CFA Franc BEAC',
    'XCD: East Caribbean Dollar', 'XDR: Special Drawing Rights', 'XOF: CFA Franc', 'XPF: CFP Franc',
    'YER: Yemeni Rial', 'ZAR: South African Rand', 'ZMW: Zambian Kwacha', 'ZWL: Zimbabwean Dollar'
]

base_currency_combobox['values'] = currencies
target_currency_combobox['values'] = currencies

base_currency_combobox.set('USD: United States Dollar')  # Default value
target_currency_combobox.set('EUR: Euro')  # Default value

app.mainloop()
