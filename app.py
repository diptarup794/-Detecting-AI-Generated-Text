# # import streamlit as st
# # import joblib
# # import requests
# # from transformers import pipeline

# # # Load the saved model
# # model_path = 'ai_detection_model.pkl'
# # model_pipeline = joblib.load(model_path)

# # # Function to classify text and optionally paraphrase using Hugging Face Transformers
# # def classify_and_paraphrase(text):
# #     predict = model_pipeline.predict([text])[0]
# #     if predict == 1:
# #         result = 'AI Generated'
# #     else:
# #         result = 'Human Written'
# #     return result

# # # Function to paraphrase text using Hugging Face Transformers
# # def paraphrase_text(text):
# #     paraphraser = pipeline("text2text-generation", model="tuner007/pegasus_paraphrase")
# #     paraphrased_text = paraphraser(text)[0]['generated_text']
# #     return paraphrased_text

# # # Streamlit app
# # def main():
# #     st.title("AI Text Classifier and Paraphraser")
# #     st.write("Enter text below to classify if it's AI generated or human written.")

# #     input_text = st.text_area("Enter text here:")

# #     if st.button("Analyze Text"):
# #         classification_result = classify_and_paraphrase(input_text)
# #         st.write(f"Classification Result: {classification_result}")

# #         if classification_result == 'AI Generated':
# #             if st.button("Humanize"):
# #                 paraphrased_text = paraphrase_text(input_text)
# #                 st.write(f"Paraphrased Text: {paraphrased_text}")

# # if __name__ == "__main__":
# #     main()

# import streamlit as st
# import joblib
# import requests
# from transformers import pipeline

# # Load the saved model
# model_path = 'ai_detection_model.pkl'
# model_pipeline = joblib.load(model_path)

# # Function to classify text and optionally paraphrase using Hugging Face Transformers
# def classify_and_paraphrase(text):
#     predict = model_pipeline.predict([text])[0]
#     if predict == 1:
#         result = 'AI Generated'
#     else:
#         result = 'Human Written'
#     return result

# # Function to paraphrase text using Hugging Face Transformers
# def paraphrase_text(text):
#     paraphraser = pipeline("text2text-generation", model="tuner007/pegasus_paraphrase")
#     paraphrased_text = paraphraser(text)[0]['generated_text']
#     return paraphrased_text

# # Streamlit app
# def main():
#     st.title("AI Text Classifier and Paraphraser")
#     st.write("Enter text below to classify if it's AI generated or human written.")

#     input_text = st.text_area("Enter text here:")

#     if st.button("Analyze Text"):
#         classification_result = classify_and_paraphrase(input_text)
#         st.write(f"Classification Result: {classification_result}")

#         # Always call paraphrase_text to generate paraphrased text
#         paraphrased_text = paraphrase_text(input_text)

#         # Show "Humanize" button only if text is analyzed
#         if st.button("Humanize"):
#             st.write(f"Paraphrased Text: {paraphrased_text}")

# if __name__ == "__main__":
#     main()

import streamlit as st
import joblib
import requests
from transformers import pipeline

# Load the saved model
model_path = 'ai_detection_model.pkl'
model_pipeline = joblib.load(model_path)

# Function to classify text and optionally paraphrase using Hugging Face Transformers
def classify_and_paraphrase(text):
    predict = model_pipeline.predict([text])[0]
    if predict == 1:
        result = 'AI Generated'
    else:
        result = 'Human Written'
    return result

# Function to paraphrase text using Hugging Face Transformers
def paraphrase_text(text):
    paraphraser = pipeline("text2text-generation", model="tuner007/pegasus_paraphrase")
    paraphrased_text = paraphraser(text)[0]['generated_text']
    return paraphrased_text

# Streamlit app
def main():
    st.title("AI Text Classifier and Paraphraser")
    st.write("Enter text below to classify if it's AI generated or human written.")

    input_text = st.text_area("Enter text here:")

    if st.button("Analyze Text"):
        classification_result = classify_and_paraphrase(input_text)
        st.write(f"Classification Result: {classification_result}")

        # Generate paraphrase text only for AI-generated content
        if classification_result == 'AI Generated':
            paraphrased_text = paraphrase_text(input_text)
        else:
            paraphrased_text = None

        # Show "Humanize" button only if text is analyzed
        if st.button("Humanize"):
            if paraphrased_text:  # Check if paraphrase exists (for AI-generated text)
                st.write(f"Paraphrased Text: {paraphrased_text}")
            else:
                st.write("Paraphrasing is only available for AI-generated text.")

if __name__ == "__main__":
    main()
