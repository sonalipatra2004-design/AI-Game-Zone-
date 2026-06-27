import streamlit as st
import random

st.set_page_config(page_title="AI Game Zone", page_icon="🎮", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&family=JetBrains+Mono:wght@500&display=swap');
*,html,body,[class*="css"]{font-family:'Nunito',sans-serif;box-sizing:border-box;}
.stApp{background:linear-gradient(160deg,#0a1628 0%,#0d2137 45%,#0a1f35 100%);min-height:100vh;}
.stApp::before{content:'';position:fixed;top:-120px;left:-120px;width:480px;height:480px;background:radial-gradient(circle,rgba(13,180,185,0.12) 0%,transparent 70%);border-radius:50%;pointer-events:none;z-index:0;}
.stApp::after{content:'';position:fixed;bottom:-100px;right:-100px;width:400px;height:400px;background:radial-gradient(circle,rgba(56,189,248,0.10) 0%,transparent 70%);border-radius:50%;pointer-events:none;z-index:0;}
.game-header{text-align:center;padding:2.2rem 0 0.5rem;position:relative;z-index:1;}
.game-title{font-size:2.8rem;font-weight:800;background:linear-gradient(90deg,#0db4b9,#38bdf8,#6ee7b7);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin:0;filter:drop-shadow(0 2px 12px rgba(13,180,185,0.35));}
.game-subtitle{color:#6cb8be;font-size:0.88rem;margin-top:0.25rem;font-family:'JetBrains Mono',monospace;letter-spacing:1px;}
.mode-card{background:rgba(10,28,50,0.55);border:1px solid rgba(13,180,185,0.15);border-radius:18px;padding:1.8rem 1rem;text-align:center;backdrop-filter:blur(12px);box-shadow:0 6px 24px rgba(0,0,0,0.3);transition:all 0.28s ease;margin-bottom:0.5rem;position:relative;overflow:hidden;}
.mode-card:hover{background:rgba(13,180,185,0.1);border-color:rgba(13,180,185,0.35);transform:translateY(-4px);}
.mode-icon{font-size:2.6rem;margin-bottom:0.6rem;display:block;}
.mode-name{color:#e0f4f4;font-size:1.1rem;font-weight:800;margin:0 0 0.3rem;}
.mode-desc{color:#6cb8be;font-size:0.82rem;line-height:1.5;margin:0;}
.score-badge{display:inline-flex;align-items:center;gap:0.4rem;background:rgba(13,180,185,0.12);border:1px solid rgba(13,180,185,0.3);color:#6ee7b7;padding:0.35rem 1rem;border-radius:50px;font-weight:700;font-family:'JetBrains Mono',monospace;font-size:0.9rem;}
.question-box{background:rgba(10,22,40,0.7);border-left:3px solid #0db4b9;border-radius:0 14px 14px 0;padding:1.2rem 1.4rem;color:#d4eef0;font-size:1.05rem;line-height:1.75;margin:1rem 0;}
.img-card{background:rgba(10,22,40,0.8);border:1px solid rgba(13,180,185,0.2);border-radius:16px;padding:2.5rem 1rem 1rem;text-align:center;margin-bottom:1rem;}
.img-emoji{font-size:6rem;line-height:1.1;display:block;filter:drop-shadow(0 4px 16px rgba(13,180,185,0.2));}
.img-label-tag{color:#0db4b9;font-size:0.72rem;font-family:'JetBrains Mono',monospace;letter-spacing:2px;text-transform:uppercase;margin-top:0.8rem;display:block;}
.answer-box{background:rgba(110,231,183,0.07);border:1px solid rgba(110,231,183,0.3);border-radius:14px;padding:1rem 1.4rem;color:#6ee7b7;margin-top:1rem;}
.wrong-box{background:rgba(251,113,133,0.07);border:1px solid rgba(251,113,133,0.3);border-radius:14px;padding:1rem 1.4rem;color:#fda4af;margin-top:1rem;}
.hint-box{background:rgba(251,191,36,0.06);border:1px solid rgba(251,191,36,0.25);border-radius:14px;padding:0.9rem 1.2rem;color:#fcd34d;font-size:0.92rem;margin-top:0.8rem;}
.section-label{color:#0db4b9;font-family:'JetBrains Mono',monospace;font-size:0.75rem;text-transform:uppercase;letter-spacing:2.5px;margin-bottom:0.6rem;display:block;}
.progress-bg{background:rgba(13,180,185,0.1);border-radius:50px;height:8px;margin:0.5rem 0 1rem;border:1px solid rgba(13,180,185,0.2);}
.progress-fill{background:linear-gradient(90deg,#0db4b9,#38bdf8);border-radius:50px;height:100%;}
div[data-testid="stButton"]>button{background:linear-gradient(135deg,rgba(13,180,185,0.18),rgba(56,189,248,0.12))!important;border:1px solid rgba(13,180,185,0.35)!important;border-radius:12px!important;color:#e0f4f4!important;font-family:'Nunito',sans-serif!important;font-weight:700!important;font-size:0.95rem!important;padding:0.55rem 1rem!important;transition:all 0.22s ease!important;}
div[data-testid="stButton"]>button:hover{background:linear-gradient(135deg,rgba(13,180,185,0.32),rgba(56,189,248,0.22))!important;border-color:rgba(13,180,185,0.6)!important;transform:translateY(-2px)!important;color:#6ee7b7!important;}
.stTextInput>div>div>input{background:rgba(10,28,50,0.6)!important;border:1px solid rgba(13,180,185,0.2)!important;border-radius:12px!important;color:#d4eef0!important;font-family:'Nunito',sans-serif!important;}
.stRadio>div{gap:0.6rem;}
.stRadio label{background:rgba(10,28,50,0.5)!important;border:1px solid rgba(13,180,185,0.15)!important;border-radius:10px!important;padding:0.5rem 0.8rem!important;color:#c8e8ea!important;transition:all 0.2s!important;}
.stRadio label:hover{background:rgba(13,180,185,0.1)!important;border-color:rgba(13,180,185,0.35)!important;}
hr{border:none!important;height:1px!important;background:linear-gradient(90deg,transparent,rgba(13,180,185,0.3),transparent)!important;margin:1.2rem 0!important;}
.stAlert{background:rgba(13,180,185,0.07)!important;border:1px solid rgba(13,180,185,0.2)!important;border-radius:12px!important;color:#94c9cc!important;}
::-webkit-scrollbar{width:6px;}
::-webkit-scrollbar-track{background:#0a1628;}
::-webkit-scrollbar-thumb{background:rgba(13,180,185,0.3);border-radius:3px;}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════
# IMAGE QUIZ DATA — emoji + questions about it
# ═══════════════════════════════════════════
IMAGE_QUIZ_DATA = [
    {"emoji":"🦁","label":"LION","questions":[
        {"q":"What is a group of lions called?","correct":"A pride","options":["A pride","A pack","A herd","A colony"]},
        {"q":"In which continent do most wild lions live?","correct":"Africa","options":["Africa","Asia","South America","Australia"]},
        {"q":"Which unique feature do male lions have?","correct":"A mane","options":["A mane","Stripes","Spots","Whiskers"]},
    ]},
    {"emoji":"🐘","label":"ELEPHANT","questions":[
        {"q":"What is the gestation period of an elephant?","correct":"22 months","options":["22 months","9 months","12 months","36 months"]},
        {"q":"Which is the largest species of elephant?","correct":"African bush elephant","options":["African bush elephant","Asian elephant","African forest elephant","Indian elephant"]},
        {"q":"What do elephants use their trunks for?","correct":"Breathing, smelling, drinking & lifting","options":["Breathing, smelling, drinking & lifting","Only for lifting","Only for drinking","Only for smelling"]},
    ]},
    {"emoji":"🌋","label":"VOLCANO","questions":[
        {"q":"What is molten rock called INSIDE a volcano?","correct":"Magma","options":["Magma","Lava","Pumice","Basalt"]},
        {"q":"Which country has the most active volcanoes?","correct":"Indonesia","options":["Indonesia","Japan","USA","Italy"]},
        {"q":"What type of rock forms when lava cools?","correct":"Igneous rock","options":["Igneous rock","Sedimentary rock","Metamorphic rock","Limestone"]},
    ]},
    {"emoji":"🚀","label":"ROCKET","questions":[
        {"q":"Who was the first human to travel to space?","correct":"Yuri Gagarin","options":["Yuri Gagarin","Neil Armstrong","Buzz Aldrin","Alan Shepard"]},
        {"q":"In which year did humans first land on the Moon?","correct":"1969","options":["1969","1972","1965","1981"]},
        {"q":"What fuel do most modern rockets use?","correct":"Liquid hydrogen & liquid oxygen","options":["Liquid hydrogen & liquid oxygen","Petrol & diesel","Coal & steam","Solar energy"]},
    ]},
    {"emoji":"🌊","label":"OCEAN WAVE","questions":[
        {"q":"What percentage of Earth's surface is covered by ocean?","correct":"71%","options":["71%","50%","85%","60%"]},
        {"q":"What primarily causes ocean tides?","correct":"Moon's gravitational pull","options":["Moon's gravitational pull","Wind patterns","Earth's rotation","Ocean currents"]},
        {"q":"What is the deepest point in the ocean?","correct":"Mariana Trench","options":["Mariana Trench","Pacific Rift","Atlantic Deep","Indian Trench"]},
    ]},
    {"emoji":"🦋","label":"BUTTERFLY","questions":[
        {"q":"What is the stage between caterpillar and butterfly?","correct":"Chrysalis (pupa)","options":["Chrysalis (pupa)","Larvae","Nymph","Egg"]},
        {"q":"How do butterflies taste their food?","correct":"Through their feet","options":["Through their feet","Through antennae","Through their tongue","Through eyes"]},
        {"q":"What is the study of butterflies & moths called?","correct":"Lepidopterology","options":["Lepidopterology","Entomology","Zoology","Ornithology"]},
    ]},
    {"emoji":"🏔️","label":"MOUNTAIN","questions":[
        {"q":"What is the highest mountain in the world?","correct":"Mount Everest","options":["Mount Everest","K2","Kangchenjunga","Mont Blanc"]},
        {"q":"The Himalayas were formed by which process?","correct":"Collision of tectonic plates","options":["Collision of tectonic plates","Volcanic eruptions","Glacial movement","River erosion"]},
        {"q":"On which border is Mount Everest located?","correct":"Nepal and Tibet (China)","options":["Nepal and Tibet (China)","India and Nepal","Bhutan and China","Pakistan and India"]},
    ]},
    {"emoji":"🌍","label":"EARTH","questions":[
        {"q":"How long does Earth take to complete one full rotation?","correct":"24 hours","options":["24 hours","12 hours","365 days","6 hours"]},
        {"q":"What is Earth's only natural satellite?","correct":"The Moon","options":["The Moon","Phobos","Europa","Titan"]},
        {"q":"Which layer of Earth generates the magnetic field?","correct":"Outer core (liquid iron)","options":["Outer core (liquid iron)","Mantle","Crust","Inner core"]},
    ]},
    {"emoji":"🧬","label":"DNA","questions":[
        {"q":"What does DNA stand for?","correct":"Deoxyribonucleic Acid","options":["Deoxyribonucleic Acid","Deoxyribose Nucleic Acid","Double Nucleic Arrangement","Dextrose Nucleotide Acid"]},
        {"q":"Who discovered the double helix structure of DNA?","correct":"Watson and Crick (1953)","options":["Watson and Crick (1953)","Gregor Mendel","Louis Pasteur","Charles Darwin"]},
        {"q":"Approximately how many base pairs does human DNA have?","correct":"3 billion","options":["3 billion","1 million","500 million","10 billion"]},
    ]},
    {"emoji":"🌞","label":"THE SUN","questions":[
        {"q":"How long does sunlight take to reach Earth?","correct":"About 8 minutes","options":["About 8 minutes","About 1 second","About 1 hour","About 24 hours"]},
        {"q":"What type of star is our Sun?","correct":"Yellow dwarf (G-type)","options":["Yellow dwarf (G-type)","Red giant","White dwarf","Blue supergiant"]},
        {"q":"What is the approximate surface temperature of the Sun?","correct":"5,500°C","options":["5,500°C","1,000°C","50,000°C","500°C"]},
    ]},
    {"emoji":"🦅","label":"EAGLE","questions":[
        {"q":"The Bald Eagle is the national bird of which country?","correct":"United States of America","options":["United States of America","Canada","Mexico","Australia"]},
        {"q":"How far can an eagle see clearly?","correct":"Up to 3 km","options":["Up to 3 km","Up to 100 m","Up to 500 m","Up to 10 km"]},
        {"q":"Eagles belong to which bird family?","correct":"Accipitridae","options":["Accipitridae","Falconidae","Strigidae","Corvidae"]},
    ]},
    {"emoji":"💻","label":"COMPUTER","questions":[
        {"q":"Who is credited as the father of modern computing?","correct":"Alan Turing","options":["Alan Turing","Bill Gates","Steve Jobs","Charles Babbage"]},
        {"q":"What does CPU stand for?","correct":"Central Processing Unit","options":["Central Processing Unit","Computer Power Unit","Core Processing Utility","Central Power Upgrade"]},
        {"q":"Which language is known as the primary language of the web frontend?","correct":"JavaScript","options":["JavaScript","Python","C++","Java"]},
    ]},
    {"emoji":"🎵","label":"MUSIC","questions":[
        {"q":"How many strings does a standard guitar have?","correct":"6","options":["6","4","8","12"]},
        {"q":"Who composed the famous 'Für Elise'?","correct":"Beethoven","options":["Beethoven","Mozart","Bach","Schubert"]},
        {"q":"What is the speed/pace of a piece of music called?","correct":"Tempo","options":["Tempo","Pitch","Rhythm","Timbre"]},
    ]},
    {"emoji":"🧪","label":"SCIENCE LAB","questions":[
        {"q":"What is the chemical formula of water?","correct":"H₂O","options":["H₂O","CO₂","NaCl","O₂"]},
        {"q":"Who proposed the theory of general relativity?","correct":"Albert Einstein","options":["Albert Einstein","Isaac Newton","Niels Bohr","Galileo"]},
        {"q":"What is the most abundant gas in Earth's atmosphere?","correct":"Nitrogen (78%)","options":["Nitrogen (78%)","Oxygen (21%)","Carbon dioxide","Argon"]},
    ]},
    {"emoji":"🏰","label":"CASTLE","questions":[
        {"q":"Which famous castle is on the River Thames in London?","correct":"Tower of London","options":["Tower of London","Windsor Castle","Edinburgh Castle","Buckingham Palace"]},
        {"q":"Neuschwanstein Castle (which inspired Disney) is in which country?","correct":"Germany","options":["Germany","France","Austria","Switzerland"]},
        {"q":"The Palace of Versailles was home to which French king?","correct":"Louis XIV","options":["Louis XIV","Napoleon","Louis XVI","Henry IV"]},
    ]},
    {"emoji":"🦖","label":"DINOSAUR","questions":[
        {"q":"When did dinosaurs go extinct?","correct":"About 66 million years ago","options":["About 66 million years ago","About 10 million years ago","About 200 million years ago","About 1 million years ago"]},
        {"q":"Which was the largest carnivorous dinosaur?","correct":"Spinosaurus","options":["Spinosaurus","T-Rex","Velociraptor","Allosaurus"]},
        {"q":"In evolutionary terms, what are birds?","correct":"Living descendants of dinosaurs","options":["Living descendants of dinosaurs","Unrelated to dinosaurs","Evolved separately from reptiles","Descended from pterosaurs"]},
    ]},
    {"emoji":"🌈","label":"RAINBOW","questions":[
        {"q":"How many colours are in a standard rainbow?","correct":"7","options":["7","5","6","8"]},
        {"q":"What causes a rainbow to form?","correct":"Refraction of sunlight in water droplets","options":["Refraction of sunlight in water droplets","Sunlight hitting clouds","Light through ice crystals","Dust scattering light"]},
        {"q":"Which colour is always on the OUTER (top) arc of a rainbow?","correct":"Red","options":["Red","Violet","Blue","Yellow"]},
    ]},
    {"emoji":"🤖","label":"AI / ROBOT","questions":[
        {"q":"Who coined the term 'Artificial Intelligence' in 1956?","correct":"John McCarthy","options":["John McCarthy","Alan Turing","Marvin Minsky","Claude Shannon"]},
        {"q":"What does 'ML' stand for in technology?","correct":"Machine Learning","options":["Machine Learning","Mechanical Logic","Memory Loop","Module Language"]},
        {"q":"Which test determines whether a machine can behave like a human?","correct":"Turing Test","options":["Turing Test","Einstein Test","Logic Test","Cognitive Test"]},
    ]},
    {"emoji":"🐠","label":"TROPICAL FISH","questions":[
        {"q":"Fish breathe underwater using which organ?","correct":"Gills","options":["Gills","Lungs","Skin pores","Fins"]},
        {"q":"What is the largest fish in the ocean?","correct":"Whale shark","options":["Whale shark","Great white shark","Blue whale","Giant oarfish"]},
        {"q":"What is a group of fish called?","correct":"A school","options":["A school","A flock","A herd","A swarm"]},
    ]},
    {"emoji":"🏛️","label":"ANCIENT MONUMENT","questions":[
        {"q":"The Parthenon temple is located in which city?","correct":"Athens, Greece","options":["Athens, Greece","Rome, Italy","Cairo, Egypt","Istanbul, Turkey"]},
        {"q":"Which civilisation built Machu Picchu?","correct":"Inca civilisation","options":["Inca civilisation","Aztec civilisation","Maya civilisation","Olmec civilisation"]},
        {"q":"The Colosseum in Rome was primarily used for?","correct":"Gladiatorial contests","options":["Gladiatorial contests","Royal ceremonies","Religious worship","Political debates"]},
    ]},
]

# ═══════════════════════════════════════════
# RIDDLE BANK
# ═══════════════════════════════════════════
RIDDLE_BANK = {
    "Science":[
        {"riddle":"I have no mass yet I bend light and travel at the universe's speed limit. What am I?","answer":"light","hint":"I come from the Sun and make plants grow."},
        {"riddle":"I am the smallest unit of matter retaining an element's properties. Split me and release enormous energy. What am I?","answer":"atom","hint":"Everything physical is made of me."},
        {"riddle":"I keep planets in orbit and apples falling from trees. I work at a distance. What am I?","answer":"gravity","hint":"Newton discovered me from a falling apple."},
        {"riddle":"I am two hydrogen atoms bonded to one oxygen. I cover 71% of Earth. What am I?","answer":"water","hint":"You drink me every day."},
        {"riddle":"I am the powerhouse of the cell, producing ATP energy currency. What am I?","answer":"mitochondria","hint":"Every biology student knows my famous nickname."},
        {"riddle":"I am the process by which plants turn sunlight into sugar. What am I?","answer":"photosynthesis","hint":"Chlorophyll is my green pigment."},
        {"riddle":"I am negatively charged and orbit the nucleus. I flow through wires as electricity. What am I?","answer":"electron","hint":"Remove me and the atom becomes positive."},
        {"riddle":"I am the backbone of all organic molecules, bonding with four others simultaneously. What element am I?","answer":"carbon","hint":"Diamonds and graphite are both forms of me."},
        {"riddle":"I am when a solid becomes gas without passing through liquid. Dry ice does this. What am I?","answer":"sublimation","hint":"Dry ice appears to smoke because of me."},
        {"riddle":"I flow from hot to cold, never the reverse on my own. I measure molecular motion. What am I?","answer":"heat","hint":"You feel me when you touch a hot stove."},
    ],
    "Nature":[
        {"riddle":"I am the tallest living organism on Earth, over 100 metres tall. My rings tell my age. What am I?","answer":"tree","hint":"I provide oxygen and shelter for many creatures."},
        {"riddle":"I travel thousands of km without a map, returning to my birth river. What am I?","answer":"salmon","hint":"Bears wait for me at waterfalls in autumn."},
        {"riddle":"I am the only mammal capable of true flight. I navigate in darkness by echo. What am I?","answer":"bat","hint":"I sleep upside-down and eat insects at night."},
        {"riddle":"I am water vapour that freezes on cold surfaces at night. Farmers fear me in spring. What am I?","answer":"frost","hint":"I paint white patterns on windowpanes."},
        {"riddle":"I am the largest living structure on Earth, visible from space, built by coral polyps. What am I?","answer":"great barrier reef","hint":"I am in Australia."},
        {"riddle":"I have no bones, brain, or eyes yet I navigate a maze to find food. What am I?","answer":"slime mould","hint":"I am not a plant, animal, or fungus — I am a protist."},
        {"riddle":"I make up 78% of Earth's atmosphere but plants cannot use me directly from air. What am I?","answer":"nitrogen","hint":"Legumes host bacteria that convert me into usable form."},
        {"riddle":"I carry my home on my back and move famously slowly. I can live over 150 years. What am I?","answer":"tortoise","hint":"The hare famously underestimated me."},
        {"riddle":"I can regrow a lost limb and never fully metamorphose. I live in Mexican rivers. What am I?","answer":"axolotl","hint":"I am a type of salamander."},
        {"riddle":"I am born in fire, shaped by wind and water, holding Earth's history in my layers. What am I?","answer":"rock","hint":"Geologists read history from my strata."},
    ],
    "Technology":[
        {"riddle":"I am the brain of a computer, performing billions of calculations per second. What am I?","answer":"cpu","hint":"I am measured in GHz and sit on the motherboard."},
        {"riddle":"I store data permanently even when power is off, replacing spinning magnetic disks. What am I?","answer":"ssd","hint":"My acronym: Solid State Drive."},
        {"riddle":"I am a programming concept where a function calls itself. What am I?","answer":"recursion","hint":"To understand me, you must first understand me."},
        {"riddle":"I convert readable data into unreadable format using a key. Banks use me. What am I?","answer":"encryption","hint":"HTTPS uses me to protect browsing."},
        {"riddle":"I allow devices to communicate wirelessly at 2.4 or 5 GHz. What am I?","answer":"wifi","hint":"Your router broadcasts me throughout your home."},
        {"riddle":"I follow last-in-first-out order. The undo function uses me. What data structure am I?","answer":"stack","hint":"Think of a stack of plates."},
        {"riddle":"I cracked the Enigma code and am called the father of computer science. Who am I?","answer":"alan turing","hint":"A famous AI test bears my name."},
        {"riddle":"I am a flaw in software that attackers exploit. Security researchers hunt for me. What am I?","answer":"vulnerability","hint":"Patches and updates fix me."},
        {"riddle":"I am a set of rules computers use to communicate over networks. What am I?","answer":"protocol","hint":"TCP/IP is my most famous example."},
        {"riddle":"I am the theoretical foundation of modern computers, conceived by a mathematician in 1936. What am I?","answer":"turing machine","hint":"I have an infinite tape, a read/write head, and a state table."},
    ],
    "History":[
        {"riddle":"I was the first empire stretching from Europe to Asia. My king never lost a battle. Who am I?","answer":"alexander the great","hint":"My empire reached from Greece to India."},
        {"riddle":"Signed in 1215, I limited the English king's power and laid foundations for democracy. What am I?","answer":"magna carta","hint":"King John signed me under pressure from barons."},
        {"riddle":"I led the 388 km Salt March to protest British rule through nonviolence. Who am I?","answer":"mahatma gandhi","hint":"I became the symbol of Indian independence."},
        {"riddle":"I was built in 20 years by 100,000 workers as a pharaoh's tomb. What am I?","answer":"great pyramid of giza","hint":"I am the only ancient wonder still standing."},
        {"riddle":"I was fought 1914–1918 and called 'the war to end all wars'. What am I?","answer":"world war one","hint":"It started with Archduke Franz Ferdinand's assassination."},
        {"riddle":"I was the first woman to win a Nobel Prize — twice, in two different sciences. Who am I?","answer":"marie curie","hint":"I discovered polonium and radium."},
        {"riddle":"I am the ancient trade network connecting China to the Mediterranean. What am I?","answer":"silk road","hint":"Marco Polo travelled parts of me."},
        {"riddle":"I divided a European city for 28 years before falling in 1989. What am I?","answer":"berlin wall","hint":"My fall symbolised the end of the Cold War."},
        {"riddle":"I built Machu Picchu high in the Andes Mountains. Who am I?","answer":"inca","hint":"Spanish conquistadors conquered me in the 16th century."},
        {"riddle":"I ended European colonial rule across Africa and Asia in the mid-20th century. What am I?","answer":"decolonisation","hint":"Many nations gained independence in the 1940s–1960s."},
    ],
    "Mathematics":[
        {"riddle":"I am the ratio of a circle's circumference to its diameter, irrational and never-ending. What am I?","answer":"pi","hint":"I am approximately 3.14159..."},
        {"riddle":"I am the only number that is neither prime nor composite. What am I?","answer":"zero","hint":"I was invented in India and revolutionised maths."},
        {"riddle":"I am the sequence 0,1,1,2,3,5,8,13... each being the sum of the two before. What am I?","answer":"fibonacci sequence","hint":"I appear in sunflower seeds and nautilus shells."},
        {"riddle":"I am a number with exactly two factors: 1 and itself. Examples: 2,3,5,7,11. What am I?","answer":"prime number","hint":"Every integer is either me or a product of me."},
        {"riddle":"I am the inverse of exponentiation — what power gives you this number? What am I?","answer":"logarithm","hint":"The Richter scale and decibels use me."},
        {"riddle":"I deal with rates of change and areas under curves. Newton and Leibniz invented me. What am I?","answer":"calculus","hint":"I have differential and integral branches."},
        {"riddle":"I am the longest side of a right triangle, always opposite the right angle. What am I?","answer":"hypotenuse","hint":"In a²+b²=c², I am c."},
        {"riddle":"I am found by adding all numbers and dividing by the count. What average am I?","answer":"mean","hint":"Median and mode are my fellow central tendencies."},
        {"riddle":"I am a shape with three sides whose internal angles sum to 180°. What am I?","answer":"triangle","hint":"Pythagoras' theorem is about my right-angled form."},
        {"riddle":"I am the branch of maths studying shapes, sizes, and positions in space. Euclid wrote about me. What am I?","answer":"geometry","hint":"Circles, triangles and squares are my subjects."},
    ],
    "Animals":[
        {"riddle":"I am the largest animal ever to live on Earth. I sing low-frequency songs. What am I?","answer":"blue whale","hint":"I am a mammal that lives entirely in the ocean."},
        {"riddle":"I can change my colour in under a second. I have three hearts and blue blood. What am I?","answer":"octopus","hint":"I have eight arms and no skeleton."},
        {"riddle":"I am the fastest land animal, reaching 120 km/h. I cannot roar, only purr. What am I?","answer":"cheetah","hint":"I have solid spots, not rings like a leopard."},
        {"riddle":"I sleep for six months without eating and emerge in spring very hungry. What am I?","answer":"bear","hint":"My winter sleep is called hibernation."},
        {"riddle":"I am a bird that cannot fly but am an excellent swimmer in the Southern Hemisphere. What am I?","answer":"penguin","hint":"I am famous for my black and white colouring."},
        {"riddle":"I am a marsupial that carries young in a pouch and is Australia's national symbol. What am I?","answer":"kangaroo","hint":"I travel by hopping and have a powerful tail."},
        {"riddle":"I am the only mammal with a full coat of scales. I roll into a ball when threatened. What am I?","answer":"pangolin","hint":"My scales are made of keratin like human fingernails."},
        {"riddle":"I undergo complete metamorphosis from caterpillar to winged beauty. What am I?","answer":"butterfly","hint":"I emerge from a chrysalis."},
        {"riddle":"I build elaborate dams to flood forests and create ponds. My flat tail is my signature. What am I?","answer":"beaver","hint":"I am nature's engineer."},
        {"riddle":"I spend most of my life underground, am nearly blind, and dig tunnels. Gardeners consider me a pest. What am I?","answer":"mole","hint":"The phrase 'blind as a mole' refers to me."},
    ],
    "Space":[
        {"riddle":"I am the closest star to Earth. Without me, life here would not exist. What am I?","answer":"the sun","hint":"I am a medium-sized yellow dwarf star."},
        {"riddle":"I am so strong that not even light can escape me. I form when massive stars collapse. What am I?","answer":"black hole","hint":"Hawking theorised I slowly emit radiation."},
        {"riddle":"I am the galaxy containing our Solar System. My band is visible on clear dark nights. What am I?","answer":"milky way","hint":"My name comes from the Latin 'via lactea'."},
        {"riddle":"I was the first human to walk on the Moon on 20 July 1969. Who am I?","answer":"neil armstrong","hint":"I said 'one small step for man...'"},
        {"riddle":"I am the largest planet in our Solar System, a gas giant with a storm lasting 350+ years. What am I?","answer":"jupiter","hint":"My storm is the Great Red Spot."},
        {"riddle":"I am a small icy body that grows a tail of gas and dust near the Sun. What am I?","answer":"comet","hint":"Halley's version returns every 75 years."},
        {"riddle":"I am the distance light travels in one year — about 9.46 trillion km. What am I?","answer":"light year","hint":"Proxima Centauri is about 4.24 of me away."},
        {"riddle":"I am the hottest planet despite not being closest to the Sun. I rotate backwards. What am I?","answer":"venus","hint":"I am the second planet from the Sun."},
        {"riddle":"I describe the universe's origin from a hot dense state 13.8 billion years ago. What am I?","answer":"big bang","hint":"Cosmic microwave background radiation supports me."},
        {"riddle":"I am a massive object bending the path of light, as Einstein predicted. What am I?","answer":"gravitational lensing","hint":"Astronomers use me to detect dark matter."},
    ],
    "General Knowledge":[
        {"riddle":"I am the longest river in the world, flowing 6,650 km through northeast Africa. What am I?","answer":"nile","hint":"Egypt's pyramids are near my delta."},
        {"riddle":"I am the world's highest mountain, first summited in 1953 on the Nepal-Tibet border. What am I?","answer":"mount everest","hint":"Sir Edmund Hillary and Tenzing Norgay first climbed me."},
        {"riddle":"I pump blood continuously, beating 100,000 times a day. I have four chambers. What am I?","answer":"heart","hint":"I am inside your chest."},
        {"riddle":"I am the process converting grapes into wine through yeast. Bread uses a similar process. What am I?","answer":"fermentation","hint":"Yeast converts sugar into alcohol and CO₂ during me."},
        {"riddle":"I am the most widely spoken language in the world by total speakers. What am I?","answer":"english","hint":"I am the language of international aviation."},
        {"riddle":"I am the legal document granting inventors exclusive rights. Edison held over 1,000 of me. What am I?","answer":"patent","hint":"Pharmaceutical companies file thousands of me."},
        {"riddle":"I am the art of writing secret codes so only intended recipients can read. What am I?","answer":"cryptography","hint":"Julius Caesar used a simple form of me."},
        {"riddle":"I am the currency used by most European countries since 2002. My symbol is €. What am I?","answer":"euro","hint":"I replaced individual national currencies in Europe."},
        {"riddle":"I am the largest ocean on Earth, covering about one-third of its surface. What am I?","answer":"pacific ocean","hint":"I separate Asia from the Americas."},
        {"riddle":"I am the branch of medicine that diagnoses and treats mental and behavioural disorders. What am I?","answer":"psychiatry","hint":"Freud was an early pioneer of me."},
    ],
}


# ═══════════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════════
defaults = {
    "mode": None, "score": 0, "round": 0,
    "img_index": None, "img_q_index": None,
    "img_answered": False, "img_selected": None, "img_used": [],
    "riddle": None, "riddle_answer": None, "riddle_hint": None,
    "riddle_revealed": False, "riddle_correct": False, "hint_used": False,
    "draw_guess": None, "draw_score": None, "draw_feedback": None,
    "draw_description": None, "draw_confidence": None,
    "what_drew": "", "draw_analysed": False,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


def load_new_image_question():
    available = [i for i in range(len(IMAGE_QUIZ_DATA)) if i not in st.session_state.img_used]
    if not available:
        st.session_state.img_used = []
        available = list(range(len(IMAGE_QUIZ_DATA)))
    idx = random.choice(available)
    st.session_state.img_used.append(idx)
    q_idx = random.randint(0, len(IMAGE_QUIZ_DATA[idx]["questions"]) - 1)
    opts = IMAGE_QUIZ_DATA[idx]["questions"][q_idx]["options"][:]
    random.shuffle(opts)
    IMAGE_QUIZ_DATA[idx]["questions"][q_idx]["shuffled_options"] = opts
    st.session_state.img_index    = idx
    st.session_state.img_q_index  = q_idx
    st.session_state.img_answered = False
    st.session_state.img_selected = None
    st.session_state.round += 1


def get_riddle(category):
    pool = RIDDLE_BANK.get(category, RIDDLE_BANK["General Knowledge"])
    r = random.choice(pool)
    return {"riddle": r["riddle"], "answer": r["answer"].strip().lower(), "hint": r["hint"]}


# ═══════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════
st.markdown("""
<div class="game-header">
  <div class="game-title">🎮 AI Game Zone</div>
  <div class="game-subtitle">// three modes · fully offline · no api needed //</div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════
# HOME
# ═══════════════════════════════════════════
if st.session_state.mode is None:
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center;color:#6cb8be;font-size:0.95rem;margin-bottom:1.5rem;'>Select a game mode to begin</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.markdown("""<div class="mode-card"><span class="mode-icon">🖼️</span>
        <p class="mode-name">Image Quiz</p>
        <p class="mode-desc">See an emoji image — answer a question about it instantly. No upload needed!</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Play Now", key="b_img", use_container_width=True):
            st.session_state.update({"mode":"image","score":0,"round":0,"img_used":[]})
            load_new_image_question()
            st.rerun()

    with col2:
        st.markdown("""<div class="mode-card"><span class="mode-icon">🧩</span>
        <p class="mode-name">Riddles</p>
        <p class="mode-desc">Solve clever riddles from 8 categories. Use hints wisely!</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Play Now", key="b_rid", use_container_width=True):
            st.session_state.update({"mode":"riddle","score":0,"round":0,
                                     "riddle":None,"riddle_revealed":False,"hint_used":False})
            st.rerun()

    with col3:
        st.markdown("""<div class="mode-card"><span class="mode-icon">✏️</span>
        <p class="mode-name">Draw & Guess</p>
        <p class="mode-desc">Upload your sketch — smart local analysis scores your art!</p>
        </div>""", unsafe_allow_html=True)
        if st.button("Play Now", key="b_draw", use_container_width=True):
            st.session_state.update({"mode":"draw","score":0,"round":0,"draw_analysed":False})
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div style="text-align:center;margin-top:1rem;">
      <div style="display:inline-block;padding:0.8rem 2rem;border-radius:50px;
           background:rgba(13,180,185,0.06);border:1px solid rgba(13,180,185,0.18);">
        <span style="color:#6cb8be;font-size:0.8rem;font-family:'JetBrains Mono',monospace;">
          🌙 Fully Offline · No API · 20 Image Topics · 80+ Riddles
        </span>
      </div></div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════
# GAME SCREENS
# ═══════════════════════════════════════════
else:
    c1, c2 = st.columns([1,1])
    with c1:
        if st.button("← Menu", key="back"):
            for k, v in defaults.items():
                st.session_state[k] = v
            st.rerun()
    with c2:
        labels = {"image":"🖼️ Image Quiz","riddle":"🧩 Riddles","draw":"✏️ Draw & Guess"}
        st.markdown(f"""<div style="text-align:right;padding-top:0.3rem;">
          <span class="score-badge">⭐ {st.session_state.score} pts &nbsp;·&nbsp;
          Q{st.session_state.round} &nbsp;·&nbsp; {labels.get(st.session_state.mode,'')}</span>
        </div>""", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    # ─── MODE 1: IMAGE QUIZ ───────────────────────────────────────────────────
    if st.session_state.mode == "image":
        st.markdown("<span class='section-label'>🖼️ Image Quiz — Look & Answer</span>", unsafe_allow_html=True)

        idx   = st.session_state.img_index
        q_idx = st.session_state.img_q_index
        item  = IMAGE_QUIZ_DATA[idx]
        q     = item["questions"][q_idx]
        opts  = q.get("shuffled_options", q["options"])

        st.markdown(f"""
        <div class="img-card">
          <span class="img-emoji">{item['emoji']}</span>
          <span class="img-label-tag">📌 Topic: {item['label']}</span>
        </div>""", unsafe_allow_html=True)

        pct = min(int((st.session_state.round / 20) * 100), 100)
        st.markdown(f"""<div class="progress-bg">
          <div class="progress-fill" style="width:{pct}%;"></div></div>
        <p style="color:#6cb8be;font-size:0.78rem;font-family:'JetBrains Mono',monospace;margin:0 0 0.5rem;">
          Question {st.session_state.round}</p>""", unsafe_allow_html=True)

        st.markdown(f"<div class='question-box'>❓ {q['q']}</div>", unsafe_allow_html=True)

        if not st.session_state.img_answered:
            choice = st.radio("Choose your answer:", opts, key=f"img_r_{st.session_state.round}")
            if st.button("✅ Submit Answer", use_container_width=True):
                st.session_state.img_answered = True
                st.session_state.img_selected = choice
                if choice == q["correct"]:
                    st.session_state.score += 10
                st.rerun()
        else:
            sel = st.session_state.img_selected
            if sel == q["correct"]:
                st.markdown(f"<div class='answer-box'>🎉 <b>Correct! +10 points</b><br>✅ {q['correct']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='wrong-box'>❌ <b>Wrong!</b> You chose: {sel}<br>✅ Correct: {q['correct']}</div>", unsafe_allow_html=True)
            if st.button("▶️ Next Question", use_container_width=True):
                load_new_image_question()
                st.rerun()

    # ─── MODE 2: RIDDLES ─────────────────────────────────────────────────────
    elif st.session_state.mode == "riddle":
        st.markdown("<span class='section-label'>🧩 Riddle Challenge</span>", unsafe_allow_html=True)

        if st.session_state.riddle is None:
            st.markdown("<p style='color:#94c9cc;font-size:0.92rem;'>Pick a category — a riddle appears instantly!</p>", unsafe_allow_html=True)
            col_a, col_b = st.columns(2)
            with col_a:
                cat = st.selectbox("Category", list(RIDDLE_BANK.keys()))
            with col_b:
                st.select_slider("Difficulty", ["Easy","Medium","Hard"])

            if st.button("🎲 Give Me a Riddle!", use_container_width=True):
                d = get_riddle(cat)
                st.session_state.riddle          = d["riddle"]
                st.session_state.riddle_answer   = d["answer"]
                st.session_state.riddle_hint     = d["hint"]
                st.session_state.riddle_revealed = False
                st.session_state.riddle_correct  = False
                st.session_state.hint_used       = False
                st.session_state.round += 1
                st.rerun()
        else:
            st.markdown(f"<div class='question-box'>🧩 {st.session_state.riddle}</div>", unsafe_allow_html=True)

            if not st.session_state.riddle_revealed:
                ans = st.text_input("Your answer:", placeholder="Type here...", key="rid_in")
                c1, c2 = st.columns(2)
                with c1:
                    if st.button("✅ Submit", use_container_width=True, key="rid_sub"):
                        correct = st.session_state.riddle_answer
                        user = ans.strip().lower()
                        matched = (user == correct) or (user in correct) or (correct in user) or \
                                  any(w in correct for w in user.split() if len(w) > 2)
                        st.session_state.riddle_correct  = matched
                        st.session_state.riddle_revealed = True
                        if matched:
                            st.session_state.score += 7 if st.session_state.hint_used else 10
                        st.rerun()
                with c2:
                    if st.button("💡 Hint (-3 pts)", use_container_width=True, key="rid_hint"):
                        if not st.session_state.hint_used:
                            st.session_state.score = max(0, st.session_state.score - 3)
                            st.session_state.hint_used = True
                        st.rerun()
                if st.session_state.hint_used:
                    st.markdown(f"<div class='hint-box'>💡 {st.session_state.riddle_hint}</div>", unsafe_allow_html=True)
            else:
                pts = "+7 pts (hint used)" if st.session_state.hint_used else "+10 pts"
                if st.session_state.riddle_correct:
                    st.markdown(f"<div class='answer-box'>🎉 <b>Correct! {pts}</b><br>Answer: <b>{st.session_state.riddle_answer.title()}</b></div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='wrong-box'>❌ <b>Not quite!</b><br>✅ Answer: <b>{st.session_state.riddle_answer.title()}</b></div>", unsafe_allow_html=True)
                if st.button("🔄 Next Riddle", use_container_width=True):
                    st.session_state.update({"riddle":None,"riddle_answer":None,"riddle_hint":None,
                                             "riddle_revealed":False,"riddle_correct":False,"hint_used":False})
                    st.rerun()

    # ─── MODE 3: DRAW & GUESS ────────────────────────────────────────────────
    elif st.session_state.mode == "draw":
        from PIL import Image, ImageStat

        st.markdown("<span class='section-label'>✏️ Draw & Guess</span>", unsafe_allow_html=True)
        st.markdown("<p style='color:#94c9cc;font-size:0.92rem;'>Upload your sketch — smart local pixel analysis scores your art!</p>", unsafe_allow_html=True)
        st.info("🎨 Draw on paper & photograph it, or use MS Paint / any drawing app, then upload here.")

        drawing = st.file_uploader("Upload your drawing", type=["jpg","jpeg","png","webp"], key="draw_up")

        if drawing and not st.session_state.draw_analysed:
            st.image(Image.open(drawing), caption="Your Drawing", use_container_width=True)
            what = st.text_input("What did you draw?", placeholder="e.g. a cat, a tree, a bicycle...", key="what_in")

            if st.button("🔍 Analyse My Drawing!", use_container_width=True):
                img = Image.open(drawing)
                thumb = img.copy(); thumb.thumbnail((200,200))
                if thumb.mode != "RGB": thumb = thumb.convert("RGB")
                stat = ImageStat.Stat(thumb)
                r,g,b = stat.mean[:3]; rs,gs,bs = stat.stddev[:3]
                brightness = (r+g+b)/3; colorfulness = (rs+gs+bs)/3
                w,h = img.size; aspect = w/h if h else 1
                colour = "green" if g>r and g>b else "blue" if b>r else "red" if r>b else "mixed"
                light  = "bright" if brightness>140 else "dark"
                guesses = {"green+bright":"outdoor nature scene","green+dark":"dense forest or jungle",
                           "blue+bright":"sky or ocean scene","blue+dark":"night sky or deep water",
                           "red+bright":"flowers or food","red+dark":"dramatic indoor scene",
                           "mixed+bright":"everyday scene","mixed+dark":"moody artistic image"}
                guess = guesses.get(f"{colour}+{light}","a photograph")
                art_score = max(4, min(9, int((colorfulness/10)*0.4+(brightness/30)*0.2+(min(w,h)/100)*0.4)))
                bright_d = "dark" if brightness<60 else "dim" if brightness<120 else "moderate" if brightness<180 else "bright"
                vibrant  = "muted" if colorfulness<20 else "natural" if colorfulness<50 else "vibrant"
                comp     = "wide landscape" if aspect>1.7 else "portrait" if aspect<0.7 else "balanced"
                st.session_state.draw_guess       = guess
                st.session_state.draw_confidence  = "Medium" if colorfulness>30 else "Low"
                st.session_state.draw_description = f"A {bright_d}, {vibrant}, {comp} image."
                st.session_state.draw_score       = art_score
                st.session_state.draw_feedback    = f"Your drawing has {vibrant} colours and a {comp} composition. Great effort!"
                st.session_state.what_drew        = what
                st.session_state.draw_analysed    = True
                st.session_state.round += 1
                gw=guess.lower(); ww=what.strip().lower()
                if ww and (ww in gw or gw in ww or any(wd in gw for wd in ww.split() if len(wd)>2)):
                    st.session_state.score += art_score
                elif ww:
                    st.session_state.score += max(2, art_score-3)
                st.rerun()

        elif drawing and st.session_state.draw_analysed:
            st.image(Image.open(drawing), caption="Your Drawing", use_container_width=True)

        if st.session_state.draw_analysed:
            st.markdown("<hr>", unsafe_allow_html=True)
            cl, cr = st.columns(2, gap="medium")
            with cl:
                st.markdown(f"""<div style="background:rgba(13,180,185,0.06);border:1px solid rgba(13,180,185,0.18);border-radius:16px;padding:1.2rem;">
                  <div style="color:#0db4b9;font-size:0.72rem;font-family:'JetBrains Mono',monospace;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.6rem;">Analysis</div>
                  <div style="color:#e0f4f4;font-size:1.1rem;font-weight:800;">"{st.session_state.draw_guess.title()}"</div>
                  <div style="color:#6cb8be;font-size:0.82rem;margin-top:0.4rem;">Confidence: <b style="color:#38bdf8">{st.session_state.draw_confidence}</b></div>
                  <div style="margin-top:0.8rem;"><span style="color:#6cb8be;font-size:0.82rem;">Art Score: </span>
                  <span style="font-size:1.4rem;font-weight:800;color:#6ee7b7;">{st.session_state.draw_score}<span style="font-size:0.85rem;color:#6cb8be;">/10</span></span></div>
                </div>""", unsafe_allow_html=True)
            with cr:
                st.markdown(f"""<div style="background:rgba(13,180,185,0.06);border:1px solid rgba(13,180,185,0.18);border-radius:16px;padding:1.2rem;">
                  <div style="color:#fcd34d;font-size:0.72rem;font-family:'JetBrains Mono',monospace;letter-spacing:2px;text-transform:uppercase;margin-bottom:0.6rem;">Feedback</div>
                  <div style="color:#d4eef0;font-size:0.88rem;line-height:1.6;">💬 {st.session_state.draw_feedback}</div>
                  <div style="color:#6cb8be;font-size:0.8rem;margin-top:0.6rem;font-style:italic;">👁️ {st.session_state.draw_description}</div>
                </div>""", unsafe_allow_html=True)

            if st.session_state.what_drew:
                gw=st.session_state.draw_guess.lower(); ww=st.session_state.what_drew.strip().lower()
                matched = ww and (ww in gw or gw in ww or any(wd in gw for wd in ww.split() if len(wd)>2))
                if matched:
                    st.markdown(f"<div class='answer-box'>🎉 <b>Great match!</b> You drew <b>{st.session_state.what_drew}</b> — +{st.session_state.draw_score} points!</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='wrong-box'>😄 Analysis saw <b>'{st.session_state.draw_guess}'</b> but you drew <b>'{st.session_state.what_drew}'</b>. Keep practising!</div>", unsafe_allow_html=True)

            if st.button("🔄 Draw Something Else", use_container_width=True):
                st.session_state.update({"draw_guess":None,"draw_score":None,"draw_feedback":None,
                                         "draw_description":None,"draw_confidence":None,
                                         "what_drew":"","draw_analysed":False})
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<div style="text-align:center;padding:0.5rem 0;">
      <span style="color:#2a5f65;font-size:0.78rem;font-family:'JetBrains Mono',monospace;">
        🎮 AI Game Zone · Streamlit · Fully Offline · No API Required
      </span></div>""", unsafe_allow_html=True)
