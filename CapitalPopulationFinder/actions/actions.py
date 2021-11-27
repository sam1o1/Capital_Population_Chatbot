# importing libraries that will help in building the custom action 

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

# Making a get method call with the API to get a list of Countries 

src=requests.get('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCountries').json()  

# Applying the lowercase method to avoid faliure in case of getting a lowercase country input. 
countries=src['body']

class CapitalPopulationFinder(Action):
    """
    This Class is used to implement the custom action find_capital_population
    it inherits from the Action parent class. 
    it checks the entities currently stored values
    and accordingly sends the right message.
    for more about the the custom actions in Rasa, Please refer to the documnetation 
    https://learning.rasa.com/conversational-ai-with-rasa/custom-actions/

    """
    def name(self) -> Text:
        return "find_capital_population"

    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """
        This method does the following:
        it gets the currently stored value in the country_name entities and checks
        if it is none or not in countries list, a proper prompt will be displayed.
        it also stores the two values of the capital_name and population_value to figure out
        the right action. for example, if the two indicators are none, it means that 
        the user asks about both the capital and location.

        """
        country = next(tracker.get_latest_entity_values("country_name"), None)
        capital_indicator=next(tracker.get_latest_entity_values("capital_name"), None)
        population_indicator=next(tracker.get_latest_entity_values("population_value"), None)

        if not country:
            msg="It seems you forgot to write a country name!"
            dispatcher.utter_message(text=msg)
            return []

        if country not in countries:      # it checks if the entered country is in the given list
            msg="I am sorry but the country you entered I cannot handle! The following list is what I can handle {}".format(countries)
             
                 
            dispatcher.utter_message(text=msg)
            return []
# this case occurs when the user did not ask about population and capital 
        if (not capital_indicator) and (not population_indicator) :  
            msg="I'm sorry! but you forgot to ask me about a capital or/and Population"
            dispatcher.utter_message(text=msg)
            return[]
# When the user asks only about the capital 
        if (capital_indicator) and  (not population_indicator):
            capital=requests.post('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital',json={"country":country}).json()
            msg=" The capital of {} is {}".format(country,capital['body']['capital'])
            dispatcher.utter_message(text=msg)
            return []
# When the user asks only about the Population 
        if (population_indicator) and (not capital_indicator):
            population=requests.post('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getPopulation',json={"country": country}).json()
            msg=" The Population of {} is {}".format(country,population['body']['population'])
            dispatcher.utter_message(text=msg)
            return []
# When the user asks  about both
        capital=requests.post('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getCapital',json={"country":country}).json()
        population=requests.post('https://qcooc59re3.execute-api.us-east-1.amazonaws.com/dev/getPopulation',json={"country": country}).json()
        msg=" The capital of {} is {} and the population is {}".format(country,capital['body']['capital'],population['body']['population'])
        dispatcher.utter_message(text=msg)
        return []


        

        


