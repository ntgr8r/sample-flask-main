from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/ny_agencies_map')
def ny_agencies_map():
    return render_template('ny_agencies_map.html')

@app.route('/plotzipboundaries')
def plotzipboundaries():
    return render_template('plotzipboundaries.html')

@app.route('/new_york_crime_map_agencies_all_crimes_corrected')
def select-state():
    return render_template('new_york_crime_map_agencies_all_crimes_corrected.html')

@app.route('/select-state')
def new_york_crime_map_agencies_all_crimes_corrected():
    return render_template('select-state.html')


@app.route('/ny_state_troopers_presentation')
def ny_state_troopers_presentation():
    return send_from_directory('static', 'NY State Troopers Presentation.txt')

if __name__ == '__main__':
    app.run(debug=True)