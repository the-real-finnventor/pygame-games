# Quickstart
## Installation
```
pip3 install pygame
pip3 install pgzero
git clone git@github.com:the-real-finnventor/pygame-games.git
cd pygame-games
```

## Run coin collector
```
pgzrun coin.py
```

## Run shoot the fruit
```
pgzrun shoot.py
```

## Run red alert
```
pgzrun red.py
```

# Extras
## Run coin collector at any time with just `coin`
```
echo alias coin-path="$PWD"/coin.py >> ~/.zprofile
echo alias coin=pgzrun coin-path >> ~/.zprofile
```

## Run shoot the fruit at any time with just `shoot`
```
echo alias shoot-path="$PWD"/shoot.py >> ~/.zprofile
echo alias shoot=pgzrun shoot-path >> ~/.zprofile
```

## Run red alert at any time with just `red`
```
echo alias red-path="$PWD"/red.py >> ~/.zprofile
echo alias red=pgzrun red-path >> ~/.zprofile
```
