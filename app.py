import json
import os.path

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
data = {
    "name": "root",
    "children": [
        {
            "name": "A",
            "children": [
                {"name": "A1", "value": 100},
                {"name": "A2", "value": 300}
            ]
        },
        {
            "name": "B",
            "children": [
                {"name": "B1",
                 "children" : [
                     {"name" : "b55", "value": 200}]},
                {"name": "B2", "value": 100},
                {"name": "B3", "value": 50}
            ]
        },
        {
            "name": "C",
            "children": [
                {"name": "C1", "value": 300}
            ]
        }
    ]
}



data2= [
           {"name": "root1",
                    "featureid": 10,
                    "feature": "x2ybar",
                    "threshold": 2.5,
                    "children": [
                        {
                            "name": 1,
                            "featureid": 8,
                            "feature": "y2bar ",
                            "threshold": 3.5,
                            "children": [
                                {
                                    "name": 3,
                                    "value": 10
                                },
                                {
                                    "name": 4,
                                    "value": 10
                                }
                            ]
                        },
                        {
                            "name": 2,
                            "featureid": 11,
                            "feature": "xy2bar",
                            "threshold": 6.5,
                            "children": [
                                {
                                    "name": 5,
                                    "featureid": 11,
                                    "feature": "xy2bar",
                                    "threshold": 4.5,
                                    "children": [
                                        {
                                            "name": 13,
                                            "value": 10
                                        },
                                        {
                                            "name": 14,
                                            "value": 10
                                        }
                                    ]
                                },
                                {
                                    "name": 6,
                                    "featureid": 12,
                                    "feature": "xedge ",
                                    "threshold": 6.5,
                                    "children": [
                                        {
                                            "name": 7,
                                            "featureid": 10,
                                            "feature": "x2ybar",
                                            "threshold": 9.5,
                                            "children": [
                                                {
                                                    "name": 9,
                                                    "featureid": 15,
                                                    "feature": "yedgex",
                                                    "threshold": 8.5,
                                                    "children": [
                                                        {
                                                            "name": 15,
                                                            "featureid": 12,
                                                            "feature": "xedge ",
                                                            "threshold": 1.5,
                                                            "children": [
                                                                {
                                                                    "name": 17,
                                                                    "value": 10
                                                                },
                                                                {
                                                                    "name": 18,
                                                                    "value": 10
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "name": 16,
                                                            "value": 10
                                                        }
                                                    ]
                                                },
                                                {
                                                    "name": 10,
                                                    "featureid": 7,
                                                    "feature": "x2bar",
                                                    "threshold": 4.5,
                                                    "children": [
                                                        {
                                                            "name": 11,
                                                            "value": 10
                                                        },
                                                        {
                                                            "name": 12,
                                                            "value": 10
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "name": 8,
                                            "value": 10
                                        }
                                    ]
                                }
                            ]
                        }
                    ]


            },
        {"name": "root2",
                            "featureid": 15,
                            "feature": "yedgex",
                            "threshold": 8.5,
                            "children": [
                                {
                                    "name": 1,
                                    "featureid": 10,
                                    "feature": "x2ybar",
                                    "threshold": 2.5,
                                    "children": [
                                        {
                                            "name": 3,
                                            "featureid": 7,
                                            "feature": "x2bar",
                                            "threshold": 3.5,
                                            "children": [
                                                {
                                                    "name": 15,
                                                    "featureid": 8,
                                                    "feature": "y2bar ",
                                                    "threshold": 4.5,
                                                    "children": [
                                                        {
                                                            "name": 17,
                                                            "size": 10
                                                        },
                                                        {
                                                            "name": 18,
                                                            "size": 10
                                                        }
                                                    ]
                                                },
                                                {
                                                    "name": 16,
                                                    "size": 10
                                                }
                                            ]
                                        },
                                        {
                                            "name": 4,
                                            "featureid": 10,
                                            "feature": "x2ybar",
                                            "threshold": 7.5,
                                            "children": [
                                                {
                                                    "name": 5,
                                                    "featureid": 13,
                                                    "feature": "xedgey",
                                                    "threshold": 9.5,
                                                    "children": [
                                                        {
                                                            "name": 13,
                                                            "size": 10
                                                        },
                                                        {
                                                            "name": 14,
                                                            "size": 10
                                                        }
                                                    ]
                                                },
                                                {
                                                    "name": 6,
                                                    "featureid": 12,
                                                    "feature": "xedge ",
                                                    "threshold": 5.5,
                                                    "children": [
                                                        {
                                                            "name": 7,
                                                            "featureid": 7,
                                                            "feature": "x2bar",
                                                            "threshold": 4.5,
                                                            "children": [
                                                                {
                                                                    "name": 9,
                                                                    "size": 10
                                                                },
                                                                {
                                                                    "name": 10,
                                                                    "size": 10
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "name": 8,
                                                            "size": 10
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "name": 2,
                                    "featureid": 11,
                                    "feature": "xy2bar",
                                    "threshold": 7.5,
                                    "children": [
                                        {
                                            "name": 11,
                                            "size": 10
                                        },
                                        {
                                            "name": 12,
                                            "size": 10
                                        }
                                    ]
                                }
                            ]


        },
    {"name": "root2",
     "featureid": 15,
     "feature": "yedgex",
     "threshold": 8.5,
     "children": [
         {
             "name": 1,
             "featureid": 10,
             "feature": "x2ybar",
             "threshold": 2.5,
             "children": [
                 {
                     "name": 3,
                     "featureid": 7,
                     "feature": "x2bar",
                     "threshold": 3.5,
                     "children": [
                         {
                             "name": 15,
                             "featureid": 8,
                             "feature": "y2bar ",
                             "threshold": 4.5,
                             "children": [
                                 {
                                     "name": 17,
                                     "size": 10
                                 },
                                 {
                                     "name": 18,
                                     "size": 10
                                 }
                             ]
                         },
                         {
                             "name": 16,
                             "size": 10
                         }
                     ]
                 },
                 {
                     "name": 4,
                     "featureid": 10,
                     "feature": "x2ybar",
                     "threshold": 7.5,
                     "children": [
                         {
                             "name": 5,
                             "featureid": 13,
                             "feature": "xedgey",
                             "threshold": 9.5,
                             "children": [
                                 {
                                     "name": 13,
                                     "size": 10
                                 },
                                 {
                                     "name": 14,
                                     "size": 10
                                 }
                             ]
                         },
                         {
                             "name": 6,
                             "featureid": 12,
                             "feature": "xedge ",
                             "threshold": 5.5,
                             "children": [
                                 {
                                     "name": 7,
                                     "featureid": 7,
                                     "feature": "x2bar",
                                     "threshold": 4.5,
                                     "children": [
                                         {
                                             "name": 9,
                                             "size": 10
                                         },
                                         {
                                             "name": 10,
                                             "size": 10
                                         }
                                     ]
                                 },
                                 {
                                     "name": 8,
                                     "size": 10
                                 }
                             ]
                         }
                     ]
                 }
             ]
         },
         {
             "name": 2,
             "featureid": 11,
             "feature": "xy2bar",
             "threshold": 7.5,
             "children": [
                 {
                     "name": 11,
                     "size": 10
                 },
                 {
                     "name": 12,
                     "size": 10
                 }
             ]
         }
     ]

     },{"name": "root1",
                    "featureid": 10,
                    "feature": "x2ybar",
                    "threshold": 2.5,
                    "children": [
                        {
                            "name": 1,
                            "featureid": 8,
                            "feature": "y2bar ",
                            "threshold": 3.5,
                            "children": [
                                {
                                    "name": 3,
                                    "value": 10
                                },
                                {
                                    "name": 4,
                                    "value": 10
                                }
                            ]
                        },
                        {
                            "name": 2,
                            "featureid": 11,
                            "feature": "xy2bar",
                            "threshold": 6.5,
                            "children": [
                                {
                                    "name": 5,
                                    "featureid": 11,
                                    "feature": "xy2bar",
                                    "threshold": 4.5,
                                    "children": [
                                        {
                                            "name": 13,
                                            "value": 10
                                        },
                                        {
                                            "name": 14,
                                            "value": 10
                                        }
                                    ]
                                },
                                {
                                    "name": 6,
                                    "featureid": 12,
                                    "feature": "xedge ",
                                    "threshold": 6.5,
                                    "children": [
                                        {
                                            "name": 7,
                                            "featureid": 10,
                                            "feature": "x2ybar",
                                            "threshold": 9.5,
                                            "children": [
                                                {
                                                    "name": 9,
                                                    "featureid": 15,
                                                    "feature": "yedgex",
                                                    "threshold": 8.5,
                                                    "children": [
                                                        {
                                                            "name": 15,
                                                            "featureid": 12,
                                                            "feature": "xedge ",
                                                            "threshold": 1.5,
                                                            "children": [
                                                                {
                                                                    "name": 17,
                                                                    "value": 10
                                                                },
                                                                {
                                                                    "name": 18,
                                                                    "value": 10
                                                                }
                                                            ]
                                                        },
                                                        {
                                                            "name": 16,
                                                            "value": 10
                                                        }
                                                    ]
                                                },
                                                {
                                                    "name": 10,
                                                    "featureid": 7,
                                                    "feature": "x2bar",
                                                    "threshold": 4.5,
                                                    "children": [
                                                        {
                                                            "name": 11,
                                                            "value": 10
                                                        },
                                                        {
                                                            "name": 12,
                                                            "value": 10
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "name": 8,
                                            "value": 10
                                        }
                                    ]
                                }
                            ]
                        }
                    ]


            }
        ]
@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data2)

@app.route('/readjson', methods=['GET'])
def readjson():
    with open('./frontend/src/rf_json_trees.json', mode='r') as f:
        data = json.loads(f.read())
        return jsonify(data)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
