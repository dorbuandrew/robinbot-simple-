A simple Crypto trading bot for python using the robin-stocks library for the robinhood api. 

The bot is currently setup to trade BTC at $50 blocks, but this can be adjusted along witht the crypto it trades. 

The various timers within the bot's code are there to give robinhood enough time to place your orders and reduce the chances of getting a TypeError when you make a call for your order during the loop. 

~Changelog 1 - Ver 1.01 
	- Made some minor adjustments to the code to clean it up a bit and to make it more usable for other cryptos.
	Altered the Comments within the code. 
	Changed the exception from a ValueError to a TypeError, because I originaly thought the error that came up was a value instead of a type error. 