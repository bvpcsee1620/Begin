m = '''
Urna Semper
1234 Main Street
Anytown, State ZIP
123-456-7890
no_reply@example.com

April 13, 2018
Trenz Pruca
4321 First Street
Anytown, State ZIP

Dear Trenz,
Lorem ipsum dolor sit amet, ligula suspendisse nulla pretium, rhoncus tempor fermentum, enim integer ad vestibulum volutpat. Nisl rhoncus turpis est, vel elit, congue wisi enim nunc ultricies sit, magna tincidunt. Maecenas aliquam maecenas ligula nostra, accumsan taciti. Sociis mauris in integer, a dolor netus non dui aliquet, sagittis felis sodales, dolor sociis mauris, vel eu libero cras. Faucibus at. Arcu habitasse elementum est, ipsum purus pede porttitor class
Ac dolor ac adipiscing amet bibendum nullam, lacus molestie ut libero nec, diam et, pharetra sodales, feugiat ullamcorper id tempor id vitae. Mauris pretium aliquet, lectus tincidunt. Porttitor mollis imperdiet libero senectus pulvinar. Etiam molestie mauris ligula laoreet, vehicula eleifend. Repellat orci erat et, sem cum, ultricies sollicitudin amet eleifend dolor.
Consectetuer arcu ipsum ornare pellentesque vehicula, in vehicula diam, ornare magna erat felis wisi a risus. Justo fermentum id. Malesuada eleifend, tortor molestie, a a vel et. Mauris at suspendisse, neque aliquam faucibus adipiscing, vivamus in. Wisi mattis leo suscipit nec amet, nisl fermentum tempor ac a, augue in eleifend in venenatis, cras sit id in vestibulum felis in, sed ligula.
Sincerely yours,

Urna Semper
'''

weekday_map_dict = {
    0: 'mon',
    1: 'tue',
    2: 'wed',
    3: 'thu',
    4: 'fri',
    5: 'sat',
    6: 'sun'
}

all_rooms = [
    'B-004',
    'B-101',
    'B-102',
    'B-103',
    'B-104',
    'C-102',
    'C-103',
    'C-104',
    'C-105',
    'C-201',
    'C-202',
    'C-204',
    'B-201',
    'B-202',
    'B-203',
    'B-204',
    'B-301',
    'B-302',
    'B-303',
    'B-304',
    'C-301',
    'E-201',
    'E-202',
    'A-102',
    'A-103',
    'A-104',
    'A-107',
    'A-202',
    'A-203',
    'A-204',
    'A-206',
    'A-207(a)',
    'A-207(b)',
    'A-302',
    'A-303',
    'A-304',
    'A-306',
    'A-307',
    'A-308',
    'B-001',
    'B-002',
    'C-302',
    'C-303',
    'C-304',
    'C-305',
    'E-101',
    'E-102',
    'E-301',
    'E-302'
]


all_batches = {
    'CSE (E)(SEM-1)': [
        {
            "value": "ETMA-101",
            "label": "Applied Mathematics-I"
        },
        {
            "value": "ETPH-103",
            "label": "Applied Physics-I"
        },
        {
            "value": "ETME-105",
            "label": "Manufacturing Processes"
        },
        {
            "value": "ETEE-107",
            "label": "Electrical Technology"
        },
        {
            "value": "ETHS-109",
            "label": "Human Values and Professional Ethics-I#"
        },
        {
            "value": "ETCS-111",
            "label": "Fundamentals of Computing"
        },
        {
            "value": "ETCH-113",
            "label": "Applied Chemistry"
        },
        {
            "value": "ETPH-151",
            "label": "Applied Physics Lab-I"
        },
        {
            "value": "ETEE-153",
            "label": "Electrical Technology Lab"
        },
        {
            "value": "ETME-155",
            "label": "Workshop Practice"
        },
        {
            "value": "ETME-157",
            "label": "Engineering Graphics Lab"
        },
        {
            "value": "ETCS-157",
            "label": "Fundamentals of Computing Lab"
        },
        {
            "value": "ETCH-161",
            "label": "Applied Chemistry Lab"
        }
    ],
    'CSE (E)(SEM-3)': [
        {
            "value": "ETMA 201",
            "label": "Applied Mathematics \u2013 III"
        },
        {
            "value": "ETCS 203",
            "label": "Foundation of Computer Science"
        },
        {
            "value": "ETEC 205",
            "label": "Switching Theory and Logic Design"
        },
        {
            "value": "ETEE 207",
            "label": "Circuits and Systems"
        },
        {
            "value": "ETCS 209",
            "label": "Data Structure"
        },
        {
            "value": "ETCS 211",
            "label": "Computer Graphics and Multimedia"
        },
        {
            "value": "ETEC 253",
            "label": "Switching Theory and Logic Design Lab"
        },
        {
            "value": "ETCS 255",
            "label": "Data Structure Lab"
        },
        {
            "value": "ETEE 257",
            "label": "Circuits and Systems Lab"
        },
        {
            "value": "ETCS 257",
            "label": "Computer Graphics and Multimedia Lab"
        }
    ],
    'CSE (E)(SEM-5)': [
        {"value": "ETCS301", "label": "Algorithms Design and Analysis"},
        {"value": "ETCS303", "label": "Software Engineering"},
        {"value": "ETCS307", "label": "Java Programming"},
        {"value": "ETMS 311", "label": "Industrial Management"},
        {"value": "ETEC-303", "label": "Digital Communication"},
        {"value": "ETHS 301", "label": "Communication Skills for Professionals"},
        {"value": "ETCS 351", "label": "Algorithms Design and Analysis Lab"},
        {"value": "ETCS 353", "label": "Software Engineering Lab"},
        {"value": "ETCS 357", "label": "Java Programming Lab"},
        {
            "value": "ETCS 359",
            "label": "Viva Industrial Training / In-house Workshop"
        },
        {"value": "ETEC-357", "label": "Digital Communication Lab"},
        {"value": "ETHS 351", "label": "Communication Skills for Professionals Lab"}
    ],
    'CSE (E)(SEM-7)': [
        {
            "value": "ETCS401",
            "label": "Information Security"
        },
        {
            "value": "ETCS403",
            "label": "Software Testing and Quality Assurance"
        },
        {
            "value": "ETEC405",
            "label": "Wireless Communication"
        },
        {
            "value": "ETCS407",
            "label": "Complexity Theory"
        },
        {
            "value": "ETCS409",
            "label": "Intellectual Property Rights"
        },
        {
            "value": "ETEC-401",
            "label": "Embedded Systems"
        },
        {
            "value": "ETCS413",
            "label": "Data Mining and Business Intelligence"
        },
        {
            "value": "ETCS415",
            "label": "Advanced Computer Architecture"
        },
        {
            "value": "ETCS 410",
            "label": "Natural Language Processing"
        },
        {
            "value": "ETIT 415",
            "label": "Digital Signal Processing"
        },
        {
            "value": "ETCS 421",
            "label": "Simulation and Modelling"
        },
        {
            "value": "ETCS 423",
            "label": "Advanced DBMS"
        },
        {
            "value": "ETCS 427",
            "label": "Parallel Computing"
        },
        {
            "value": "ETIT 401",
            "label": "Advanced Computer Networks"
        },
        {
            "value": "ETEE-429",
            "label": "Control System"
        },
        {
            "value": "ETHS-419",
            "label": "Sociology and Elements of Indian History for Engineers"
        },
        {
            "value": "ETCS 451",
            "label": "Information Security Lab"
        },
        {
            "value": "ETCS 453",
            "label": "Software Testing and QA Lab"
        },
        {
            "value": "ETEC 463",
            "label": "Wireless Communication Lab"
        },
        {
            "value": "ETCS 457",
            "label": "Lab based on Elective I or II"
        },
        {
            "value": "ETCS 459",
            "label": "Summer Training / Industrial Workshop/ Certification"
        },
        {
            "value": "ETCS 461",
            "label": "Minor Project"
        }
    ],
    'CSE (M)(SEM-1)': [
        {
            "value": "ETMA-101",
            "label": "Applied Mathematics-I"
        },
        {
            "value": "ETPH-103",
            "label": "Applied Physics-I"
        },
        {
            "value": "ETME-105",
            "label": "Manufacturing Processes"
        },
        {
            "value": "ETEE-107",
            "label": "Electrical Technology"
        },
        {
            "value": "ETHS-109",
            "label": "Human Values and Professional Ethics-I#"
        },
        {
            "value": "ETCS-111",
            "label": "Fundamentals of Computing"
        },
        {
            "value": "ETCH-113",
            "label": "Applied Chemistry"
        },
        {
            "value": "ETPH-151",
            "label": "Applied Physics Lab-I"
        },
        {
            "value": "ETEE-153",
            "label": "Electrical Technology Lab"
        },
        {
            "value": "ETME-155",
            "label": "Workshop Practice"
        },
        {
            "value": "ETME-157",
            "label": "Engineering Graphics Lab"
        },
        {
            "value": "ETCS-157",
            "label": "Fundamentals of Computing Lab"
        },
        {
            "value": "ETCH-161",
            "label": "Applied Chemistry Lab"
        }
    ],
    'CSE (M)(SEM-3)': [
        {
            "value": "ETMA 201",
            "label": "Applied Mathematics \u2013 III"
        },
        {
            "value": "ETCS 203",
            "label": "Foundation of Computer Science"
        },
        {
            "value": "ETEC 205",
            "label": "Switching Theory and Logic Design"
        },
        {
            "value": "ETEE 207",
            "label": "Circuits and Systems"
        },
        {
            "value": "ETCS 209",
            "label": "Data Structure"
        },
        {
            "value": "ETCS 211",
            "label": "Computer Graphics and Multimedia"
        },
        {
            "value": "ETEC 253",
            "label": "Switching Theory and Logic Design Lab"
        },
        {
            "value": "ETCS 255",
            "label": "Data Structure Lab"
        },
        {
            "value": "ETEE 257",
            "label": "Circuits and Systems Lab"
        },
        {
            "value": "ETCS 257",
            "label": "Computer Graphics and Multimedia Lab"
        }
    ],
    'CSE (M)(SEM-5)': [
        {"value": "ETCS301", "label": "Algorithms Design and Analysis"},
        {"value": "ETCS303", "label": "Software Engineering"},
        {"value": "ETCS307", "label": "Java Programming"},
        {"value": "ETMS 311", "label": "Industrial Management"},
        {"value": "ETEC-303", "label": "Digital Communication"},
        {"value": "ETHS 301", "label": "Communication Skills for Professionals"},
        {"value": "ETCS 351", "label": "Algorithms Design and Analysis Lab"},
        {"value": "ETCS 353", "label": "Software Engineering Lab"},
        {"value": "ETCS 357", "label": "Java Programming Lab"},
        {
            "value": "ETCS 359",
            "label": "Viva Industrial Training / In-house Workshop"
        },
        {"value": "ETEC-357", "label": "Digital Communication Lab"},
        {"value": "ETHS 351", "label": "Communication Skills for Professionals Lab"}
    ],
    'CSE (M)(SEM-7)': [
        {
            "value": "ETCS401",
            "label": "Information Security"
        },
        {
            "value": "ETCS403",
            "label": "Software Testing and Quality Assurance"
        },
        {
            "value": "ETEC405",
            "label": "Wireless Communication"
        },
        {
            "value": "ETCS407",
            "label": "Complexity Theory"
        },
        {
            "value": "ETCS409",
            "label": "Intellectual Property Rights"
        },
        {
            "value": "ETEC-401",
            "label": "Embedded Systems"
        },
        {
            "value": "ETCS413",
            "label": "Data Mining and Business Intelligence"
        },
        {
            "value": "ETCS415",
            "label": "Advanced Computer Architecture"
        },
        {
            "value": "ETCS 410",
            "label": "Natural Language Processing"
        },
        {
            "value": "ETIT 415",
            "label": "Digital Signal Processing"
        },
        {
            "value": "ETCS 421",
            "label": "Simulation and Modelling"
        },
        {
            "value": "ETCS 423",
            "label": "Advanced DBMS"
        },
        {
            "value": "ETCS 427",
            "label": "Parallel Computing"
        },
        {
            "value": "ETIT 401",
            "label": "Advanced Computer Networks"
        },
        {
            "value": "ETEE-429",
            "label": "Control System"
        },
        {
            "value": "ETHS-419",
            "label": "Sociology and Elements of Indian History for Engineers"
        },
        {
            "value": "ETCS 451",
            "label": "Information Security Lab"
        },
        {
            "value": "ETCS 453",
            "label": "Software Testing and QA Lab"
        },
        {
            "value": "ETEC 463",
            "label": "Wireless Communication Lab"
        },
        {
            "value": "ETCS 457",
            "label": "Lab based on Elective I or II"
        },
        {
            "value": "ETCS 459",
            "label": "Summer Training / Industrial Workshop/ Certification"
        },
        {
            "value": "ETCS 461",
            "label": "Minor Project"
        }
    ],
    'IT (M)(SEM-1)': [
        {"value": "ETMA-101", "label": "Applied Mathematics-I"},
        {"value": "ETPH-103", "label": "Applied Physics-I"},
        {"value": "ETME-105", "label": "Manufacturing Processes"},
        {"value": "ETEE-107", "label": "Electrical Technology"},
        {"value": "ETHS-109", "label": "Human Values and Professional Ethics-I#"},
        {"value": "ETCS-111", "label": "Fundamentals of Computing"},
        {"value": "ETCH-113", "label": "Applied Chemistry"},
        {"value": "ETPH-151", "label": "Applied Physics Lab-I"},
        {"value": "ETEE-153", "label": "Electrical Technology Lab"},
        {"value": "ETME-155", "label": "Workshop Practice"},
        {"value": "ETME-157", "label": "Engineering Graphics Lab"},
        {"value": "ETCS-157", "label": "Fundamentals of Computing Lab"},
        {"value": "ETCH-161", "label": "Applied Chemistry Lab"}
    ],
    'IT (M)(SEM-3)': [
        {
            "value": "ETMA 201",
            "label": "Applied Mathematics \u2013 III"
        },
        {
            "value": "ETCS 203",
            "label": "Foundation of Computer Science "
        },
        {
            "value": "ETEC 205",
            "label": "Switching Theory and Logic Design"
        },
        {
            "value": "ETEE 207",
            "label": "Circuits  and Systems"
        },
        {
            "value": "ETCS 209",
            "label": "Data Structure "
        },
        {
            "value": "ETCS 211",
            "label": "Computer Graphics and Multimedia"
        },
        {
            "value": "ETEC 253",
            "label": "Switching Theory and Logic Design Lab"
        },
        {
            "value": "ETCS 255",
            "label": "Data Structure  Lab"
        },
        {
            "value": "ETEE 257",
            "label": "Circuits and Systems Lab"
        },
        {
            "value": "ETCS 257",
            "label": "Computer Graphics and Multimedia Lab"
        }
    ],
    'IT (M)(SEM-5)': [
        {"value": "ETCS 301", "label": "Algorithms Design and Analysis "},
        {"value": "ETCS 303", "label": "Software Engineering "},
        {"value": "ETCS-307", "label": "Java Programming "},
        {"value": "ETMS 311", "label": "Industrial Management"},
        {"value": "ETIT-309", "label": "Communication Systems"},
        {"value": "ETHS 301", "label": "Communication Skills for Professionals "},
        {"value": "ETCS 351", "label": "Algorithms Design and Analysis  Lab  "},
        {"value": "ETCS 353", "label": "Software Engineering Lab"},
        {"value": "ETCS 357", "label": "Java Programming Lab"},
        {
            "value": "ETIT 359",
            "label": "Viva Industrial Training / In-house Workshop"
        },
        {"value": "ETIT 357", "label": "Communication Systems Lab"},
        {"value": "ETHS 351", "label": "Communication Skills for Professionals Lab"}
    ],
    'IT (M)(SEM-7)': [
        {
            "value": "ETIT-401",
            "label": "Advanced Computer Networks"
        },
        {
            "value": "ETIT-403",
            "label": "Cryptography and Network  Security"
        },
        {
            "value": "ETEC-405",
            "label": "Wireless Communication"
        },
        {
            "value": "ETEC-401",
            "label": "Embedded Systems "
        },
        {
            "value": "ETEC-403",
            "label": "Optoelectronics and Optical Communication "
        },
        {
            "value": "ETIT-407",
            "label": "Cloud Computing"
        },
        {
            "value": "ETIT-409",
            "label": "Distributed Databases"
        },
        {
            "value": "ETIT-411",
            "label": "Semantic Web Technologies "
        },
        {
            "value": "ETIT-413",
            "label": "Software Testing "
        },
        {
            "value": "ETIT-415",
            "label": "Digital Signal Processing"
        },
        {
            "value": "ETIT-419",
            "label": ".NET and C#  Programming "
        },
        {
            "value": "ETIT-421",
            "label": "Enterprise Computing in Java "
        },
        {
            "value": "ETIT-423",
            "label": "System and Network Administration "
        },
        {
            "value": "ETIT-425",
            "label": "Grid Computing "
        },
        {
            "value": "ETIT-427",
            "label": "Advanced Database Administration "
        },
        {
            "value": "ETIT-429",
            "label": "Probablistic Graphical Models"
        },
        {
            "value": "ETHS-419",
            "label": "Sociology and Elements of Indian History for Engineers "
        },
        {
            "value": "ETIT-453",
            "label": "Advanced Computer Networks  Lab "
        },
        {
            "value": "ETIT-455",
            "label": "Cryptography and Network  Security  Lab"
        },
        {
            "value": "ETEC-463",
            "label": "Wireless Communication Lab"
        },
        {
            "value": "ETIT-459",
            "label": "Lab based on Elective Group\u2013 A or B"
        },
        {
            "value": "ETIT-461",
            "label": "Summer Training / Industrial workshop / Certification "
        },
        {
            "value": "ETIT-463",
            "label": "Minor Project+"
        }
    ],
    'IT (E)(SEM-1)': [
        {"value": "ETMA-101", "label": "Applied Mathematics-I"},
        {"value": "ETPH-103", "label": "Applied Physics-I"},
        {"value": "ETME-105", "label": "Manufacturing Processes"},
        {"value": "ETEE-107", "label": "Electrical Technology"},
        {"value": "ETHS-109", "label": "Human Values and Professional Ethics-I#"},
        {"value": "ETCS-111", "label": "Fundamentals of Computing"},
        {"value": "ETCH-113", "label": "Applied Chemistry"},
        {"value": "ETPH-151", "label": "Applied Physics Lab-I"},
        {"value": "ETEE-153", "label": "Electrical Technology Lab"},
        {"value": "ETME-155", "label": "Workshop Practice"},
        {"value": "ETME-157", "label": "Engineering Graphics Lab"},
        {"value": "ETCS-157", "label": "Fundamentals of Computing Lab"},
        {"value": "ETCH-161", "label": "Applied Chemistry Lab"}
    ],
    'IT (E)(SEM-3)': [
        {
            "value": "ETMA 201",
            "label": "Applied Mathematics \u2013 III"
        },
        {
            "value": "ETCS 203",
            "label": "Foundation of Computer Science "
        },
        {
            "value": "ETEC 205",
            "label": "Switching Theory and Logic Design"
        },
        {
            "value": "ETEE 207",
            "label": "Circuits  and Systems"
        },
        {
            "value": "ETCS 209",
            "label": "Data Structure "
        },
        {
            "value": "ETCS 211",
            "label": "Computer Graphics and Multimedia"
        },
        {
            "value": "ETEC 253",
            "label": "Switching Theory and Logic Design Lab"
        },
        {
            "value": "ETCS 255",
            "label": "Data Structure  Lab"
        },
        {
            "value": "ETEE 257",
            "label": "Circuits and Systems Lab"
        },
        {
            "value": "ETCS 257",
            "label": "Computer Graphics and Multimedia Lab"
        }
    ],
    'IT (E)(SEM-5)': [
        {"value": "ETCS 301", "label": "Algorithms Design and Analysis "},
        {"value": "ETCS 303", "label": "Software Engineering "},
        {"value": "ETCS-307", "label": "Java Programming "},
        {"value": "ETMS 311", "label": "Industrial Management"},
        {"value": "ETIT-309", "label": "Communication Systems"},
        {"value": "ETHS 301", "label": "Communication Skills for Professionals "},
        {"value": "ETCS 351", "label": "Algorithms Design and Analysis  Lab  "},
        {"value": "ETCS 353", "label": "Software Engineering Lab"},
        {"value": "ETCS 357", "label": "Java Programming Lab"},
        {
            "value": "ETIT 359",
            "label": "Viva Industrial Training / In-house Workshop"
        },
        {"value": "ETIT 357", "label": "Communication Systems Lab"},
        {"value": "ETHS 351", "label": "Communication Skills for Professionals Lab"}
    ],
    'IT (E)(SEM-7)': [
        {
            "value": "ETIT-401",
            "label": "Advanced Computer Networks"
        },
        {
            "value": "ETIT-403",
            "label": "Cryptography and Network  Security"
        },
        {
            "value": "ETEC-405",
            "label": "Wireless Communication"
        },
        {
            "value": "ETEC-401",
            "label": "Embedded Systems "
        },
        {
            "value": "ETEC-403",
            "label": "Optoelectronics and Optical Communication "
        },
        {
            "value": "ETIT-407",
            "label": "Cloud Computing"
        },
        {
            "value": "ETIT-409",
            "label": "Distributed Databases"
        },
        {
            "value": "ETIT-411",
            "label": "Semantic Web Technologies "
        },
        {
            "value": "ETIT-413",
            "label": "Software Testing "
        },
        {
            "value": "ETIT-415",
            "label": "Digital Signal Processing"
        },
        {
            "value": "ETIT-419",
            "label": ".NET and C#  Programming "
        },
        {
            "value": "ETIT-421",
            "label": "Enterprise Computing in Java "
        },
        {
            "value": "ETIT-423",
            "label": "System and Network Administration "
        },
        {
            "value": "ETIT-425",
            "label": "Grid Computing "
        },
        {
            "value": "ETIT-427",
            "label": "Advanced Database Administration "
        },
        {
            "value": "ETIT-429",
            "label": "Probablistic Graphical Models"
        },
        {
            "value": "ETHS-419",
            "label": "Sociology and Elements of Indian History for Engineers "
        },
        {
            "value": "ETIT-453",
            "label": "Advanced Computer Networks  Lab "
        },
        {
            "value": "ETIT-455",
            "label": "Cryptography and Network  Security  Lab"
        },
        {
            "value": "ETEC-463",
            "label": "Wireless Communication Lab"
        },
        {
            "value": "ETIT-459",
            "label": "Lab based on Elective Group\u2013 A or B"
        },
        {
            "value": "ETIT-461",
            "label": "Summer Training / Industrial workshop / Certification "
        },
        {
            "value": "ETIT-463",
            "label": "Minor Project+"
        }
    ],
    'ECE (M1)(SEM-1)': [
        {"value": "ETMA-101", "label": "Applied Mathematics-I"},
        {"value": "ETPH-103", "label": "Applied Physics-I"},
        {"value": "ETME-105", "label": "Manufacturing Processes"},
        {"value": "ETEE-107", "label": "Electrical Technology"},
        {"value": "ETHS-109", "label": "Human Values and Professional Ethics-I#"},
        {"value": "ETCS-111", "label": "Fundamentals of Computing"},
        {"value": "ETCH-113", "label": "Applied Chemistry"},
        {"value": "ETPH-151", "label": "Applied Physics Lab-I"},
        {"value": "ETEE-153", "label": "Electrical Technology Lab"},
        {"value": "ETME-155", "label": "Workshop Practice"},
        {"value": "ETME-157", "label": "Engineering Graphics Lab"},
        {"value": "ETCS-157", "label": "Fundamentals of Computing Lab"},
        {"value": "ETCH-161", "label": "Applied Chemistry Lab"}
    ],
    'ECE (M1)(SEM-3)': [
        {"value": "ETMA-201", "label": "Applied Mathematics \u2013 III"},
        {"value": "ETEC-203", "label": "Analog Electronics - I"},
        {"value": "ETEC-205", "label": "Switching Theory and Logic Design"},
        {"value": "ETEC-207", "label": "Electronic Instruments and\nMeasurements"},
        {"value": "ETCS-209", "label": "Data Structures"},
        {"value": "ETEC-211", "label": "Signals and Systems"},
        {"value": "ETEC-251", "label": "*Analog Electronics-I Lab"},
        {"value": "ETEC-253", "label": "Switching Theory and Logic Design Lab"},
        {
            "value": "ETEC-257",
            "label": "Electronic Instruments and\nMeasurements Lab"
        },
        {"value": "ETCS-255", "label": "Data Structures Lab"},
        {"value": "ETEC-259", "label": "Signals and Systems Lab *"}
    ],
    'ECE (M1)(SEM-5)': [
        {
            "value": "ETHS-301",
            "label": "Communication Skills for Professionals"
        },
        {
            "value": "ETEC-303",
            "label": "Digital Communication"
        },
        {
            "value": "ETEC-305",
            "label": "Microprocessors and Microcontrollers"
        },
        {
            "value": "ETEL-307",
            "label": "Control Systems"
        },
        {
            "value": "ETEC-309",
            "label": "Digital System Design"
        },
        {
            "value": "ETMS-311",
            "label": "Industrial Management"
        },
        {
            "value": "ETHS-351",
            "label": "Communication Skills for  Professionals Lab"
        },
        {
            "value": "ETEC-351",
            "label": "Digital System Design Lab"
        },
        {
            "value": "ETEL-355",
            "label": "Control Systems Lab"
        },
        {
            "value": "ETEC-355",
            "label": "Microprocessors   and   Microcontrollers Lab"
        },
        {
            "value": "ETEC-357",
            "label": "Digital Communication Lab"
        },
        {
            "value": "ETEC-359",
            "label": "Industrial training / In-house electronics Workshop#"
        }
    ],
    'ECE (M1)(SEM-7)': [
        {"value": "ETEC-401", "label": "Embedded Systems"},
        {"value": "ETEC-403", "label": "Optoelectronics and Communication"},
        {"value": "ETEC-405", "label": "Wireless Communication"},
        {"value": "ETEC-407", "label": "Advanced DSP"},
        {"value": "ETEC-409", "label": "Introduction to MEMS"},
        {"value": "ETEC-411", "label": "Advanced VLSI Design"},
        {"value": "ETIC-403", "label": "Biomedical Instrumentation"},
        {"value": "ETEE-413", "label": "PLC and SCADA Systems"},
        {"value": "ETEE-415", "label": "Power Electronics"},
        {"value": "ETEC-417", "label": "RF Devices and Circuits"},
        {"value": "ETCS-425", "label": "Database Management System"},
        {"value": "ETEE-419", "label": "Renewable Energy Resources"},
        {"value": "ETEC-419", "label": "Radar and Navigation"},
        {"value": "ETMS-421", "label": "Project Management"},
        {"value": "ETMS-423", "label": "Economics for Engineers"},
        {"value": "ETIT-425", "label": "Grid Computing"},
        {"value": "ETCS-427", "label": "Parallel Computing"},
        {
            "value": "ETHS-419",
            "label": "Sociology and Elements of Indian History for Engineers"
        },
        {"value": "ETEC 429", "label": "Selected topics in ECE**"},
        {"value": "ETEC-451", "label": "Optical and Wireless Communication Lab"},
        {"value": "ETEC-453", "label": "Embedded System Lab"},
        {"value": "ETEC-455", "label": "Lab Based on Elective I and/or II"},
        {"value": "ETEC-457", "label": "Seminar"},
        {"value": "ETEC-459", "label": "Minor Project+"},
        {"value": "ETEC-461", "label": "Industrial Training@"}
    ],
    'ECE (E)(SEM-1)': [
        {"value": "ETMA-101", "label": "Applied Mathematics-I"},
        {"value": "ETPH-103", "label": "Applied Physics-I"},
        {"value": "ETME-105", "label": "Manufacturing Processes"},
        {"value": "ETEE-107", "label": "Electrical Technology"},
        {"value": "ETHS-109", "label": "Human Values and Professional Ethics-I#"},
        {"value": "ETCS-111", "label": "Fundamentals of Computing"},
        {"value": "ETCH-113", "label": "Applied Chemistry"},
        {"value": "ETPH-151", "label": "Applied Physics Lab-I"},
        {"value": "ETEE-153", "label": "Electrical Technology Lab"},
        {"value": "ETME-155", "label": "Workshop Practice"},
        {"value": "ETME-157", "label": "Engineering Graphics Lab"},
        {"value": "ETCS-157", "label": "Fundamentals of Computing Lab"},
        {"value": "ETCH-161", "label": "Applied Chemistry Lab"}
    ],
    'ECE (E)(SEM-3)': [
        {"value": "ETMA-201", "label": "Applied Mathematics \u2013 III"},
        {"value": "ETEC-203", "label": "Analog Electronics - I"},
        {"value": "ETEC-205", "label": "Switching Theory and Logic Design"},
        {"value": "ETEC-207", "label": "Electronic Instruments and\nMeasurements"},
        {"value": "ETCS-209", "label": "Data Structures"},
        {"value": "ETEC-211", "label": "Signals and Systems"},
        {"value": "ETEC-251", "label": "*Analog Electronics-I Lab"},
        {"value": "ETEC-253", "label": "Switching Theory and Logic Design Lab"},
        {
            "value": "ETEC-257",
            "label": "Electronic Instruments and\nMeasurements Lab"
        },
        {"value": "ETCS-255", "label": "Data Structures Lab"},
        {"value": "ETEC-259", "label": "Signals and Systems Lab *"}
    ],
    'ECE (E)(SEM-5)': [
        {
            "value": "ETHS-301",
            "label": "Communication Skills for Professionals"
        },
        {
            "value": "ETEC-303",
            "label": "Digital Communication"
        },
        {
            "value": "ETEC-305",
            "label": "Microprocessors and Microcontrollers"
        },
        {
            "value": "ETEL-307",
            "label": "Control Systems"
        },
        {
            "value": "ETEC-309",
            "label": "Digital System Design"
        },
        {
            "value": "ETMS-311",
            "label": "Industrial Management"
        },
        {
            "value": "ETHS-351",
            "label": "Communication Skills for  Professionals Lab"
        },
        {
            "value": "ETEC-351",
            "label": "Digital System Design Lab"
        },
        {
            "value": "ETEL-355",
            "label": "Control Systems Lab"
        },
        {
            "value": "ETEC-355",
            "label": "Microprocessors   and   Microcontrollers Lab"
        },
        {
            "value": "ETEC-357",
            "label": "Digital Communication Lab"
        },
        {
            "value": "ETEC-359",
            "label": "Industrial training / In-house electronics Workshop#"
        }
    ],
    'ECE (E)(SEM-7)': [
        {"value": "ETEC-401", "label": "Embedded Systems"},
        {"value": "ETEC-403", "label": "Optoelectronics and Communication"},
        {"value": "ETEC-405", "label": "Wireless Communication"},
        {"value": "ETEC-407", "label": "Advanced DSP"},
        {"value": "ETEC-409", "label": "Introduction to MEMS"},
        {"value": "ETEC-411", "label": "Advanced VLSI Design"},
        {"value": "ETIC-403", "label": "Biomedical Instrumentation"},
        {"value": "ETEE-413", "label": "PLC and SCADA Systems"},
        {"value": "ETEE-415", "label": "Power Electronics"},
        {"value": "ETEC-417", "label": "RF Devices and Circuits"},
        {"value": "ETCS-425", "label": "Database Management System"},
        {"value": "ETEE-419", "label": "Renewable Energy Resources"},
        {"value": "ETEC-419", "label": "Radar and Navigation"},
        {"value": "ETMS-421", "label": "Project Management"},
        {"value": "ETMS-423", "label": "Economics for Engineers"},
        {"value": "ETIT-425", "label": "Grid Computing"},
        {"value": "ETCS-427", "label": "Parallel Computing"},
        {
            "value": "ETHS-419",
            "label": "Sociology and Elements of Indian History for Engineers"
        },
        {"value": "ETEC 429", "label": "Selected topics in ECE**"},
        {"value": "ETEC-451", "label": "Optical and Wireless Communication Lab"},
        {"value": "ETEC-453", "label": "Embedded System Lab"},
        {"value": "ETEC-455", "label": "Lab Based on Elective I and/or II"},
        {"value": "ETEC-457", "label": "Seminar"},
        {"value": "ETEC-459", "label": "Minor Project+"},
        {"value": "ETEC-461", "label": "Industrial Training@"}
    ],
    'ECE (M2)(SEM-1)': [
        {"value": "ETMA-101", "label": "Applied Mathematics-I"},
        {"value": "ETPH-103", "label": "Applied Physics-I"},
        {"value": "ETME-105", "label": "Manufacturing Processes"},
        {"value": "ETEE-107", "label": "Electrical Technology"},
        {"value": "ETHS-109", "label": "Human Values and Professional Ethics-I#"},
        {"value": "ETCS-111", "label": "Fundamentals of Computing"},
        {"value": "ETCH-113", "label": "Applied Chemistry"},
        {"value": "ETPH-151", "label": "Applied Physics Lab-I"},
        {"value": "ETEE-153", "label": "Electrical Technology Lab"},
        {"value": "ETME-155", "label": "Workshop Practice"},
        {"value": "ETME-157", "label": "Engineering Graphics Lab"},
        {"value": "ETCS-157", "label": "Fundamentals of Computing Lab"},
        {"value": "ETCH-161", "label": "Applied Chemistry Lab"}
    ],
    'ECE (M2)(SEM-3)': [
        {"value": "ETMA-201", "label": "Applied Mathematics \u2013 III"},
        {"value": "ETEC-203", "label": "Analog Electronics - I"},
        {"value": "ETEC-205", "label": "Switching Theory and Logic Design"},
        {"value": "ETEC-207", "label": "Electronic Instruments and\nMeasurements"},
        {"value": "ETCS-209", "label": "Data Structures"},
        {"value": "ETEC-211", "label": "Signals and Systems"},
        {"value": "ETEC-251", "label": "*Analog Electronics-I Lab"},
        {"value": "ETEC-253", "label": "Switching Theory and Logic Design Lab"},
        {
            "value": "ETEC-257",
            "label": "Electronic Instruments and\nMeasurements Lab"
        },
        {"value": "ETCS-255", "label": "Data Structures Lab"},
        {"value": "ETEC-259", "label": "Signals and Systems Lab *"}
    ],
    'ECE (M2)(SEM-5)': [
        {
            "value": "ETHS-301",
            "label": "Communication Skills for Professionals"
        },
        {
            "value": "ETEC-303",
            "label": "Digital Communication"
        },
        {
            "value": "ETEC-305",
            "label": "Microprocessors and Microcontrollers"
        },
        {
            "value": "ETEL-307",
            "label": "Control Systems"
        },
        {
            "value": "ETEC-309",
            "label": "Digital System Design"
        },
        {
            "value": "ETMS-311",
            "label": "Industrial Management"
        },
        {
            "value": "ETHS-351",
            "label": "Communication Skills for  Professionals Lab"
        },
        {
            "value": "ETEC-351",
            "label": "Digital System Design Lab"
        },
        {
            "value": "ETEL-355",
            "label": "Control Systems Lab"
        },
        {
            "value": "ETEC-355",
            "label": "Microprocessors   and   Microcontrollers Lab"
        },
        {
            "value": "ETEC-357",
            "label": "Digital Communication Lab"
        },
        {
            "value": "ETEC-359",
            "label": "Industrial training / In-house electronics Workshop#"
        }
    ],
    'ECE (M2)(SEM-7)': [
        {"value": "ETEC-401", "label": "Embedded Systems"},
        {"value": "ETEC-403", "label": "Optoelectronics and Communication"},
        {"value": "ETEC-405", "label": "Wireless Communication"},
        {"value": "ETEC-407", "label": "Advanced DSP"},
        {"value": "ETEC-409", "label": "Introduction to MEMS"},
        {"value": "ETEC-411", "label": "Advanced VLSI Design"},
        {"value": "ETIC-403", "label": "Biomedical Instrumentation"},
        {"value": "ETEE-413", "label": "PLC and SCADA Systems"},
        {"value": "ETEE-415", "label": "Power Electronics"},
        {"value": "ETEC-417", "label": "RF Devices and Circuits"},
        {"value": "ETCS-425", "label": "Database Management System"},
        {"value": "ETEE-419", "label": "Renewable Energy Resources"},
        {"value": "ETEC-419", "label": "Radar and Navigation"},
        {"value": "ETMS-421", "label": "Project Management"},
        {"value": "ETMS-423", "label": "Economics for Engineers"},
        {"value": "ETIT-425", "label": "Grid Computing"},
        {"value": "ETCS-427", "label": "Parallel Computing"},
        {
            "value": "ETHS-419",
            "label": "Sociology and Elements of Indian History for Engineers"
        },
        {"value": "ETEC 429", "label": "Selected topics in ECE**"},
        {"value": "ETEC-451", "label": "Optical and Wireless Communication Lab"},
        {"value": "ETEC-453", "label": "Embedded System Lab"},
        {"value": "ETEC-455", "label": "Lab Based on Elective I and/or II"},
        {"value": "ETEC-457", "label": "Seminar"},
        {"value": "ETEC-459", "label": "Minor Project+"},
        {"value": "ETEC-461", "label": "Industrial Training@"}
    ],
    'EEE (M)(SEM-1)': [
        {
            "value": "ETMA-101",
            "label": "Applied Mathematics-I"
        },
        {
            "value": "ETPH-103",
            "label": "Applied Physics-I"
        },
        {
            "value": "ETME-105",
            "label": "Manufacturing Processes"
        },
        {
            "value": "ETEE-107",
            "label": "Electrical Technology"
        },
        {
            "value": "ETHS-109",
            "label": "Human Values and Professional Ethics-I#"
        },
        {
            "value": "ETCS-111",
            "label": "Fundamentals of Computing"
        },
        {
            "value": "ETCH-113",
            "label": "Applied Chemistry"
        },
        {
            "value": "ETPH-151",
            "label": "Applied Physics Lab-I"
        },
        {
            "value": "ETEE-153",
            "label": "Electrical Technology Lab"
        },
        {
            "value": "ETME-155",
            "label": "Workshop Practice"
        },
        {
            "value": "ETME-157",
            "label": "Engineering Graphics Lab"
        },
        {
            "value": "ETCS-157",
            "label": "Fundamentals of Computing Lab"
        },
        {
            "value": "ETCH-161",
            "label": "Applied Chemistry Lab"
        }
    ],
    'EEE (M)(SEM-3)': [
        {
            "value": "ETMA-201",
            "label": "Applied Mathematics \u2013 III"
        },
        {
            "value": "ETEC-203",
            "label": "Analog Electronics-I"
        },
        {
            "value": "ETEE-205",
            "label": "Materials in Electrical Systems"
        },
        {
            "value": "ETEE-207",
            "label": "Circuits and Systems"
        },
        {
            "value": "ETCS-209",
            "label": "Data Structures"
        },
        {
            "value": "ETEE-211",
            "label": "Electrical Machines-I"
        },
        {
            "value": "ETEC-251",
            "label": "Analog Electronics \u2013 I Lab"
        },
        {
            "value": "ETEE-253",
            "label": "Electrical Machines-I Lab"
        },
        {
            "value": "ETCS-255",
            "label": "Data Structures Lab."
        },
        {
            "value": "ETEE-257",
            "label": "Circuits and Systems Lab"
        },
        {
            "value": "ETEE-259",
            "label": "Scientific Computing Lab"
        }
    ],
    'EEE (M)(SEM-5)': [
        {
            "value": "ETHS 301",
            "label": "Communication Skills for Professionals"
        },
        {"value": "ETEE-303", "label": "Power Electronics"},
        {"value": "ETEE 305", "label": "Sensors and Transducers"},
        {"value": "ETEE 307", "label": "Switching Theory and Logic Design"},
        {"value": "ETEE 309", "label": "Communication Systems"},
        {"value": "ETMS 311", "label": "Industrial Management"},
        {"value": "ETEE 351", "label": "Sensors and Transducers Lab"},
        {"value": "ETEE 353", "label": "Power Electronics Lab"},
        {"value": "ETEE 355", "label": "Switching Theory and Logic Design Lab"},
        {"value": "ETEE 357", "label": "Communication Systems Lab"},
        {"value": "ETEE 359", "label": "Electrical and Electronic Workshop"},
        {
            "value": "ETHS 351",
            "label": "Communication Skills for Professionals Lab"
        }
    ],
    'EEE (M)(SEM-7)': [
        {"value": "ETEE 401", "label": "Electrical Drives"},
        {"value": "ETEE 403", "label": "Advanced Control Systems"},
        {"value": "ETEE 405", "label": "EHV AC and HVDC Transmissions"},
        {"value": "ETEE 419", "label": "Renewable Energy Resources"},
        {"value": "ETEE 409", "label": "Power Distribution System"},
        {"value": "ETEE 411", "label": "Telemetry and Data Acquisition Systems"},
        {"value": "ETEE 413", "label": "PLC and SCADA Systems"},
        {"value": "ETAT 403", "label": "Mechatronics"},
        {"value": "ETEE 417", "label": "High Voltage Engineering"},
        {"value": "ETEE 421", "label": "Selected topics in EEE"},
        {"value": "ETEC-403", "label": "Optoelectronics and Optical Communication"},
        {"value": "ETCS 425", "label": "Database Management Systems"},
        {"value": "ETIC 403", "label": "Biomedical Instrumentation"},
        {"value": "ETEC 427", "label": "Digital System Design"},
        {"value": "ETEE 431", "label": "Power line Carrier Communication"},
        {"value": "ETEL 405", "label": "Electrical Machines Design"},
        {
            "value": "ETHS 419",
            "label": "Sociology and Elements of Indian History for Engineers"
        },
        {"value": "ETEE-451", "label": "Electrical Drives Lab"},
        {"value": "ETEE-453", "label": "Advanced Control Systems Lab"},
        {"value": "ETEE-455", "label": "Practical Based on Electives Group A or B"},
        {"value": "ETEE-457", "label": "Seminar"},
        {"value": "ETEE-459", "label": "Minor Project+"},
        {"value": "ETEE-461", "label": "Industrial Training"}
    ],
    'ICE (M)(SEM-1)': [
        {"value": "ETMA - 101", "label": "Applied Mathematics - I"},
        {"value": "ETPH - 103", "label": "Applied Physics - I"},
        {"value": "ETME - 105", "label": "Manufacturing Processes"},
        {"value": "ETEE - 107", "label": "Electrical Technology"},
        {
            "value": "ETHS - 109",
            "label": "Human Values and Professional Ethics - 1"
        },
        {"value": "ETCS - 111", "label": "Fundamentals of Computing"},
        {"value": "ETCH - 113", "label": "Applied Chemistry"},
        {"value": "ETPH - 151", "label": "Applied Physics Lab - I"},
        {"value": "ETEE - 153", "label": " Electrical Technology Lab"},
        {"value": "ETME - 155", "label": "Workshop Practice"},
        {"value": "ETME - 157", "label": "Enginnering Graphics lab"},
        {"value": "ETCS - 157", "label": "Fundamentals of Computing Lab"},
        {"value": "ETCH - 161", "label": "Applied Chemistry lab"}
    ],
    'ICE (M)(SEM-3)': [
        {
            "value": "ETMA - 201",
            "label": "Applied Mathematics - III"
        },
        {
            "value": "ETIC - 203",
            "label": "Sensors and Transducers"
        },
        {
            "value": "ETEC - 205",
            "label": "Switching Theory and Logics Design"
        },
        {
            "value": "ETEE - 207",
            "label": "Circuits and Systems"
        },
        {
            "value": "ETCS - 209",
            "label": "Data Structures"
        },
        {
            "value": "ETIC - 211",
            "label": "Basics of Measurements"
        },
        {
            "value": "ETIC - 251",
            "label": "Sensors and Transducers Lab"
        },
        {
            "value": "ETEC - 251",
            "label": "Switching Theory and Logics Design Lab"
        },
        {
            "value": "ETCS - 255",
            "label": "Data Structures Lab"
        },
        {
            "value": "ETEE - 257",
            "label": "Circuits and Systems Lab"
        }
    ],
    'ICE (M)(SEM-5)': [
        {
            "value": "ETHS - 301",
            "label": "Communication Skills for Professionals"
        },
        {
            "value": "ETIC - 303",
            "label": "Industrial Instrumentation"
        },
        {
            "value": "ETEC - 305",
            "label": "Microprocessors and Microcontrollers"
        },
        {
            "value": "ETEC - 309",
            "label": "Digital System Design "
        },
        {
            "value": "ETIC - 309",
            "label": "Object Oriented Programming using  JAVA"
        },
        {
            "value": "ETMS - 311",
            "label": "Industrial Management"
        },
        {
            "value": "ETHS - 351",
            "label": "communication Skills for Professionals Lab"
        },
        {
            "value": "ETIC - 353",
            "label": "Industrial instrumentation Lab"
        },
        {
            "value": "ETEC - 355",
            "label": "Microprocessors and Microcontrollers Lab"
        },
        {
            "value": "ETEC - 351",
            "label": "Digital System Design Lab"
        },
        {
            "value": "ETIC -357",
            "label": "Object Oriented Programming using  JAVA Lab"
        },
        {
            "value": " ",
            "label": "Industrial training / In - house Instrumentation Workshop#*"
        }
    ],
    'ICE (M)(SEM-7)': [
        {
            "value": "ETIC - 401",
            "label": "Digital Control Systems"
        },
        {
            "value": "ETIC - 403",
            "label": "Biomedical Instrumentation"
        },
        {
            "value": "ETIC - 405",
            "label": "Artificial Neural Networks"
        },
        {
            "value": "ETIC - 407",
            "label": "Industrial Automation and Control"
        },
        {
            "value": "ETAT - 403",
            "label": "Mechatronics"
        },
        {
            "value": "ETEE - 401",
            "label": "Electrical Drives"
        },
        {
            "value": "ETIC - 413",
            "label": "Instrumentation Diagnostics"
        },
        {
            "value": "ETMT - 415",
            "label": "Process Modeling and Optimization Techniques"
        },
        {
            "value": "ETCS - 425",
            "label": "Database Management Systems"
        },
        {
            "value": "ETEE - 419",
            "label": "Renewable Energy Resources"
        },
        {
            "value": "ETIC - 417",
            "label": "Selected Topics in ICE**"
        },
        {
            "value": "ETIC - 419",
            "label": "Engineering Materials"
        },
        {
            "value": "ETIC - 421",
            "label": "Computer Architecture"
        },
        {
            "value": "ETIC - 423",
            "label": "Software Engineering"
        },
        {
            "value": "ETIC - 427",
            "label": "Operating Systems"
        },
        {
            "value": "ETHS - 419",
            "label": "Sociology and Elements of Indian History for Engineers"
        },
        {
            "value": "ETIC - 451",
            "label": "Digital Control Systems Lab"
        },
        {
            "value": "ETIC - 453",
            "label": "Biomedical Instrumentation Lab"
        },
        {
            "value": "ETIC - 455",
            "label": "Seminar(topic should be linked to industrial training/Soft Skills learnt) #"
        },
        {
            "value": "ETIC - 461",
            "label": "Lab based on Electives Group A or B"
        },
        {
            "value": "ETIC - 457",
            "label": "Minor Project +"
        },
        {
            "value": "ETIC - 459",
            "label": "Industrial Training@"
        }
    ]
}


fingerPrintCode = {
    "001": "aniket965.as@gmail.com",
    "002": "ujjwalupadhyay8@gmail.com",
    "003": "manojs11@gmail.com",
    "004": "oberoivansh01@gmail.com",
    "005": "mohit.tiwari@bharatividyapeeth.edu"
}
