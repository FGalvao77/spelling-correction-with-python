from textblob import TextBlob

text = TextBlob('I havv a guud ideeaa')

correct_text = text.correct()

print('[ORIGINAL] Text:', text)
print('[CORRECTED] Text:', correct_text)