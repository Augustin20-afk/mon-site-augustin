# sections/game_section.py

import streamlit as st
import json
from core.helpers import get_image_base64_resized
from config.settings import RUNNER_PHOTO_PATH as PHOTO_PATH

QUIZ_QUESTIONS = [
    {
        "question": "Quel marathon a couru Augustin ?",
        "answers": ["Paris", "Barcelone", "Londres"],
        "correct": "Barcelone"
    },
    {
        "question": "Quel marathon déguisé a couru Augustin ?",
        "answers": ["Chicago", "Berlin", "Médoc"],
        "correct": "Médoc"
    },
    {
        "question": "Quel outil Augustin a développé dans son temps libre ?",
        "answers": ["Une appli de recettes", "Un radar à news Forex", "Un jeu de cartes Pokémon"],
        "correct": "Un radar à news Forex"
    },
    {
        "question": "Quelle est la priorité absolue d'Augustin un vendredi soir ?",
        "answers": ["Réviser ses KPIs", "Appeler son banquier", "Prévoir le weekend"],
        "correct": "Prévoir le weekend"
    },
    {
        "question": "Au camping, Augustin est plutôt ?",
        "answers": ["Celui qui dort jusqu'à midi", "Celui qui oublie la tente", "Celui qui gère la logistique et le feu"],
        "correct": "Celui qui gère la logistique et le feu"
    },
    {
        "question": "Ce qui motive Augustin au quotidien ?",
        "answers": ["Finir à 17h pile", "Construire des projets concrets et créer de la valeur", "Éviter les réunions du lundi"],
        "correct": "Construire des projets concrets et créer de la valeur"
    },
    {
        "question": "Quel liquide boit Augustin à 13h30 pour rester concentré ?",
        "answers": ["Il boit rien et s'endort sur le bureau", "VODKA", "Café"],
        "correct": "Café"
    },
]


def render_game() -> None:
    """Affiche la section jeu."""

    st.markdown('<div class="game-wrapper">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-header">
            <span class="section-tag">Mini-jeu</span>
            <h2 class="section-title">Joue avant de me juger 🎮</h2>
            <p class="section-desc">
                Saute par-dessus les obstacles de ma vie — puis réponds à des questions sur moi.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    quiz_json = json.dumps(QUIZ_QUESTIONS)
    photo_b64 = get_image_base64_resized(PHOTO_PATH, size=120) or ""
    photo_data_url = f"data:image/jpeg;base64,{photo_b64}" if photo_b64 else ""
    game_html = f"""

    <div id="game-container">

        <!-- RUNNER -->
        <div id="runner-section">
            <div id="score-display">Score : <span id="score">0</span></div>
            <canvas id="gameCanvas" width="800" height="250"></canvas>
            <div id="game-message">Appuie sur ESPACE ou clique pour sauter !</div>
        </div>

        <!-- QUIZ -->
        <div id="quiz-section" style="display:none;">
            <div id="quiz-header">
                <h3 id="quiz-title">Tu connais Augustin ? 🤔</h3>
                <p id="quiz-subtitle">Score runner : <span id="final-runner-score">0</span> pts</p>
            </div>
            <div id="quiz-body">
                <div id="question-counter"></div>
                <div id="question-text"></div>
                <div id="answers-container"></div>
                <div id="quiz-feedback"></div>
            </div>
        </div>

        <!-- RÉSULTAT FINAL -->
        <div id="result-section" style="display:none;">
            <div id="result-body">
                <div id="result-emoji"></div>
                <h3 id="result-title"></h3>
                <p id="result-desc"></p>
                <div id="result-scores"></div>
                <button id="restart-btn" onclick="restartGame()">Rejouer 🔄</button>
            </div>
        </div>

    </div>

    <style>
        #game-container {{
            background: rgba(255,255,255,0.85);
            border: 1px solid #e2e8f0;
            border-radius: 20px;
            padding: 2rem;
            max-width: 860px;
            margin: 0 auto;
            box-shadow: 0 4px 24px rgba(0,0,0,0.07);
            font-family: 'Inter', sans-serif;
        }}
        #score-display {{
            text-align: right;
            font-size: 1rem;
            font-weight: 700;
            color: #3b82f6;
            margin-bottom: 0.5rem;
        }}
        #gameCanvas {{
            display: block;
            margin: 0 auto;
            border-radius: 12px;
            background: linear-gradient(180deg, #e0f2fe 0%, #f0f9ff 60%, #bfdbfe 100%);
            cursor: pointer;
            width: 100%;
            max-width: 800px;
        }}
        #game-message {{
            text-align: center;
            margin-top: 0.8rem;
            font-size: 0.9rem;
            color: #64748b;
        }}
        #quiz-section {{
            text-align: center;
            padding: 1rem;
        }}
        #quiz-title {{
            font-size: 1.5rem;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 0.3rem;
        }}
        #quiz-subtitle {{
            color: #64748b;
            font-size: 0.9rem;
            margin-bottom: 1.5rem;
        }}
        #question-counter {{
            font-size: 0.8rem;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 0.8rem;
        }}
        #question-text {{
            font-size: 1.15rem;
            font-weight: 600;
            color: #0f172a;
            margin-bottom: 1.2rem;
            min-height: 3rem;
        }}
        #answers-container {{
            display: flex;
            flex-direction: column;
            gap: 0.6rem;
            max-width: 500px;
            margin: 0 auto 1rem auto;
        }}
        .answer-btn {{
            padding: 0.75rem 1.2rem;
            border-radius: 10px;
            border: 2px solid #e2e8f0;
            background: #f8fafc;
            color: #0f172a;
            font-size: 0.95rem;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.15s ease;
            text-align: left;
        }}
        .answer-btn:hover {{ background: #eff6ff; border-color: #3b82f6; }}
        .answer-btn.correct {{ background: #dcfce7; border-color: #22c55e; color: #15803d; }}
        .answer-btn.wrong {{ background: #fee2e2; border-color: #ef4444; color: #b91c1c; }}
        #quiz-feedback {{
            font-size: 1rem;
            font-weight: 600;
            min-height: 1.5rem;
            margin-top: 0.5rem;
        }}
        #result-section {{
            text-align: center;
            padding: 2rem 1rem;
        }}
        #result-emoji {{ font-size: 3.5rem; margin-bottom: 1rem; }}
        #result-title {{ font-size: 1.6rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; }}
        #result-desc {{ font-size: 0.95rem; color: #64748b; margin-bottom: 1.5rem; }}
        #result-scores {{
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }}
        .score-block {{
            background: #f1f5f9;
            border-radius: 12px;
            padding: 0.8rem 1.5rem;
            text-align: center;
        }}
        .score-block .score-val {{
            font-size: 1.8rem;
            font-weight: 700;
            color: #3b82f6;
        }}
        .score-block .score-lbl {{
            font-size: 0.78rem;
            color: #94a3b8;
            text-transform: uppercase;
            letter-spacing: 0.06em;
        }}
        #restart-btn {{
            background: #3b82f6;
            color: white;
            border: none;
            padding: 0.7rem 2rem;
            border-radius: 10px;
            font-size: 0.95rem;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }}
        #restart-btn:hover {{ background: #2563eb; }}
    </style>

    <script>
        const QUIZ = {quiz_json};

        // Image joueur
        const playerImg = new Image();
        playerImg.src = '{photo_data_url}';
        let imgLoaded = false;
        playerImg.onload = () => {{ imgLoaded = true; }};

        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        let gameState = 'waiting';
        let score = 0;
        let frameCount = 0;
        let speed = 5;
        let animId;

       const player = {{
    x: 80, y: 185, w: 55, h: 65,
    vy: 0, jumping: false,
    groundY: 185
}};

        const OBSTACLES = [
            {{ emoji: '📦', label: 'Packaging' }},
            {{ emoji: '📉', label: 'Crash Forex' }},
            {{ emoji: '📊', label: 'Dashboard' }},
            {{ emoji: '🏕️', label: 'Camping' }},
            {{ emoji: '✈️', label: 'Voyage' }},
            {{ emoji: '👨‍👩‍👧‍👦', label: 'Famille' }},
            {{ emoji: '🌍', label: 'Commerce' }},
            {{ emoji: '☀️', label: 'Good vibes' }},
            {{ emoji: '🚀', label: 'Ambition' }},
            {{ emoji: '☁️', label: 'Nuage' }},
            {{ emoji: '🔍', label: 'Curiosité' }},
        ];

        let obstacles = [];
        let nextObstacle = 80;

        function jump() {{
            if (gameState === 'waiting') {{ startGame(); return; }}
            if (gameState === 'running' && !player.jumping) {{
                player.vy = -15;
                player.jumping = true;
            }}
        }}

        document.addEventListener('keydown', e => {{ if (e.code === 'Space') {{ e.preventDefault(); jump(); }} }});
        canvas.addEventListener('click', jump);
        canvas.addEventListener('touchstart', e => {{ e.preventDefault(); jump(); }});

        function startGame() {{
            gameState = 'running';
            score = 0;
            frameCount = 0;
            speed = 5;
            obstacles = [];
            nextObstacle = 80;
            player.y = player.groundY;
            player.vy = 0;
            player.jumping = false;
            document.getElementById('game-message').textContent = 'ESPACE ou clic pour sauter !';
            document.getElementById('score').textContent = '0';
            gameLoop();
        }}

        function gameLoop() {{
            if (gameState !== 'running') return;
            animId = requestAnimationFrame(gameLoop);
            update();
            draw();
        }}

        function update() {{
            frameCount++;
            score = Math.floor(frameCount / 6);
            document.getElementById('score').textContent = score;

            if (frameCount % 300 === 0) speed += 0.5;

            player.vy += 0.9;
            player.y += player.vy;
            if (player.y >= player.groundY) {{
                player.y = player.groundY;
                player.vy = 0;
                player.jumping = false;
            }}

            nextObstacle--;
            if (nextObstacle <= 0) {{
                const obs = OBSTACLES[Math.floor(Math.random() * OBSTACLES.length)];
                obstacles.push({{ x: 820, y: 193, w: 50, h: 60, emoji: obs.emoji }});
                nextObstacle = 60 + Math.floor(Math.random() * 60);
            }}

            obstacles.forEach(o => o.x -= speed);
            obstacles = obstacles.filter(o => o.x > -60);

            for (let o of obstacles) {{
                if (
                    player.x + 8 < o.x + o.w - 8 &&
                    player.x + player.w - 8 > o.x + 8 &&
                    player.y + 8 < o.y + o.h &&
                    player.y + player.h > o.y + 8
                ) {{
                    gameState = 'gameover';
                    cancelAnimationFrame(animId);
                    draw();
                    setTimeout(() => showQuiz(), 800);
                    return;
                }}
            }}
        }}

        function draw() {{
            ctx.clearRect(0, 0, canvas.width, canvas.height);

            // Sol
            ctx.fillStyle = '#93c5fd';
            ctx.fillRect(0, 245, canvas.width, 5);

            // Nuages
            ctx.fillStyle = 'rgba(255,255,255,0.6)';
            ctx.beginPath();
            ctx.arc(100 - (frameCount * 0.3 % 900), 30, 20, 0, Math.PI * 2);
            ctx.arc(120 - (frameCount * 0.3 % 900), 25, 25, 0, Math.PI * 2);
            ctx.arc(140 - (frameCount * 0.3 % 900), 30, 18, 0, Math.PI * 2);
            ctx.fill();
            ctx.beginPath();
            ctx.arc(500 - (frameCount * 0.2 % 900), 50, 15, 0, Math.PI * 2);
            ctx.arc(518 - (frameCount * 0.2 % 900), 45, 20, 0, Math.PI * 2);
            ctx.arc(534 - (frameCount * 0.2 % 900), 50, 14, 0, Math.PI * 2);
            ctx.fill();

            // Joueur — photo en cercle
            const cx = player.x + player.w / 2;
            const cy = player.y + player.h / 2;
            const r = 24;

            if (imgLoaded) {{
                ctx.save();
                ctx.beginPath();
                ctx.arc(cx, cy, r, 0, Math.PI * 2);
                ctx.closePath();
                ctx.clip();
                if (gameState === 'gameover') ctx.globalAlpha = 0.5;
                ctx.drawImage(playerImg, cx - r, cy - r, r * 2, r * 2);
                ctx.restore();

                // Contour
                ctx.beginPath();
                ctx.arc(cx, cy, r, 0, Math.PI * 2);
                ctx.strokeStyle = gameState === 'gameover' ? '#ef4444' : '#ffffff';
                ctx.lineWidth = 3;
                ctx.stroke();

                // Emoji game over
                if (gameState === 'gameover') {{
                    ctx.font = '20px serif';
                    ctx.fillText('😵', cx - 10, cy - r - 5);
                }}
            }} else {{
                ctx.font = '42px serif';
                ctx.fillText(gameState === 'gameover' ? '😵' : '🏃', player.x - 5, player.y + player.h - 5);
            }}

            // Obstacles
            obstacles.forEach(o => {{
                ctx.font = '36px serif';
                ctx.fillText(o.emoji, o.x, o.y + o.h - 5);
            }});

            // Game over overlay
            if (gameState === 'gameover') {{
                ctx.fillStyle = 'rgba(15,23,42,0.45)';
                ctx.fillRect(0, 0, canvas.width, canvas.height);
                ctx.fillStyle = '#ffffff';
                ctx.font = 'bold 28px Inter, sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('Game Over !', canvas.width / 2, 90);
                ctx.font = '18px Inter, sans-serif';
                ctx.fillText('Score : ' + score, canvas.width / 2, 125);
                ctx.textAlign = 'left';
            }}
        }}

        // --- QUIZ ---
        let quizIndex = 0;
        let quizScore = 0;
        let runnerScore = 0;
        let answered = false;

        function showQuiz() {{
            runnerScore = score;
            quizIndex = 0;
            quizScore = 0;
            document.getElementById('runner-section').style.display = 'none';
            document.getElementById('quiz-section').style.display = 'block';
            document.getElementById('final-runner-score').textContent = runnerScore;
            showQuestion();
        }}

        function showQuestion() {{
            answered = false;
            const q = QUIZ[quizIndex];
            document.getElementById('question-counter').textContent =
                'Question ' + (quizIndex + 1) + ' / ' + QUIZ.length;
            document.getElementById('question-text').textContent = q.question;
            document.getElementById('quiz-feedback').textContent = '';

            const container = document.getElementById('answers-container');
            container.innerHTML = '';
            q.answers.forEach(a => {{
                const btn = document.createElement('button');
                btn.className = 'answer-btn';
                btn.textContent = a;
                btn.onclick = () => selectAnswer(a, q.correct);
                container.appendChild(btn);
            }});
        }}

        function selectAnswer(selected, correct) {{
            if (answered) return;
            answered = true;

            const btns = document.querySelectorAll('.answer-btn');
            btns.forEach(btn => {{
                btn.disabled = true;
                if (btn.textContent === correct) btn.classList.add('correct');
                else if (btn.textContent === selected) btn.classList.add('wrong');
            }});

            const feedback = document.getElementById('quiz-feedback');
            if (selected === correct) {{
                quizScore++;
                feedback.textContent = '✅ Bonne réponse !';
                feedback.style.color = '#16a34a';
            }} else {{
                feedback.textContent = '❌ Raté — bonne réponse : ' + correct;
                feedback.style.color = '#dc2626';
            }}

            setTimeout(() => {{
                quizIndex++;
                if (quizIndex < QUIZ.length) {{
                    showQuestion();
                }} else {{
                    showResult();
                }}
            }}, 1200);
        }}

        function showResult() {{
            document.getElementById('quiz-section').style.display = 'none';
            document.getElementById('result-section').style.display = 'block';

            const total = QUIZ.length;
            const pct = Math.round((quizScore / total) * 100);

            let emoji, title, desc;
            if (pct >= 80) {{
                emoji = '🏆'; title = 'Tu me connais bien !';
                desc = "Impressionnant — t'aurais peut-être dû postuler à ma place.";
            }} else if (pct >= 50) {{
                emoji = '👍'; title = 'Pas mal du tout !';
                desc = "Tu as saisi l'essentiel. Le reste, on en parle autour d'un café ☕";
            }} else {{
                emoji = '😄'; title = 'On se connaît pas encore !';
                desc = "Mais c'est exactement pour ça que ce site existe.";
            }}

            document.getElementById('result-emoji').textContent = emoji;
            document.getElementById('result-title').textContent = title;
            document.getElementById('result-desc').textContent = desc;
            document.getElementById('result-scores').innerHTML = `
                <div class="score-block">
                    <div class="score-val">${{runnerScore}}</div>
                    <div class="score-lbl">Score Runner</div>
                </div>
                <div class="score-block">
                    <div class="score-val">${{quizScore}}/${{total}}</div>
                    <div class="score-lbl">Score Quiz</div>
                </div>
            `;
        }}

        function restartGame() {{
            document.getElementById('result-section').style.display = 'none';
            document.getElementById('quiz-section').style.display = 'none';
            document.getElementById('runner-section').style.display = 'block';
            document.getElementById('game-message').textContent = 'Appuie sur ESPACE ou clique pour sauter !';
            gameState = 'waiting';
            score = 0;
            document.getElementById('score').textContent = '0';
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            draw();
        }}

        draw();
    </script>
    """

    st.components.v1.html(game_html, height=580, scrolling=False)
    st.markdown('</div>', unsafe_allow_html=True)

def render_runner() -> None:
    """Affiche uniquement le runner sans le quiz."""

    st.markdown('<div class="game-wrapper">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-header">
            <span class="section-tag">Runner</span>
            <h2 class="section-title">Un dernier obstacle avant de partir 🏃</h2>
            <p class="section-desc">
                Saute par-dessus les défis de mon parcours — si tu oses.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    photo_b64 = get_image_base64_resized(PHOTO_PATH, size=120) or ""
    photo_data_url = f"data:image/jpeg;base64,{photo_b64}" if photo_b64 else ""

    runner_html = f"""
    <div id="runner-container" style="
        background: rgba(255,255,255,0.85);
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 2rem;
        max-width: 860px;
        margin: 0 auto;
        box-shadow: 0 4px 24px rgba(0,0,0,0.07);
        font-family: 'Inter', sans-serif;
    ">
        <div id="score-display" style="text-align:right;font-size:1rem;font-weight:700;color:#3b82f6;margin-bottom:0.5rem;">
            Score : <span id="score">0</span>
        </div>
        <canvas id="gameCanvas" width="800" height="250" style="
            display:block;margin:0 auto;border-radius:12px;
            background:linear-gradient(180deg,#e0f2fe 0%,#f0f9ff 60%,#bfdbfe 100%);
            cursor:pointer;width:100%;max-width:800px;
        "></canvas>
        <div id="game-message" style="text-align:center;margin-top:0.8rem;font-size:0.9rem;color:#64748b;">
            Appuie sur ESPACE ou clique pour sauter !
        </div>
    </div>

    <script>
        const canvas2 = document.getElementById('gameCanvas');
        const ctx2 = canvas2.getContext('2d');

        const playerImg2 = new Image();
        playerImg2.src = '{photo_data_url}';
        let imgLoaded2 = false;
        playerImg2.onload = () => {{ imgLoaded2 = true; }};

        let gameState2 = 'waiting';
        let score2 = 0;
        let frameCount2 = 0;
        let speed2 = 5;
        let animId2;

        const player2 = {{
            x: 80, y: 185, w: 55, h: 65,
            vy: 0, jumping: false,
            groundY: 185
        }};

        const OBSTACLES2 = [
            {{ emoji: '📦' }}, {{ emoji: '📉' }}, {{ emoji: '📊' }},
            {{ emoji: '🏕️' }}, {{ emoji: '✈️' }}, {{ emoji: '👨‍👩‍👧‍👦' }},
            {{ emoji: '🌍' }}, {{ emoji: '☀️' }}, {{ emoji: '🚀' }},
            {{ emoji: '☁️' }}, {{ emoji: '🔍' }},
        ];

        let obstacles2 = [];
        let nextObstacle2 = 80;

        function jump2() {{
            if (gameState2 === 'waiting') {{ startGame2(); return; }}
            if (gameState2 === 'running' && !player2.jumping) {{
                player2.vy = -15;
                player2.jumping = true;
            }}
        }}

        document.addEventListener('keydown', e => {{
            if (e.code === 'Space') {{ e.preventDefault(); jump2(); }}
        }});
        canvas2.addEventListener('click', jump2);
        canvas2.addEventListener('touchstart', e => {{ e.preventDefault(); jump2(); }});

        function startGame2() {{
            gameState2 = 'running';
            score2 = 0; frameCount2 = 0; speed2 = 5;
            obstacles2 = []; nextObstacle2 = 80;
            player2.y = player2.groundY;
            player2.vy = 0; player2.jumping = false;
            document.getElementById('game-message').textContent = 'ESPACE ou clic pour sauter !';
            document.getElementById('score').textContent = '0';
            gameLoop2();
        }}

        function gameLoop2() {{
            if (gameState2 !== 'running') return;
            animId2 = requestAnimationFrame(gameLoop2);
            update2(); draw2();
        }}

        function update2() {{
            frameCount2++;
            score2 = Math.floor(frameCount2 / 6);
            document.getElementById('score').textContent = score2;
            if (frameCount2 % 300 === 0) speed2 += 0.5;

            player2.vy += 0.9;
            player2.y += player2.vy;
            if (player2.y >= player2.groundY) {{
                player2.y = player2.groundY;
                player2.vy = 0; player2.jumping = false;
            }}

            nextObstacle2--;
            if (nextObstacle2 <= 0) {{
                const obs = OBSTACLES2[Math.floor(Math.random() * OBSTACLES2.length)];
                obstacles2.push({{ x: 820, y: 193, w: 50, h: 60, emoji: obs.emoji }});
                nextObstacle2 = 60 + Math.floor(Math.random() * 60);
            }}

            obstacles2.forEach(o => o.x -= speed2);
            obstacles2 = obstacles2.filter(o => o.x > -60);

            for (let o of obstacles2) {{
                if (
                    player2.x + 8 < o.x + o.w - 8 &&
                    player2.x + player2.w - 8 > o.x + 8 &&
                    player2.y + 8 < o.y + o.h &&
                    player2.y + player2.h > o.y + 8
                ) {{
                    gameState2 = 'gameover';
                    cancelAnimationFrame(animId2);
                    draw2();
                    document.getElementById('game-message').textContent =
                        'Game Over ! Score : ' + score2 + ' — Clique pour rejouer';
                    canvas2.onclick = () => {{ startGame2(); canvas2.onclick = jump2; }};
                    return;
                }}
            }}
        }}

        function draw2() {{
            ctx2.clearRect(0, 0, canvas2.width, canvas2.height);

            ctx2.fillStyle = '#93c5fd';
            ctx2.fillRect(0, 245, canvas2.width, 5);

            ctx2.fillStyle = 'rgba(255,255,255,0.6)';
            ctx2.beginPath();
            ctx2.arc(100 - (frameCount2 * 0.3 % 900), 30, 20, 0, Math.PI * 2);
            ctx2.arc(120 - (frameCount2 * 0.3 % 900), 25, 25, 0, Math.PI * 2);
            ctx2.arc(140 - (frameCount2 * 0.3 % 900), 30, 18, 0, Math.PI * 2);
            ctx2.fill();

            const cx = player2.x + player2.w / 2;
            const cy = player2.y + player2.h / 2;
            const r = 32;

            if (imgLoaded2) {{
                ctx2.save();
                ctx2.beginPath();
                ctx2.arc(cx, cy, r, 0, Math.PI * 2);
                ctx2.closePath();
                ctx2.clip();
                if (gameState2 === 'gameover') ctx2.globalAlpha = 0.5;
                ctx2.drawImage(playerImg2, cx - r, cy - r, r * 2, r * 2);
                ctx2.restore();
                ctx2.beginPath();
                ctx2.arc(cx, cy, r, 0, Math.PI * 2);
                ctx2.strokeStyle = gameState2 === 'gameover' ? '#ef4444' : '#ffffff';
                ctx2.lineWidth = 3;
                ctx2.stroke();
                if (gameState2 === 'gameover') {{
                    ctx2.font = '20px serif';
                    ctx2.fillText('😵', cx - 10, cy - r - 5);
                }}
            }} else {{
                ctx2.font = '42px serif';
                ctx2.fillText(gameState2 === 'gameover' ? '😵' : '🏃', player2.x - 5, player2.y + player2.h - 5);
            }}

            obstacles2.forEach(o => {{
                ctx2.font = '36px serif';
                ctx2.fillText(o.emoji, o.x, o.y + o.h - 5);
            }});

            if (gameState2 === 'gameover') {{
                ctx2.fillStyle = 'rgba(15,23,42,0.45)';
                ctx2.fillRect(0, 0, canvas2.width, canvas2.height);
                ctx2.fillStyle = '#ffffff';
                ctx2.font = 'bold 28px Inter, sans-serif';
                ctx2.textAlign = 'center';
                ctx2.fillText('Game Over !', canvas2.width / 2, 90);
                ctx2.font = '18px Inter, sans-serif';
                ctx2.fillText('Score : ' + score2, canvas2.width / 2, 125);
                ctx2.textAlign = 'left';
            }}
        }}

        draw2();
    </script>
    """

    st.components.v1.html(runner_html, height=420, scrolling=False)
    st.markdown('</div>', unsafe_allow_html=True)    
