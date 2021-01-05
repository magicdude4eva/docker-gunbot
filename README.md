[paypal]: https://paypal.me/GerdNaschenweng

Gunbot Edition Docker for Synology NAS

[![Docker Pulls](https://img.shields.io/docker/pulls/magicdude4eva/gunbot-colorised.svg)](https://hub.docker.com/r/magicdude4eva/gunbot-colorised)
[![](https://images.microbadger.com/badges/image/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised "Get your own image badge on microbadger.com")
[![](https://images.microbadger.com/badges/version/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised "Get your own version badge on microbadger.com")
[![Docker Automated build](https://img.shields.io/docker/automated/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised)
[![Docker Build Status](https://img.shields.io/docker/build/magicdude4eva/gunbot-colorised.svg)](https://microbadger.com/images/magicdude4eva/gunbot-colorised)

Compatible with Gunbot version : Gunbot v21
`https://github.com/GuntharDeNiro/BTCT/releases`


<p align="center">
<a href="https://wiki.gunthy.org/"><img src="https://gblobscdn.gitbook.com/assets%2F-L_Rejuz9K0BDQxSQvUH%2F-MP8i9_pHeuD_bvxnAAl%2F-MP8j1c3cbIvuS9yckyg%2Fimage.png?alt=media&token=90c41159-642e-4978-ba26-ee6c7713ee2a" alt="Gunbot Docker File"></a><br/>
<b>Gunbot Dockerfile with glibc and colorised output</b><br/>
</p>

___
![paypal](https://img.shields.io/badge/PayPal--ffffff.svg?style=social&logo=data%3Aimage%2Fpng%3Bbase64%2CiVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8%2F9hAAAABHNCSVQICAgIfAhkiAAAAZZJREFUOI3Fkb1PFFEUxX%2F3zcAMswFCw0KQr1BZSKUQYijMFibGkhj9D4zYYAuU0NtZSIiNzRZGamqD%2BhdoJR%2FGhBCTHZ11Pt%2B1GIiEnY0hFNzkFu%2FmnHPPPQ%2Buu%2BTiYGjy0ZPa5N1t0SI5m6mITeP4%2B%2FGP%2Fbccvto8j3cuCsQTSy%2FCzLkdxqkXpoUXJoUXJrkfFTLMwHiDYLrFz897Z3jT6ckdBwsiYDMo0tNOIGuBqS%2Beh7sdAkU2g%2BkBFGkd%2FrtSgD8Z%2BrBxj68MAGG1A9efRhVsXrKMU7Y4cNyGOwtDU28OtrqdUMetldvzFKxCYSHJ4NsJ%2BnRJGexHba7VJ%2FTff4BaQFBjVcbqIEZ1bESYn4PRUcHx2N952awUkOHZedUcWm14%2FtjqjREHawUEsgx6Ajg5%2Bsi7jWqBwA%2BmIrXlo9YHUVTmEP%2F6hOO1Ofiyy3pjo%2BsvBDX%2FZpSakhz4BqvQDvdYvrXQEXZViI5rPpBEOwR2l16vtN7bd9SN3L1WXj%2BjGSnN38rq%2B7VL8xXQOdDF%2F0KvXn8BlbuY%2FvUAHysAAAAASUVORK5CYII%3D)
:beer: **Please support me**: Although all my software is free, it is always appreciated if you can support my efforts on Github with a [contribution via Paypal][paypal] - this allows me to write cool projects like this in my personal time and hopefully help you or your business. 
___

## Docker image with colorised output

<p align="center">
<a href="https://wiki.gunthy.org/"><img src="https://github.com/magicdude4eva/docker-gunbot/raw/main/gunbot.png" alt="Gunbot Colorised Output"></a><br/>
<b>Gunbot Dockerfile with glibc and colorised output</b><br/>
</p>

## Setup On Synology
To run Gunbot via Docker download the contents of this repo. Then:

1) Adjust the mountpoints of `/volume1/docker/gunbot/`in docker-compose.yml

2) Adjust the download Link in `Dockerfile` for `INSTALL_URL` - latest software can be found via: https://github.com/GuntharDeNiro/BTCT/releases

3) Place your config.js into `/config`


and then execute:
```
cd /volume1/docker/gunbot/
docker build -t gunbot .
docker-compose up -d
docker logs -f gunbot
```


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
