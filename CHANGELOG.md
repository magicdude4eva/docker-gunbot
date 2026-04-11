## Gunbot v31.0.1
_Released: 2026-04-08T14:57:09+00:00_

#### Fixes
- fix TypeError: Converting circular structure to JSON during bb buy execution on Coinbase
- fix Bot not spinning if autoconfig.json is totally missing
- Hyperliquid: fix sidebar stats for non spot pairs  _(by @boekenbox)_
- autoconfig: improve memory usage, especially for jobs using tickers data. fix possible crash on manageOverrides2 job type  _(by @boekenbox)_

#### Improved
- unit cost: improve handling of user configured 0 fees  _(by @boekenbox)_

#### Changed
- spotgridadvanced: change hardcoded upper tf 240 to use alternate in case exchange doesn't offer 240  _(by @boekenbox)_


---

## Gunbot v30.9.9
_Released: 2026-03-07T09:55:01+00:00_

#### Fixes
- fix for Alpaca doesn't load under very latest
- fix for Aster futures shows quote balance while no position
- fix for bybit short pairs in Unrealized PnL column in the “Compare pairs” view shows n/a, while the LONG side of the same symbol correctly displays Unrealized PnL.
- fix for Hyperliquid backtesting fail to start
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - The biggest usability upgrade yet. One click, fully configured. No more guessing which settings work for your style.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - Wick Scalp — 1m ultra-fast entries, tight trailing, aggressive momentum. For adrenaline junkies with liquid pairs.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - Fast Momentum — 5m balanced speed, smart DCA spacing. The all-rounder with teeth.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - Trend Sniper — 15m confirmed entries only. SuperTrend shield, 2-green HA filter, higher profit targets. Patient and precise.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - Swing Hunter — 15m swing trades with Smart Capital protection and same-ratio partial sells. Lets winners run.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - Position Flow — 1h position building with limit orders, deep DCA zones and tight capital management. Set and forget.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - Select a preset from the GUI, adjust your Capital, Trading Limit and Min Volume to Sell, and you are trading. Every override is written to config so Gunbot never falls back to engine defaults.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - Changed your mind? Switch presets anytime. Want to tweak after? Go ahead, your adjustments are preserved until you pick a new preset.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - Full parameter audit: defaults aligned across all 96 strategy variables  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - New Limit Orders section in the GUI (OL Spread, Depth, TTL)  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - Pullback, cooldown and trailing params now exposed for advanced users  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V4 is live* - Deprecated keys auto-cleaned on startup  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_

#### Other
- created gb.method.returnPublicTradeHistory for custom strats


---

## Gunbot v30.9.7
_Released: 2026-02-20T17:21:50+00:00_

#### Fixes
- @boekenbox fix for OKX exchange: Autoconfig Add Pairs not wroking
- @boekenbox  commits Chart: possibly fix a case where chart remains in loading status. ty @T_K_O_1(loading symbol based on query params works, sorry for last one)
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - Massive reliability and precision patch. The bot is now leaner (1,400 lines of dead code removed), smarter, and more honest about what it's doing on your chart.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - Chart lines now show the REAL DCA levels — exactly where the bot will actually buy, not an approximation.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - Fixed a bug where DCA zones could appear ABOVE your last buy price (made no sense, now impossible).  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - Freeze zone now tracks the correct reference price after partial sells.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - Fixed a rare cooldown bypass where timestamp comparisons silently failed, letting trades through with zero delay.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - Rebuilt limit order tracking from scratch — no more ghost orders or lost fills.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - Auto-cancels stale orders (TTL expired, price drifted too far, or would execute as taker).  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - Works across all entry types: Ultra, HA, Aggressive, Breakout, Pullback, Re-entries.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - 62 unused functions removed, 1,400+ lines of dead code gone.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - Garbage Collector v2: clean state transitions when selling entire position.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch V is live* - Faster execution, smaller memory footprint.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_

#### Added
- How to enable self-signed ssl:

#### GUI
- some services demand SSL for gunbot, especially some i'm developing to be used in a near future. I've implemented a self-signed certificate function in gunbot that would automatically serve the gui over https
- that's it: it will create self-signed certs and serve the gui over https


---

## Gunbot v30.9.6
_Released: 2026-02-14T14:40:37+00:00_

#### Fixes
- [Bug] TradingView Charting Library Fails to Render (Blank Chart Area)
- *gtrendfutures 10.7* - 1. fixed dcaing entries: now reading from last purchase (was incorrectly reading break even) 📉  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_
- *gtrendfutures 10.7* - 2. fixed reversals: users can use reversals before max position hit 🔄  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_
- *gtrendfutures 10.7* - 3. fixed reentryvalue: now reading from the last order instead of the first 🎯  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_

#### Added
- The 24h high price and low price in add pairs tab at kraken.com isn't updated.

#### GUI
- 30.7.7 - AsterFutures - Ghostrider - Limit order cannot be placed in GUI

#### Exchange
- #feature Hyperliquid does expose ClosedPnL + fees via API (fills endpoint)
- Binance Futures: builder strategy double long opened in same candle
- Kraken Futures orders parsing creates bogus orders (epoch 1970 + NaN rows)
- Kraken Futures balance desync after manual position close (TypeError: position undefined)
- futuresGrid roe an upnl in sidebar not correct when set with default cross leverage for kraken Futures.
- Bitget futures coin-m no base balance

#### Other
- https://github.com/GuntharDeNiro/issues/issues/339
- Aster futures shows quote balance while no position
- Aster futures market close doesn’t work
- Alpaca trading terminal retuns error : "message": "Request failed with status code 422",


---

## Gunbot v30.9.5
_Released: 2026-02-07T16:54:49+00:00_

#### Fixes
- [BUG] Gunbot State Candle Data Mismatch with GUI and Exchange OHLCV on Hyperliquid
- [Bug] TradingView Charting Library Fails to Render (Blank Chart Area)
- [30.9.4]| [Binance] | [Bug] - "Fetch Trade History" Result incorrect
- *🚀 Wick Magic R.C. 2.9.9 – Patch U is live* - Patch U focuses on stability, precision, and trust. This update tightens core execution logic and removes a few subtle edge cases that could affect real-world performance over long trading sessions.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch U is live* - What’s new in Patch U:  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch U is live* - We’ve resolved the remaining edge cases in the DCA flow. Re-entries now trigger exactly when conditions are met, without false blocks or missed opportunities after partial sells.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch U is live* - 📉 Partial Sell Edge Case Fixed  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch U is live* - 🧠 CoinMarketCap FGI Connection Fixed  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch U is live* - 🛡 Improved Internal Guards & State Handling  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *🚀 Wick Magic R.C. 2.9.9 – Patch U is live* - No new complexity added. Patch U is about reliability, not noise. Your charts, orders, and decisions now align even more tightly under the hood.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *#GTRENDFUTURES  10.6* - 🧹Fixed on the futures hedging GTREND_CUSTOM_STRATEGY": "automated_GTREND", fetching local timeframe from hedging timeframe issue thank you @V_Sheyko  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_
- *#GTRENDFUTURES  10.6* - Visual Debug & Guided Reports 📸: Upload images/videos of errors for instant analysis. The AI ​​helps you generate a structured bug report with all the mandatory data required for developers to find solutions faster.  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_

#### Improved
- *#GTRENDFUTURES  10.6* - Performance Tracking 📉: Helps you monitor bot uptime and resource usage to ensure zero downtime.  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_
- *#GTRENDFUTURES  10.6* - Performance Tuning ⚙️: AI acts as a co-pilot, adjusting leverage suggestions based on current market risk levels.  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_

#### Added
- *#GTRENDFUTURES  10.6* - 🧹 Cleaned up unnecessary filters that were causing interference with the new micro-hedge maximum position logic. ⚙️  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_
- *#GTRENDFUTURES  10.6* - G-Trend Roadmap and new toys: AI Specialist Gems 💎  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_
- *#GTRENDFUTURES  10.6* - Update Guide 🔄: Simplifies software updates, helping you migrate settings to new versions safely.  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_

#### Exchange
- Bitget futures coin-m no base balance

#### Other
- Alpaca doesn't trade with ExoTrader, not enough candles
- The pnl displayed in the main dashbord includes fees in one leg of each position instead of both.
- Aster futures shows quote balance while no position
- Aster futures market close doesn’t work
- compact a bit more telegram messages

**Download:** files are available at https://www.gunbot.com/downloads


---

## Gunbot v30.9.4
_Released: 2026-01-24T14:05:32+00:00_

#### Fixes
- fix my charts disappearing
- fix mexc market orders, thanks @Ahpigsy
- @crazymop fix for an issue with limit orders at wickmagic


---

## Gunbot v30.8.9
_Released: 2026-01-02T20:45:31+00:00_

#### Fixes
- *Wick Magic R.C. 2.9.9 – Patch S is now live* - This update brings the pulse of the market directly into your strategy.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 – Patch S is now live* - While Patch R focused on internal precision, Patch S focuses on external intelligence. We have integrated the gold standard of crypto market sentiment analysis: The CoinMarketCap (CMC) Fear & Greed Index.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 – Patch S is now live* - Highlights of this update:  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 – Patch S is now live* - Dual-Mode Sentiment Logic Patch S introduces two distinct ways to utilize this powerful data, giving you total control over how the bot reacts to market fear:  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 – Patch S is now live* - The "Safety Shield" (Block Mode): If the market enters a state of panic (Index drops below your defined threshold), Wick Magic will automatically deploy a safety net. It pauses new buy entries and DCA operations to prevent "catching a falling knife," waiting for the panic to subside before resuming trading.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 – Patch S is now live* - Midnight Guard: Intelligently detects the exact moment CoinMarketCap updates their daily score (handling the UTC midnight crossover) and forces a data refresh, ensuring you never trade on yesterday's news.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_
- *Wick Magic R.C. 2.9.9 – Patch S is now live* - 📅 Visual History Engine Your dashboard Sidebar has been upgraded with a new interactive element. Hovering over the CMC tile now reveals a dynamic historical log.  _(by ɄⱤł - Gunbot.com/es wickmagic.gunthy.es - @CrazyMop)_

#### Improved
- *🚀 GTREND FUTURES HEDGING v10.2 | CHANGELOG HIGHLIGHTS* - Solo-Trend Exits: Optimized Take-Profit and Break-even tracking  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_

#### Added
- *🚀 GTREND FUTURES HEDGING v10.2 | CHANGELOG HIGHLIGHTS* - Happy New Year and Merry Christmas to all! 🎄🥂✨  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_
- *🚀 GTREND FUTURES HEDGING v10.2 | CHANGELOG HIGHLIGHTS* - A brand new year, fresh goals, and one mission:  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_
- *🚀 GTREND FUTURES HEDGING v10.2 | CHANGELOG HIGHLIGHTS* - To start the year with some exciting new toys, I've just separated the Futures strategy into ready-to-deploy templates for super-fast setup!  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_
- *🚀 GTREND FUTURES HEDGING v10.2 | CHANGELOG HIGHLIGHTS* - Plus, two powerful new modes:  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_

#### Changed
- *🚀 GTREND FUTURES HEDGING v10.2 | CHANGELOG HIGHLIGHTS* - Important note: All updates have been thoroughly tested only on Bybit for now — please use caution if deploying on other exchanges!  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_

#### GUI
- *🚀 GTREND FUTURES HEDGING v10.2 | CHANGELOG HIGHLIGHTS* - Unified Neon Dashboard: Real-time P&L% and condition breakdown  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_


---

## Gunbot v30.8.6
_Released: 2025-12-22T13:54:06+00:00_

#### Fixes
- fix huobi and many other exchanges with initial startup errors in core
- API slot management: fix hanging page triggered by tooltip hover #319
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Live price fix  _(by Ahpigsy)_

#### Improved
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Improved candle handling  _(by Ahpigsy)_

#### Added
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Trailing Minimum Sell Level (introduced in 1.84)  _(by Ahpigsy)_
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - MSL now follows new highs upward – lets strong pumps run longer instead of selling on the first red candle.  _(by Ahpigsy)_
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Added internal logging for cases where Safety Exit is not needed (e.g., price above Expected Low), without cluttering the panel.  _(by Ahpigsy)_

#### Changed
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Improvements to Moon Mode and bag values updating.  _(by Ahpigsy)_
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Smart cache refresh  _(by Ahpigsy)_
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Improvements to Expected Move % and Profit Target values.  _(by Ahpigsy)_
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Intra-candle Moon exit  _(by Ahpigsy)_
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Independent Safety Exit (pseudo stop-loss)  _(by Ahpigsy)_
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Refined Safety Exit messaging  _(by Ahpigsy)_
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Updated messaging for Safety Exit to be more concise (e.g., removed ROE value from the blocked message for cleaner panel display).  _(by Ahpigsy)_
- *Candle Analysis Tournament Edition – Change Log 1.84.  💪* - Overall stability  _(by Ahpigsy)_

#### GUI
- I'm also building the GUI (Gunbot User Interface) based on Gunbot v30.8.6


---

## Gunbot v30.8.4
_Released: 2025-12-10T11:55:49+00:00_

#### Fixes
- *Quanta G-Type v1.3* - v1.3 is a significant update to strategy code. Whilst all efforts are made and long term tested, it cannot be guaranteed bug free. Please test in a sim environment and ensure proper backing up of state files before updating your long term production instances.  _(by Dave)_
- Dashboard: fix sorting issue in recent trades table

#### Improved
- *Quanta G-Type v1.3* - New ANALYSIS output in sidebar gives percentile performance and suggested interval  _(by Dave)_
- gui server: serveral performance improvements

#### Added
- **Added Aditional temptlates and easier formating for easely deploying the no bag  one click strategies* - *added the BB trending scalps for BB buying and selling with Gtrends  _(by LUIS 🏴‍☠️ https://ai-markets.shop/en CRYPTO BOT, MINING & GOODS SUPPLIER)_

#### Changed
- *Quanta G-Type v1.3* - Period changes will only affect the candle analysis  _(by Dave)_

#### Strategy
- *Quanta G-Type v1.3* - There is no activation or action needed to activate MM mode - simply see intervals in the sidebar and decide if you want to use them  _(by Dave)_
- *Quanta G-Type v1.3* - QG data has its own state file and is no longer part of GB state  _(by Dave)_
- *Quanta G-Type v1.3* - Autosetup #1 support request is no clearing previous trade data - this is now automated in the setup process  _(by Dave)_
- *Quanta G-Type v1.3* - QG trims order history to ensure no slowdown over long periods of time  _(by Dave)_
- *Quanta G-Type v1.3* - Code base refactor (efficiency etc)  _(by Dave)_
- *Quanta G-Type v1.3* - Verbose ‘false’ produces a mini log output instead of full logging  _(by Dave)_
- *Quanta G-Type v1.3* - HODL mode now posts sell order  _(by Dave)_
- *Quanta G-Type v1.3* - If price exceeds bounds, orders will post when price once again inside bounds  _(by Dave)_


---

## Gunbot v30.8.3
_Released: 2025-12-07T11:29:28+00:00_

#### Fixes
- fix telegram enabled crashing win and lin users


---

## Gunbot v30.8.1
_Released: 2025-11-28T23:46:53+00:00_

#### Fixes
- bitget v3 spot market orders fix. Thanks @crazymop @jay_nxtstrat

#### Changed
- The Prize Pool updates automatically at YT Streaming as fans deposit out loved, beloved, eternal and unique love: BITCOIN


---

## Gunbot v30.7.9
_Released: 2025-11-27T22:00:58+00:00_

#### Fixes
- nightly build to fix hopefully the last urgent thing at refactored bitget exchange: by tomorrow you gotta use this build for your bitget. Thanks @UncreatedRolf @BoertjE77


---

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
