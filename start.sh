echo "Cloning Repo...."
git clone https://github.com/LoopXS/Radio-Music-Bot.git /Radio-Music-Bot
cd /Radio-Music-Bot
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 main.py
