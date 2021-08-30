from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from flask_mail_check import send_email
import zomatopy
import json
from zomato_budget import results

user_key = "1ef184a660cc5ce371a2a2d8b3da7de4"

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')

		global restaurants

		restaurants = results(loc, cuisine, price)
		top5 = restaurants.head(5) 
		
		# top 5 results to display
		if len(top5)>0:
			response = 'Showing you top results:' + "\n"
			for index, row in top5.iterrows():
				response = response + str(row["restaurant_name"]) + ' (rated ' + row['restaurant_rating'] + ') in ' + row['restaurant_address'] + ' and the average budget for two people ' + str(row['budget_for2people'])+"\n"
		else:
			response = 'No restaurants found' 

		dispatcher.utter_message(str(response))
        

dict_city = ['Ahmedabad','Bangalore','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer',
'Aligarh','Allahabad','Amravati','Amritsar','Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi',
'Bhopal','Bhubaneswar','Bikaner','Bokaro Steel City','Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad',
'Durg-Bhilai Nagar','Durgapur','Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur',
'Gurgaon','Guwahati‚ Gwalior','Hubli-Dharwad','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar','Jamshedpur',
'Jhansi','Jodhpur','Kannur','Kanpur','Kakinada','Kochi','Kottayam','Kolhapur','Kollam','Kota','Kozhikode','Kurnool',
'Lucknow','Ludhiana','Madurai','Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik',
'Nellore','Noida','Palakkad','Patna','Pondicherry','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Siliguri',
'Solapur','Srinagar','Sultanpur','Surat','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tirunelveli','Tiruppur','Ujjain','Vijayapura',
'Vadodara','Varanasi','Vasai-Virar City','Vijayawada','Visakhapatnam','Warangal']

dict_city = [x.lower() for x in dict_city]
def check_location(loc,dict_city =dict_city):
	config={"user_key":user_key}
	zomato = zomatopy.initialize_app(config)
	location_detail=zomato.get_location(loc, 1)
	location_json = json.loads(location_detail)
	location_results = len(location_json['location_suggestions'])

	if location_results ==0:
		return {'location_f' : 'notfound', 'location_new' : None}
	elif loc.lower() not in dict_city:
		return {'location_f' : 'tier3', 'location_new' : None}
	else:
		return {'location_f' : 'found', 'location_new' : loc}

class Check_location(Action):
	def name(self):
		return 'action_check_location'
		
	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		check = check_location(loc)
		
		return [SlotSet('location',check['location_new']), SlotSet('location_found',check['location_f'])]
       
        
class SendMail(Action):
	def name(self):
		return 'email_restaurant_details'
		
	def run(self, dispatcher, tracker, domain):
		recipient = tracker.get_slot('email')

		top10 = restaurants.head(10)
		print("got this correct")
		send_email(recipient, top10)

		dispatcher.utter_message("Sent.")