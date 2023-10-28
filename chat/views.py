
# views.py
from django.shortcuts import render
from google.cloud import dialogflow

def chat_with_bot(request):
    if request.method == 'POST':
        user_input = request.POST['user_input']

        # Initialize a Dialogflow client
        client = dialogflow.SessionsClient()

        # Define your Dialogflow project ID
        project_id = 'your-project-id'

        # Create a session
        session = client.session_path(project_id, 'unique-session-id')

        # Send user input to Dialogflow
        text_input = dialogflow.TextInput(text=user_input, language_code='en')
        query_input = dialogflow.QueryInput(text=text_input)

        response = client.detect_intent(
            session=session, query_input=query_input)

        bot_response = response.query_result.fulfillment_text

        return render(request, 'chat.html', {'user_input': user_input, 'bot_response': bot_response})

    return render(request, 'chat.html')
