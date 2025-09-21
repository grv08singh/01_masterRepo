 Key-Value Store DBMS
--XML, JSON, BSON

{
  "user123": "John Doe",
  "user124": "Jane Smith",
  "first_name": "John",
  "user125": "Alice Johnson",
  "last_name": "Doe"
}

--Column Store DBMS
{
  "users": {
    "columns": ["user_id", "first_name", "last_name", "age"],
    "data": [
      ["1", "John", "Doe", "30"],
      ["2", "Jane", "Smith", "25"],
      ["3", "Alice", "Johnson", "28"]
    ]
  }
}
Document Store DBMS:
{
  "user123": {
    "_id": "user123",
    "first_name": "John",
    "last_name": "Doe",
    "profile": {
      "email": "john.doe@example.com",
      "age": 30
    },
    "interests": ["reading", "skiing", "hiking"]
  }
}

Graph DBMS
{
  "nodes": [
    {"id": "1", "type": "Person", "name": "John Doe"},
    {"id": "2", "type": "Person", "name": "Jane Smith"},
    {"id": "3", "type": "Company", "name": "Tech Solutions"}
  ],
  "edges": [
    {"source": "1", "target": "3", "type": "EMPLOYED_BY"},
    {"source": "2", "target": "3", "type": "EMPLOYED_BY"}
  ]
}


{
  "nodes": [
    {"id": "User1", "type": "User", "name": "Alice"},
    {"id": "User2", "type": "User", "name": "Bob"},
    {"id": "Post1", "type": "Post", "content": "Loving the new camera I got!", "timestamp": "2023-02-01T12:00:00Z"},
    {"id": "Comment1", "type": "Comment", "content": "Looks awesome, Alice!", "timestamp": "2023-02-01T13:00:00Z"}
  ],
  "edges": [
    {"source": "User1", "target": "User2", "type": "FRIENDS_WITH"},
    {"source": "User1", "target": "Post1", "type": "POSTED"},
    {"source": "User2", "target": "Comment1", "type": "COMMENTED_ON"},
    {"source": "User2", "target": "Post1", "type": "LIKES"}
  ]
}


{
  "nodes": [
    {"id": "Router1", "type": "Router", "location": "Data Center 1"},
    {"id": "Switch1", "type": "Switch", "location": "Data Center 1"},
    {"id": "User1", "type": "User", "address": "123 Elm St"},
    {"id": "ServicePoint1", "type": "Service Point", "service": "Internet"}
  ],
  "edges": [
    {"source": "Router1", "target": "Switch1", "type": "CONNECTED_TO"},
    {"source": "User1", "target": "ServicePoint1", "type": "USES"}
  ]
}


--###############################################################
--XML
<person>
  <name>Alice</name>
  <age>30</age>
  <city>New York</city>
</person>

--JSON
{
  "person": {
    "name": "Alice",
    "age": 30,
    "city": "New York"
  }
}

--txt , csv, excel , xml , json , ......



