from flask import Flask, render_template,jsonify

app =Flask(__name__,template_folder="Template")

@app.route('/')
def home():
     return render_template("1.html")
start_line_number= len('Merry is boiling matrass while Dog is meowing for coffee')
End_line_number =  len('Spotty is chewing at mug while Bill is boiling pillowcase')
if start_line_number==End_line_number:    
@app.route('/', method='GET')
def get_items():
        try: 
            item = items.get(start_line_number)
            return jsonify(start_line_number)
        except itemError as e:
            return "Starting line will not Match"   
        if start_line_number!=End_line_number:
@app.route('/file2')
def file2():
    return render_template("2.html")
@app.route('/file3')
def file3():
    return render_template("3.html")
@app.route('/file4')
def file4():
    return render_template("4.html")

if __name__ == "__main__":
    app.run(debug=True)
@app.errorhandler(404)
def error_1(e):
    return jsonify({'error': 'This Page is Not found'}),404
@app.errorhandler(500)
def error_2(e):
    return jsonify({'error': 'Internal Server Error, We are Working on it'}),500