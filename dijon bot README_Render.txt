
GainzAlgo Premium Bot on Render
===============================

1. Create a free GitHub repo (e.g., gainzalgo-telegram-bot)
2. Upload these files:
   - main.py
   - users.json
   - requirements.txt

3. Go to https://render.com > New > Web Service
   - Environment: Python 3
   - Build Command: pip install -r requirements.txt
   - Start Command: python main.py
   - Instance Type: Free

4. Connect it to your GitHub repo and click "Deploy"

5. Done! Your Telegram bot is now running on Render 24/7

⚠️ Don't forget to:
- Replace 'your_admin_username' in `main.py` with your actual Telegram @username
