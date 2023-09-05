# Load the model and tokenizer
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F


tokenizer = AutoTokenizer.from_pretrained("SamLowe/roberta-base-go_emotions")
model = AutoModelForSequenceClassification.from_pretrained("SamLowe/roberta-base-go_emotions")
input_sentence = "Just tell me how many days are left"


inputs = tokenizer(input_sentence, return_tensors="pt")
outputs = model(**inputs)

logits = outputs.logits

probabilities = F.softmax(logits, dim=1)
predicted_emotion_label = probabilities.argmax().item()


labels = ["admiration", "amusement", "anger", "annoyance", 
          "approval", "caring", "confusion", "curiosity", 
          "desire", "disappointment", "disapproval", "disgust", 
          "embarrassment", "excitement", "fear", "gratitude", 
          "grief", "joy", "love", "nervousness", 
          "optimism", "pride", "realization", "relief", 
          "remorse", "sadness", "surprise", "neutral"]
predicted_emotion = labels[predicted_emotion_label]
print(predicted_emotion)
