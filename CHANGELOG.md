## Gunbot v30.6.7
_Released: 2025-10-18T14:42:19+00:00_

#### Fixes
- fix hyperliquid payload for orders
- @boekenbox commits Dashboard: fix total assets chart for mexc and other exchanges with non statndard tickers strucutre

#### Added
- *📢 Introducing Candle Analysis Tournament Edition v1.83* - We’re pleased to share a new version of our trading strategy.  _(by Ahpigsy)_

#### Changed
- *📢 Introducing Candle Analysis Tournament Edition v1.83* - 🔑 In This Update:  _(by Ahpigsy)_

#### Strategy
- *📢 Introducing Candle Analysis Tournament Edition v1.83* - When using Safe Mode improvements to sideways market detection  _(by Ahpigsy)_

---

## Gunbot v30.6.6
_Released: 2025-10-16T15:33:24+00:00_

### Added
- futuresgrid, sgsfutures, stepgridhedge: add additional protection against placing orders while exchange data went stale since last order (#258)  _(by @boekenbox)_

### Changed
- *Quanta Athena v1.2* - Athena should work across GB support spot exchanges. Where your chosen spot exchange changes quote asset name, let me know and I’ll update the manual asset table so it works (example: Your exchange calls BTC, WBTC).  _(by Dave)_
- update mexc v3 orderbook endpoint to their latest breaking change. Thanks @IwillDeliver  _(by @boekenbox)_

### GUI
- Trading settings: make currency tabs smaller in the area for pair lists, to not need horizontal scrolling  _(by @boekenbox)_

### Exchange
- *Quanta Athena v1.2* - US customers are actually firewalled from Binance live options data streams, moving server location to Canada works around or employ your geo tricks - thanks @trader2022j  _(by Dave)_

### Strategy
- *Quanta Athena v1.2* - Snapshot detection to detect if api is giving stale data.  _(by Dave)_
- *Quanta Athena v1.2* - Method deciding ATM or ITM for options has better automated decision making.  _(by Dave)_
- *Quanta Athena v1.2* - Edge case where rate is a string, buy low settings are not respected.  _(by Dave)_

---

## Gunbot v30.6.5
_Released: 2025-10-15T09:14:26+00:00_

### Fixes
- fix GhostRider strategy being in built-in strats rather than CommunityDevs category

### Improved
- *📢 Introducing Candle Analysis Tournament Edition v1.82* - optimization of buying algorithm  _(by Ahpigsy)_

### Changed
- *📢 Introducing Candle Analysis Tournament Edition v1.82* - 🔑 In This Update:  _(by Ahpigsy)_

### Strategy
- *📢 Introducing Candle Analysis Tournament Edition v1.82* - Fixes an error where some users were seeing an incorrect 'insufficient funds' message.  _(by Ahpigsy)_

---

## Gunbot v30.6.4
_Released: 2025-10-14T18:41:28+00:00_

### Fixes
- Fix problem with filesystem actions of clear database feature
- *#Wick Magic R.C. 2.9.9 patch k* - #Fixed Smart capital check.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch k* - #Added Inverse mode to Wick Magic, Use simulator first. (alpha status).  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch k* - #Fixed FGI in some conditions was reading old data or wrong cached data specially when set with a multi-instance above 10 pairs, as Fear and Greed Index is a daily indicator now will make sure it updates on UTC day change to give always the real value.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch k* - #Fixed edge case for long candles  when using USE_TREND.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch k* - #Added shield to don't use multipliers if trend algo detects a Bear market, breakout and DCA affected.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_

### Improved
- Gui server: performance improvement

---

## Gunbot v30.6.3
_Released: 2025-10-14T08:42:03+00:00_

### Fixes
- fix gridbot at asterdex spot. Thanks @jacquesefs for helping in this debug
- Dashboard: fix "Portfolio Value" showing missing Data. (#255)
- if you notice wrong data, might be a "tickers" issue at the specific exchange

### GUI
- Dashboard: ensure pagination works properly in recent trades table (#250)

---

## Gunbot v30.6.2
_Released: 2025-10-12T12:46:41+00:00_

### Added
- *📢 Introducing Candle Analysis Tournament Edition v1.81* - Introduced caching for expectedMovePercent, profitTarget, and minimumSellLevel in stratStore, allowing the strategy to reuse previous calculations instead of recomputing them unnecessarily.  _(by Ahpigsy)_
- *📢 Introducing Candle Analysis Tournament Edition v1.81* - Added a 50% discrepancy threshold: If the new expectedMovePercent or profitTarget differs by more than 50% from the cached value, it reverts to the previous stable value to prevent erratic adjustments.  _(by Ahpigsy)_

### Changed
- *📢 Introducing Candle Analysis Tournament Edition v1.81* - 🔑 In This Update:  _(by Ahpigsy)_
- *📢 Introducing Candle Analysis Tournament Edition v1.81* - Detailed logging (e.g., "Cached values updated - Expected Move % Range: 6.74, ...") helps track when and why recalculations occur.  _(by Ahpigsy)_
- *📢 Introducing Candle Analysis Tournament Edition v1.81* - Other logging changes and updating of some other Panel Messages to be more concise  _(by Ahpigsy)_
- *📢 Introducing Candle Analysis Tournament Edition v1.81* - Reset cycle activated on config change, recalculating Profit Target and Expected Move % values  _(by Ahpigsy)_

### GUI
- it is just an initial commit, not gui yet, just set them in your config.js as "asterdex" and "asterdexFutures" and let's start testing the various strategies. Please report anything at our github issues tracker https://github.com/GuntharDeNiro/issues/issues

### Strategy
- *📢 Introducing Candle Analysis Tournament Edition v1.81* - minimumSellLevel is recalculated based on the effective profit target and average buy price (ABP), with the same stability check applied.  _(by Ahpigsy)_
- *📢 Introducing Candle Analysis Tournament Edition v1.81* - check that lastBuyTime is being reset after a sell, triggering the timeSinceLastBuy cooldown.  _(by Ahpigsy)_
- *📢 Introducing Candle Analysis Tournament Edition v1.81* - ensured the MAX_BASE_FUND_LIMIT check applies globally to all buy attempts (regular and BUY_ON_ENTRY)  _(by Ahpigsy)_

### Other
- initial commit of asterdex and asterdexFutures

---

## Gunbot v30.6.1
_Released: 2025-10-12T09:51:24+00:00_

### Fixes
- fix parsing of bitget open orders (ccxt issue)

### Improved
- *Quanta Athena* - Athena combines options-informed analytics, statistical modelling and dynamic capital optimisation into a single adaptive system.  _(by Dave)_

### Added
- Dashboard: add order type filtering to 'recent trades' table. #250  _(by @boekenbox)_
- Clear instance option: add checkbox to also remove pairs from config (along with removal from db and file memory)  _(by @boekenbox)_
- 'fetch additional candles': add support for INVERSE mode  _(by @boekenbox)_
- It is my personal pleasure to introduce yet another pearl from our Quanta friends. The amount of contributions @flightcommander added to Gunbot over years is stunning. So it is the value he added to Gunbot as well. It is called Quanta Athena, let's hear from him directly  _(by @boekenbox)_

### GUI
- Dashboard: ensure chart headroom for all time resolution. Ty @pls_insert_username_here  _(by @boekenbox)_

### Exchange
- *Quanta Athena* - It will launch only on Binance spot market and only available on Binance pairs that support Options trading.  _(by Dave)_

### Strategy
- *Quanta Athena* - Quanta Athena operates within that structure. It quantifies how implied volatility, strike distance and time decay shape the probabilistic distribution of future price action.  _(by Dave)_
- *Quanta Athena* - By using real-time options data, Black-Scholes probability models and regime-aware scaling, Athena aligns its trade logic with prevailing volatility states, expanding or contracting intelligently as the structure of risk evolves.  _(by Dave)_
- *Quanta Athena* - Thats a lot of technical words to unpack - a lot you might not yet understand… the good news is, you dont have to. Athena manages all this for you.  _(by Dave)_
- *Quanta Athena* - TLDR; Athena tracks the behaviour of options traders (smart money) then uses models to project where spot market price will go. Like the competition winning Quanta G-Type, Athena is another 100% quantitative trading system.  _(by Dave)_

---

## Gunbot v30.6.0
_Released: 2025-10-02T09:30:24+00:00_

### Fixes
- fix kraken AUD pairs
- @boekenbox fix for autoconfig.json add pairs job at kraken.com
- fix for PUMP token missing from Bitget
- *📜 Latest Change Log – GhostRider* - 🛠 Myriad of bug fixes that may have affected performance till date  _(by Mfanya)_

### Improved
- *📜 Latest Change Log – GhostRider* - 🔹 Improved Exit Logic  _(by Mfanya)_

### Added
- *📜 Latest Change Log – GhostRider* - 🔹 New Options & Controls  _(by Mfanya)_
- *📜 Latest Change Log – GhostRider* - ⚡️ Introduced Sharp Close (enabled by default) → closes positions faster in sideways/bad market conditions  _(by Mfanya)_

### Changed
- *📜 Latest Change Log – GhostRider* - ⚙️ Ability to disable DCA protections if desired  _(by Mfanya)_
- *📜 Latest Change Log – GhostRider* - 📏 Adjusted DCA distance to be more practical for real market conditions  _(by Mfanya)_
- *📜 Latest Change Log – GhostRider* - 💰 When Ride Profit Wave is disabled → positions now sell quickly at minimum profit level  _(by Mfanya)_
- *📜 Latest Change Log – GhostRider* - ⚡️ General refinements for smoother execution & better market adaptation  _(by Mfanya)_

---

## Gunbot v30.5.9
_Released: 2025-09-26T08:45:59+00:00_

### Fixes
- fixed bitget swap klines lenght
- fix for [30.5.8] - Hyperliquid - Ghostrider strat - Errors on multiple pair ( ETH/Hype) but no error on btc
- Fix several issues related to data displayed on portfolio value chart on dashboard. ty @pls_insert_username_here
- *#Wick Magic R.C. 2.9.9 patch I* - #Added more audit to smart capital.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch I* - #Added long period for smart capital and trend condition.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch I* - #Added check we trigger with Long Period.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch I* - #Fixed use Trend with Long Period, more anal logs.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch I* - #Added more logging for Fear and Greed Index indicator.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_

### Added
- Add to Hyperliquid USOL

### Changed
- stepgridhybrid: several changes to allow it to run on inverse mode (#182)

### GUI
- @boekenbox implemented [GUI] [Feature Request] [Quality of Life] - PNL per Pair
- @boekenbox implemented [GUI] [Feature Request] [Quality of Life] - Purge Pair/Instance
