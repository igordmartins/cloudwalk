from flask import Flask, request, jsonify
import pickle
import pandas as pd
from datetime import datetime
# from flask_limiter import Limiter

app = Flask(__name__)
# limiter = Limiter(
#     app,
#     key_func=lambda: request.json['user_id'],
#     default_limits=["200 per day", "50 per hour"],
#     storage_uri="memory://",
# )

@app.route('/recommendation', methods=['POST'])
# @limiter.limit("3/minute")
def index():
    data = request.json
    recommendation = 'decline'

    try:
        approved = is_rule_based_approved(data)
        if (approved):
            score = get_score(data)
            threshold = 0.9
            if score < threshold:
                recommendation = 'approve'
    except Exception as e:
        print('Error recommendation', e)
        recommendation = 'decline'

    return jsonify({ 'transaction_id': data['transaction_id'], 'recommendation': recommendation})


def is_rule_based_approved(data):
    if data['device_id'] is None:
        return False
    return True

def get_score(data):
    try:
        ml = pickle.load(open('ml.sav', 'rb'))

        transaction_date = datetime.strptime(data['transaction_date'], '%Y-%m-%dT%H:%M:%S.%f')
        df = pd.DataFrame([{
            'merchant_id': str(data['merchant_id']),
            'user_id': str(data['user_id']),
            'transaction_amount': float(data['transaction_amount']),
            'device_id': str(data['device_id'] or 0),
            'bin': data['card_number'][:6],
            'last_digits': data['card_number'][12:],
            'day': transaction_date.day,
            'hour': transaction_date.hour,
            'minute': transaction_date.minute,
        }])

        fraud_prob = ml.predict_proba(df)[0][1]
        print('fraud_prob', fraud_prob)
        return fraud_prob

    except Exception as e:
        print('Error score', e)
        return 1

app.run(host='0.0.0.0', port=5000)
