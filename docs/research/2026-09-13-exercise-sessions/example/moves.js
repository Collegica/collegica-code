// Each move is a loop of keyframes over one repetition. Angles are absolute, in degrees, in the side view: 0 points right, 90 up, 180 left, 270 down. The figure faces right when standing; supine and quadruped poses have the head to the left. 'alternate' mirrors left and right every other rep. 'tempo' is seconds per rep.
export default {
 "dead-bug": {
  "name": "Dead bug",
  "family": "Anti-extension",
  "cue": "Low back pressed into the floor; move slowly, breathe out as the limbs go away from you.",
  "root": [
   0,
   0.1
  ],
  "tempo": 5,
  "alternate": true,
  "keyframes": [
   {
    "t": 0.0,
    "torso": 180,
    "head": 180,
    "armL": [
     90,
     90
    ],
    "armR": [
     90,
     90
    ],
    "legL": [
     90,
     0
    ],
    "legR": [
     90,
     0
    ]
   },
   {
    "t": 0.4,
    "torso": 180,
    "head": 180,
    "armL": [
     168,
     168
    ],
    "armR": [
     90,
     90
    ],
    "legL": [
     90,
     0
    ],
    "legR": [
     14,
     6
    ]
   },
   {
    "t": 0.6,
    "torso": 180,
    "head": 180,
    "armL": [
     168,
     168
    ],
    "armR": [
     90,
     90
    ],
    "legL": [
     90,
     0
    ],
    "legR": [
     14,
     6
    ]
   },
   {
    "t": 1.0,
    "torso": 180,
    "head": 180,
    "armL": [
     90,
     90
    ],
    "armR": [
     90,
     90
    ],
    "legL": [
     90,
     0
    ],
    "legR": [
     90,
     0
    ]
   }
  ]
 },
 "bird-dog": {
  "name": "Bird dog",
  "family": "Anti-rotation",
  "cue": "Hips level, neck long. Reach the heel back and the hand forward; nothing else moves.",
  "root": [
   0,
   0.3
  ],
  "tempo": 5,
  "alternate": true,
  "keyframes": [
   {
    "t": 0.0,
    "torso": 180,
    "head": 180,
    "armL": [
     270,
     270
    ],
    "armR": [
     270,
     270
    ],
    "legL": [
     270,
     180
    ],
    "legR": [
     270,
     180
    ]
   },
   {
    "t": 0.4,
    "torso": 180,
    "head": 180,
    "armL": [
     270,
     270
    ],
    "armR": [
     178,
     178
    ],
    "legL": [
     2,
     2
    ],
    "legR": [
     270,
     180
    ]
   },
   {
    "t": 0.6,
    "torso": 180,
    "head": 180,
    "armL": [
     270,
     270
    ],
    "armR": [
     178,
     178
    ],
    "legL": [
     2,
     2
    ],
    "legR": [
     270,
     180
    ]
   },
   {
    "t": 1.0,
    "torso": 180,
    "head": 180,
    "armL": [
     270,
     270
    ],
    "armR": [
     270,
     270
    ],
    "legL": [
     270,
     180
    ],
    "legR": [
     270,
     180
    ]
   }
  ]
 },
 "jog-in-place": {
  "name": "Jogging in place",
  "family": "Aerobic",
  "cue": "Light on the feet, elbows bent, shoulders down. Slow to a march whenever you need to.",
  "root": [
   0,
   0.5
  ],
  "tempo": 0.7,
  "alternate": true,
  "keyframes": [
   {
    "t": 0.0,
    "torso": 92,
    "head": 92,
    "armL": [
     258,
     348
    ],
    "armR": [
     282,
     12
    ],
    "legL": [
     268,
     270
    ],
    "legR": [
     268,
     270
    ]
   },
   {
    "t": 0.5,
    "torso": 92,
    "head": 92,
    "armL": [
     282,
     12
    ],
    "armR": [
     258,
     348
    ],
    "legL": [
     268,
     270
    ],
    "legR": [
     316,
     252
    ]
   },
   {
    "t": 1.0,
    "torso": 92,
    "head": 92,
    "armL": [
     258,
     348
    ],
    "armR": [
     282,
     12
    ],
    "legL": [
     268,
     270
    ],
    "legR": [
     268,
     270
    ]
   }
  ]
 },
 "march-in-place": {
  "name": "Marching in place",
  "family": "Aerobic",
  "cue": "Knees to hip height, opposite arm swings. This one never gets skipped.",
  "root": [
   0,
   0.5
  ],
  "tempo": 1.2,
  "alternate": true,
  "keyframes": [
   {
    "t": 0.0,
    "torso": 90,
    "head": 90,
    "armL": [
     265,
     300
    ],
    "armR": [
     275,
     340
    ],
    "legL": [
     270,
     270
    ],
    "legR": [
     270,
     270
    ]
   },
   {
    "t": 0.5,
    "torso": 90,
    "head": 90,
    "armL": [
     275,
     340
    ],
    "armR": [
     250,
     320
    ],
    "legL": [
     270,
     270
    ],
    "legR": [
     345,
     262
    ]
   },
   {
    "t": 1.0,
    "torso": 90,
    "head": 90,
    "armL": [
     265,
     300
    ],
    "armR": [
     275,
     340
    ],
    "legL": [
     270,
     270
    ],
    "legR": [
     270,
     270
    ]
   }
  ]
 },
 "side-plank": {
  "name": "Side plank",
  "family": "Anti-lateral-flexion",
  "cue": "Straight line from ear to ankle; press the floor away. From the knees if the feet version breaks.",
  "root": [
   0,
   0.22
  ],
  "tempo": 6,
  "alternate": false,
  "keyframes": [
   {
    "t": 0.0,
    "torso": 168,
    "head": 168,
    "armL": [
     255,
     200
    ],
    "armR": [
     95,
     95
    ],
    "legL": [
     352,
     352
    ],
    "legR": [
     352,
     352
    ]
   },
   {
    "t": 1.0,
    "torso": 168,
    "head": 168,
    "armL": [
     255,
     200
    ],
    "armR": [
     95,
     95
    ],
    "legL": [
     352,
     352
    ],
    "legR": [
     352,
     352
    ]
   }
  ]
 },
 "goblet-squat": {
  "name": "Goblet squat",
  "family": "Weights, two hands",
  "cue": "Weight held at the chest, elbows inside the knees at the bottom, heels down.",
  "root": [
   0,
   0.5
  ],
  "tempo": 4,
  "alternate": false,
  "keyframes": [
   {
    "t": 0.0,
    "torso": 90,
    "head": 90,
    "armL": [
     250,
     20
    ],
    "armR": [
     250,
     20
    ],
    "legL": [
     270,
     270
    ],
    "legR": [
     270,
     270
    ]
   },
   {
    "t": 0.45,
    "torso": 70,
    "head": 80,
    "armL": [
     240,
     20
    ],
    "armR": [
     240,
     20
    ],
    "legL": [
     200,
     300
    ],
    "legR": [
     200,
     300
    ]
   },
   {
    "t": 0.55,
    "torso": 70,
    "head": 80,
    "armL": [
     240,
     20
    ],
    "armR": [
     240,
     20
    ],
    "legL": [
     200,
     300
    ],
    "legR": [
     200,
     300
    ]
   },
   {
    "t": 1.0,
    "torso": 90,
    "head": 90,
    "armL": [
     250,
     20
    ],
    "armR": [
     250,
     20
    ],
    "legL": [
     270,
     270
    ],
    "legR": [
     270,
     270
    ]
   }
  ],
  "rootMotion": [
   [
    0,
    0
   ],
   [
    0.45,
    -0.2
   ],
   [
    0.55,
    -0.2
   ],
   [
    1,
    0
   ]
  ]
 },
 "suitcase-carry": {
  "name": "Suitcase carry",
  "family": "Weights, one hand",
  "cue": "Stand tall, shoulders level, the free hand relaxed. Walk slowly; swap hands halfway.",
  "root": [
   0,
   0.5
  ],
  "tempo": 1.4,
  "alternate": true,
  "keyframes": [
   {
    "t": 0.0,
    "torso": 90,
    "head": 90,
    "armL": [
     268,
     268
    ],
    "armR": [
     262,
     300
    ],
    "legL": [
     258,
     262
    ],
    "legR": [
     282,
     262
    ]
   },
   {
    "t": 0.5,
    "torso": 90,
    "head": 90,
    "armL": [
     268,
     268
    ],
    "armR": [
     262,
     300
    ],
    "legL": [
     282,
     262
    ],
    "legR": [
     258,
     262
    ]
   },
   {
    "t": 1.0,
    "torso": 90,
    "head": 90,
    "armL": [
     268,
     268
    ],
    "armR": [
     262,
     300
    ],
    "legL": [
     258,
     262
    ],
    "legR": [
     282,
     262
    ]
   }
  ],
  "weightIn": "armL"
 }
};
