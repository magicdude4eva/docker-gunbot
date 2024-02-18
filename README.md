[paypal]: https://paypal.me/GerdNaschenweng

# Gunbot Docker Edition for Synology NAS (Binance, Kucoin)

[![Docker Pulls](https://img.shields.io/docker/pulls/magicdude4eva/gunbot-colorised.svg)](https://hub.docker.com/r/magicdude4eva/gunbot-colorised)
[![](https://images.microbadger.com/badges/image/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised "Get your own version badge on microbadger.com")
[![Docker Automated build](https://img.shields.io/docker/automated/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised)
[![Docker Build Status](https://img.shields.io/docker/build/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised)

:white_check_mark: Compatible with Gunbot version : Gunbot v28.4 [https://www.gunbot.com/downloads/](https://www.gunbot.com/downloads/)

:white_check_mark: Compatible with Synology DSM6.0, DSM7.0 (both on DS1019+)

Although this Docker Image has been tested on a Synology NAS, it will work essentially in any Docker-environment with the adjustment of the mount-point needed. I have provided a base-configuration under `/config/` which I suggest you read and adjust. If you use the autoconfig (please read the `/config/autoconfig-instructions.txt` before enabling) provided, and once you have added your Binance credentials, the BOT will start trading.

:warning: The provided config contains a Autoconfig using a Stepgrid trading algorithm with the base of BTC, trading 8 pairs. This works at the moment extremly well for at the current market (August 2021) with returns of 1-8% per trade and trading between 20-50 times per day on Binance. Do read the `/config/autoconfig-instructions.txt` and only change what is allowed. Alternatively use the standard Gunbot install and use an algorithm you understand / are comfortable with.

:sob: Do not come crying to me if you lost your house and your wife left you because you traded away your savings. Be responsible and only trade what you are prepared to lose. I am not a financial advisor, and will not help you with your financial troubles.

Detailed Gunbot documentation and support is available via [https://wiki.gunthy.org/](https://wiki.gunthy.org/)

<p align="center">
<a href="https://wiki.gunthy.org/"><img src="https://gblobscdn.gitbook.com/assets%2F-L_Rejuz9K0BDQxSQvUH%2F-MP8i9_pHeuD_bvxnAAl%2F-MP8j1c3cbIvuS9yckyg%2Fimage.png?alt=media&token=90c41159-642e-4978-ba26-ee6c7713ee2a" alt="Gunbot Docker File"></a><br/>
<b>Gunbot Trading Console via Webview</b><br/>
</p>

___
![paypal](https://img.shields.io/badge/PayPal--ffffff.svg?style=social&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8%2F9hAAAABHNCSVQICAgIfAhkiAAAAZZJREFUOI3Fkb1PFFEUxX%2F3zcAMswFCw0KQr1BZSKUQYijMFibGkhj9D4zYYAuU0NtZSIiNzRZGamqD%2BhdoJR%2FGhBCTHZ11Pt%2B1GIiEnY0hFNzkFu%2FmnHPPPQ%2Buu%2BTiYGjy0ZPa5N1t0SI5m6mITeP4%2B%2FGP%2Fbccvto8j3cuCsQTSy%2FCzLkdxqkXpoUXJoUXJrkfFTLMwHiDYLrFz897Z3jT6ckdBwsiYDMo0tNOIGuBqS%2Beh7sdAkU2g%2BkBFGkd%2FrtSgD8Z%2BrBxj68MAGG1A9efRhVsXrKMU7Y4cNyGOwtDU28OtrqdUMetldvzFKxCYSHJ4NsJ%2BnRJGexHba7VJ%2FTff4BaQFBjVcbqIEZ1bESYn4PRUcHx2N952awUkOHZedUcWm14%2FtjqjREHawUEsgx6Ajg5%2Bsi7jWqBwA%2BmIrXlo9YHUVTmEP%2F6hOO1Ofiyy3pjo%2BsvBDX%2FZpSakhz4BqvQDvdYvrXQEXZViI5rPpBEOwR2l16vtN7bd9SN3L1WXj%2BjGSnN38rq%2B7VL8xXQOdDF%2F0KvXn8BlbuY%2FvUAHysAAAAASUVORK5CYII%3D)
:beer: **Please support me**: Although all my software is free, it is always appreciated if you can support my efforts on Github with a [contribution via Paypal][paypal] - this allows me to write cool projects like this in my personal time and hopefully help you or your business. 
___

### I am a Gunbot Reseller and Binance Affiliate
You need at least a "Gunbot Standard" License to trade on Binance and use the provided autoconfig tool which automatically trades BTC-ALT coins for you. I am an offical [Gunbot Reseller](https://gunthy.org/resellers/) and you can purchase a license straight from the links below or via [gunbot.at](https://gunbot.at/):


| Gunbot Edition   |   Price    |  Link |
| ---------------- |------------| ------------------------------------------------------------------------------ |
| Gunbot Starter   | BTC 0.0100 | [gunbot/promoStarter](https://otc.gunthy.org/magicdude4eva/promoStarter)   |
| Gunbot Standard  | BTC 0.0250 | [gunbot/promoStandard](https://otc.gunthy.org/magicdude4eva/promoStandard) |
| Gunbot Pro       | BTC 0.0375 | [gunbot/promoPro](https://otc.gunthy.org/magicdude4eva/promoPro)           |
| Gunbot Ultimate  | BTC 0.0625 | [gunbot/promoUltimate](https://otc.gunthy.org/magicdude4eva/promoUltimate) |

<p align="center">
(*) You can always upgrade to a higher license later - I can help you - contact me on Telegram <a href="https://t.me/magicdude4eva" title="Contact @magicdude4eva on Telegram">@magicdude4eva</a>
</p>


:trophy: If you are new to Binance, [I can share my affiliate link where both of us will earn 10% commission on trades](https://www.binance.com/en/register?ref=WXNEJLQB).

:trophy: 2021-11-20: I have started trading CRO on Kucoin with Gunbot - if you are not signed up with them use my link: [Kucoin Signup Referral](https://www.kucoin.com/ucenter/signup?rcode=7wrbxe)

:rocket: 2021-11-20: If you have not signed up with Crypto.com to trade in CRO, read this: [Crypto.com Visa Debit Card with Cashback and 100% rebate on Netflix, Spotify & Amazon Prime](https://www.naschenweng.info/2021/11/10/crypto_com_visa_debit_card_supercharger/)

## Docker image with colorised output & Telegram Support

<p align="center">
<a href="https://wiki.gunthy.org/"><img src="https://github.com/magicdude4eva/docker-gunbot/raw/main/gunbot-console.gif" alt="Gunbot Colorised Console Output via Docker"></a><br/>
<b>Gunbot Dockerfile with glibc and colorised output</b><br/>
</p>

<p align="center">
<a href="https://wiki.gunthy.org/"><img src="https://github.com/magicdude4eva/docker-gunbot/raw/main/gunbot-telegram.gif" alt="Gunbot Telegram Notifications via Docker"></a><br/>
<b>Gunbot Dockerfile with Telegram Notifications</b><br/>
</p>


## Setup On Synology
:info: I use the container `gunbot` for Binance and the container `gunbot-kucoin`for Kucoin. If you do not need both, delete the one you are using.
:info: The container `gunbot-kucoin` only trades USDT-CRO as I like Crypto.com - please adjust if you need anything else. The trading limit for USDT-CRO is set to USDT=150 per trade (see `"TRADING_LIMIT": "150",`in 

1) If you have a mount-point `/volume1/`, create the directory `/volume1/docker/gunbot/` and skip to Step 3)

2) If you do not have `/volume1/`, adjust the mountpoints of `/volume1/docker/gunbot/` in `docker-compose.yml`

3) Copy `docker-compose.yml`, `dockerignore` and `Dockerfile` from this repo to your `./gunbot/`-folder. If you also want to use beta-releases, use the `Dockerfile.slipstream.local` instead and rename it to `Dockerfile`. This requires that you have the beta-release in the same folder as the Dockerfile named as `gunthy-linux.zip`

4) Adjust the timezone setting `TZ=Europe/Vienna` in `docker-compose.yml` and `Dockerfile` to your local settings

5) Place your config.js into `/config` and/or `/config-kucoin`

6) Adjust the download Link in `Dockerfile` for `INSTALL_URL`. The latest software can be found via: https://github.com/GuntharDeNiro/BTCT/releases

7) and then execute:
```
cd /volume1/docker/gunbot/
docker build -t gunbot .
docker-compose up -d

# Logs for Gunbot-Binance
docker logs -n 100 -f gunbot

# Logs for Gunbot-Kucoin
docker logs -n 100 -f gunbot-kucoin
```

## Updating Gunbot
From time to time I publish updates - mostly to adjust the Linux image or to include the latest Gunbot release. You can manually update by:
1) Stop and delete the Gunbot-Container in Synology Docker
2) Repeat Steps 6-7 above

## Telegram Configuration
Notifications work by first creating a personal bot on Telegram, Gunbot then connects to this bot to push notifications to you.

This is how to create a bot:
* Talk to @botfather. Create a new bot with the command /newbot and choose a name and username for your bot. Save the bot token shown.
* Talk to @myidbot to see your Chat ID, save it.
* Enable Telegram notifications for Gunbot, and enter the token and ID you've just gathered. Use the ID for both the user and admin ID fields, this makes sure that only you can interact with the Telegram bot. Alternatively, you can set a comma separated list for Admin ID, specifying multiple IDs who may interact with the bot.
* Start a chat with the username you've picked for your bot, and hit the start button. If you don't see a start button, write "/start" and send it as message.
* To enable trade notifications, enable these in the settings menu inside the Telegram bot.
* The Telegram bot is fully integrated into Gunbot. All you need to do to start the Telegram bot is enable Telegram notifications in your Gunbot settings.
* After setting it up, type /start to your bot to open the menu.

## Overview of Gunbot Licenses
Note: You will need to have at lease "Gunbot Standard" to support all strategies, and I strongly recommend it. If you want to trade on multiple exchanges use "Gunbot Pro" (3 API Slots) or "Gunbot Ultimate (5 API Slots)

<p align="center">
<a href="https://otc.gunthy.org/magicdude4eva/promoStandard"><img src="https://user-images.githubusercontent.com/1632781/107265057-18b88b80-6a44-11eb-8071-5c3f48ba4bf4.png" alt="Gunbot License differences"></a><br/>
<b>Gunbot License differences - click to purchase a "Gunbot Standard License" or pick other licenses from above</b><br/>
</p>


## How does the autoconfig work?
The idea is to have a fully automated setup for BTC-alt trading that trades relatively frequently (in tests, about 20-50 times per day) and only focusses on small trades with around 0.5% to 2% profit per trade. This config bundle offers completely autonomous trading with the stepGrid strategy. You set a few basic settings like how many pairs to trade, the script handles everything else.

<img width="1335" alt="CleanShot 2021-09-19 at 11 53 11@2x" src="https://user-images.githubusercontent.com/1632781/133923199-378e3e51-5771-4894-a4d6-e0ec3cd44ce3.png">

The setup consists of a config.js and autoconfig.json file, which do the following (summarized):

:warning: The "autoconfig.json" in the "gunbot" container trades as base both BTC-ALT and BNB-ALT and each base uses 6 pairs - so you will have 6 BTC-trades and 6-BNB-trades. Please adjust this if you do not want to trade in these volumes (you will need 0,3BTC and 2BNB for it to properly work)

`Autoconfig.json`

:children_crossing: Warnings:
* Because of how trading limit compounding is handled, the setup is difficult to combine with other trades on the same acount
* Manual trading on the same exchange account and base currency, or manually made config changes can lead to unexpected behavior
* Due to the lack of a bid/ask spread filter on Huobi, pair selection is likely more risky there
* Since stop losses are sometimes used in this setup, losing sell orders can happen
* The stepGrid strategy is great, but beware for very low volume markets as trading behavior might get erratic. In such a case using the enforce step size option in the strategy itself can help.
* All pairs for the exchange must be handled by the included AutoConfig jobs
* READ THE WHOLE INSTRUCTIONS 

Features:
* Scans markets for volatile pairs and adds them automatically, trades them with the stepGrid strategy
* Evaluates results for active trading pairs, continously replacing the worst performing pair with another
* Supports trading multiple base currencies on the same account, overlap between pairs is prevented automatically
* Supports the following base currencies: BTC
* Compounding trading limit, with an option to keep reserves
* Occasionally uses a higher trading limit when the market seems favorable, including a stop loss mechanism
* Frees up funds in case the account runs out of money for further buy orders
* Protection against possible losing trades after a very large price difference between buy orders

Notes:
* Don’t use all your funds for this. Keeping reserves is always a good idea, you never know what the market will bring in the future
* Try to keep relatively low numbers of pairs, to ensure frequent processing per pair
* You'll see more pairs being added than it may trade, this is fine because it won't actually trade every single added pair
* Upgrades are as simple as overwriting the autoconfig.json file, unless specified differently in the release notes


-----


## Donations are always welcome
:beer: **Please support me**: If the above helped you in any way, then [follow me on Twitter](https://twitter.com/gerdnaschenweng) or send me some coins: 
```
(CRO)    cro1w2kvwrzp23aq54n3amwav4yy4a9ahq2kz2wtmj (Memo: 644996249) or 0xb83c3Fe378F5224fAdD7a0f8a7dD33a6C96C422C (Cronos)
(USDC)   0xb83c3Fe378F5224fAdD7a0f8a7dD33a6C96C422C
(BTC)    3628nqihXvw2RXsKtTR36dN6WvYzaHyr52
(ETH)    0xb83c3Fe378F5224fAdD7a0f8a7dD33a6C96C422C
(BAT)    0xb83c3Fe378F5224fAdD7a0f8a7dD33a6C96C422C
(LTC)    MQxRAfhVU84KDVUqnZ5eV9MGyyaBEcQeDf
(Ripple) rKV8HEL3vLc6q9waTiJcewdRdSFyx67QFb (Tag: 1172047832)
(XLM)    GB67TJFJO3GUA432EJ4JTODHFYSBTM44P4XQCDOFTXJNNPV2UKUJYVBF (Memo ID: 1406379394)
```

Go to [Curve.com to add your Crypto.com card to ApplePay](https://www.curve.com/join#DWPXKG6E) and signup to [Crypto.com for a staking and free Crypto debit card](https://crypto.com/app/ref6ayzqvp) - please use referral **ref6ayzqvp** to get that sweep $25 bonus.


Use [Binance Exchange](https://www.binance.com/?ref=13896895) to trade #altcoins. Sign up with [Coinbase](https://www.coinbase.com/join/nasche_x) and **instantly get $10 in BTC**. I also accept old-school **[PayPal](https://paypal.me/GerdNaschenweng)**.

If you have no crypto, follow me at least on [Twitter](https://twitter.com/gerdnaschenweng).

## Use Rotki for Crypto Tracking
Referral: A great crypto currency tracking platform which can be selfhosted is [Rotki](https://github.com/rotki/rotki)
![CleanShot 2021-10-03 at 10 09 53@2x](https://user-images.githubusercontent.com/1632781/135745563-1d0880a8-486d-450a-823a-499763f14d57.png)

You can find the composer file under the `rotki` folder.


![visitors](https://visitor-badge.laobi.icu/badge?page_id=magicdude4eva.magicdude4eva)
