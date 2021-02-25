import mechanicalsoup
import random
import urllib3
import time
import os


def auto_kort(antall):

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    url = 'http://start.deepwater.com/'

    os.remove("brukte.txt")

    kort_fil = open("kort.txt", "r", encoding='utf-8')
    
    kort_liste = []
    tid = 0

    print("Startkort presse starter!")

    for kort in kort_fil:
        kort_liste.append(kort)

    random.shuffle(kort_liste)

    for x in range(antall):
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
        browser['field_name[und][0][value]'] = '*'

        #First Name
        browser['field_first_name[und][0][value]'] = '*'

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

        print('Sender kort ' + str(x+1) + ' av ' + str(antall) + '...') 

        response = browser.submit_selected()
        if response.status_code == 200:
          
          # Skriver kort til fil så man kan se hva som er sendt.
          sendte_kort = open("brukte.txt", "a")
          sendte_kort.write(kort_text)
          sendte_kort.close()

          print('Startkort ' + str(x+1) + ' av ' + str(antall) + ' sendt!')
          
          if (x+1) != antall:
            tid = random.randint(60, 600) # 60-600 sekunder pause mellom hvert kort
            print('Neste kort sendes om ' + "%.2f" % (tid/60) + ' minutter')
            time.sleep(tid)

    ubrukte_kort = open("ubrukte.txt", "a")
    for kort in kort_liste:
      ubrukte_kort.write(kort)

    ubrukte_kort.close()
    kort_fil.close()
    print("Startkort presse stoppet!")

if __name__ == '__main__':
    auto_kort(1)