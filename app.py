from flask import Flask, jsonify, request
import pickle
import numpy as np

APP = Flask(__name__)

@APP.route('/api', methods=['POST'])
def returnRisk():
    data = request.get_json(force=True)

    risk_rating = {'amazon': "risk", 'apple': "risk", 'bofa': "risk", 'berkshire': "risk", 'google': "risk", 'jpm': "risk",
                   'johnson': "risk", 'mastercard': "risk", 'microsoft': "risk", 'proctor': "risk", 'visa': "risk",
                   'boeing': "risk", 'citi': "risk", 'comcast': "risk", 'cisco': "risk", 'disney': "risk",'hd': "risk",
                   'intel': "risk", 'coke': "risk", 'mcdonalds': "risk", 'merck': "risk", 'pepsi': "risk", 'pfizer': "risk",
                   'att': "risk", 'unh': "risk",'verizon': "risk", 'wells': "risk", 'walmart': "risk"}

    if data['company'] in risk_rating.keys():

        # model_dict = {
        #     'amazon': pickle.load(open('not_real_model.pk1', "rb")),
        #     'apple': pickle.load(open('not_real_model.pk1', "rb")),
        #     'bofa': pickle.load(open('not_real_model.pk1', "rb")),
        #     'berkshire': pickle.load(open('not_real_model.pk1', "rb")),
        #     'google': pickle.load(open('not_real_model.pk1', "rb")),
        #     'jpm': pickle.load(open('not_real_model.pk1', "rb")),
        #     'johnson': pickle.load(open('not_real_model.pk1', "rb")),
        #     'mastercard': pickle.load(open('not_real_model.pk1', "rb")),
        #     'microsoft': pickle.load(open('not_real_model.pk1', "rb")),
        #     'proctor': pickle.load(open('not_real_model.pk1', "rb")),
        #     'visa': pickle.load(open('not_real_model.pk1', "rb")),
        #     'boeing': pickle.load(open('not_real_model.pk1', "rb")),
        #     'citi': pickle.load(open('not_real_model.pk1', "rb")),
        #     'comcast': pickle.load(open('not_real_model.pk1', "rb")),
        #     'cisco': pickle.load(open('not_real_model.pk1', "rb")),
        #     'disney': pickle.load(open('not_real_model.pk1', "rb")),
        #     'hd': pickle.load(open('not_real_model.pk1', "rb")),
        #     'intel': pickle.load(open('not_real_model.pk1', "rb")),
        #     'coke': pickle.load(open('not_real_model.pk1', "rb")),
        #     'mcdonalds' pickle.load(open('not_real_model.pk1', "rb")),
        #     'merck': pickle.load(open('not_real_model.pk1', "rb")),
        #     'pepsi': pickle.load(open('not_real_model.pk1', "rb")),
        #     'pfizer': pickle.load(open('not_real_model.pk1', "rb")),
        #     'att': pickle.load(open('not_real_model.pk1', "rb")),
        #     'unh': pickle.load(open('not_real_model.pk1', "rb")),
        #     'verizon': pickle.load(open('not_real_model.pk1', "rb")),
        #     'wells': pickle.load(open('not_real_model.pk1', "rb")),
        #     'walmart': pickle.load(open('not_real_model.pk1', "rb")),
        # }
        # model = model_dict['company name here']

        # predict_req = [data['price']]
        # predict_req = np.array(predict_req).reshape(1,-1)

        # y_hat = model.predict(predict_req)

        # output = {'company_name': data['company'], 'risk_score': int(y_hat[0])}
        output = {'company_name': data['company'], 'risk_score': risk_rating.get(data['company'])}
        return jsonify(output)
    else:
        return jsonify({'err_msg': 'We do not currently support this company.'}), 422

if __name__ == '__main__':
    APP.run(debug=True)