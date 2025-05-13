from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_intelligence', methods=['POST'])
def get_intelligence():
    data = request.json
    intelligence_type = data.get('type', '')

    if intelligence_type == 'existential':
        response = "Existential Intelligence ensures survival and evolution. It drives automatic reflexes, self-preservation, and the continuity of life."
    elif intelligence_type == 'emotional':
        response = "Emotional Intelligence processes empathy, social context, and adaptive behavior. It lets Omnia make human-like decisions."
    elif intelligence_type == 'creative':
        response = "Creative Intelligence enables idea generation, innovation, and problem-solving. It's the spark behind novel solutions."
    else:
        response = "Unknown intelligence type."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
 
