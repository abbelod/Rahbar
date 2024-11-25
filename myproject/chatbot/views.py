from django.http import JsonResponse
from django.shortcuts import render
import markdown
from groq import Groq
from django.conf import settings


# Initialize the Groq client with the API key
client = Groq(api_key=settings.GROQ_API_KEY)


def chatbot_view(request):
    # Check if the request method is POST to handle user input
    if request.method == "POST":
        # Get the user input from the POST request
        user_message = request.POST.get("message", "")

        if not user_message:
            return JsonResponse({"error": "No message provided"}, status=400)

        try:
            # Create a chat completion using the Groq API
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role":"system",
                        "content": "you are RahbarBot, a tour guide for Pakistan. Keep the answers short and to the point. Keep answers formatted as markdown"
                    },
                    {
                        "role": "user",
                        "content": user_message,
                    },
                    
                ],
                model="llama3-8b-8192",
            )

            # Extract the chatbot's response
            bot_response = chat_completion.choices[0].message.content
            html_response = markdown.markdown(bot_response)

            # Return the response as JSON
            return JsonResponse({"response": html_response})

        except Exception as e:
            # Handle exceptions and return an error response
            return JsonResponse({"error": str(e)}, status=500)

    # Return an error for non-POST requests
    return JsonResponse({"error": "Invalid request method"}, status=405)


def chatbot_page_view(request):
    return render(request, 'chatbot/chatbot_page.html')