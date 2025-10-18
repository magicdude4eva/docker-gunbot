## 2025-10-18

### v30.6.5
- (no granular changes posted)

### v30.6.4
- Fix problem with filesystem actions of clear database feature
- Gui server: performance improvement
- #Fixed Smart capital check.
- #Added Inverse mode to Wick Magic, Use simulator first. (alpha status).
- #Fixed FGI in some conditions was reading old data or wrong cached data specially when set with a multi-instance above 10 pairs, as Fear and Greed Index is a daily indicator now will make sure it updates on UTC day change to give always the real value.
- #Fixed edge case for long candles when using USE_TREND.
- #Added shield to don't use multipliers if trend algo detects a Bear market, breakout and DCA affected.

### v30.6.3
- fix gridbot at asterdex spot. Thanks @jacquesefs for helping in this debug
- Dashboard: ensure pagination works properly in recent trades table (#250)
- Dashboard: fix "Portfolio Value" showing missing Data. (#255)

### v30.6.2
- initial commit of asterdex and asterdexFutures

### v30.6.1
- fix parsing of bitget open orders (ccxt issue)
- Dashboard: ensure chart headroom for all time resolution. Ty @pls_insert_username_here
- Dashboard: add order type filtering to 'recent trades' table. #250
- Clear instance option: add checkbox to also remove pairs from config (along with removal from db and file memory)
- 'fetch additional candles': add support for INVERSE mode
- It is my personal pleasure to introduce yet another pearl from our Quanta friends. The amount of contributions @flightcommander added to Gunbot over years is stunning. So it is the value he added to Gunbot as well. It is called Quanta Athena, let's hear from him directly
- It will launch only on Binance spot market and only available on Binance pairs that support Options trading.

