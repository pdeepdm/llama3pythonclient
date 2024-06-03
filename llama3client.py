import streamlit as st
import json
import http.client
st.title("Welcome to Llama3 client!")

prompt_text = st.text_input("Enter prompt text:")

if st.button("submit"):
    conn = http.client.HTTPConnection("localhost", 11434)
    payload = "{\r\n    \"model\": \"llama3\",\r\n   \"prompt\":\" " + prompt_text +  " \"\r\n  }"
    headers = {
        'Content-Type': 'text/plain'
    }
    conn.request("POST", "/api/generate", payload, headers)
    res = conn.getresponse()
    data = res.read()
    processedData = data.decode("utf-8")
    split = processedData.split('\n')
    combinedText = ""
    for item in split:
        if item != '':
            json_object = json.loads(item)
            combinedText += json_object["response"]
            #st.text(json_object["response"])
    #print(data.decode("utf-8"))

    st.text(combinedText)

