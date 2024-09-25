# 1. Setup:

    # Make sure you have Python installed (preferably Python 3.7 or higher).
    # Install necessary packages:

pip install pandas flask

# Make sure your Flask setup is correct. Here’s how you can do that:

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/query', methods=['GET'])
def api_query():
    term = request.args.get('term')
    if not term:
        return jsonify({"error": "No search term provided"}), 400
    results = query_tweets(term)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)

  # 2. Running the System:

    Create a script (e.g., app.py) and paste the ingestion and query functions.
  
#Run the script to start querying:

python app.py

#Call the query_tweets function with your search term:

results = query_tweets('music')
print(results)
