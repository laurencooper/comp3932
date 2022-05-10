from flask import Flask, jsonify

app= Flask(__name__)

#Pi Calculator source code taken from https://www.geeksforgeeks.org/calculate-pi-with-python/ 
#Pradipta Mukherjee, 2021, Calculate Pi With Python, GeeksforGeeks, viewed 2 February 2022, https://www.geeksforgeeks.org/calculate-pi-with-python/  


@app.route("/")
def calculate_pi():
     # Initialize denominator
    k = 1

    # Initialize sum
    s = 0

    for i in range(100000000):
	    # even index elements are positive
	    if i % 2 == 0:
		    s += 4/k
	    else:
		    # odd index elements are negative
		    s -= 4/k
	    # denominator is odd
	    k += 2
	
    return jsonify({"pi": str(s)})

if __name__ == "__main__":
    app.run(debug=True)