import streamlit as st
import requests

def get_domain_recommendations(phrase):
    json_data = {
        'source': 'OPENAI_GPT',
        'input': {
            'phrase': phrase,
            'prompt': 'phrase',
        },
        'availabilityCheck': True,
        'showOnlyAvailable': True,
    }
    response = requests.post('https://umbrella-api.ionos.org/recommendations?limit=100&offset=0', json=json_data)
    return response.json()

def main():
    st.title("Domain Finder")
    phrase = st.text_input("Enter a description for your service:", "")
    if st.button("Find Domain"):
        results = get_domain_recommendations(phrase)

        for domain in results:
            st.write(domain['name'])
        

if __name__ == "__main__":
    main()
