from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

TEMPLATE = '''
<!doctype html>
<title>Demo Echo</title>
<h2>Echo Demo (Benign)</h2>
<form method="GET">
  <label>q: <input name="q" /></label>
  <button>Send</button>
</form>
<p>Echoed (safe): {{ q }}</p>
'''

@app.route('/', methods=['GET'])
def index():
    q = request.args.get('q','')
    # Important: We intentionally escape user input to avoid any real XSS.
    return render_template_string(TEMPLATE, q=q)

@app.route('/api/echo', methods=['POST'])
def api_echo():
    data = request.json or {}
    return jsonify({'echo': data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
