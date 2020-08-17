import requests
from bs4 import BeautifulSoup

def cfm_web_scraper(link):
    r = requests.get(link)

    c = r.content

    soup = BeautifulSoup(c, 'html.parser')

    player_info = soup.find_all('div', {'class': 'card flex-row align-items-center align-items-stretch rounded-left Teamcolors'})
    contract_info = soup.find_all('div', {'class': 'd-flex Teamcolors'})
    
    d = {}
    
    contract_info_list = [i for i in contract_info[0].text.replace('\n', ' ').split(' ') + contract_info[1].text.replace('\n', ' ').split(' ') if i != '']
    player_info_list = [i for i in player_info[0].find('div', {'class': 'col-10 py-3 rounded-right cfm-player-info'}).text.replace('\n', ' ').split(' ') if i != '']
    
    if player_info_list[0] != 'Ha':
        d['Name'] = player_info_list[0] + ' ' + player_info_list[1]
        d['Position'] = player_info_list[2]
        d['Overall'] = int(player_info_list[4])
    else:
        player_info_list.pop(1)
        player_info_list[0] = "Ha'Sean"
        d['Name'] = player_info_list[0] + ' ' + player_info_list[1]
        d['Position'] = player_info_list[2]
        d['Overall'] = int(player_info_list[4])

    d['Height'] = player_info_list[6]
    d['Weight'] = player_info_list[8]
    d['Age'] = player_info_list[10]
    d['Years in League'] = player_info_list[12]

    d['Dev'] = player_info_list[17]
    d['Trade Value'] = player_info_list[19]
    
    d['Contract Total'] = contract_info_list[0]
    d['Years Total'] = contract_info_list[2]
    d['Salary'] = contract_info_list[7]
    d['Cap Hit'] = contract_info_list[9]
    d['Years Left'] = contract_info_list[12]
    
    d['Link'] = link
    
    return d