[paypal]: https://paypal.me/GerdNaschenweng

# Gunbot Docker Edition for Synology NAS (Binance, Kucoin)

![GitHub stars](https://img.shields.io/github/stars/magicdude4eva/docker-gunbot?style=social)
![GitHub forks](https://img.shields.io/github/forks/magicdude4eva/docker-gunbot?style=social)
![GitHub issues](https://img.shields.io/github/issues/magicdude4eva/docker-gunbot)
![Docker Pulls](https://img.shields.io/docker/pulls/magicdude4eva/gunbot-colorised)
![Docker Stars](https://img.shields.io/docker/stars/magicdude4eva/gunbot-colorised)
[![GitHub last commit](https://img.shields.io/github/last-commit/magicdude4eva/docker-gunbot.svg)](https://github.com/magicdude4eva/docker-gunbot/commits/master)
[![Build and Push Docker image](https://github.com/magicdude4eva/docker-gunbot/actions/workflows/docker-build-gunbot-core.yml/badge.svg)](https://github.com/magicdude4eva/docker-gunbot/actions/workflows/docker-build-gunbot-core.yml)

✅ Compatible with Gunbot version: Gunbot v30.6.0 [https://gunthy.org/downloads/](https://gunthy.org/downloads/)

✅ Compatible with Synology DSM6.0, DSM7.0 (both on DS1019+)

🆘 Help and support via [magicdude4eva/docker-gunbot](https://github.com/magicdude4eva/docker-gunbot)

Although this Docker Image has been tested on a Synology NAS, it will work essentially in any Docker-environment with the adjustment of the mount-point needed. I have provided a base-configuration under `/config/` which I suggest you read and adjust. If you use the autoconfig (please read the `/config/autoconfig-instructions.txt` before enabling) provided, and once you have added your Binance credentials, the BOT will start trading.

🚸 The provided config contains a Autoconfig using a Stepgrid trading algorithm with the base of BTC, trading 8 pairs. This works at the moment extremely well for at the current market (August 2021) with returns of 1-8% per trade and trading between 20-50 times per day on Binance. Do read the `/config/autoconfig-instructions.txt` and only change what is allowed. Alternatively, use the standard Gunbot install and use an algorithm you understand / are comfortable with.

😭 Do not come crying to me if you lost your house and your wife left you because you traded away your savings. Be responsible and only trade what you are prepared to lose. I am not a financial advisor, and will not help you with your financial troubles.

Detailed Gunbot documentation and support is available via [https://wiki.gunthy.org/](https://wiki.gunthy.org/)

<p align="center">
<a href="https://wiki.gunthy.org/"><img src="https://gblobscdn.gitbook.com/assets%2F-L_Rejuz9K0BDQxSQvUH%2F-MP8i9_pHeuD_bvxnAAl%2F-MP8j1c3cbIvuS9yckyg%2Fimage.png?alt=media&token=90c41159-642e-4978-ba26-ee6c7713ee2a" alt="Gunbot Docker File"></a><br/>
<b>Gunbot Trading Console via Webview</b><br/>
</p>

___
![paypal](https://img.shields.io/badge/PayPal--ffffff.svg?style=social&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8%2F9hAAAABHNCSVQICAgIfAhkiAAAAZZJREFUOI3Fkb1PFFEUxX%2F3zcAMswFCw0KQr1BZSKUQYijMFibGkhj9D4zYYAuU0NtZSIiNzRZGamqD%2BhdoJR%2FGhBCTHZ11Pt%2B1GIiEnY0hFNzkFu%2FmnHPPPQ%2Buu%2BTiYGjy0ZPa5N1t0SI5m6mITeP4%2B%2FGP%2Fbccvto8j3cuCsQTSy%2FCzLkdxqkXpoUXJoUXJrkfFTLMwHiDYLrFz897Z3jT6ckdBwsiYDMo0tNOIGuBqS%2Beh7sdAkU2g%2BkBFGkd%2FrtSgD8Z%2BrBxj68MAGG1A9efRhVsXrKMU7Y4cNyGOwtDU28OtrqdUMetldvzFKxCYSHJ4NsJ%2BnRJGexHba7VJ%2FTff4BaQFBjVcbqIEZ1bESYn4PRUcHx2N952awUkOHZedUcWm14%2FtjqjREHawUEsgx6Ajg5%2Bsi7jWqBwA%2BmIrXlo9YHUVTmEP%2F6hOO1Ofiyy3pjo%2BsvBDX%2FZpSakhz4BqvQDvdYvrXQEXZViI5rPpBEOwR2l16vtN7bd9SN3L1WXj%2BjGSnN38rq%2B7VL8xXQOdDF%2F0KvXn8BlbuY%2FvUAHysAAAAASUVORK5CYII%3D)
🍺 **Please support me**: Although all my software is free, it is always appreciated if you can support my efforts on Github with a [contribution via Paypal][paypal] - this allows me to write cool projects like this in my personal time and hopefully help you or your business. 
___

### I am a Gunbot Reseller and Binance Affiliate
You need at least a "Gunbot Standard" License to trade on Binance and use the provided autoconfig tool which automatically trades BTC-ALT coins for you. I am an offical [Gunbot Reseller](https://gunthy.org/resellers/) and you can purchase a license straight from the links below or via [gunbot.at](https://gunbot.at/):


| Gunbot Edition   |   Price    |  Link |
| ---------------- |------------| ------------------------------------------------------------------------------ |
| Gunbot Standard  |   $  59,00 | [gunbot/promoStandard](https://checkout.gunbot.com/awesome/promoStandard?inviteRef=EOTSI) |
| Gunbot Pro       |   $ 149,00 | [gunbot/promoPro](https://checkout.gunbot.com/awesome/promoPro?inviteRef=EOTSI)           |
| Gunbot Defi      |   $ 249,00 | [gunbot/promoUltimate](https://checkout.gunbot.com/awesome/ultimate?inviteRef=EOTSI) |

<p align="center">
(*) You can always upgrade to a higher license later - I can help you - contact me on Telegram <a href="https://t.me/magicdude4eva" title="Contact @magicdude4eva on Telegram">@magicdude4eva</a>
</p>


🏆 If you are new to Binance, [I can share my affiliate link where both of us will earn 10% commission on trades](https://accounts.binance.com/register?ref=13896895).

🚀 2021-11-20: If you have not signed up with Crypto.com to trade in CRO, read this: [Crypto.com Visa Debit Card with Cashback and 100% rebate on Netflix, Spotify & Amazon Prime](https://www.naschenweng.info/2021/11/10/crypto_com_visa_debit_card_supercharger/)


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
ℹ️ I use the container `gunbot` for Binance and the container `gunbot-kucoin`for Kucoin. If you do not need both, delete the one you are using.

ℹ️ The container `gunbot-kucoin` only trades USDT-CRO as I like Crypto.com - please adjust if you need anything else. The trading limit for USDT-CRO is set to USDT=150 per trade (see `"TRADING_LIMIT": "150",`in 

1) If you have a mount-point `/volume1/`, create the directory `/volume1/docker/gunbot/` and skip to Step 3)

2) If you do not have `/volume1/`, adjust the mountpoints of `/volume1/docker/gunbot/` in `docker-compose.yml`

3) Copy `docker-compose.yml`, `dockerignore` and `Dockerfile` from this repo to your `./gunbot/`-folder. If you also want to use beta-releases, use the `Dockerfile.slipstream.local` instead and rename it to `Dockerfile`. This requires that you have the beta-release in the same folder as the Dockerfile named as `gunthy-linux.zip`

3.a.) I created a `setup.sh` which you can execute in your gunbot-directory which will do the copying of files and adjusting permissions - run this in your gunbot directory:
```
curl -fsSL -H 'Cache-Control: no-cache' -o setup.sh https://raw.githubusercontent.com/magicdude4eva/docker-gunbot/refs/heads/main/setup.sh && bash setup.sh
```

ℹ️ Note: you will still need to adjust config/config.js and adjust your `docker-compose.yml`

5) Adjust the timezone setting `TZ=Europe/Vienna` in `docker-compose.yml` and `Dockerfile` to your local settings

6) Place your config.js into `/config` and/or `/config-kucoin`

7) Adjust the download Link in `Dockerfile` for `INSTALL_URL`. The latest software can be found via: [https://www.gunbot.com/downloads/](https://www.gunbot.com/downloads/)

8) and then execute:
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
Note: You will need to have at leasT "Gunbot Standard" to support all strategies, and I strongly recommend it. If you want to trade on multiple exchanges use "Gunbot Pro" (3 API Slots) or "Gunbot Ultimate (5 API Slots)

<p align="center">
<a href="https://checkout.gunbot.com/awesome/promoStandard?inviteRef=EOTSI"><img src="https://raw.githubusercontent.com/magicdude4eva/docker-gunbot/refs/heads/main/licenses.jpg" alt="Gunbot License differences"></a><br/>
<b>Gunbot License differences - click to purchase a "Gunbot Standard License" or pick other licenses from above</b><br/>
</p>


## How does the autoconfig work?
The idea is to have a fully automated setup for BTC-alt trading that trades relatively frequently (in tests, about 20-50 times per day) and only focusses on small trades with around 0.5% to 2% profit per trade. This config bundle offers completely autonomous trading with the stepGrid strategy. You set a few basic settings like how many pairs to trade, the script handles everything else.

<img width="1335" alt="CleanShot 2021-09-19 at 11 53 11@2x" src="https://user-images.githubusercontent.com/1632781/133923199-378e3e51-5771-4894-a4d6-e0ec3cd44ce3.png">

The setup consists of a config.js and autoconfig.json file, which do the following (summarized):

🚸 The "autoconfig.json" in the "gunbot" container trades as base both BTC-ALT and BNB-ALT and each base uses 6 pairs - so you will have 6 BTC-trades and 6-BNB-trades. Please adjust this if you do not want to trade in these volumes (you will need 0,3BTC and 2BNB for it to properly work)

`Autoconfig.json`

🚸 Warnings:
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

## Troubleshooting
If you do not manage to resolve your problems with basic troubleshooting, log a Issue in this project. For basic problems:

1) Check that your permissions of folders are correct:
<img width="578" alt="image" src="https://github.com/user-attachments/assets/78607496-c566-46b2-b903-97ed5951e1d9">

2) Check the log output when starting the container
`docker logs -n 100 -f gunbot`

3) Check for any Gunbot errors - most of the time the JSON is invalid (missing brackets, commas, quotes)

If you log an issue, ensure that you include your logs, but make sure to remove any reference to your API keys or Gunbot masterkeys/passwords.


## Donations are always welcome

[paypal]: https://paypal.me/GerdNaschenweng

🍻 **Support my work**  
All my software is free and built in my personal time. If it helps you or your business, please consider a small donation via [PayPal][paypal] — it keeps the coffee ☕ and ideas flowing!

💸 **Crypto Donations**  
You can also send crypto to one of the addresses below:

```
(BTC)   bc1qdgdkk7l98pje8ny9u4xavsvrea8dw6yu8jpnyf
(ETH)   0x5986f713A538D6bCaC0865564dCD45E2600A3469  
(POL)   0x5986f713A538D6bCaC0865564dCD45E2600A3469
(CRO)   0xb83c3Fe378F5224fAdD7a0f8a7dD33a6C96C422C (Cronos or Crypto.com Paystring magicdude$paystring.crypto.com)
(BNB)   0x5986f713A538D6bCaC0865564dCD45E2600A3469
(LTC)   ltc1qexst2exxksfyg7erfzlfrm23twkjgf7e5fn64t
(DOGE)  DMQsxc9XGF6526drBJDZeX7AjFDJsEz4mN
(SOL)   t4bYQCUuoCUrp7kJ4Mz314npcTuKoUSXj28UgdMrfTb
```

🧾 **Recommended Platforms**  
- 👉 [Curve.com](https://www.curve.com/join#DWPXKG6E): Add your Crypto.com card to Apple Pay  
- 🔐 [Crypto.com](https://crypto.com/app/ref6ayzqvp): Stake and get your free Crypto Visa card  
- 📈 [Binance](https://accounts.binance.com/register?ref=13896895): Trade altcoins easily
## Use Rotki for Crypto Tracking
Referral: A great crypto currency tracking platform which can be selfhosted is [Rotki](https://github.com/rotki/rotki)
![CleanShot 2021-10-03 at 10 09 53@2x](https://user-images.githubusercontent.com/1632781/135745563-1d0880a8-486d-450a-823a-499763f14d57.png)

You can find the composer file under the `rotki` folder.

![visitors](https://visitor-badge.laobi.icu/badge?page_id=magicdude4eva.magicdude4eva)
