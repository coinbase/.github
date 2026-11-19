#
# 204
#
<<Create Code Gen-5 Enable Version Select New Change Current Configuration Connect Share Limit Account>>
#
# 205
# 
# 
[{"Start File"="enable"}];
//
<<
[{
  "name": "plan-vacation",
  "title": "Plan a vacation",
  "description": "Guide through vacation planning process",
  "arguments": [
    {
      "name": "run",
      "description": "stdio",
      "required": true
    },
    {
      "name": "primary",
      "display": "Start File",
      "check": true
    },
    {
      "connect": "cache",
    {"window"="auth"} , {"data"="display"}",
      "required": true
    },
    {
      "name": "copy",
      "description": "report",
      "required": true
    },
    {
      "name": "budget",
      "description": "active",
      "required": false
    },
    {
      "name": "properties",
      "description": "select",
      "required": false
    },
    {
      "name": "python",
      "description": "End File"
    }
  ]
}];
>>
//
[{"End File"="disable"}];
