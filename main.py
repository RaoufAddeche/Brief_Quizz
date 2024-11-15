import streamlit as st
import json



#fonction pour sauv et charger les questions dans un fichier json

def sauv_questions(questions):
    with open("quizz_questions.json", "w") as file:
        json.dump(questions, file)

def charger_questions():
    with open("quizz_questions.json", "r") as file:
        return json.load(file)
    

#fonction lancer le quiz   
 
def lancer_quizz():

    st.title("Lancer le Quizz")

    if len(st.session_state["questions"]) > 0:
        questions = st.session_state["questions"]
    else:
        st.write("Veuillez créer un Quizz")
        return


    score = st.session_state["score"]
    index_question_actuelle = st.session_state["question_actuelle"]

    # Afficher la question actuelle
    
    question_data = questions[index_question_actuelle]
    reponse_utilisateur = st.radio(f"Question {index_question_actuelle + 1}: {question_data['question']}", question_data['options'], key=f"value{index_question_actuelle}")


    # Boutons pour valider passer à la question suivante (beug appuyer deux fois)

    col1, col2 = st.columns(2)
    

    # Bouton de validation col1 (beug appuyer deux fois)

    col1_boutton = col1.button("Valider", key=f"valider{index_question_actuelle}")
    if col1_boutton:
        if reponse_utilisateur == question_data["reponse_correcte"]:
            st.success("Bonne réponse !")
            score += 1
        else:
            st.error("Mauvaise réponse")
        st.session_state["score"] = score


    # Bouton de validation col2 (beug appuyer deux fois)

    col2_boutton = col2.button("Question suivante", key=f"next{index_question_actuelle}")
    if col2_boutton and index_question_actuelle < len(questions) - 1:
        st.session_state["question_actuelle"] += 1
        st.rerun()


    #afficher le score

    st.write(f"Votre score actuel : {score}/{len(questions)}")


# Liste pour stocker les questions, réponses et score

if "questions" not in st.session_state:
    st.session_state["questions"] = []

if "score" not in st.session_state:
    st.session_state["score"] = 0

if "question_actuelle" not in st.session_state:
    st.session_state["question_actuelle"] = 0

if "page_actuelle" not in st.session_state:
    st.session_state["page_actuelle"] = "creation"


# Menu

st.sidebar.title("Menu")
choix = st.sidebar.radio("Choisissez une option: ", ["Créer un quizz", "Lancer le quizz"])

if choix == "Créer un quizz":
    st.title('Configuration du Quizz')
    st.markdown('Merci de saisir les champs suivants:')

    # Saisir la question
    question = st.text_input('Saisir une question:')

    # Saisir les réponses
    reponse_input = st.text_input("Entrez les réponses (séparées par des virgules, sans espace)")

    
    # liste des reponses possibles

    options = [] 

    if reponse_input:
        options = [option for option in reponse_input.split(',')]


    if options:
        option_selectionner = st.radio("Choisissez une réponse", options)
        bonne_reponse = st.selectbox('Choisissez la bonne réponse', options)

    
    # Générer la question

    if st.button("Générer la question"):
        if question and bonne_reponse and options:
            st.session_state['questions'].append({
                'question': question,
                'options': options,
                'reponse_correcte': bonne_reponse
            })
            st.success("Question ajoutée")
        else:
            st.error('Erreur : Veuillez remplir tous les champs.')

    
    # Afficher les questions

    if st.session_state['questions']:
        for key, value in enumerate(st.session_state["questions"]):
            st.write(f"Question {key + 1}: {value['question']}")
            st.write(f"Réponses possibles: {' | '.join(value['options'])}")
            st.write(f"Bonne réponse: {value['reponse_correcte']}")

    # Sauve dans fichier json

    if st.button("Sauvegarder les questions"):
        sauv_questions(st.session_state["questions"])
        st.success("Les questions ont été sauvegardées.")

    # Petite image
    st.image("/home/addeche/Documents/Projet_Simplon/Brief_Streamlit/fondquizz.jpg")


elif choix == "Lancer le quizz":
    lancer_quizz()

    # Réinitialiser le quiz
    if st.button("Réinitialiser le quiz"):
        st.session_state["questions"] = []
        st.session_state["score"] = 0
        st.session_state["question_actuelle"] = 0
        st.session_state["reponses_utilisateur"] = []
        st.write("Quiz réinitialisé !")

    # Petite image
    st.image("jeffrey-betts-CCl4lKNO5H8-unsplash.jpg")
