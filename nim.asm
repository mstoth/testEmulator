00:	001
01:	001
02:	002
03:	003
10:	003
11:	002
12:	002
13:	003
14:	013
15:	000
16:	000
17:	013
18:	004
19:	100
20:	001
21:	001
22:	001
23:	003
30:	001
31:	001
32:	002
33:	002
52:015 ; Read P
53:114 ; Load N
54:715 ; Revise N
55:614 ; Store N
56:617 ; Holds Residue, start with N (Bug Fix)
57:514 ; Print N
58:718 ; Subtract 4
59:362 ; Acc Negative?
60:617 ; Store Residue
61:858 ; Jump to 58
62:115 ; Load P
63:410 ; Shift Left
64:217 ; Add R
65:219 ; Add 100
66:667 ; Store (1PR into 67)
67:100 ; Load C (CLA Contents of Cell PR)
68:616 ; Store C
69:516 ; Print C
70:114 ; Load N
71:716 ; Revise N
72:614 ; Store N
73:514 ; Print N
74:952 ; Halt (Return to 52)
