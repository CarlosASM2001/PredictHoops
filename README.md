# PredictHoops: NBA Live Win Probability Predictor

This project is a real-time NBA win probability prediction system. It uses historical and live play-by-play data to estimate each team’s chance of winning throughout a game.

The system processes game events into structured game states, trains a neural network model using PyTorch, serves predictions through a Flask API, and streams live updates to an interactive dashboard using WebSockets.

## Key Features

```
- Real-time NBA win probability prediction- Play-by-play data ingestion using nba_api- Game state feature engineering with pandas- PyTorch neural network model- Flask prediction API- WebSocket-powered live dashboard- Win probability chart over time- Possession, score, time, and foul-aware predictions
```

## Tech Stack

```
Python, pandas, NumPy, PyTorch, scikit-learn, Flask, Flask-SocketIO, React, Recharts, nba_api
```