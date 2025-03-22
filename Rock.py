import streamlit as st
import random
from collections import Counter

# Function to get computer's choice based on difficulty level
def get_computer_choice(difficulty, user_choice_history=None):
    if difficulty == "Easy":
        # Easy mode: Random choice
        return random.choice(["Rock", "Paper", "Scissors"])
    elif difficulty == "Medium":
        # Medium mode: Slightly smarter, avoids repeating the same choice
        if user_choice_history and len(user_choice_history) >= 2:
            last_user_choice = user_choice_history[-1]
            return random.choice([c for c in ["Rock", "Paper", "Scissors"] if c != last_user_choice])
        else:
            return random.choice(["Rock", "Paper", "Scissors"])
    elif difficulty == "Hard":
        # Hard mode: Predicts user's next move based on history
        if user_choice_history and len(user_choice_history) >= 3:
            # Find the most frequent user choice and counter it
            most_common_choice = Counter(user_choice_history).most_common(1)[0][0]
            counter_choices = {"Rock": "Paper", "Paper": "Scissors", "Scissors": "Rock"}
            return counter_choices[most_common_choice]
        else:
            return random.choice(["Rock", "Paper", "Scissors"])
    else:
        # Default to random choice if no condition is met
        return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice, text):
    if user_choice == computer_choice:
        return text["tie"]
    elif (user_choice == text["rock"] and computer_choice == text["scissors"]) or \
         (user_choice == text["paper"] and computer_choice == text["rock"]) or \
         (user_choice == text["scissors"] and computer_choice == text["paper"]):
        return text["win"]
    else:
        return text["lose"]

def update_score(result, scores):
    if result == text["win"]:
        scores['User'] += 1
        st.session_state.win_flag = "win"
    elif result == text["lose"]:
        scores['Computer'] += 1
        st.session_state.win_flag = "lose"
    else:
        st.session_state.win_flag = "tie"

def reset_scores():
    return {'User': 0, 'Computer': 0}

# Gamification: Track achievements
def check_achievements(scores, text):
    if scores['User'] >= 5 and text["win_5_games"] not in st.session_state.achievements:
        st.session_state.achievements.append(text["win_5_games"])
    if scores['User'] >= 10 and text["win_10_games"] not in st.session_state.achievements:
        st.session_state.achievements.append(text["win_10_games"])
    if scores['User'] >= 3 and st.session_state.win_flag == "win" and text["win_3_in_a_row"] not in st.session_state.achievements:
        st.session_state.achievements.append(text["win_3_in_a_row"])

# Localization: Text in multiple languages
def get_localized_text(language):
    texts = {
        "English": {
            "title": "Rock-Paper-Scissors Game ✊✋✌️",
            "choose": "Choose one and play against the computer!",
            "difficulty": "Select Difficulty:",
            "game_mode": "Choose Game Mode:",
            "your_choice": "Your Choice:",
            "play": "Play!",
            "computer_chose": "Computer chose:",
            "result": "Result:",
            "scoreboard": "Live Scoreboard",
            "reset": "Reset Score",
            "reset_confirmation": "Scores reset!",
            "achievements": "Achievements 🏆",
            "language": "Select Language:",
            "you": "You",
            "computer": "Computer",
            "single_round": "Single Round",
            "best_of_3": "Best of 3",
            "best_of_5": "Best of 5",
            "sudden_death": "Sudden Death",
            "easy": "Easy",
            "medium": "Medium",
            "hard": "Hard",
            "rock": "Rock",
            "paper": "Paper",
            "scissors": "Scissors",
            "tie": "It's a tie! 🤝",
            "win": "You win! 🎉",
            "lose": "Computer wins! 🤖",
            # Localized achievements
            "win_5_games": "Win 5 Games",
            "win_10_games": "Win 10 Games",
            "win_3_in_a_row": "Win 3 in a Row",
        },
        "Arabic": {
            "title": "لعبة حجر-ورقة-مقص ✊✋✌️",
            "choose": "اختر واحدًا والعب ضد الكمبيوتر!",
            "difficulty": "اختر مستوى الصعوبة:",
            "game_mode": "اختر نمط اللعبة:",
            "your_choice": "اختيارك:",
            "play": "لعب!",
            "computer_chose": "الكمبيوتر اختار:",
            "result": "النتيجة:",
            "scoreboard": "لوحة النتائج المباشرة",
            "reset": "إعادة النقاط",
            "reset_confirmation": "تم إعادة النقاط!",
            "achievements": "الإنجازات 🏆",
            "language": "اختر اللغة:",
            "you": "أنت",
            "computer": "الكمبيوتر",
            "single_round": "جولة واحدة",
            "best_of_3": "أفضل من 3",
            "best_of_5": "أفضل من 5",
            "sudden_death": "الجولة الحاسمة",
            "easy": "سهل",
            "medium": "متوسط",
            "hard": "صعب",
            "rock": "حجر",
            "paper": "ورقة",
            "scissors": "مقص",
            "tie": "تعادل! 🤝",
            "win": "لقد فزت! 🎉",
            "lose": "الكمبيوتر فاز! 🤖",
            # Localized achievements
            "win_5_games": "الفوز بـ 5 ألعاب",
            "win_10_games": "الفوز بـ 10 ألعاب",
            "win_3_in_a_row": "الفوز بـ 3 مرات متتالية",
        },
        "French": {
            "title": "Jeu Pierre-Papier-Ciseaux ✊✋✌️",
            "choose": "Choisissez une option et jouez contre l'ordinateur!",
            "difficulty": "Sélectionnez la difficulté:",
            "game_mode": "Choisissez le mode de jeu:",
            "your_choice": "Votre choix:",
            "play": "Jouer!",
            "computer_chose": "L'ordinateur a choisi:",
            "result": "Résultat:",
            "scoreboard": "Tableau des scores en direct",
            "reset": "Réinitialiser les scores",
            "reset_confirmation": "Scores réinitialisés!",
            "achievements": "Récompenses 🏆",
            "language": "Sélectionnez la langue:",
            "you": "Vous",
            "computer": "Ordinateur",
            "single_round": "Une seule manche",
            "best_of_3": "Meilleur de 3",
            "best_of_5": "Meilleur de 5",
            "sudden_death": "Mort subite",
            "easy": "Facile",
            "medium": "Moyen",
            "hard": "Difficile",
            "rock": "Pierre",
            "paper": "Papier",
            "scissors": "Ciseaux",
            "tie": "C'est une égalité! 🤝",
            "win": "Vous avez gagné! 🎉",
            "lose": "L'ordinateur a gagné! 🤖",
            # Localized achievements
            "win_5_games": "Gagner 5 parties",
            "win_10_games": "Gagner 10 parties",
            "win_3_in_a_row": "Gagner 3 fois de suite",
        },
    }
    return texts[language]

# Streamlit UI
# Language Selection
if 'language' not in st.session_state:
    st.session_state.language = "English"

language = st.sidebar.selectbox("Select Language:", ["English", "Arabic", "French"], key="language_select")
st.session_state.language = language
text = get_localized_text(st.session_state.language)

# Initialize session state for achievements
if 'achievements' not in st.session_state:
    st.session_state.achievements = []

# Title
st.title(text["title"])
st.write(text["choose"])

# Difficulty Selection
difficulty = st.selectbox(text["difficulty"], [text["easy"], text["medium"], text["hard"]])

# Game Mode Selection
game_mode = st.selectbox(text["game_mode"], [text["single_round"], text["best_of_3"], text["best_of_5"], text["sudden_death"]])

if 'scores' not in st.session_state:
    st.session_state.scores = reset_scores()
if 'win_flag' not in st.session_state:
    st.session_state.win_flag = None
if 'user_choice_history' not in st.session_state:
    st.session_state.user_choice_history = []

# Your Choice Section (Translated)
user_choice = st.radio(text["your_choice"], [text["rock"], text["paper"], text["scissors"]])

if st.button(text["play"]):
    # Get computer's choice based on difficulty and user's history
    computer_choice = get_computer_choice(difficulty, st.session_state.user_choice_history)
    
    # Ensure computer_choice is not None
    if computer_choice is None:
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    
    # Translate computer's choice
    computer_choice_translated = {
        "Rock": text["rock"],
        "Paper": text["paper"],
        "Scissors": text["scissors"],
    }[computer_choice]
    
    # Determine the result
    result = determine_winner(user_choice, computer_choice_translated, text)
    update_score(result, st.session_state.scores)
    
    # Update user's choice history
    st.session_state.user_choice_history.append(user_choice)
    
    st.write(f"**{text['computer_chose']}** {computer_choice_translated}")
    st.write(f"**{text['result']}** {result}")
    
    # Check for achievements
    check_achievements(st.session_state.scores, text)
    
    # Display emojis based on the result
    if st.session_state.win_flag == "win":
        st.balloons()
    elif st.session_state.win_flag == "lose":
        sad_face_css = """
        <style>
        @keyframes fall {
            from {transform: translateY(-100px) rotate(0deg);}
            to {transform: translateY(100vh) rotate(360deg);}
        }
        .sad-face {
            position: fixed;
            font-size: 50px;
            opacity: 0.8;
            animation: fall 2s linear infinite;
        }
        </style>
        <div class="sad-face" style="top:5%; left:10%;">😢</div>
        <div class="sad-face" style="top:10%; left:30%;">😢</div>
        <div class="sad-face" style="top:20%; left:50%;">😢</div>
        <div class="sad-face" style="top:30%; left:70%;">😢</div>
        <div class="sad-face" style="top:40%; left:20%;">😢</div>
        <div class="sad-face" style="top:50%; left:80%;">😢</div>
        """
        st.markdown(sad_face_css, unsafe_allow_html=True)
    elif st.session_state.win_flag == "tie":
        handshake_css = """
        <style>
        @keyframes shake {
            0% {transform: translateY(0px);}
            50% {transform: translateY(-10px);}
            100% {transform: translateY(0px);}
        }
        .handshake {
            position: fixed;
            font-size: 50px;
            opacity: 0.8;
            animation: shake 1s ease-in-out infinite;
        }
        </style>
        <div class="handshake" style="top:5%; left:15%;">🤝</div>
        <div class="handshake" style="top:15%; left:35%;">🤝</div>
        <div class="handshake" style="top:25%; left:55%;">🤝</div>
        <div class="handshake" style="top:35%; left:75%;">🤝</div>
        <div class="handshake" style="top:45%; left:25%;">🤝</div>
        <div class="handshake" style="top:55%; left:85%;">🤝</div>
        """
        st.markdown(handshake_css, unsafe_allow_html=True)
    
    # Reset the win_flag after displaying the emojis
    st.session_state.win_flag = None
    
# Display live scoreboard
st.subheader(text["scoreboard"])
st.write(f"👤 {text['you']}: {st.session_state.scores['User']} | 🤖 {text['computer']}: {st.session_state.scores['Computer']}")
    
# Game Mode Logic
if game_mode in [text["best_of_3"], text["best_of_5"]]:
    required_wins = int(game_mode.split()[-1]) // 2 + 1
    if st.session_state.scores['User'] >= required_wins:
        st.success("🎉 You won the match! 🎉")
        st.session_state.scores = reset_scores()
        st.session_state.user_choice_history = []  # Reset history
    elif st.session_state.scores['Computer'] >= required_wins:
        st.warning("🤖 Computer won the match! Try again!")
        st.session_state.scores = reset_scores()
        st.session_state.user_choice_history = []  # Reset history
elif game_mode == text["sudden_death"] and (st.session_state.scores['User'] > 0 or st.session_state.scores['Computer'] > 0):
    winner = text["you"] if st.session_state.scores['User'] > 0 else text["computer"]
    st.error(f"🔥 {winner} won the match! Sudden Death over! 🔥")
    st.session_state.scores = reset_scores()
    st.session_state.user_choice_history = []  # Reset history
    
if st.button(text["reset"]):
    st.session_state.scores = reset_scores()
    st.session_state.win_flag = None
    st.session_state.user_choice_history = []  # Reset history
    st.write(text["reset_confirmation"])

# Display achievements in the sidebar as checkboxes
st.sidebar.subheader(text["achievements"])
for achievement_key in ["win_5_games", "win_10_games", "win_3_in_a_row"]:
    achievement_text = text[achievement_key]
    if achievement_text in st.session_state.achievements:
        st.sidebar.checkbox(achievement_text, value=True, disabled=True)
    else:
        st.sidebar.checkbox(achievement_text, value=False, disabled=True)
