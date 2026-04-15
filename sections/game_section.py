# sections/game_section.py

import streamlit as st
import json
from core.helpers import get_image_base64_resized
from config.settings import PHOTO_PATH, RUNNER_PHOTO_PATH


QUIZ_QUESTIONS = [
    {
        "question": "Qu'est-ce qui motive le plus Augustin dans ce qu'il entreprend ?",
        "answers": [
            "Finir avant tout le monde",
            "Construire des choses concrètes et créer de la valeur",
            "Éviter les réunions du lundi"
        ],
        "correct": "Construire des choses concrètes et créer de la valeur",
        "context": "Augustin est animé par l'envie de construire des choses utiles et durables. C'est cette logique qui guide autant ses projets perso que son engagement professionnel."
    },
    {
        "question": "Quel environnement lui correspond le mieux pour progresser ?",
        "answers": [
            "Un environnement calme sans contraintes",
            "Un environnement exigeant, structuré et formateur",
            "Un environnement où personne ne vérifie rien"
        ],
        "correct": "Un environnement exigeant, structuré et formateur",
        "context": "Chez Coloplast, Augustin évolue dans un cadre exigeant qui lui apprend à structurer, coordonner et faire avancer des sujets avec sérieux."
    },
    {
        "question": "En dehors du travail, comment Augustin recharge-t-il son énergie ?",
        "answers": [
            "Netflix et silence total",
            "Sport, nature, amis et projets perso",
            "Il prépare ses slides pour le lundi"
        ],
        "correct": "Sport, nature, amis et projets perso",
        "context": "Le sport, la nature et les moments simples font partie de son équilibre. Des valeurs qu'il retrouve aussi dans son rapport au travail : régularité, effort et engagement."
    },
    {
        "question": "Quelle place le camping a-t-il dans son univers ?",
        "answers": [
            "Une activité qu'il évite soigneusement",
            "Un business familial qui l'a construit dès l'enfance",
            "Un endroit où il va juste pour ne rien faire"
        ],
        "correct": "Un business familial qui l'a construit dès l'enfance",
        "context": "Grandir dans un camping familial lui a transmis une culture du terrain, du service et du concret. C'est là qu'une partie essentielle de sa manière de travailler s'est construite."
    },
    {
        "question": "Quelle habitude l'aide à rester concentré et engagé ?",
        "answers": [
            "Il boit rien et s'endort sur le bureau",
            "Une routine claire, du sport et un bon café",
            "Il écoute du heavy metal à fond"
        ],
        "correct": "Une routine claire, du sport et un bon café",
        "context": "La régularité et la discipline font partie de son fonctionnement. Une bonne routine, c'est ce qui lui permet de rester efficace et impliqué sur la durée."
    },
    {
        "question": "Dans quel type de défi Augustin aime-t-il se lancer ?",
        "answers": [
            "Le marathon du Médoc — déguisé en cuisinier",
            "Un tournoi de pétanque régional",
            "Un concours de karaoké d'entreprise"
        ],
        "correct": "Le marathon du Médoc — déguisé en cuisinier",
        "context": "Le Marathon du Médoc est une course de 42km dans les vignes du Bordelais, où les participants courent déguisés. Une expérience mémorable qui résume bien son rapport au défi : sérieux dans l'effort, fun dans l'approche."
    },
    {
        "question": "Quel outil Augustin a développé dans son temps libre ?",
        "answers": [
            "Une appli de recettes de cuisine",
            "Un radar à news Forex sous Streamlit",
            "Un jeu de cartes Pokémon en Python"
        ],
        "correct": "Un radar à news Forex sous Streamlit",
        "context": "Passionné par les marchés financiers, Augustin a développé un outil de veille Forex pour filtrer et prioriser l'information utile. Un projet perso qui montre sa curiosité et sa capacité à construire des outils concrets."
    },
]


def render_game() -> None:
    """Affiche uniquement le quiz."""

    st.markdown('<div class="game-wrapper">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-header">
            <span class="section-tag">Quiz</span>
            <h2 class="section-title">Un format rapide pour découvrir mon univers 🎯</h2>
            <p class="section-desc">
                Quelques questions pour découvrir ma manière de fonctionner et ce qui me motive.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    quiz_json = json.dumps(QUIZ_QUESTIONS)

    quiz_html = f"""
    <div id="game-container">
        <div id="quiz-section">
            <div id="quiz-header">
                <h3 id="quiz-title">Connais-tu Augustin ? 🤔</h3>
            </div>
            <div id="quiz-body">
                <div id="question-counter"></div>
                <div id="question-text"></div>
                <div id="answers-container"></div>
                <div id="quiz-feedback"></div>
                <div id="quiz-context" style="display:none;"></div>
                <button id="next-btn" onclick="nextQuestion()"
                    style="display:none;margin:1rem auto 0 auto;
                           background:#2563eb;color:white;border:none;
                           padding:0.65rem 1.8rem;border-radius:8px;
                           font-size:0.9rem;font-weight:600;cursor:pointer;">
                    Question suivante →
                </button>
            </div>
        </div>
        <div id="result-section" style="display:none;">
            <div id="result-body">
                <div id="result-emoji"></div>
                <h3 id="result-title"></h3>
                <p id="result-desc"></p>
                <div id="result-scores"></div>
                <button id="restart-btn" onclick="restartQuiz()">Rejouer 🔄</button>
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
        #quiz-section {{ text-align: center; padding: 1rem; }}
        #quiz-title {{ font-size: 1.5rem; font-weight: 700; color: #0f172a; margin-bottom: 1.5rem; }}
        #question-counter {{
            font-size: 0.8rem; color: #94a3b8;
            text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.8rem;
        }}
        #question-text {{
            font-size: 1.15rem; font-weight: 600; color: #0f172a;
            margin-bottom: 1.2rem; min-height: 3rem;
        }}
        #answers-container {{
            display: flex; flex-direction: column; gap: 0.6rem;
            max-width: 500px; margin: 0 auto 1rem auto;
        }}
        .answer-btn {{
            padding: 0.75rem 1.2rem; border-radius: 10px;
            border: 2px solid #e2e8f0; background: #f8fafc;
            color: #0f172a; font-size: 0.95rem; font-weight: 500;
            cursor: pointer; transition: all 0.15s ease; text-align: center;
        }}
        .answer-btn:hover {{ background: #eff6ff; border-color: #3b82f6; }}
        .answer-btn.correct {{ background: #dcfce7; border-color: #22c55e; color: #15803d; }}
        .answer-btn.wrong {{ background: #fee2e2; border-color: #ef4444; color: #b91c1c; }}
        #quiz-feedback {{ font-size: 1rem; font-weight: 600; min-height: 1.5rem; margin-top: 0.5rem; }}
        #quiz-context {{
            font-size: 0.88rem; color: #475569; line-height: 1.6;
            background: #f8fafc; border-left: 3px solid #2563eb;
            border-radius: 0 8px 8px 0; padding: 0.8rem 1rem;
            margin: 0.8rem auto 0 auto; max-width: 500px; text-align: left;
        }}
        #result-section {{ text-align: center; padding: 2rem 1rem; }}
        #result-emoji {{ font-size: 3.5rem; margin-bottom: 1rem; }}
        #result-title {{ font-size: 1.6rem; font-weight: 700; color: #0f172a; margin-bottom: 0.5rem; }}
        #result-desc {{ font-size: 0.95rem; color: #64748b; margin-bottom: 1.5rem; }}
        #result-scores {{
            display: flex; justify-content: center; gap: 2rem;
            margin-bottom: 1.5rem; flex-wrap: wrap;
        }}
        .score-block {{
            background: #f1f5f9; border-radius: 12px;
            padding: 0.8rem 1.5rem; text-align: center;
        }}
        .score-block .score-val {{ font-size: 1.8rem; font-weight: 700; color: #3b82f6; }}
        .score-block .score-lbl {{
            font-size: 0.78rem; color: #94a3b8;
            text-transform: uppercase; letter-spacing: 0.06em;
        }}
        #restart-btn {{
            background: #3b82f6; color: white; border: none;
            padding: 0.7rem 2rem; border-radius: 10px;
            font-size: 0.95rem; font-weight: 600; cursor: pointer;
        }}
        #restart-btn:hover {{ background: #2563eb; }}
    </style>

    <script>
        const QUIZ = {quiz_json};
        let quizIndex = 0;
        let quizScore = 0;
        let answered = false;

        function showQuestion() {{
            answered = false;
            const q = QUIZ[quizIndex];
            document.getElementById('question-counter').textContent =
                'Question ' + (quizIndex + 1) + ' / ' + QUIZ.length;
            document.getElementById('question-text').textContent = q.question;
            document.getElementById('quiz-feedback').textContent = '';
            document.getElementById('quiz-context').style.display = 'none';
            document.getElementById('quiz-context').textContent = '';
            document.getElementById('next-btn').style.display = 'none';

            const container = document.getElementById('answers-container');
            container.innerHTML = '';
            q.answers.forEach(a => {{
                const btn = document.createElement('button');
                btn.className = 'answer-btn';
                btn.textContent = a;
                btn.onclick = () => selectAnswer(a, q.correct, q.context);
                container.appendChild(btn);
            }});
        }}

        function selectAnswer(selected, correct, context) {{
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

            const contextEl = document.getElementById('quiz-context');
            contextEl.textContent = context;
            contextEl.style.display = 'block';
            document.getElementById('next-btn').style.display = 'block';
        }}

        function nextQuestion() {{
            quizIndex++;
            if (quizIndex < QUIZ.length) {{
                showQuestion();
            }} else {{
                showResult();
            }}
        }}

        function showResult() {{
            document.getElementById('quiz-section').style.display = 'none';
            document.getElementById('result-section').style.display = 'block';

            const total = QUIZ.length;
            const pct = Math.round((quizScore / total) * 100);

            let emoji, title, desc;
            if (pct >= 80) {{
                emoji = '🏆'; title = 'Tu me connais bien !';
                desc = "Impressionnant — tu aurais peut-être dû postuler à ma place.";
            }} else if (pct >= 50) {{
                emoji = '👍'; title = 'Pas mal du tout !';
                desc = "Tu as saisi l'essentiel. Le reste, on en parle autour d'un café ☕";
            }} else if (pct > 0) {{
                emoji = '😄'; title = 'On apprend à se connaître !';
                desc = "C'est exactement pour ça que ce site existe.";
            }} else {{
                emoji = '🤝'; title = 'Nous ne nous connaissons pas encore.';
                desc = "C'est précisément pour cela que ce site existe. Prenez le temps de le découvrir.";
            }}

            document.getElementById('result-emoji').textContent = emoji;
            document.getElementById('result-title').textContent = title;
            document.getElementById('result-desc').textContent = desc;
            document.getElementById('result-scores').innerHTML = `
                <div class="score-block">
                    <div class="score-val">${{quizScore}}/${{total}}</div>
                    <div class="score-lbl">Score Quiz</div>
                </div>
            `;
        }}

        function restartQuiz() {{
            quizIndex = 0; quizScore = 0;
            document.getElementById('result-section').style.display = 'none';
            document.getElementById('quiz-section').style.display = 'block';
            showQuestion();
        }}

        showQuestion();
    </script>
    """

    st.components.v1.html(quiz_html, height=520, scrolling=False)
    st.markdown('</div>', unsafe_allow_html=True)


def render_runner() -> None:
    """Affiche uniquement le runner sans le quiz."""

    st.markdown('<div class="game-wrapper">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="section-header">
            <span class="section-tag">Mini-jeu</span>
            <h2 class="section-title">Un dernier obstacle avant de partir 🏃</h2>
            <p class="section-desc">
                Saute par-dessus les défis de mon parcours — si tu oses.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    photo_b64 = get_image_base64_resized(RUNNER_PHOTO_PATH, size=120) or ""
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
        <div id="score-display2" style="text-align:right;font-size:1rem;font-weight:700;
                                        color:#3b82f6;margin-bottom:0.5rem;">
            Score : <span id="score2">0</span>
        </div>
        <canvas id="gameCanvas2" width="800" height="250" style="
            display:block;margin:0 auto;border-radius:12px;
            background:linear-gradient(180deg,#e0f2fe 0%,#f0f9ff 60%,#bfdbfe 100%);
            cursor:pointer;width:100%;max-width:800px;
        "></canvas>
        <div id="game-message2" style="text-align:center;margin-top:0.8rem;
                                       font-size:0.9rem;color:#64748b;">
            Appuie sur ESPACE ou clique pour sauter !
        </div>
    </div>

    <script>
        const canvas2 = document.getElementById('gameCanvas2');
        const ctx2 = canvas2.getContext('2d');

        const playerImg2 = new Image();
        playerImg2.src = '{photo_data_url}';
        let imgLoaded2 = false;
        playerImg2.onload = () => {{ imgLoaded2 = true; }};

        let gameState2 = 'waiting';
        let score2 = 0;
        let frameCount2 = 0;
        let speed2 = 4;
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
        let nextObstacle2 = 100;

        function jump2() {{
            if (gameState2 === 'waiting') {{ startGame2(); return; }}
            if (gameState2 === 'running' && !player2.jumping) {{
                player2.vy = -16;
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
            score2 = 0; frameCount2 = 0; speed2 = 4;
            obstacles2 = []; nextObstacle2 = 100;
            player2.y = player2.groundY;
            player2.vy = 0; player2.jumping = false;
            document.getElementById('game-message2').textContent = 'ESPACE ou clic pour sauter !';
            document.getElementById('score2').textContent = '0';
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
            document.getElementById('score2').textContent = score2;
            if (frameCount2 % 400 === 0) speed2 += 0.4;

            player2.vy += 0.8;
            player2.y += player2.vy;
            if (player2.y >= player2.groundY) {{
                player2.y = player2.groundY;
                player2.vy = 0; player2.jumping = false;
            }}

            nextObstacle2--;
            if (nextObstacle2 <= 0) {{
                const obs = OBSTACLES2[Math.floor(Math.random() * OBSTACLES2.length)];
                obstacles2.push({{ x: 820, y: 193, w: 50, h: 60, emoji: obs.emoji }});
                nextObstacle2 = 70 + Math.floor(Math.random() * 60);
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
                    document.getElementById('game-message2').textContent =
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
