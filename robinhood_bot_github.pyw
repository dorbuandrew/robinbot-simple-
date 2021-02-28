# Importing the libraries used in this bot.
import time 
import robin_stocks

#An object to login into robinhood.
#You will need to enter a code texted to your phone number into the console, when you login for the first time.
 

login_user = robin_stocks.login("insert username/email here","insert password here", by_sms = True)
#You will need to place the first buy order manually before running the bot. 
#This object gets the average price of the order.
 
get_order = robin_stocks.orders.get_all_crypto_orders(info= "average_price")
get_order_float = float(get_order[0])

# The counters here are used within the loop to determine when certain events are triggered. 

count = [0]
stop_loss = [0]
loop_counter = [0]

while count[0]<10:
	loop_counter[0] = loop_counter[0]+1
	print(loop_counter[0])
	wait_timer_2 = time.sleep(5)
	get_order_quantity = robin_stocks.orders.get_all_crypto_orders(info= "quantity")
	get_order_quantity_float = float(get_order_quantity[0])	
	get_order = robin_stocks.orders.get_all_crypto_orders(info= "average_price")
	try:
		get_order_float = float(get_order[0])

	except TypeError:
		wait_timer_8 = time.sleep(3600)
		get_order = robin_stocks.orders.get_all_crypto_orders(info= "average_price")
		get_order_float = float(get_order[0])
		
	get_current_price = robin_stocks.crypto.get_crypto_quote(symbol = "BTC", info="ask_price")
	get_current_price_float = float(get_current_price)
	if get_current_price_float >= (get_order_float + (get_order_float*0.005)):
		sell_order = robin_stocks.orders.order_crypto(symbol = "BTC", side ="sell", quantityOrPrice = get_order_quantity_float, amountIn = "quantity")
		count[0] = count[0]+1 
		wait_timer = time.sleep(5)
		buy_order = robin_stocks.orders.order_crypto(symbol = "BTC", side ="buy", quantityOrPrice = 50, amountIn = "price")
		wait_timer_3 = time.sleep(300)
	elif get_current_price_float <= (get_order_float-(get_order_float*0.05)) and stop_loss[0] != 3:
		sell_order_1 = robin_stocks.orders.order_crypto(symbol = "BTC", side ="sell", quantityOrPrice = get_order_quantity_float, amountIn = "quantity")
		stop_loss[0] = stop_loss[0]+1
		wait_timer_1 = time.sleep(43200)
		buy_order_1 = robin_stocks.orders.order_crypto(symbol = "BTC", side ="buy", quantityOrPrice = 50, amountIn = "price")
	elif loop_counter[0] >= 1000 and get_current_price_float <= (get_order_float -(get_order_float*0.015)):
		sell_order_3 = robin_stocks.orders.order_crypto(symbol = "BTC", side ="sell", quantityOrPrice = get_order_quantity_float, amountIn = "quantity")
		stop_loss[0] = stop_loss[0] + 1
		wait_timer_4 = time.sleep(300)
		buy_order_4 = robin_stocks.orders.order_crypto(symbol = "BTC", side ="buy", quantityOrPrice = 50, amountIn = "price")
		wait_timer_5 = time.sleep(600)
	elif stop_loss[0] >= 3:
		break 


	


		 


