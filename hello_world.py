from pieces_copilot_sdk import PiecesClient

# Initialize the client
config = {
    'baseUrl': 'http://localhost:1000'  
}
pieces_client = PiecesClient(config)

# Print "Hello, World!"
print("Hello, World!")

# Use the ask_question method
question = "In which continent is Japan?"
response = pieces_client.ask_question(question)

# Print the response
print(response)
