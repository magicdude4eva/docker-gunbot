[paypal]: https://paypal.me/GerdNaschenweng

# Gunbot Docker Edition for Synology NAS / Linux

![GitHub stars](https://img.shields.io/github/stars/magicdude4eva/docker-gunbot?style=social)
![GitHub forks](https://img.shields.io/github/forks/magicdude4eva/docker-gunbot?style=social)
![GitHub issues](https://img.shields.io/github/issues/magicdude4eva/docker-gunbot)
![Docker Pulls](https://img.shields.io/docker/pulls/magicdude4eva/gunbot-colorised)
![Docker Stars](https://img.shields.io/docker/stars/magicdude4eva/gunbot-colorised)
[![GitHub last commit](https://img.shields.io/github/last-commit/magicdude4eva/docker-gunbot.svg)](https://github.com/magicdude4eva/docker-gunbot/commits/master)
[![Build and Push Docker image](https://github.com/magicdude4eva/docker-gunbot/actions/workflows/docker-build-gunbot-core.yml/badge.svg)](https://github.com/magicdude4eva/docker-gunbot/actions/workflows/docker-build-gunbot-core.yml)

![paypal](https://img.shields.io/badge/PayPal--ffffff.svg?style=social&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8%2F9hAAAABHNCSVQICAgIfAhkiAAAAZZJREFUOI3Fkb1PFFEUxX%2F3zcAMswFCw0KQr1BZSKUQYijMFibGkhj9D4zYYAuU0NtZSIiNzRZGamqD%2BhdoJR%2FGhBCTHZ11Pt%2B1GIiEnY0hFNzkFu%2FmnHPPPQ%2Buu%2BTiYGjy0ZPa5N1t0SI5m6mITeP4%2B%2FGP%2Fbccvto8j3cuCsQTSy%2FCzLkdxqkXpoUXJoUXJrkfFTLMwHiDYLrFz897Z3jT6ckdBwsiYDMo0tNOIGuBqS%2Beh7sdAkU2g%2BkBFGkd%2FrtSgD8Z%2BrBxj68MAGG1A9efRhVsXrKMU7Y4cNyGOwtDU28OtrqdUMetldvzFKxCYSHJ4NsJ%2BnRJGexHba7VJ%2FTff4BaQFBjVcbqIEZ1bESYn4PRUcHx2N952awUkOHZedUcWm14%2FtjqjREHawUEsgx6Ajg5%2Bsi7jWqBwA%2BmIrXlo9YHUVTmEP%2F6hOO1Ofiyy3pjo%2BsvBDX%2FZpSakhz4BqvQDvdYvrXQEXZViI5rPpBEOwR2l16vtN7bd9SN3L1WXj%2BjGSnN38rq%2B7VL8xXQOdDF%2F0KvXn8BlbuY%2FvUAHysAAAAASUVORK5CYII%3D)
🍺 **Please support me**: Although all my software is free, it is always appreciated if you can support my efforts on Github with a [contribution via Paypal][paypal] - this allows me to write cool projects like this in my personal time and hopefully help you or your business. 

✅ Compatible with Gunbot version: Gunbot v30.7.3

✅ Compatible with Synology DSM6.0, DSM7.0 (both on DS1019+)

🆘 Help and support via [magicdude4eva/docker-gunbot](https://github.com/magicdude4eva/docker-gunbot)

A minimal, colorised Docker setup for [Gunbot](https://www.gunbot.com) — the advanced crypto trading bot that runs securely on your own machine.

## 🚀 What is Gunbot?

**Gunbot** is an advanced yet easy-to-use crypto trading bot. You define or select a trading strategy, and Gunbot executes trades automatically, 24/7. It can handle **hundreds of trades per day**, adapting to market conditions with precision. For security, Gunbot runs **entirely on your own computer or server**, keeping your exchange API keys private and your data out of third-party hands.
<p align="center">
<a href="https://wiki.gunthy.org/"><img src="https://gblobscdn.gitbook.com/assets%2F-L_Rejuz9K0BDQxSQvUH%2F-MP8i9_pHeuD_bvxnAAl%2F-MP8j1c3cbIvuS9yckyg%2Fimage.png?alt=media&token=90c41159-642e-4978-ba26-ee6c7713ee2a" alt="Gunbot Docker File"></a><br/>
<b>Gunbot Trading Console via Webview</b><br/>
</p>


## 📘 Official Documentation

To get familiar with Gunbot concepts and strategies:

- **Built-in Strategies** → [Gunbot Built-in Strategies](https://www.gunbot.com/support/docs/ways-to-trade/built-in-strategies/)
- **Quickstart Guide** → [Gunbot Quickstart Guide](https://www.gunbot.com/support/guides/getting-started/gunbot-quickstart-guide/)

## 🐳 Quick Setup (Recommended)

Run the one-liner below to download the latest `docker-compose.yml` and configuration:

```bash
curl -fsSL -H 'Cache-Control: no-cache' -o setup.sh https://raw.githubusercontent.com/magicdude4eva/docker-gunbot/refs/heads/main/setup.sh && bash setup.sh
```

You’ll be prompted whether to install Gunbot in the current directory or in a new `./gunbot` folder.



🌐 Once complete, your Gunbot stack will start automatically. You can **Access the Gunbot Web UI** 👉 [http://localhost:5555/](http://localhost:5555/)

Start and stop as usual:

```bash
docker compose up -d
docker compose down
```

To update:

```bash
docker compose pull
docker compose up -d
```

## 🗂️ File Structure

```
gunbot/
├── binance_data/          # Persistent trading data and settings
├── docker-compose.yml     # Service definition
└── setup.sh               # Installer (optional)
```

## 💡 Notes

- Each exchange configuration is stored inside `binance_data`.
- Logs and config files persist across restarts.
- Adjust ports or environment variables in `docker-compose.yml` as needed.
- For troubleshooting or updates, refer to the official Gunbot support documentation.

## I am a Gunbot Reseller and Binance Affiliate
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

🚀 If you have not signed up with Crypto.com to trade in CRO, read this: [Crypto.com Visa Debit Card with Cashback and 100% rebate on Netflix, Spotify & Amazon Prime](https://www.naschenweng.info/2021/11/10/crypto_com_visa_debit_card_supercharger/)


## Docker image with colorised output & Telegram Support

<p align="center">
<a href="https://wiki.gunthy.org/"><img src="https://github.com/magicdude4eva/docker-gunbot/raw/main/gunbot-console.gif" alt="Gunbot Colorised Console Output via Docker"></a><br/>
<b>Gunbot Dockerfile with glibc and colorised output</b><br/>
</p>

<p align="center">
<a href="https://wiki.gunthy.org/"><img src="https://github.com/magicdude4eva/docker-gunbot/raw/main/gunbot-telegram.gif" alt="Gunbot Telegram Notifications via Docker"></a><br/>
<b>Gunbot Dockerfile with Telegram Notifications</b><br/>
</p>

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


-----

## Troubleshooting
If you do not manage to resolve your problems with basic troubleshooting, log a Issue in this project. For basic problems:

1) Check that your permissions of folders are correct:
<img width="578" alt="image" src="https://github.com/user-attachments/assets/78607496-c566-46b2-b903-97ed5951e1d9">

2) Check the log output when starting the container
`docker logs -n 100 -f gunbot-binance`

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