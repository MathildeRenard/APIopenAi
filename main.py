import openai

if __name__ == '__main__':
    openai.api_key = "RemplacerCeTexteParLaClefOpenAI"
    completion = openai.Completion.create(engine="text-davinci-003", prompt="Quelle heure est il?", max_tokens=1000)
    print(completion.choices[0]['text'])






# See PyCharm help at https://www.jetbrains.com/help/pycharm/






# See PyCharm help at https://www.jetbrains.com/help/pycharm/
