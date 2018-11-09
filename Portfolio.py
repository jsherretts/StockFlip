from collections import defaultdict
import json
import Utils

'''
This is the data for the logged-in user that is loaded from the db. It contains things like balance, owned stocks, and some functions to 
add/remove stocks for a given company
'''

owned_stocks = {}
quick_access_companies = []
username = ''
credits = 5000
total_value = 0


def calculate_total_value():
	pass
	#stock_value = sum(list(owned_stocks.values)) 

def add_symbol_to_quick_access(symbol):
	symbol = str(symbol)
	quick_access_companies.append(symbol)

'''
Set the stock to [quantity] at key value [symbol], independent of previous value
Returns True on success, else False
'''
def set_stock(symbol, quantity):
	try:
		owned_stocks[symbol] = quantity
	except KeyError as e:
		raise e
		print("KeyErrorL " + e)
		return False

	assert owned_stocks[symbol] >= 0
	return True


'''
Set the quantity of owned stock equal to the old quantity + [quantity] at key [symbol]
Returns True if successful, else False
'''
def add_stock(symbol, quantity):
	if not (isinstance(symbol, str) and (isinstance(quantity, int))):
		return False
	try:
		owned_stocks[symbol] += quantity
	except KeyError as e:
		raise e
		print("KeyError: " + e)
		return False
	assert owned_stocks[symbol] >= 0
	return True


'''
Set the quantity of owned stock equal to the old quantity - [quantity] at key [symbol]
Returns True if successful, else False
'''
def remove_stock(symbol, quantity):
	owned_stocks[symbol] -= quantity
	assert owned_stocks[symbol] >= 0


'''
Load a user using the username as the file, in JSON format into this object.
Return true if loaded
		false if None
'''
def load_user(username):
	pass


'''
Serialize (self) object and dump it into a file with self.username as the filename
'''
def dump_user_data():
	pass
