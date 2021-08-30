## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"price": "less than 300"}
    - slot{"price": "more than 700"}
	- action_search_restaurants
	- utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details


## 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "surat"}
    - slot{"location": "surat"}
    - action_check_location
    - slot{"location": "surat"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye
## 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details


## 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mbusmkwoid"}
    - slot{"location": "mbusmkwoid"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye

	
##
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mbumkdjjo"}
    - slot{"location": "mbumkdjjo"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye

## 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details
	
	
## 
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "haridwar"}
    - slot{"location": "haridwar"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye	
	
##  
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "ooty"}
    - slot{"location": "ooty"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details

	
	
##  
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye

	
##  
* greet
    - utter_greet
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye
	
##  
* greet
    - utter_greet
* restaurant_search{"location": "mbunvkdi"}
    - slot{"location": "mbunvkdi"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "mysore"}
    - slot{"location": "mysore"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye
	
	
##  
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - slot{"location": "pune"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye
	
	
##  
* greet
    - utter_greet
* restaurant_search{"location": "manali"}
    - slot{"location": "manali"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details


* greet
    - utter_greet
* restaurant_search{"location": "graaar"}
    - slot{"location": "graaar"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details
	
##  
* greet
    - utter_greet
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location": "jaipur"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye
##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "haridwar"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "haridwar"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details
	
##  
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye
##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye
	
##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "goa"}
    - slot{"cuisine": "italian"}
    - slot{"location": "goa"}
    - action_check_location
    - slot{"location": "goa"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details
	
##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "ptnsneha"}
    - slot{"cuisine": "italian"}
    - slot{"location": "ptnsneha"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye
	
##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "ooty"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "ooty"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "tier3"}
    - utter_foodie_not_working
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye

##  
* greet
    - utter_greet
* restaurant_search{"location": "hwusirinc"}
    - slot{"location": "hwusirinc"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "jammu"}
    - slot{"location": "jammu"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye

	
##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "rohtak"}
    - slot{"cuisine": "american"}
    - slot{"location": "rohtak"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details
	
	

##  
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "gwalior"}
    - slot{"location": "gwalior"}
    - action_check_location
    - slot{"location": "gwalior"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details

##  
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "filmkidiejf"}
    - slot{"location": "filmkidiejf"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye

	
##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details


##  
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details
    - export

##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* restaurant_search{"price": "lesser than 300"}
    - slot{"price": "lesser than 300"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details
##  
* greet
    - utter_greet
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_check_location
    - slot{"location": "ahmedabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details


##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - slot{"location": "bangalore"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details


##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_location
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details


##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details
	

##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "delhi"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye
##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_location
    - slot{"location": "mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details
    - export


##  
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "ptsnkela"}
    - slot{"cuisine": "italian"}
    - slot{"location": "ptsnkela"}
    - action_check_location
    - slot{"location": null}
    - slot{"location_found": "notfound"}
    - utter_location_notfound
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - utter_ask_budget
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* affirm{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details


##  
* greet
    - utter_greet
* restaurant_search{"location": "chandigarh"}
    - slot{"location": "chandigarh"}
    - action_check_location
    - slot{"location": "chandigarh"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye

##  
* greet
    - utter_greet
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_check_location
    - slot{"location": "jaipur"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurant_search{"price": "between 300 to 700"}
    - slot{"price": "between 300 to 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* deny
    - utter_final_bye


* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "delhi"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "italian"}
    - action_check_location
    - slot{"location": "delhi"}
    - slot{"location_found": "found"}
    - utter_ask_budget
* get_price{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - utter_ask_whethermail
* affirm
    - utter_ask_mail
* get_email{"email": "ashok.surapuraj@gmail.com"}
    - slot{"email": "ashok.surapuraj@gmail.com"}
    - email_restaurant_details
