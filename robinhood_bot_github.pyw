
# Importing the libraries used for this bot.
import time 
import robin_stocks 


# Loggining the user into Robinhood.
# Will send an authorization text to the cellphone number on file when logging on for the first time.
# Enter the number you recieve via text into the console when it prompts you to. 

login_user = robin_stocks.login("Insert username or email here","Insert password here", by_sms = True)
# Object to get the average price of the most recent cryptocurrency you purchased. 
# Buy some crypto before running the code or the bot does nothing but loop. 
# Bot trades bit coin, but you can change the crypto it trades in the loop. 

get_order = robin_stocks.orders.get_all_crypto_orders(info= "average_price")
get_order_float = float(get_order[0])

# Counters for the loop. 
# they are used to prompt stop losses for the bot. 
# the count object is used to determine how many positive trade the bot can make and is used as a stop for the while loop. 

count = [0]
stop_loss = [0]
loop_counter = [0]

while count[0]<10:
	loop_counter[0] = loop_counter[0]+1
	print(loop_counter[0])
	wait_timer_2 = time.sleep(5)
# Used to obtain the quantity of the crypto purchased, allowing you to trade all of it at once. 
# You can alter the amount traded if you wish. 

	get_order_quantity = robin_stocks.orders.get_all_crypto_orders(info= "quantity")
	get_order_quantity_float = float(get_order_quantity[0])	
	get_order = robin_stocks.orders.get_all_crypto_orders(info= "average_price")

# The try and except are here because you sometimes run into the issue where a purchase order hasn't cleared and the get_order returns a none.
# The exception puts in a wait timer then checks again. The wait should be long enough for an order to clear. 
	try:
		get_order_float = float(get_order[0])

	except ValueError:
		wait_timer_8 = time.sleep(3600)
		get_order = robin_stocks.orders.get_all_crypto_orders(info= "average_price")
		get_order_float = float(get_order[0])
# gets the current price of the crypto, in this case BTC
		
	get_current_price = robin_stocks.crypto.get_crypto_quote(symbol = "BTC", info="ask_price")
	get_current_price_float = float(get_current_price)

# if statements for the bot's decision making. 
# they are just simple percent changes that prompt them.
# the wait timers are in place to allow robinhood to clear your orders after they are placed or just to wait during stop losses and try again later. 

	if get_current_price_float >= (get_order_float + (get_order_float*0.005)):
		sell_order = robin_stocks.orders.order_crypto(symbol = "BTC", side ="sell", quantityOrPrice = get_order_quantity_float, amountIn = "quantity")
		count[0] = count[0]+1 
		wait_timer = time.sleep(5)
		buy_order = robin_stocks.orders.order_crypto(symbol = "BTC", side ="buy", quantityOrPrice = 50, amountIn = "price")
		wait_timer_3 = time.sleep(300)
	elif get_current_price_float <= (get_order_float-(get_order_float*0.015)) and stop_loss[0] != 3:
		sell_order_1 = robin_stocks.orders.order_crypto(symbol = "BTC", side ="sell", quantityOrPrice = get_order_quantity_float, amountIn = "quantity")
		stop_loss[0] = stop_loss[0]+1
		wait_timer_1 = time.sleep(600)
		buy_order_1 = robin_stocks.orders.order_crypto(symbol = "BTC", side ="buy", quantityOrPrice = 50, amountIn = "price")
	elif loop_counter[0] >= 1000 and get_current_price_float <= (get_order_float - 500):
		sell_order_3 = robin_stocks.orders.order_crypto(symbol = "BTC", side ="sell", quantityOrPrice = get_order_quantity_float, amountIn = "quantity")
		stop_loss[0] = stop_loss[0] + 1
		wait_timer_4 = time.sleep(300)
		buy_order_4 = robin_stocks.orders.order_crypto(symbol = "BTC", side ="buy", quantityOrPrice = 50, amountIn = "price")
		wait_timer_5 = time.sleep(600)
	elif stop_loss[0] >= 3:
		break 


	


		 


