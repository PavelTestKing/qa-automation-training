PS C:\QA-Automation\week2\day8> newman run "TEST JSONPlaceholder.postman_collection.json" --insecure --timeout-request 55000 --timeout-script 55000
(node:15924) [DEP0176] DeprecationWarning: fs.F_OK is deprecated, use fs.constants.F_OK instead
(Use `node --trace-deprecation ...` to show where the warning was created)
newman

TEST JSONPlaceholder

→ Get single user
  GET https://jsonplaceholder.typicode.com/users/1 [200 OK, 1.65kB, 278ms]
  √  Status code is 200
  √  User id is 1
  √  User has name and email

→ Get all users
  GET https://jsonplaceholder.typicode.com/users [errored]
     read ECONNRESET
  2. Status code is 200
  3. Response is an array
  4. Array contains 10 users

→ Update post (PUT)
  PUT https://jsonplaceholder.typicode.com/posts/1 [200 OK, 1.27kB, 668ms]
  √  Status code is 200
  √  Title updated

→ Create a post
  POST https://jsonplaceholder.typicode.com/posts [errored]
     read ECONNRESET
  6. Status code is 201
  7. Response has id
  8. Title matches

→ Delete post
  DELETE https://jsonplaceholder.typicode.com/posts/1 [200 OK, 1.11kB, 336ms]
  √  Status code is 200

┌─────────────────────────┬─────────────────────┬────────────────────┐
│                         │            executed │             failed │
├─────────────────────────┼─────────────────────┼────────────────────┤
│              iterations │                   1 │                  0 │
├─────────────────────────┼─────────────────────┼────────────────────┤
│                requests │                   5 │                  2 │
├─────────────────────────┼─────────────────────┼────────────────────┤
│            test-scripts │                  10 │                  0 │
├─────────────────────────┼─────────────────────┼────────────────────┤
│      prerequest-scripts │                   5 │                  0 │
├─────────────────────────┼─────────────────────┼────────────────────┤
│              assertions │                  12 │                  6 │
├─────────────────────────┴─────────────────────┴────────────────────┤
│ total run duration: 24.4s                                          │
├────────────────────────────────────────────────────────────────────┤
│ total data received: 653B (approx)                                 │
├────────────────────────────────────────────────────────────────────┤
│ average response time: 393ms [min: 278ms, max: 668ms, s.d.: 166ms] │
└────────────────────────────────────────────────────────────────────┘

  #  failure                detail

 1.  Error                  read ECONNRESET
                            at request
                            inside ""

 2.  AssertionError         Status code is 200
                            expected PostmanResponse{ …(5) } to have property 'code'
                            at assertion:0 in test-script
                            inside "Get all users"

 3.  JSONError              Response is an array
                            "undefined" is not valid JSON
                            at assertion:1 in test-script
                            inside "Get all users"

 4.  JSONError              Array contains 10 users
                            "undefined" is not valid JSON
                            at assertion:2 in test-script
                            inside "Get all users"

 5.  Error                  read ECONNRESET
                            at request
                            inside ""

 6.  AssertionError         Status code is 201
                            expected PostmanResponse{ …(5) } to have property 'code'
                            at assertion:0 in test-script
                            inside "Create a post"

 7.  JSONError              Response has id
                            "undefined" is not valid JSON
                            at assertion:1 in test-script
                            inside "Create a post"

 8.  JSONError              Title matches
                            "undefined" is not valid JSON
                            at assertion:2 in test-script
                            inside "Create a post"