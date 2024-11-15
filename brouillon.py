
#st.title('Configuration du Quizz')
#st.markdown('Merci de saisir les champs suivants:')
#st.text_input('Saisir une question:')
#reponse_input = st.text_input("Entrez les réponses (séparées par des virgules, sans espace)")

#if reponse_input:
#    options = [ option for option in reponse_input.split(',')]
#    option_selectionner = st.radio("Choisissez une réponse", options)
#st.selectbox('Choissisez la bonne réponse', options)
#st.success('Bonne réponse') 
#st.error('Mauvaise réponse')
#st.button('Generer la question')
#st.button('Rajouter une question')
#st.image("jeffrey-betts-CCl4lKNO5H8-unsplash.jpg")
#st.session_state

#fond d'ecran quizz

#st.markdown(
 #   """
  #  <style>
   # .reportview-container {
    #    background-image : url(/home/addeche/Documents/Projet_Simplon/Brief_Streamlit/fondquizz.jpg)
    #}
   #.sidebar .sidebar-content {
    #    background: url(/home/addeche/Documents/Projet_Simplon/Brief_Streamlit/fondquizz.jpg)
    #}
    #</style>
    #""",
    #unsafe_allow_html=True
#)
import streamlit as st
import json


#fonction sauv questions dans un fichier json

def sauv_questions(questions):
    with open("quizz_questions", "w") as file:
        json.dump(questions, file)

#fonction charger les questions depuis un fichier json

def charger_questions():
    with open("quizz_questions", "r") as file:
        return json.load(file)
    


def lancer_quizz():
    
    st.title("Lancer le Quizz")

    if len(st.session_state["questions"]) > 0:
        questions = st.session_state["questions"] 
    else:
        st.write("Veuillez d'abord créer le Quizz")
        return

    
    score = 0
    

    #Afficher questions et choix
    for key, value in enumerate(st.session_state["questions"]):
        reponse_utilisateur = st.radio(f"Question {key +1} : {value['question']}", value['options'], key=f"value{key}")
        
        if reponse_utilisateur == value["reponse_correcte"]:
            st.success("Bonne réponse !")
            score +=1
        
        else:
            st.error("Mauvaise réponse")

    st.write(f"Votre score : {score}/{len(questions)}")




#liste pour stocker les questions,reponses et score 

if "questions" not in st.session_state:
    st.session_state["questions"] = []

if "score" not in st.session_state:
    st.session_state["score"] = 0

if "reponse_utilisateur" not in st.session_state:
    st.session_state["reponse_utilisateur"] = []

if "page_actuelle" not in st.session_state:
    st.session_state["page_actuelle"] = "creation"


#fonction menu
st.sidebar.title("Menu")
choix = st.sidebar.radio("Choisissez une option: ", ["Créer un quizz", "Lancer le quizz"])

if choix == "Créer un quizz":
    #Titre de la page

    st.title('Configuration du Quizz')
    st.markdown('Merci de saisir les champs suivants:')

    #Saisir la question

    question = st.text_input('Saisir une question:')

    # Saisir les réponses

    reponse_input = st.text_input("Entrez les réponses (séparées par des virgules, sans espace)")

    if reponse_input:
        options = [ option for option in reponse_input.split(',')]
        option_selectionner = st.radio("Choisissez une réponse", options)

    #saisir bonne reponse
        bonne_reponse = st.selectbox('Choissisez la bonne réponse', options)

    #generer la question

    if st.button("Générer la question"):
        if question and bonne_reponse:
            #(rajout en cours)
            st.session_state['questions'].append({
                'question': question,
                'options': options,
                'reponse_correcte': bonne_reponse
            })
            st.success("Question ajoutée")
        else:
            st.error('erreur')

    #afficher les questions
    if st.session_state['questions']:
        for key, value in enumerate(st.session_state["questions"]):
            st.write(f"Question {key + 1} :  {value['question']}")
            st.write(f"Réponses possibles : {'|'.join(value['options'])}")
            st.write(f"Bonne réponse : {value['reponse_correcte']}")

    #sauvegarde des questions sur fichier json

    if st.button("Sauvegarder les questions"):
        sauv_questions(st.session_state["questions"])
        st.success("Les questions ont été sauvegardées.")

    #bouton demarrer quizz (a travaille)

    if st.button("Démarrer le quizz"):
        st.session_state['page_actuelle'] = "quiz"

    #petite image
    st.image("jeffrey-betts-CCl4lKNO5H8-unsplash.jpg")


elif choix == "Lancer le quizz":
    lancer_quizz()

    #reinitisaliser le quizz
    if st.button("Réinitialiser le quiz"):
            st.session_state["questions"] = []
            st.session_state["score"] = 0
            st.session_state["reponses_utilisateur"] = []
            st.write("Quiz réinitialisé !")

    #petite image
    st.image("jeffrey-betts-CCl4lKNO5H8-unsplash.jpg") 



    import streamlit as st
import json


#fonction sauv questions dans un fichier json

def sauv_questions(questions):
    with open("quizz_questions", "w") as file:
        json.dump(questions, file)

#fonction charger les questions depuis un fichier json

def charger_questions():
    with open("quizz_questions", "r") as file:
        return json.load(file)
    


def lancer_quizz():
    
    st.title("Lancer le Quizz")

    if len(st.session_state["questions"]) > 0:
        questions = st.session_state["questions"] 
    else:
        st.write("Veuillez d'abord créer le Quizz")
        return

    
    score = 0
    

    #Afficher questions et choix
    for key, value in enumerate(st.session_state["questions"]):
        reponse_utilisateur = st.radio(f"Question {key +1} : {value['question']}", value['options'], key=f"value{key}")

        if st.button("Valider",key = key+1):
            if reponse_utilisateur == value["reponse_correcte"]:
                st.success("Bonne réponse !")
                score +=1
        
            else:
                st.error("Mauvaise réponse")

    st.write(f"Votre score : {score}/{len(questions)}")




#liste pour stocker les questions,reponses et score 

if "questions" not in st.session_state:
    st.session_state["questions"] = []

if "score" not in st.session_state:
    st.session_state["score"] = 0

if "reponse_utilisateur" not in st.session_state:
    st.session_state["reponse_utilisateur"] = []

if "page_actuelle" not in st.session_state:
    st.session_state["page_actuelle"] = "creation"


#menu
st.sidebar.title("Menu")
choix = st.sidebar.radio("Choisissez une option: ", ["Créer un quizz", "Lancer le quizz"])

if choix == "Créer un quizz":
    #Titre de la page

    st.title('Configuration du Quizz')
    st.markdown('Merci de saisir les champs suivants:')

    #Saisir la question

    question = st.text_input('Saisir une question:')

    # Saisir les réponses

    reponse_input = st.text_input("Entrez les réponses (séparées par des virgules, sans espace)")

    if reponse_input:
        options = [ option for option in reponse_input.split(',')]
        option_selectionner = st.radio("Choisissez une réponse", options)

    #saisir bonne reponse
        bonne_reponse = st.selectbox('Choissisez la bonne réponse', options)

    #generer la question

    if st.button("Générer la question"):
        if question and bonne_reponse:
            #(rajout en cours)
            st.session_state['questions'].append({
                'question': question,
                'options': options,
                'reponse_correcte': bonne_reponse
            })
            st.success("Question ajoutée")
        else:
            st.error('erreur')

    #afficher les questions
    if st.session_state['questions']:
        for key, value in enumerate(st.session_state["questions"]):
            st.write(f"Question {key + 1} :  {value['question']}")
            st.write(f"Réponses possibles : {'|'.join(value['options'])}")
            st.write(f"Bonne réponse : {value['reponse_correcte']}")

    #sauvegarde des questions sur fichier json

    if st.button("Sauvegarder les questions"):
        sauv_questions(st.session_state["questions"])
        st.success("Les questions ont été sauvegardées.")

    #bouton demarrer quizz (a travaille)

    if st.button("Démarrer le quizz"):
        st.session_state['page_actuelle'] = "quiz"

    #petite image
    st.image("jeffrey-betts-CCl4lKNO5H8-unsplash.jpg")


elif choix == "Lancer le quizz":
    lancer_quizz()

    #reinitisaliser le quizz
    if st.button("Réinitialiser le quiz"):
            st.session_state["questions"] = []
            st.session_state["score"] = 0
            st.session_state["reponses_utilisateur"] = []
            st.write("Quiz réinitialisé !")

    #petite image
    st.image("jeffrey-betts-CCl4lKNO5H8-unsplash.jpg") 
        
        