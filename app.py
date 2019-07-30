from flask import Flask, jsonify, request

APP = Flask(__name__)

@APP.route('/api', methods=['POST'])
def returnRisk():
    data = request.get_json(force=True)

    risk_rating = {'amazon': "risk", 'apple': "risk", 'bofa': "risk", 'berkshire': "risk", 'google': "risk", 'jpm': "risk",
                   'johnson': "risk", 'mastercard': "risk", 'microsoft': "risk", 'proctor': "risk", 'visa': "risk",
                   'boeing': "risk", 'citi': "risk", 'comcast': "risk", 'cisco': "risk", 'disney': "risk",'hd': "risk",
                   'intel': "risk", 'coke': "risk", 'mcdonalds': "risk", 'merck': "risk", 'pepsi': "risk", 'pfizer': "risk",
                   'att': "risk", 'unh': "risk",'verizon': "risk", 'wells': "risk", 'walmart': "risk", 'boeing': "risk"}

    if data['company'] in risk_rating.keys():
        output = {'company_name': data['company'], 'risk_score': risk_rating.get(data['company'])}
        return jsonify(output)
    else:
        return jsonify({'err_msg': 'We do not currently support this company.'}), 422

if __name__ == '__main__':
    APP.run(debug=True)