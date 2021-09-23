# Regex for replacing all urls with custom url
import re
import markovify
import textwrap
import streamlit as st

with open("./tweets.txt", "r") as f:
  tweets = f.read()
f.close()

def replace_URLs(string, custom_URL):
    modified_string = re.sub(
        "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        f" {custom_URL} ",
        string,
    )
    return modified_string


def generate_fake_tweets(EVIL_URL,model):
    found = False
    while not found:
        sent = model.make_sentence()
        if sent and EVIL_URL in sent:
            found = True
    return sent


st.title('Genterate fake tweets with a url')
evil_url_input = st.text_input("Input your url", "http://evil.url")
preprocessed = replace_URLs(tweets, evil_url_input)
model = markovify.Text(preprocessed)
if st.button("Generate"):
    output = generate_fake_tweets(evil_url_input,model)
    st.code(textwrap.fill(output, 70))

st.caption("Built by NYP AI team")
