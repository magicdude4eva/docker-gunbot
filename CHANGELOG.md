## 2025-10-18

### v30.6.7
- fix hyperliquid payload for orders
- @boekenbox commits Dashboard: fix total assets chart for mexc and other exchanges with non statndard tickers strucutre
- 📢 Introducing Candle Analysis Tournament Edition v1.83
  - We’re pleased to share a new version of our trading strategy.
  - 🔑 In This Update:
  - When using Safe Mode improvements to sideways market detection
  - We hope the Candle Analysis Tournament Edition v1.83 provides a helpful tool for your trading journey.
  - Thank you for being part of our community!


### v30.6.6
- @flightcommander commits:
- Quanta Athena v1.2
  - Changes in Behaviour:
  - Athena should work across GB support spot exchanges. Where your chosen spot exchange changes quote asset name, let me know and I’ll update the manual asset table so it works (example: Your exchange calls BTC, WBTC).
  - US customers are actually firewalled from Binance live options data streams, moving server location to Canada works around or employ your geo tricks - thanks @trader2022j
  - Enhancements:
  - Snapshot detection to detect if api is giving stale data.
  - Method deciding ATM or ITM for options has better automated decision making.
  - Bug Fixes:
  - Edge case where rate is a string, buy low settings are not respected.
- @boekenbox commits:
- futuresgrid, sgsfutures, stepgridhedge: add additional protection against placing orders while exchange data went stale since last order (#258)
- Trading settings: make currency tabs smaller in the area for pair lists, to not need horizontal scrolling
- update mexc v3 orderbook endpoint to their latest breaking change. Thanks @IwillDeliver

### v30.6.5
- fix GhostRider strategy being in built-in strats rather than CommunityDevs category
- 📢 Introducing Candle Analysis Tournament Edition v1.82
  - We’re pleased to share a new version of our trading strategy.
  - 🔑 In This Update:
  - Fixes an error where some users were seeing an incorrect 'insufficient funds' message.
  - optimization of buying algorithm
  - We hope the Candle Analysis Tournament Edition v1.82 provides a helpful tool for your trading journey.
  - Thank you for being part of our community!

### v30.6.4
- @boekenbox commits
- Fix problem with filesystem actions of clear database feature
- Gui server: performance improvement
- @crazymop commits:
- #Wick Magic R.C. 2.9.9 patch k
  - #Fixed Smart capital check.
  - #Added Inverse mode to Wick Magic, Use simulator first. (alpha status).
  - #Fixed FGI in some conditions was reading old data or wrong cached data specially when set with a multi-instance above 10 pairs, as Fear and Greed Index is a daily indicator now will make sure it updates on UTC day change to give always the real value.
  - #Fixed edge case for long candles when using USE_TREND.
  - #Added shield to don't use multipliers if trend algo detects a Bear market, breakout and DCA affected.

### v30.6.3
- fix gridbot at asterdex spot. Thanks @jacquesefs for helping in this debug
- @boekenbox commits
- Dashboard: ensure pagination works properly in recent trades table (#250)
- Dashboard: fix "Portfolio Value" showing missing Data. (#255)
- in this build yu can use gunbot monitor and see this value
- if you notice wrong data, might be a "tickers" issue at the specific exchange
- in that case, please report at github issues tracker and attach any json state file for that specific exchange
- tested at binance, bitget, gate.io, huobi and crypto.com
- in alternative you can just send your json file in my pm saying something like "this exchange doesnt show total balances in monitor"

### v30.6.2
- initial commit of asterdex and asterdexFutures
- Instructions:
- it is just an initial commit, not gui yet, just set them in your config.js as "asterdex" and "asterdexFutures" and let's start testing the various strategies. Please report anything at our github issues tracker https://github.com/GuntharDeNiro/issues/issues
- asterdex is a decentralized exchange, you need a deFi license to run it
- @Ahpigsy commits:
- 📢 Introducing Candle Analysis Tournament Edition v1.81
  - We’re pleased to share a new version of our trading strategy.
  - 🔑 In This Update:
  - Introduced caching for expectedMovePercent, profitTarget, and minimumSellLevel in stratStore, allowing the strategy to reuse previous calculations instead of recomputing them unnecessarily.
  - Added a 50% discrepancy threshold: If the new expectedMovePercent or profitTarget differs by more than 50% from the cached value, it reverts to the previous stable value to prevent erratic adjustments.
  - minimumSellLevel is recalculated based on the effective profit target and average buy price (ABP), with the same stability check applied.
  - Detailed logging (e.g., "Cached values updated - Expected Move % Range: 6.74, ...") helps track when and why recalculations occur.
  - check that lastBuyTime is being reset after a sell, triggering the timeSinceLastBuy cooldown.
  - ensured the MAX_BASE_FUND_LIMIT check applies globally to all buy attempts (regular and BUY_ON_ENTRY)
  - Other logging changes and updating of some other Panel Messages to be more concise
  - Reset cycle activated on config change, recalculating Profit Target and Expected Move % values
  - We hope the Candle Analysis Tournament Edition v1.81 provides a helpful tool for your trading journey.
  - Thank you for being part of our community!
- Which one of all of these strategies are being more profitable?
- Let's discover it at our leaderboard https://www.gunbot.com/leaderboard/
- I've started to filter it for the ongoing tournament, now they all have at least 60 days of trading, stay tuned for more updates on the Gunbot Community Tournament as we are approaching Xmas Time with the finals!

