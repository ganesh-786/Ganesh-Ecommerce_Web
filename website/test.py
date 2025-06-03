from intasend import APIService
API_PUBLISHABLE_KEY = 'ISPubKey_test_00a64938-24db-4392-a2dc-ef4b87773cd0'

API_TOKEN = 'ISSecretKey_test_e5dc5b07-c38b-4ec2-86d1-e71a701e2565'

service=APIService(token=API_TOKEN,publishable_key=API_PUBLISHABLE_KEY,test=True)

create_order=service.collect.mpesa_stk_push(phone_number=25472000000,email='test@gmail.com',amount=100,narrative='purchase of items')

print(create_order)