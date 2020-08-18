import pandas as pd
import requests
from bs4 import BeautifulSoup

def cfm_web_scraper(link):
    
    '''
    This function takes a Madden Connected Franchise Link and grabs the most relevant information for people who are putting players on a trade block.     It will be used in a Discord bot for the Franchise. 
    '''
    
    # Request the link and grab its content, setting up our BeautifulSoup parser
    r = requests.get(link)
    c = r.content
    soup = BeautifulSoup(c, 'html.parser')

    # Scrape the classes that give us the player's general information (name, height, weight etc.) as well as contract information (salary, total             years, years left, cap hit etc.) 
    player_info = soup.find_all('div', {'class': 'card flex-row align-items-center align-items-stretch rounded-left Teamcolors'})
    contract_info = soup.find_all('div', {'class': 'd-flex Teamcolors'})
    
    # Take the data from the lists above and replace all of the "new lines" (\n) with spaces, split on those spaces and remove those from the list,           leaving only the info we want.
    contract_info_list = [i for i in contract_info[0].text.replace('\n', ' ').split(' ') + contract_info[1].text.replace('\n', ' ').split(' ') if i != '']
    player_info_list = [i for i in player_info[0].find('div', {'class': 'col-10 py-3 rounded-right cfm-player-info'}).text.replace('\n', ' ').split(' ') if i != '']
    
    d = {}
    
    # Here we are grabbing information from the contract_info_list and player_info_list and will put them into an empty dictionary. All but one player       will fall into the elif or else statement, but Ha Ha Clinton-Dix was a special case, so he was given his own if statement.
    if player_info_list[0] == 'Ha':
        player_info_list.pop(1)
        player_info_list[0] = "Ha'Sean"
        d['Name'] = player_info_list[0] + ' ' + player_info_list[1]
        d['Position'] = player_info_list[2]
        d['Overall'] = player_info_list[4]
        d['Height'] = player_info_list[6]
        d['Weight'] = player_info_list[8]
        d['Age'] = player_info_list[10]
        d['Years in League'] = player_info_list[12]
        d['Dev'] = player_info_list[17]
        d['Trade Value'] = player_info_list[19]
    elif len(player_info_list) == 33:
        d['Name'] = player_info_list[0] + ' ' + player_info_list[1]
        d['Position'] = player_info_list[2]
        d['Overall'] = player_info_list[4]
        d['Height'] = player_info_list[6]
        d['Weight'] = player_info_list[8]
        d['Age'] = player_info_list[10]
        d['Years in League'] = player_info_list[12]
        d['Dev'] = player_info_list[17]
        d['Trade Value'] = player_info_list[19]        
    else:
        d['Name'] = player_info_list[0] + ' ' + player_info_list[1] + ' ' + player_info_list[2]
        d['Position'] = player_info_list[3]
        d['Overall'] = int(player_info_list[5])
        d['Height'] = player_info_list[7]
        d['Weight'] = player_info_list[9]
        d['Age'] = player_info_list[11]
        d['Years in League'] = player_info_list[13]
        d['Dev'] = player_info_list[19]
        d['Trade Value'] = player_info_list[21]   
    
    # Putting the contract info into the dictionary
    d['Contract Total'] = contract_info_list[0]
    d['Years Total'] = contract_info_list[2]
    d['Salary'] = contract_info_list[7]
    d['Cap Hit'] = contract_info_list[9]
    d['Years Left'] = contract_info_list[12]
    
    d['Link'] = link
    
    return pd.DataFrame(d, index=[0])