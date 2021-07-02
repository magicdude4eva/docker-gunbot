[paypal]: https://paypal.me/GerdNaschenweng

# Gunbot Docker Edition for Synology NAS

[![Docker Pulls](https://img.shields.io/docker/pulls/magicdude4eva/gunbot-colorised.svg)](https://hub.docker.com/r/magicdude4eva/gunbot-colorised)
[![](https://images.microbadger.com/badges/image/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised "Get your own version badge on microbadger.com")
[![Docker Automated build](https://img.shields.io/docker/automated/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised)
[![Docker Build Status](https://img.shields.io/docker/build/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised)

:white_check_mark: Compatible with Gunbot version : Gunbot v21 [https://github.com/GuntharDeNiro/BTCT/releases](https://github.com/GuntharDeNiro/BTCT/releases)

:white_check_mark: Compatible with Synology DSM6.0, DSM7.0 (both on DS1019+)

Although this Docker Image has been tested on a Synology NAS, it will work essentially in any Docker-environment with the adjustment of the mount-point needed. I have provided a base-configuration under `/config/` which I suggest you read and adjust. If you use the autoconfig provided, and once you have added your Binance credentials, the BOT will start trading. The only thing to adjust is your "TRADING_LIMIT" in `config/config.js` and your Telegram and Binance settings.

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
1) If you have a mount-point `/volume1/`, create the directory `/volume1/docker/gunbot/` and skip to Step 3)

2) If you do not have `/volume1/`, adjust the mountpoints of `/volume1/docker/gunbot/` in `docker-compose.yml`

3) Copy `docker-compose.yml`, `dockerignore` and `Dockerfile` from this repo to your `./gunbot/`-folder

4) Adjust the timezone setting `TZ=Europe/Vienna` in `docker-compose.yml` and `Dockerfile` to your local settings

5) Place your config.js into `/config`

6) Adjust the download Link in `Dockerfile` for `INSTALL_URL`. The latest software can be found via: https://github.com/GuntharDeNiro/BTCT/releases

7) and then execute:
```
cd /volume1/docker/gunbot/
docker build -t gunbot .
docker-compose up -d
docker logs -f gunbot
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
The idea is to have a fully automated setup for BTC-alt trading that trades relatively frequently (in tests, about 10 times per day) and only focusses on small trades with around 0.5% to 2% profit per trade.

![image](https://user-images.githubusercontent.com/1632781/107397927-6940ef00-6aff-11eb-9c0f-803125b178a8.png)

The setup consists of a config.js and autoconfig.json file, which do the following (summarized):

`Autoconfig.json`
- Adds & removes pairs, mainly based on their direction in the past 12h
- Disables buying on all pairs when USDT-BTC is moving up or down more than average in the last hour
- Changes some settings based on the DCA phase: when DCA started it increases the buydown for the second DCA order, the strategy sell criteria are set to a minimal 0.1% gain once DCA is completed.

`Config.js`
- Contains only one preconfigured trading strategy, based on buy trailing and stochrsi selling. It's very basic but does its job.


-----

## Donations are always welcome
:beer: **Please support me**: If the above helped you in any way, then [follow me on Twitter](https://twitter.com/gerdnaschenweng) or send me some coins: 
```
(BTC)    36nBgsAhBBzkTvJMut851XVj47bUrdsmQx
(ETH)    0xE572b3B1187a3Ab77D72f7d6AeCd18DF26306cfC
(BAT)    0x48c65D6f768D92d4a23E4e9d25329E7De67c14d9
(LTC)    M8TNsiQWe591HTkDtLubZeftbejfPMcoUy
(Ripple) rw2ciyaNshpHe7bCHo4bRWq6pqqynnWKQg (Tag: 2478959347)
(XLM)    GDQP2KPQGKIHYJGXNUIYOMHARUARCA7DJT5FO2FFOOKY3B2WSQHG4W37 (Memo ID: 909493707)
```

Sign up to [Cointracking](https://cointracking.info?ref=M263159) which uses APIs to connect to all exchanges and helps you with tax. Use [Binance Exchange](https://www.binance.com/?ref=13896895) to trade #altcoins. Join [TradingView](http://tradingview.go2cloud.org/aff_c?offer_id=2&aff_id=7432) to get trend-reports. Sign up with [Coinbase](https://www.coinbase.com/join/nasche_x) and **instantly get $10 in BTC**. I also accept old-school **[PayPal](https://paypal.me/GerdNaschenweng)**.

If you have no crypto, follow me at least on [Twitter](https://twitter.com/gerdnaschenweng).
