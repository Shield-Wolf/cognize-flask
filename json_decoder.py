#Code to strip out delimiters from a JSON file
def decode(encoded_JSON):

    #Strip out the new line characters, quotes and other characters
    encoded_JSON = encoded_JSON.replace('\n', '')
    encoded_JSON = encoded_JSON.replace('\r', '')
    encoded_JSON = encoded_JSON.replace('{"', '{')
    encoded_JSON = encoded_JSON.replace("'{", '{')
    encoded_JSON = encoded_JSON.replace('"{', '{')
    encoded_JSON = encoded_JSON.replace('"}', '}')
    encoded_JSON = encoded_JSON.replace('}"', '}')
    encoded_JSON = encoded_JSON.replace('"[', '[')
    encoded_JSON = encoded_JSON.replace('["', '[')
    encoded_JSON = encoded_JSON.replace(',"', ",") 
    encoded_JSON = encoded_JSON.replace('" \'', "")
    encoded_JSON = encoded_JSON.replace("```json","")
    encoded_JSON = encoded_JSON.replace("```", "") 

    decoded_JSON = encoded_JSON
    return decoded_JSON