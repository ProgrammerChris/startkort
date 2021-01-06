import mechanicalsoup
import random
import urllib3

def auto_kort(antall):

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = 'http://start.deepwater.com/'

    personer_fil = open("personer.txt", "r", encoding='utf-8')
    kort_fil = open("kort.txt", "r", encoding='utf-8')

    kort_liste = []
    personer = []

    for kort in kort_fil:
        kort_liste.append(kort)

    for person in personer_fil:
        personer.append(person)

    random.shuffle(personer)
    random.shuffle(kort_liste)


    for x in range(antall):
        person = random.choice(personer)
        kort_text = random.choice(kort_liste)
        kort_liste.remove(kort_text)

        browser = mechanicalsoup.StatefulBrowser()
        browser.open(url, verify=False)
        browser.select_form()

        # Start_type
        browser['field_care_card_type[und]'] = '1'

        #Observation - What was seen? *
        browser['field_description_of_issue[und][0][value]'] = kort_text

        #Conversation - What was discussed? *
        browser['field_description_of_recommended[und][0][value]'] = '.'

        #Reinforcement - What was agreed? *
        browser['field_what_did_you_agree_[und][0][value]'] = '.'

        #Company
        browser['field_company_transocean[und]'] = 'Transocean'

        #Unit
        browser['field_unit_transocean[und]'] = 'END - Transocean Endurance'

        #Name
        browser['field_name[und][0][value]'] = person

        #First Name
        browser['field_first_name[und][0][value]'] = '.'

        #The agreement
        browser['field_agreement_transocean[und]'] = '0'

        #Job position
        browser['field_job_position_trancocean[und]'] = '3'

        #Location
        browser['field_location_transocean[und]'] = '4'

        #Behaviors
        browser['field_hazards_transocean[und]'] = '15'

        #Requirements
        browser['field_requirements_transocean[und]'] = '5'

        #Submit
        #browser.launch_browser()

        response = browser.submit_selected()
        if response.status_code == 200:
            print('Startkort ' + str(x+1) + ' av ' + str(antall) + ' sendt!')

    personer_fil.close()
    kort_fil.close()

if __name__ == '__main__':
    auto_kort(21)