#!/bin/bash


# GET API to fetch a bank details, given branch IFSC code
echo -e '\nGET API to fetch a bank details, given branch IFSC code\n\n'
 curl -X GET http://127.0.0.1:8000/bank/ABHY0065001 -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1MTE0Njc2LCJqdGkiOiI3ZGJhMjg1NTViMTQ0YjQ3OTUyMGQyYjJkZjJkNGY4ZiIsInVzZXJfaWQiOjF9.EyWP7SZpjgF9NUwDbwrfptFW-ybdpG08WcMnDGSFOZk'


# GET API to fetch all details of branches, given bank name and a city
echo -e '\n\n\n'

echo -e '\nGET API to fetch all details of branches, given bank name and a city\n\n'
curl -X GET 'http://127.0.0.1:8000/bank/ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED/MUMBAI?limit=10&offset=20' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1MTE0Njc2LCJqdGkiOiI3ZGJhMjg1NTViMTQ0YjQ3OTUyMGQyYjJkZjJkNGY4ZiIsInVzZXJfaWQiOjF9.EyWP7SZpjgF9NUwDbwrfptFW-ybdpG08WcMnDGSFOZk'
echo -e '\n'

