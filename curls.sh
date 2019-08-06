#!/bin/bash


# GET API to fetch a bank details, given branch IFSC code
echo -e '\nGET API to fetch a bank details, given branch IFSC code\n\n'
curl -X GET 'https://calm-wave-12873.herokuapp.com/bank/?ifsc=ABHY0065018&limit=1&offset=0' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1MTIwMDkwLCJqdGkiOiI3ZjVmOTAxNDI3NGI0YmI5OWI5N2FiNDYxY2NjMjUzNiIsInVzZXJfaWQiOjF9.PqmklrjadSjNHUsscqeor6dgdOl3ZJvlNnD7ZN9ZjtE'


# GET API to fetch all details of branches, given bank name and a city
echo -e '\n\n\n'

echo -e '\nGET API to fetch all details of branches, given bank name and a city\n\n'
curl -X GET 'https://calm-wave-12873.herokuapp.com/bank/branches?bank_name=ABHYUDAYA%20COOPERATIVE%20BANK%20LIMITED&city=MUMBAI&limit=10&offset=20' -H 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTY1MTIwMDkwLCJqdGkiOiI3ZjVmOTAxNDI3NGI0YmI5OWI5N2FiNDYxY2NjMjUzNiIsInVzZXJfaWQiOjF9.PqmklrjadSjNHUsscqeor6dgdOl3ZJvlNnD7ZN9ZjtE'
echo -e '\n'


