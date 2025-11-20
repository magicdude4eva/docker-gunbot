## Gunbot v30.7.7
_Released: 2025-11-19T13:44:34+00:00_

#### Fixes
- fix bybit url for global users. Thanks @crazymop
- fix for Mexc - purchase too low
- *Wick Magic R.C. 2.9.9 - Patch n released* - Introducing the Fear & Greed Index Mimix Profile  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 - Patch n released* - A new adaptive sentiment module that enhances precision in entries, exposure control and market alignment.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 - Patch n released* - This patch also brings the new Love This Shizcoin mode:  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 - Patch n released* - This patch also includes:  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 - Patch n released* - Refined % Capital Use display  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 - Patch n released* - Updated internal math for more accurate position metrics  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 - Patch n released* - Better risk alignment across all market conditions  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_

#### Added
- API key management: add options to select bybit api url  _(by @boekenbox)_
- frontend: add support for bitget period 3  _(by @boekenbox)_

#### GUI
- Dashboard: refresh total assets chart less often  _(by @boekenbox)_


---

## Gunbot v30.7.6
_Released: 2025-11-13T20:56:00+00:00_

#### Fixes
- *#Wick Magic R.C. 2.9.9 patch m* - #First commit of Limit orders (post/limit) with orderbook smart placement.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch m* - #Fixed Typo in strategy editor Pullback field.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch m* - #Possible fix for Edge  Inverse wiring case, feedback needed.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch m* - #Added human readable time in console logs for breakout cooldown.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch m* - #Fixed displaying old grid lines when the user did swap strat to wick magic.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch m* - #Fixed max capital respected with DCA.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- Trading settings: fix case that sometims required importing a strategy from leaderboard twice. #299  _(by @boekenbox)_

#### Added
- check the new implementation behaves like expected in terms of balances, position size, open and filled orders, orderbook, klines etc
- to configure the above i've implemented a new parameter in your config.js same place you set your api keys (and @boekenbox is preparing a drowdown menu in the frontend for you)
- *📢 Introducing update for Expected Move Version 1.07 and Expected Move Plus Version 1.2* - We’re pleased to share a new version of our trading strategy.  _(by Ahpigsy)_

#### Changed
- *📢 Introducing update for Expected Move Version 1.07 and Expected Move Plus Version 1.2* - 🔑 In This Update:  _(by Ahpigsy)_
- *📢 Introducing update for Expected Move Version 1.07 and Expected Move Plus Version 1.2* - Fixes an error where in some circumstances Expected Move % returns 0% no matter what period is selected.  _(by Ahpigsy)_
- *📢 Introducing update for Expected Move Version 1.07 and Expected Move Plus Version 1.2* - We hope the Expected Move updates  provides a helpful tool for your trading journey.  _(by Ahpigsy)_

#### Other
- Dasbhoard: ensure date range picker popover stays visible  _(by @boekenbox)_


---

## Gunbot v30.7.5
_Released: 2025-11-08T14:26:17+00:00_

#### Fixes
- @boekenbox and @crazymop found a case where pnl values got null: the fix will allow us to play with this new toy for the week-end. Thank you boys


---

## Gunbot v30.7.3
_Released: 2025-10-31T13:24:11+00:00_

#### Fixes
- *📜 New Update – MFRider & GhostRider* - 🧩 Fixed short DCA issues on Hyperliquid (HL)  _(by Mfanya)_
- *📜 New Update – MFRider & GhostRider* - 🛠 General stability improvements and minor bug fixes  _(by Mfanya)_
- *📜 New Update – MFRider & GhostRider* - 🛠 Fixed minor issues affecting execution and performance  _(by Mfanya)_
- *📜 New Update – MFRider & GhostRider* - ⚡️ Additional small bug fixes and refinements  _(by Mfanya)_
- FuturesGrid: fix for "The strat doesn't open its initial position" #277  _(by @boekenbox)_

#### Added
- *📜 New Update – MFRider & GhostRider* - 📲 Join the discussion & get updates: https://t.me/tradewithmfanya  _(by Mfanya)_

#### Changed
- trading settings: change import from leaderboard, previously imported strategy only, now also configures the pair for it  _(by @boekenbox)_

#### GUI
- Chart: use order timestamp for order notifications, instead of current time. #269  _(by @boekenbox)_

#### Other
- stepgrid, stepgridhybrid, stepgridscalp, channelmaestro: much faster math to determine partial sell volumes.  _(by @boekenbox)_

**Download:** files are available at https://www.gunbot.com/downloads


---

## Gunbot v30.7.2
_Released: 2025-10-28T21:45:11+00:00_

#### Fixes
- fix hyperliquid spinning with the new KPIs stats, thanks @crazymop @T_K_O_1 @DWT80s @iPUMPUSHA
- fix Hyperliquid - simulator
- fix GimmePairs on latest on kraken Spot doesn't return the USD-BTC pair.

**Download:** files are available at https://www.gunbot.com/downloads


---

## Gunbot v30.7.0
_Released: 2025-10-25T11:20:13+00:00_

#### Improved
- AI: Based on the global indicators, your trading performance this week has been positive with a Return on Investment (ROI) of 0.32 and a Risk Reward ratio (RR) of 0.84. Your Capital Efficiency (CapEff) is at 74.06%, and you currently have assets totaling $10,397.58.
- You: are those ROI, RR and Capital Efficiency values good or could you suggest something to improve my trades profit?
- AI: The Return on Investment (ROI) of 0.32 means that for every dollar you have invested, you are currently earning $0.32 in profit. In the context of trading, an ROI of 0.32 is considered decent, but there is room for improvement.
- To enhance your trading profitability, you could consider reallocating your investments towards exchanges or assets that have historically shown higher realized Profit and Loss (PnL). By focusing on exchanges or assets that have a track record of delivering better returns, you can potentially increase your ROI and overall trading performance.
- It's important to conduct thorough research and analysis before reallocating your investments to ensure that you are making informed decisions based on historical data and market trends. Additionally, diversifying your portfolio across different exchanges or assets can help spread risk and potentially improve your ROI over time.
- By strategically reallocating your investments towards exchanges with higher realized PnL, you can aim to enhance your trading profitability and optimize your portfolio efficiency.
- To enhance your profits and optimize your capital allocation, here are some realistic reallocation ideas based on measurable metrics:
- 1. Reallocation towards Bitget and Binance: Since Bitget and Binance have shown consistent positive returns over various timeframes, you could consider reallocating a portion of your capital from exchanges with lower PnL performance to Bitget and Binance. This reallocation can potentially increase your overall ROI and capitalize on the historical performance of these exchanges.
- 2. Diversification: While Bitget and Binance have performed well, it's also important to diversify your portfolio to spread risk. Consider allocating a portion of your capital to gateio, which has shown moderate but positive returns. Diversification can help mitigate risk and potentially improve your overall portfolio efficiency.
- 3. Regular Monitoring and Adjustment: Continuously monitor the performance of your investments on different exchanges and adjust your capital allocation accordingly. If an exchange starts underperforming or shows a decline in PnL, consider reallocating your capital to exchanges with better performance to optimize your returns.
- By strategically reallocating your capital towards exchanges with better performance metrics and maintaining a diversified portfolio, you can aim to increase your returns and enhance your overall trading profitability. Remember to regularly review and adjust your capital allocation based on the performance of each exchange to optimize your trading strategy.

#### Added
- add convertedBalances in ledger (useful for Gunbot Monitor): they represent the total holding you have at your exchange, converted in each and every asset
- I'm also uploading a new build for Gunbot Monitor, you will be able to download it from the same link you initially downloaded it (find it in your welcome email or ask uri)
- added some more metrics in the Overview (please help me to understand which of those are really useful to you and what you would like to display there)
- Added some more metrics in Analysis tab, help me find out what would be really interesting for us there (special KPI or whatever)
- a better settings page, dividing config parameters and override by categories, also allowing to add any pair override you want directly from MONIT
- she knows everything about your trading performances, about your capital allocation, about your profit and losses and she is always excited to give you new ideas to enhance your trading experience


---

## Gunbot v30.6.9
_Released: 2025-10-23T16:41:57+00:00_

#### Fixes
- Dashboard: fix date range filter behavior, which sometimes didn't show newly filtered data (#260)  _(by @boekenbox)_

#### Improved
- *📜 Latest Change Log – Mfanya Strategies* - 🕯 Added Wick Trade feature – automatically enabled for improved entry precision  _(by Mfanya)_
- gui web server: increase compression to default setting, improve use of caching  _(by @boekenbox)_

#### Changed
- *📜 Latest Change Log – Mfanya Strategies* - 📏 Increased DCA distance slightly – previous range was too tight, now allows better trade spacing and safer scaling  _(by Mfanya)_

#### Exchange
- API key management: input field for vault address, needed when used on a subaccount at Hyperliquid  _(by @boekenbox)_

#### Strategy
- *Quanta Athena v1.3* - None  _(by Dave)_
- *Quanta Athena v1.3* - Retrieve options unit basket data for assets where units are greater than 1. Thank you @ztam75  _(by Dave)_

#### Other
- Custom strategies: make it easier to collect candle data from all timeframes above the main strategy PERIOD. Set 'MULTI_COMP' true as override, regardless of ws or rest api, and get all higher tf candle data in gb.data.multiTfData  _(by @boekenbox)_


---

## Gunbot v30.6.8
_Released: 2025-10-20T18:28:47+00:00_

#### Fixes
- fix [Hyperliquid] GB post-only order method is not respected
- @boekenbox fix [Kraken futures] Multiple orders sent instead of one
- fix asterdex
- fix [30.6.0] - DYDX - FARTCOIN, XRP, SOL missing on DYDX
- fix fix parsing of bitget open orders (ccxt issue)
- fix Quanta-G does not function on MEXC because gunbot does not detect a fulfilled sell order
- fix PUMP token missing from Bitget
- *📜 Exchange Fix Update – GhostRider v1.1.6* - 🔹 🧮 Fixed issue with Hyperliquid PnL calculations  _(by Mfanya)_
- *📜 Exchange Fix Update – GhostRider v1.1.6* - 🔥 These fixes ensure more accurate performance tracking and reliable position management on Hyperliquid.  _(by Mfanya)_
- *📜 Exchange Fix Update – GhostRider v1.1.6* - 📲 Join the discussion & get updates: https://t.me/tradewithmfanya  _(by Mfanya)_
- *#Wick Magic R.C. 2.9.9 patch l* - #Fixed capital for all entries and re-entries.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch l* - #Fixed FGI to respect DCA entry too.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#Wick Magic R.C. 2.9.9 patch l* - #Fixed an issue where breakout didn't respect HH with the long period.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_


---

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
