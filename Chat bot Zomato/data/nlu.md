## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- yes Please
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:deny
- No
- no
- Nope
- No,Thanks
- No need
- I don't need them.
- no. Thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- no. thanks
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- wassup
- Hey Mate
- hello there
- Namaste
- Heyo
- good morning
- good evening
- dear sir
- Hola

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I’m hungry. Looking out for some good restaurant.
- Craving for some [mexican](cuisine) food
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [American](cuisine)
- [Mexican](cuisine)
- [Lithuania](location)
- looking for a restaurant with avg price less than 300](price)
- find a [italian](cuisine) restaurant [between 300 and 700](price) price range
- looking for a fine restaurant having price [greater than 700](price)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food for [four]{"entity": "people", "value": "4"} people
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurant in [bangalore](location)
- [mumbai](location)
- show me restaurants
- show me some [oriental](cuisine)
- find a [mexican](cuisine) restaurant in [Allahbad](location)
- Can you suggest some good restaurants in [kolkata](location)
- Can you suggest some good restaurants in [Rishikesh](location)
- please find me [chinese](cuisine) restaurant in [delhi](location)
- I’m hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- can you find me a [chinese](cuisine) restaurant
- find a restaurant with a budget of [between 300 and 700](price)
- find a restaurant with a budget of [less than 300](price)
- find a [italian](cuisine) with a budget of [more than 700](price)
- look for a [italian](cuisine) with a budget of [more than 700](price)
- [delhi](location)
- find a restaurant in [Dilli](location)
- find a restaurant with a budget of [>300](price)
- find a resstaurant with average cost [less than 300](price)
- look for a [italian](cuisine) with a budget of [>700](price)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- test
- find me a [italian](cuisine) restaurent in [delhi](location)

## intent:get_price
- [less than 300](price)
- [between 300 and 700](price)
- [more than 700](price)
- [<300](price)
- [< 300](price)
- [>700](price)
- [300 max](price)
- [300-700]
- [around 300 to 700](price)
- [300 to 700](price)
- [more than 700](price)

## intent:get_email
- please email me at [test.test@mailme.com](email)
- mail me the list at [test@testdom.com](email)
- send that to [sidharth.test@tryout.co.in](email)
- please send that to [sidharth.test@tryout.co.in](email)
- fwd that to [sidharth.test@tryout.co.in](email)
- send the same to [tryit.12@tryout.com](email)
- yes. Please send it to [ahbcdj@dkj.com](email)
- Please send it to [ahbcdj@dkj.com](email)
- [tryit124@abclive.in](email)
- [ashok.surapuraj@gmail.com](email)

## synonym:4
- four

## synonym:Delhi
- New Delhi
- Dilli

## synonym:Mumbai
- Bombay
- Bombai
- Bambai

## synonym:North Indian
- Northern Indian
- North India
- Nrth Indian
- Northern part

## synonym:South Indian
- Southern Indian
- South India
- S India
- Southern part

## synonym:bangalore
- Bengaluru
- Bangalor

## synonym:between 300 and 700
- 300 - 700
- around 300 to 700
- 300 to 700
- 700 - 300

## synonym:chennai
- Madras
- Chennai

## synonym:chinese
- chines
- Chinese
- Chines
- Asian
- Oriental

## synonym:italian
- italion
- itlion

## synonym:kolkata
- Calcutta
- Kolkatta

## synonym:less than 300
- < 300
- <300
- 300 or less
- less 300
- upto 300
- 300 max
- atmost 300

## synonym:mid
- moderate
- moderateitlion

## synonym:more than 700
- > 700
- 700 or more
- 700 plus
- 700+
- >700

## synonym:prayagraj
- Allahbad
- Ellahbad

## synonym:varanasi
- Benaras
- Banaras

## synonym:vegetarian
- veggie
- vegg

## regex:deny
- No need[^\s]*
- No[^\s]*
- Nope[^\s]*
- no.[^\s]*

## regex:email
- ([\w.-]+)@(([[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.)|(([\w-]+.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(]?)

## regex:greet
- Hola[^\s]*
- hey[^\s]*
- hi[^\s]*
- howdy[^\s]*

## regex:pincode
- [0-9]{6}
