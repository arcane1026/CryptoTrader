import json #for api support
import requests #for api support
import time #for cycle timing
import os #
from twilio.rest import Client #for text verifications

import tkinter as tk #for GUI support

from tkinter import * #for GUI support 

import robin_stocks.robinhood as r

#import pyotp for security later

login = r.login('************','**************') #robinhood login information
#r.authentication.logout() logout when necessary
# r.order_buy_crypto_by_price('eth',1) example 

#api call for testing 
#x = requests.get('https://www.alphavantage.co/queryO?function=CURRENCY_EXCHANGE_RATE&from_currency=' + 'eth' + '&to_currency=USD&apikey=LAY6PZLV9B85KEJ3')

#api results
#y = x.json()

#drill down for current value in USD 
#seedString = (y['Realtime Currency Exchange Rate']['5. Exchange Rate'])

print("hi")#testing
#seed = float(seedString)


count3 = 0 # master count

ltcBuy = 1 #initializing the variable that marks for buy
ltcSell = 1 #initiating the variable that marks for buy

seedReset3 = 1 #initializing the variable that determines if seed value is reset after a buy/sell
marked3Buy = 1 #marking for sale and waiting for price to change direction
markPrice3 = 1 #the price when sell/buy threshhold was met, waiting for one proce in opposite direction as to not avoid profit from larger spikes and drops
marked3Sell = 1 
count2 = 0 # master count

ethBuy = 1 #initializing the variable that marks for buy
ethSell = 1 #initiating the variable that marks for buy

seedReset2 = 1 #initializing the variable that determines if seed value is reset after a buy/sell
marked2Buy = 1 #marking for sale and waiting for price to change direction
markPrice2 = 1 #the price when sell/buy threshhold was met, waiting for one proce in opposite direction as to not avoid profit from larger spikes and drops
marked2Sell = 1 

count1 = 0 # master count

btcBuy = 1 #initializing the variable that marks for buy
btcSell = 1 #initiating the variable that marks for buy

seedReset1 = 1 #initializing the variable that determines if seed value is reset after a buy/sell
marked1Buy = 1 #marking for sale and waiting for price to change direction
markPrice1 = 1 #the price when sell/buy threshhold was met, waiting for one proce in opposite direction as to not avoid profit from larger spikes and drops
marked1Sell = 1 


count4 = 0 # master count

etcBuy = 1 #initializing the variable that marks for buy
etcSell = 1 #initiating the variable that marks for buy

seedReset4 = 1 #initializing the variable that determines if seed value is reset after a buy/sell
marked4Buy = 1 #marking for sale and waiting for price to change direction
markPrice4 = 1 #the price when sell/buy threshhold was met, waiting for one proce in opposite direction as to not avoid profit from larger spikes and drops
marked4Sell = 1 

count5 = 0 # master count

dogeBuy = 1 #initializing the variable that marks for buy
dogeSell = 1 #initiating the variable that marks for buy

seedReset5 = 1 #initializing the variable that determines if seed value is reset after a buy/sell
marked5Buy = 1 #marking for sale and waiting for price to change direction
markPrice5 = 1 #the price when sell/buy threshhold was met, waiting for one proce in opposite direction as to not avoid profit from larger spikes and drops
marked5Sell = 1 





while True:                        
        count2 += 1 #increment master count        
        print("ETH")
        print(str(ethSell))
        print(str(ethBuy))
        print(str(seedReset2))
        print(str(marked2Buy))
        print(str(marked2Sell))
        print(str(markPrice2))
        print(str(count2)) #print number of cycles       
        x2 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+ 'eth' + '&to_currency=USD&apikey=LAY6PZLV9B85KEJ3')
        y2 = x2.json()
        priceString2 = (y2['Realtime Currency Exchange Rate']['5. Exchange Rate'])        
        PriceInt2 = float(priceString2)
        ## Setting initial seed value
        if count2 == 1:
               print("say hi")
               seedString2 = (y2['Realtime Currency Exchange Rate']['5. Exchange Rate'])
               seed2 = float(seedString2)
               PriceInt2 = float(seed2)                     
        amountMin2 = seed2 - (seed2 * .04)
        print("minimum amount = " + str(amountMin2))       
        print("Current seed = " + str(seed2))
        amountMax2 = seed2 + (seed2 * .04)
        print("maximum amount = " + str(amountMax2))
        print("current price = " + str(PriceInt2))
        print (type(PriceInt2))
        if ((PriceInt2 < amountMin2) and (ethBuy == 1)):#if current price is less than min limit.....
            
            marked2Buy = 2
            markPrice2 = PriceInt2
            
            print("###############################################################")
            
           
            
            ethBuy = 2
            ethSell =  2 
        if(marked2Buy == 2) and (PriceInt2 > (markPrice2)):
            print("buy++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            r.order_buy_crypto_by_price('ETH',20)
            marked2Buy = 1
            if (seedReset2 == 2):
                seed2 = PriceInt2
                seedReset2 = 1
                ethBuy = 1
                ethSell = 1
                seedReset2 = 1
            elif (seedReset2 == 1):
                ethBuy = 1
                seed2 = PriceInt2
                seedReset2 = 1
                ethSell = 1 
            print("new seed = " + str(seed2))                       
        if ((PriceInt2 > amountMax2) and (ethSell == 1)):#if current price is more than max limit.....
           
             #sell 1$ of crypto
            #r.order_sell_crypto_by_price('eth',1)   
           
            marked2Sell = 2
            markPrice2 = PriceInt2
            
            print("###############################################################")
            
            ethSell = 2
            ethBuy = 2            
        if(marked2Sell == 2) and (PriceInt2 < (markPrice2)):
            marked2Sell = 1
            print("sell++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            r.order_sell_crypto_by_price('ETH',20)
            if (seedReset2 == 2):
                seed2 = PriceInt2
                seedReset2 = 1
                ethBuy = 1
                ethSell = 1
            elif (seedReset2 == 1):
                seed2 = PriceInt2
                seedReset2 = 1
                ethBuy = 1 
                ethSell = 1
            print("new seed = " + str(seed2))            
        if (marked2Buy == 2) or (marked2Sell == 2):
            markPrice2 = PriceInt2  




            
        count1 += 1 #increment master count 



        
        print("btc")
        print(str(btcSell))
        print(str(btcBuy))
        print(str(seedReset1))
        print(str(marked1Buy))
        print(str(marked1Sell))
        print(str(markPrice1))
        print(str(count1)) #print number of cycles             
        #api call
        x1 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+ 'btc' + '&to_currency=USD&apikey=LAY6PZLV9B85KEJ3')
        #api results
        y1 = x1.json()        
        #drilling for price in string 
        priceString1 = (y1['Realtime Currency Exchange Rate']['5. Exchange Rate'])        
        PriceInt1 = float(priceString1)
        ## Setting initial seed value
        if count1 == 1:
               print("say hi")
               seedString1 = (y1['Realtime Currency Exchange Rate']['5. Exchange Rate'])
               seed1 = float(seedString1)
               PriceInt1 = float(seed1)                                      
         #if current value is less than seed value -  1 percent. (if crypto drops 1 percent buy 1 dollar)
        amountMin1 = seed1 - (seed1 * .04)
        print("minimum amount = " + str(amountMin1))        
        print("Current seed = " + str(seed1))
        amountMax1 = seed1 + (seed1 * .04)
        print("maximum amount = " + str(amountMax1))                            
        print("current price = " + str(PriceInt1))
        print (type(PriceInt1))
        if ((PriceInt1 < amountMin1) and (btcBuy == 1)):#if current price is less than min limit.....
            
            marked1Buy = 2
            markPrice1 = PriceInt1
            
            #buy 1$ of crypto
            #r.order_buy_crypto_by_price('btc',1)
            
            #send text notification
            
           
             
            print("###############################################################")
            
           
            
            btcBuy = 2
            btcSell = 2
        if(marked1Buy == 2) and (PriceInt1 > (markPrice1)):
            print("buy++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            r.order_buy_crypto_by_price('btc',100)
            marked1Buy = 1
            if (seedReset1 == 2):
                seed1 = PriceInt1
                seedReset1 = 1
                btcBuy = 1
                btcSell = 1
                
            elif (seedReset1 == 1):
                seed1 = PriceInt1
                seedReset1 = 1
                btcSell = 1 
                btcBuy = 1
            print("new seed = " + str(seed1))                       
        if ((PriceInt1 > amountMax1) and (btcSell == 1)):#if current price is more than max limit.....
           
             #sell 1$ of crypto
            #r.order_sell_crypto_by_price('btc',1)   
           
            marked1Sell = 2
            markPrice1 = PriceInt1
            print("###############################################################")
           
            
            btcSell = 2
            btcBuy = 2           
        if(marked1Sell == 2) and (PriceInt1 < (markPrice1)):
            marked1Sell = 1
            print("sel++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++l")
            r.order_sell_crypto_by_price('btc',100)  
            if (seedReset1 == 2):
                seed1 = PriceInt1
                seedReset1 = 1
                btcBuy = 1
                btcSell = 1
                seedReset1 = 1
            elif (seedReset1 == 1):
                seed1 = PriceInt1
                seedReset1 = 1
                btcBuy = 1
                btcSell = 1
            print("new seed = " + str(seed1))            
        if (marked1Buy == 2) or (marked1Sell == 2):
            markPrice1 = PriceInt1                         
        count3 += 1 #increment master count      



        
        print("ltc")
        print(str(ltcSell))
        print(str(ltcBuy))
        print(str(seedReset3))
        print(str(marked3Buy))
        print(str(marked3Sell))
        print(str(markPrice3))
        print(str(count3)) #print number of cycles            
        #api call
        x3 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+ 'ltc' + '&to_currency=USD&apikey=LAY6PZLV9B85KEJ3')
        #api results
        y3 = x3.json()        
        #drilling for price in string 
        priceString3 = (y3['Realtime Currency Exchange Rate']['5. Exchange Rate'])        
        PriceInt3 = float(priceString3)
        ## Setting initial seed value
        if count3 == 1:
               print("say hi")
               seedString3 = (y3['Realtime Currency Exchange Rate']['5. Exchange Rate'])
               seed3 = float(seedString3)
               PriceInt3 = float(seed3)                                               
         #if current value is less than seed value -  1 percent. (if crypto drops 1 percent buy 1 dollar)
        amountMin3 = seed3 - (seed3 * .04)
        print("minimum amount = " + str(amountMin3))        
        print("Current seed = " + str(seed3))
        amountMax3 = seed3 + (seed3 * .04)
        print("maximum amount = " + str(amountMax3))                
        #print(price)            
        print("current price = " + str(PriceInt3))
        print (type(PriceInt3))
        if ((PriceInt3 < amountMin3) and (ltcBuy == 1)):#if current price is less than min limit.....
            
            marked3Buy = 2
            markPrice3 = PriceInt3
            
            #buy 1$ of crypto
            #r.order_buy_crypto_by_price('ltc',1)
            print("###############################################################")
            #send text notification
            
           
            
           
            
            ltcBuy = 2
            ltcSell = 2
        if(marked3Buy == 2) and (PriceInt3 > (markPrice3)):
            print("buy++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            r.order_buy_crypto_by_price('ltc',50)
            marked3Buy = 1
            if (seedReset3 == 2):
                seed3 = PriceInt3
                seedReset3 = 1
                ltcBuy = 1
                ltcSell = 1
                seedReset3 = 1
            elif (seedReset3 == 1):
                seed3 = PriceInt3
                seedReset3 = 1
                ltcSell = 1 
                ltcBuy = 1
            print("new seed = " + str(seed3))                        
        if ((PriceInt3 > amountMax3) and (ltcSell == 1)):#if current price is more than max limit.....
           
             #sell 1$ of crypto
            #r.order_sell_crypto_by_price('ltc',1)   
           
            marked3Sell = 2
            markPrice3 = PriceInt3
            print("###############################################################")
            
           
            
            ltcSell = 2
            ltcBuy = 2           
        if(marked3Sell == 2) and (PriceInt3 < (markPrice3)):
            marked3Sell = 1
            print("sell++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            r.order_sell_crypto_by_price('ltc',50)  
            if (seedReset3 == 2):
                seed3 = PriceInt3
                seedReset3 = 1
                ltcBuy = 1
                ltcSell = 1
                seedReset3 = 1
            elif (seedReset3 == 1):
                seed3 = PriceInt3
                seedReset3 = 1
                ltcBuy = 1 
                ltcSell = 1
            print("new seed = " + str(seed3))            
        if (marked3Buy == 2) or (marked3Sell == 2):
            markPrice3 = PriceInt3                           
        count4 += 1 #increment master count        
        
        
        
        
        print("etc")
        print(str(etcSell))
        print(str(etcBuy))
        print(str(seedReset4))
        print(str(marked4Buy))
        print(str(marked4Sell))
        print(str(markPrice4))
        print(str(count4)) #print number of cycles              
        #api call
        x4 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+ 'etc' + '&to_currency=USD&apikey=LAY6PZLV9B85KEJ3')
        #api results
        y4 = x4.json()        
        #drilling for price in string 
        priceString4 = (y4['Realtime Currency Exchange Rate']['5. Exchange Rate'])        
        PriceInt4 = float(priceString4)
        ## Setting initial seed value
        if count4 == 1:
               print("say hi")
               seedString4 = (y4['Realtime Currency Exchange Rate']['5. Exchange Rate'])
               seed4 = float(seedString4)
               PriceInt4 = float(seed4)                              
         #if current value is less than seed value -  1 percent. (if crypto drops 1 percent buy 1 dollar)
        amountMin4 = seed4 - (seed4 * .04)
        print("minimum amount = " + str(amountMin4))        
        print("Current seed = " + str(seed4))
        amountMax4 = seed4 + (seed4 * .04)
        print("maximum amount = " + str(amountMax4))                
        #print(price)            
        print("current price = " + str(PriceInt4))
        print (type(PriceInt4))
        if ((PriceInt4 < amountMin4) and (etcBuy == 1)):#if current price is less than min limit.....
            
            marked4Buy = 2
            markPrice4 = PriceInt4
            
            #buy 1$ of crypto
            #r.order_buy_crypto_by_price('etc',1)
            
            #send text notification
            print("###############################################################")
           
            
            
           
            
            etcBuy = 2
            etcSell = 2
        if(marked4Buy == 2) and (PriceInt4 > (markPrice4)):
            print("buy++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            r.order_buy_crypto_by_price('etc',50)
            marked4Buy = 1
            if (seedReset4 == 2):
                seed4 = PriceInt4
                seedReset4 = 1
                etcBuy = 1
                etcSell = 1
                seedReset4 = 1
            elif (seedReset4 == 1):
                seedReset4 = 1
                etcSell = 1 
                etcBuy = 1
                seed4 = PriceInt4
            print("new seed = " + str(seed4))                        
        if ((PriceInt4 > amountMax4) and (etcSell == 1)):#if current price is more than max limit.....
           
             #sell 1$ of crypto
            #r.order_sell_crypto_by_price('etc',1)   
           
            marked4Sell = 2
            markPrice4 = PriceInt4
            
            print("###############################################################")
            etcSell = 2
            etcBuy = 2            
        if(marked4Sell == 2) and (PriceInt4 < (markPrice4)):
            marked4Sell = 1
            print("sell++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            r.order_sell_crypto_by_price('etc',50)  
            if (seedReset4 == 2):
                seed4 = PriceInt4
                seedReset4 = 1
                etcBuy = 1
                etcSell = 1
                seedReset4 = 1
            elif (seedReset4 == 1):
                seedReset4 = 1
                etcBuy = 1 
                etcSell = 1
            print("new seed = " + str(seed4))            
        if (marked4Buy == 2) or (marked4Sell == 2):
            markPrice4 = PriceInt4                                     
        count5 += 1 #increment master count       
        
        
        
        
        print("doge")
        print(str(dogeSell))
        print(str(dogeBuy))
        print(str(seedReset5))
        print(str(marked5Buy))
        print(str(marked5Sell))
        print(str(markPrice5))
        print(str(count5)) #print number of cycles              
        #api call
        x5 = requests.get('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency='+ 'doge' + '&to_currency=USD&apikey=LAY6PZLV9B85KEJ3')
        #api results
        y5 = x5.json()        
        #drilling for price in string 
        priceString5 = (y5['Realtime Currency Exchange Rate']['5. Exchange Rate'])        
        PriceInt5 = float(priceString5)
        ## Setting initial seed value
        if count5 == 1:
               print("say hi")
               seedString5 = (y5['Realtime Currency Exchange Rate']['5. Exchange Rate'])
               seed5 = float(seedString5)
               PriceInt5 = float(seed5)                                            
         #if current value is less than seed value -  1 percent. (if crypto drops 1 percent buy 1 dollar)
        amountMin5 = seed5 - (seed5 * .04)
        print("minimum amount = " + str(amountMin5))        
        print("Current seed = " + str(seed5))
        amountMax5 = seed5 + (seed5 * .04)
        print("maximum amount = " + str(amountMax5))
        print("current price = " + str(PriceInt5))
        print (type(PriceInt5))
        if ((PriceInt5 < amountMin5) and (dogeBuy == 1)):#if current price is less than min limit.....
            
            marked5Buy = 2
            markPrice5 = PriceInt5
            
            #buy 1$ of crypto
            #r.order_buy_crypto_by_price('doge',1)
            
            #send text notification
            
           
            print("###############################################################")
            
            
            
           
            
            dogeBuy = 2
            dogeSell = 2
        if(marked5Buy == 2) and (PriceInt5 > (markPrice5)):
            print("buy++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            r.order_buy_crypto_by_price('doge',100)
            marked5Buy = 1
            if (seedReset5 == 2):
                seed5 = PriceInt5
                seedReset5 = 1
                dogeBuy = 1
                dogeSell = 1
                seedReset5 = 1
            elif (seedReset5 == 1):
                seedReset5 = 1
                dogeSell = 1 
                seed5 = PriceInt5
                dogeBuy = 1
            print("new seed = " + str(seed5))                
        if ((PriceInt5 > amountMax5) and (dogeSell == 1)):#if current price is more than max limit.....
           
             #sell 1$ of crypto
            #r.order_sell_crypto_by_price('doge',1)   
           
            marked5Sell = 2
            markPrice5 = PriceInt5
            
            print("###############################################################")
            
            dogeSell = 2
            dogeBuy = 2       
        if(marked5Sell == 2) and (PriceInt5 < (markPrice5)):
            marked5Sell = 1
            print("sell++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            r.order_sell_crypto_by_price('doge',100)  
            if (seedReset5 == 2):
                seed5 = PriceInt5
                seedReset5 = 1
                dogeBuy = 1
                dogeSell = 1
                seedReset5 = 1
            elif (seedReset5 == 1):
                seed5 = PriceInt5
                seedReset5 = 2
                dogeBuy = 1 
                dogeSell = 1
            print("new seed = " + str(seed5))
            
        if (marked5Buy == 2) or (marked5Sell == 2):
            markPrice5 = PriceInt5      
            
     
        time.sleep(300)  
