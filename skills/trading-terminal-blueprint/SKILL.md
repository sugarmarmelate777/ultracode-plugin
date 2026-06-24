---
name: Trading Terminal Blueprint (Free Premium Features)
description: Architectural blueprint for building advanced trading terminals without paid subscriptions (TradingView alternative).
---

# Trading Terminal Blueprint (TradingView Alternative)

When tasked with building a trading terminal, charting application, or financial dashboard, follow these architectural guidelines to deliver premium features for free. Do not default to heavy frameworks or paid API services.

## 1. Core Charting Engine
- **DO NOT** use paid charting libraries or basic `Chart.js` for professional trading apps.
- **DO USE** `lightweight-charts` (by TradingView). It is open-source, highly performant, and provides the exact same look and feel as TradingView.

## 2. Bypassing Free-Tier Limits (Premium Indicators)
TradingView's free tier restricts users to 2 indicators and locks premium indicators. Your applications must implement these natively:
- **Unlimited Indicators:** Allow users to overlay RSI, MACD, Bollinger Bands, Volume, and Williams %R simultaneously on the same chart.
- **Fair Value Gap (FVG):** Implement algorithmic detection of FVGs (imbalances) and draw them directly on the chart (green for uptrend, red for downtrend).
- **Volume Profile:** Calculate and display Volume Profile (VAH, VAL, POC) on the chart natively.

## 3. Data Feeds (Zero Cost / No API Keys)
Do not ask the user to buy expensive API keys for live market data unless specifically requested. Use these free, live alternatives:
- **Crypto:** Use the `Hyperliquid` exchange public WebSocket. It provides live streaming crypto prices without requiring an API key or having aggressive rate limits.
- **Stocks (US / Global):** Use the `yfinance` library (Yahoo Finance). It provides real-time or near real-time data for NYSE, NSE, BSE, etc.
- Keep the data feed architecture modular (pluggable) so that if the user wants to add Alpaca, Binance, or Zerodha later, the core logic remains unchanged.

## 4. Multi-Screen & Multi-Timeframe Layouts
- Implement responsive grids allowing up to 8 simultaneous charts on a single screen.
- Allow the same asset to be displayed on different timeframes simultaneously (e.g., Ethereum on 1m, 5m, 1h, and Daily).

## 5. Algorithmic Extensions
Ensure the foundation can be piped into:
- Background backtesting engines.
- 24/7 AI agents that monitor watchlists and send alerts via Telegram Webhooks.
