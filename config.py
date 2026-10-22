import os
from dotenv import load_dotenv

load_dotenv()

TRANSLATIONS = {
    "English": {
        "lang_code": "en-US",
        "title": "AgroPasture: Rangeland Carrying Capacity Detector",
        "subtitle": "Grazing & Livestock Management Dashboard- by Team AgroTech",
        "select_lang": "Select Language",
        "land_details": "1. Land & Paddock Inputs",
        "area_label": "Total Usable Land (Acres)",
        "paddock_count": "Number of Grazing Paddocks",
        "livestock_label": "2. Livestock Inventory (Total: 100)",
        "cows": "Cows",
        "sheep": "Sheep",
        "goats": "Goats",
        "climate_label": "3. Climate Zone",
        "climate_options": ["Temperate / Mild Mid-Latitude (Strict Zone)"],
        "water_prompt": "4. Water Source & Location Info",
        "country_input": "Country / Region",
        "water_source_input": "Describe your nearest water source:",
        "image_label": "5. Photo Uploads",
        "weather_label": "6. Weather & Rainfall Analysis",
        "lat_label": "Latitude (or type NA to skip)",
        "lon_label": "Longitude (or type NA to skip)",
        "run_button": "Run Forage Forecast & Sustainability Analysis",
        "results_title": "Rangeland Analysis & Nutritional Results",
        "voice_title": "Audio Summary & Voice Controls",
        "listen_btn": "Play Full Audio Summary",
        "stop_btn": "Stop Audio",
        "nutrition_header": "Grass Type & Nutritional Value Identification",
        "grass_type_label": "Identified Grass Species",
        "protein_label": "Estimated Crude Protein",
        "digestibility_label": "Dry Matter Digestibility",
        "capacity_header": "Carrying Capacity & Forage Budget Breakdown",
        "usable_forage_text": "Total Usable Forage Available: {forage_lb:,.0f} lbs (~{forage_kg:,.0f} kg) per year.",
        "daily_demand_text": "Daily Herd Consumption Demand: {demand_lb:,.1f} lbs/day for {total_animals} animals ({cows} cows, {sheep} sheep, {goats} goats).",
        "duration_text": "Estimated Forage Duration: {days:.1f} days of continuous grazing capacity.",
        "paddock_plan_text": "Rotational Paddock Plan: Dividing {acres} acres into {paddocks} paddocks gives {paddock_size:.1f} acres per paddock.",
        "water_assessment": "Water & Hydration Assessment",
        "sustainable_methods": "10 Practical Field-Tested Rangeland Solutions",
        "solutions_list": [
            {
                "title": "1. Implement Rotational Grazing (Paddock Subdivision)",
                "issue": "Continuous grazing leads to animals over-consuming favored plant species while ignoring weeds.",
                "solution": "Divide the pasture into smaller paddocks using temporary or permanent fencing. Rotate livestock frequently (e.g., every 3 to 5 days) to give grazed grass 30 to 45 days of uninterrupted rest and root recovery.",
                "benefit": "Accelerates plant recovery, improves root depth, and increases total seasonal forage yield by 20% to 30%."
            },
            {
                "title": "2. Enforce Strict Stubble Height Thresholds",
                "issue": "Overgrazing weakens plants by forcing them to deplete root energy reserves.",
                "solution": "Set a mandatory grazing cutoff. Pull livestock out of a paddock once cool-season grasses are grazed down to a minimum stubble height of 3 to 4 inches to protect crowns and maintain photosynthetic capacity.",
                "benefit": "Protects plant solar panels for faster regrowth and prevents long-term pasture degradation."
            },
            {
                "title": "3. Deploy Mobile Water Troughs to Improve Distribution",
                "issue": "Livestock overgraze areas close to permanent water sources while underutilizing distant forage.",
                "solution": "Move water troughs periodically or install pipeline networks to distribute water evenly across the field. Encourages cattle to graze uniform patterns across slopes and corners.",
                "benefit": "Eliminates localized overgrazing around water points and ensures 100% pasture area utilization."
            },
            {
                "title": "4. Adjust Stocking Rates Dynamically (Flexible Stocking)",
                "issue": "Carrying capacities fluctuate wildly between wet spring seasons and dry autumns or droughts.",
                "solution": "Use a core breeding herd plus stocker model. Keep a stable core herd, but use flexible, short-term stocker animals that can be easily sold off when forage biomass drops below safety thresholds.",
                "benefit": "Prevents catastrophic financial losses during droughts and avoids forced emergency herd liquidation."
            },
            {
                "title": "5. Practice Multi-Species Grazing (Cattle & Sheep/Goats)",
                "issue": "Pastures become dominated by weeds, brush, or specific grass types that single species refuse to eat.",
                "solution": "Combine cattle (which prefer tall grasses) with sheep or goats (which browse broadleaf weeds and woody shrubs).",
                "benefit": "Maximizes total land productivity by 10% to 15%, naturally controls weeds without chemicals, and breaks livestock parasite cycles."
            },
            {
                "title": "6. Protect Saturated Soils with Winter Feeding Pads",
                "issue": "In temperate wet winters, heavy animal traffic destroys soil structure, causing severe compaction and muddy poaching.",
                "solution": "Remove animals from vulnerable pastures during heavy rainfall or winter thawing periods. Feed livestock on designated rock/concrete feeding pads or sacrifice paddocks.",
                "benefit": "Preserves fragile soil structure, prevents topsoil erosion, and ensures rapid spring pasture startup."
            },
            {
                "title": "7. Introduce Legume Inter-Seeding (e.g., White or Red Clover)",
                "issue": "Declining soil fertility and low protein content in mature mid-latitude grasses.",
                "solution": "Over-seed pastures with nitrogen-fixing legumes like clover. Boosts soil fertility, reduces dependence on synthetic fertilizers, and increases nutritional quality.",
                "benefit": "Fixes 50 to 150 lbs of atmospheric nitrogen per acre annually and improves animal weight gain due to higher protein content."
            },
            {
                "title": "8. Implement Deferred Grazing for Seed Recovery",
                "issue": "Permanent degradation of native perennial grasses due to lack of natural reproduction.",
                "solution": "Completely rest a specific paddock for an entire growing season every few years. Allows desirable perennial plants to flower, set seed, and replenish root reserves.",
                "benefit": "Restores native pasture biodiversity and thickens plant density naturally without expensive re-seeding."
            },
            {
                "title": "9. Establish Riparian Buffer Strips",
                "issue": "Stream banks collapsing due to livestock trampling, leading to water pollution and erosion.",
                "solution": "Fence off natural streams, rivers, and ponds to create vegetated buffer zones. Provide alternative off-stream watering points.",
                "benefit": "Protects clean water sources, stops soil erosion along waterways, and improves farm biosecurity."
            },
            {
                "title": "10. Over-Seed with Deep-Rooted, Climate-Resilient Forage Varieties",
                "issue": "Summer heatwaves or unpredictable mid-latitude droughts cause shallow-rooted pastures to go dormant or die off prematurely.",
                "solution": "Introduce deep-rooted perennial grasses (such as tall fescue or orchardgrass mixed with chicory or plantain) that tap into deeper soil moisture.",
                "benefit": "Extends the green grazing window during dry summer months and improves climate resilience."
            }
        ],
        "speech_template": "Forage forecast summary for {country} in the temperate zone. Identified grass is {species} with {protein} protein. Total usable forage is {forage} pounds for one hundred animals. Estimated continuous grazing duration is {days} days across {paddocks} paddocks.",
        "qa_livestock": "Livestock Breakdown: Your {cows} cows require {cow_demand:.0f} lbs/day, your {sheep} sheep require {sheep_demand:.0f} lbs/day, and your {goats} goats require {goat_demand:.0f} lbs/day. Applying Solution 5 (Multi-Species Grazing) optimizes forage across your {acres} acres.",
        "qa_duration": "Based on your inputs ({acres} acres, {cows} cows, {sheep} sheep, {goats} goats), your herd consumes {daily_demand:.1f} lbs/day against an annual usable supply of {total_forage:,.0f} lbs. Your baseline grazing duration is {days:.1f} days.",
        "qa_paddock": "With {acres} acres divided into {paddocks} paddocks, each paddock provides {paddock_size:.1f} acres. Rotating your herd every 3 to 5 days allows optimal 30-to-45-day rest periods.",
        "qa_general": "For your {acres}-acre temperate operation in {country} with 14-day rainfall at {rainfall} mm, combining Rotational Grazing with Mobile Water Troughs ensures uniform pasture utilization."
    },
    "Hindi (हिन्दी)": {
        "lang_code": "hi-IN",
        "title": "चारा पूर्वानुमान 360: चारागाह वहन क्षमता",
        "subtitle": "अनुकूली चराई और पशुधन प्रबंधन डैशबोर्ड",
        "select_lang": "भाषा चुनें",
        "land_details": "1. भूमि और पैडॉक इनपुट",
        "area_label": "कुल उपयोगी भूमि (एकड़)",
        "paddock_count": "चराई पैडॉक की संख्या",
        "livestock_label": "2. पशुधन सूची (कुल: 100)",
        "cows": "गाय",
        "sheep": "भेड़",
        "goats": "बकरी",
        "climate_label": "3. जलवायु क्षेत्र",
        "climate_options": ["शीतोष्ण /Mild Mid-Latitude (Strict Zone)"],
        "water_prompt": "4. जल स्रोत और स्थान की जानकारी",
        "country_input": "देश / क्षेत्र",
        "water_source_input": "अपने निकटतम जल स्रोत का वर्णन करें:",
        "image_label": "5. फोटो अपलोड करें",
        "weather_label": "6. मौसम और वर्षा विश्लेषण",
        "lat_label": "अक्षांश (या छोड़ने के लिए NA लिखें)",
        "lon_label": "देशांतर (या छोड़ने के लिए NA लिखें)",
        "run_button": "चारा पूर्वानुमान और स्थिरता विश्लेषण चलाएं",
        "results_title": "चारागाह विश्लेषण और पोषण परिणाम",
        "voice_title": "ऑडियो सारांश और आवाज नियंत्रण",
        "listen_btn": "पूर्ण ऑडियो सारांश सुनें",
        "stop_btn": "ऑडियो बंद करें",
        "nutrition_header": "घास का प्रकार और पोषण मूल्य पहचान",
        "grass_type_label": "पहचाने गए घास की प्रजाति",
        "protein_label": "अनुमानित क्रूड प्रोटीन",
        "digestibility_label": "शुष्क पदार्थ पचने की क्षमता",
        "capacity_header": "वहन क्षमता और चारा बजट विवरण",
        "usable_forage_text": "कुल उपलब्ध उपयोगी चारा: {forage_lb:,.0f} पाउंड (~{forage_kg:,.0f} किग्रा) प्रति वर्ष।",
        "daily_demand_text": "दैनिक झुंड खपत मांग: {total_animals} पशुओं ({cows} गायें, {sheep} भेड़, {goats} बकरियां) के लिए {demand_lb:,.1f} पाउंड/दिन।",
        "duration_text": "अनुमानित चारा अवधि: निरन्तर चराई क्षमता के {days:.1f} दिन।",
        "paddock_plan_text": "रोटेशनल पैडॉक योजना: {acres} एकड़ को {paddocks} पैडॉक में विभाजित करने पर प्रति पैडॉक {paddock_size:.1f} एकड़ प्राप्त होता है।",
        "water_assessment": "जल और जलयोजन मूल्यांकन",
        "sustainable_methods": "10 व्यावहारिक चारागाह समाधान और उनके लाभ",
        "solutions_list": [
            {
                "title": "1. रोटेशनल पैडॉक चराई लागू करें",
                "issue": "लगातार एक ही स्थान पर चराने से पशु पसंदीदा घास को अधिक खा लेते हैं और खरपतवार छोड़ देते हैं।",
                "solution": "अस्थायी या स्थायी बाड़ का उपयोग करके चरागाह को छोटे पैडॉक में विभाजित करें। पशुओं को हर 3 से 5 दिनों में घुमाएं ताकि घास को 30 से 45 दिनों का विश्राम मिले।",
                "benefit": "पौधों की वृद्धि तेज होती है, जड़ों की गहराई बढ़ती है, और मौसम की कुल उपज 20% से 30% तक बढ़ जाती है।"
            },
            {
                "title": "2. घास की ऊंचाई का सख्त नियम बनाएं",
                "issue": "अत्यधिक चराई से पौधों की जड़ें कमजोर हो जाती हैं।",
                "solution": "घास की ऊंचाई 3 से 4 इंच तक पहुंचते ही पशुओं को उस पैडॉक से बाहर निकाल लें।",
                "benefit": "पौधों को तेजी से दोबारा बढ़ने में मदद मिलती है और चरागाह को दीर्घकालिक नुकसान से बचाया जा सकता है।"
            },
            {
                "title": "3. मोबाइल जल कुंडों का उपयोग करें",
                "issue": "पशु स्थायी पानी के स्रोतों के पास अत्यधिक चराई करते हैं और दूर की घास छोड़ देते हैं।",
                "solution": "पानी के कुंडों को समय-समय पर स्थानांतरित करें ताकि पशु पूरे मैदान में समान रूप से चरें।",
                "benefit": "पानी के पास अत्यधिक चराई समाप्त होती है और पूरे खेत का 100% उपयोग होता है।"
            },
            {
                "title": "4. पशुओं की संख्या को मौसम के अनुसार बदलें",
                "issue": "गीले वसंत और सूखे के मौसम के बीच चरागाह की क्षमता में भारी बदलाव आता है।",
                "solution": "एक मुख्य झुंड रखें और अतिरिक्त पशुओं को चारा कम होने पर आसानी से बेच दें।",
                "benefit": "सूखे के दौरान भारी वित्तीय नुकसान और आपातकालीन बिक्री से बचा जा सकता है।"
            },
            {
                "title": "5. मिश्रित पशु प्रजातियों को एक साथ चराएं",
                "issue": "चरागाहों में खरपतवार और झाड़ियां बढ़ जाती हैं।",
                "solution": "गायों (जो लंबी घास पसंद करती हैं) को भेड़ों या बकरियों (जो खरपतवार खाती हैं) के साथ मिलाएं।",
                "benefit": "भूमि की उत्पादकता 10% से 15% बढ़ती है और बिना रसायनों के खरपतवार नियंत्रित होते हैं।"
            },
            {
                "title": "6. गीली मिट्टी को सर्दियों में बचाएं",
                "issue": "सर्दियों की बारिश में पशुओं की आवाजाही से मिट्टी की संरचना नष्ट हो जाती है।",
                "solution": "भारी बारिश के दौरान पशुओं को पक्के या कंक्रीट के फीडिंग पैड पर रखें।",
                "benefit": "मिट्टी के कटाव को रोकता है और वसंत में तेजी से घास उगने में मदद करता है।"
            },
            {
                "title": "7. फलिया (जैसे कलोवर) घास में मिलाएं",
                "issue": "मिट्टी की उर्वरता में कमी और पुरानी घास में कम प्रोटीन।",
                "solution": "नाइट्रोजन स्थिरीकरण करने वाले कलोवर के बीज चरागाह में बोएं।",
                "benefit": "यह प्रति वर्ष प्रति एकड़ 50 से 150 पाउंड नाइट्रोजन जोड़ता है और पशुओं का वजन तेजी से बढ़ाता है।"
            },
            {
                "title": "8. बीज पुनरुत्पादन के लिए चराई रोकें",
                "issue": "प्राकृतिक पुनरुत्पादन की कमी के कारण देशी घास का विनाश।",
                "solution": "हर कुछ वर्षों में एक विशिष्ट पैडॉक को पूरे मौसम के लिए विश्राम दें।",
                "benefit": "देशी पौधों में फूल और बीज आते हैं, जिससे बिना महंगे बीजों के चरागाह घना होता है।"
            },
            {
                "title": "9. नदियों और जल स्रोतों के किनारे बाड़ लगाएं",
                "issue": "पशुओं के रौंदने से नदी के किनारे धंसते हैं और पानी दूषित होता है।",
                "solution": "प्राकृतिक नदियों और तालाबों के चारों ओर बाड़ लगाएं।",
                "benefit": "साफ पानी के स्रोतों की रक्षा होती है और मिट्टी का कटाव रुकता है।"
            },
            {
                "title": "10. गहरी जड़ों वाली घास किस्मों को बोएं",
                "issue": "गर्मी की लहरों या सूखे में छोटी जड़ों वाली घास सूख जाती है।",
                "solution": "टॉल फेस्क्यू या ऑर्चर्डग्रास जैसी गहरी जड़ों वाली किस्मों को बोएं।",
                "benefit": "सूखे के महीनों में भी हरी चराई की अवधि बढ़ती है।"
            }
        ],
        "speech_template": "{country} के लिए चारा पूर्वानुमान सारांश। पहचानी गई घास {species} है जिसमें {protein} प्रोटीन है। कुल उपयोग योग्य चारा एक सौ पशुओं के लिए {forage} पाउंड है। अनुमानित चराई अवधि {days} दिन है।",
        "qa_livestock": "पशुधन विवरण: आपकी {cows} गायों को {cow_demand:.0f} पाउंड/दिन, {sheep} भेड़ों को {sheep_demand:.0f} पाउंड/दिन, और {goats} बकरियों को {goat_demand:.0f} पाउंड/दिन की आवश्यकता है। मिश्रित चराई समाधान लागू करने से आपकी {acres} एकड़ भूमि का उपयोग अनुकूलित होता है।",
        "qa_duration": "आपके इनपुट ({acres} एकड़, {cows} गायें, {sheep} भेड़, {goats} बकरियां) के आधार पर, आपका झुंड {daily_demand:.1f} पाउंड/दिन खपत करता है। आपकी कुल चारा अवधि {days:.1f} दिन है।",
        "qa_paddock": "{acres} एकड़ को {paddocks} पैडॉक में विभाजित करने पर, प्रत्येक पैडॉक {paddock_size:.1f} एकड़ का होता है। हर 3 से 5 दिनों में चराई बदलने से घास को 30 से 45 दिनों का विश्राम मिलता है।",
        "qa_general": "{country} में आपके {acres} एकड़ के मॉडल के लिए जहां 14-दिन की वर्षा {rainfall} मिमी है, रोटेशनल चराई और मोबाइल जल कुंडों का उपयोग पूरे खेत में समान चराई सुनिश्चित करता है."
    },
    "Spanish (Español)": {
        "lang_code": "es-ES",
        "title": "Pronóstico de Forraje 360: Capacidad de Carga",
        "subtitle": "Panel de Pastoreo Adaptativo y Gestión Ganadera",
        "select_lang": "Seleccionar Idioma",
        "land_details": "1. Entradas de Tierra y Potreros",
        "area_label": "Tierra Útil Total (Acres)",
        "paddock_count": "Número de Potreros de Pastoreo",
        "livestock_label": "2. Inventario Ganadero (Total: 100)",
        "cows": "Vacas",
        "sheep": "Ovejas",
        "goats": "Cabras",
        "climate_label": "3. Zona Climática",
        "climate_options": ["Templado / Latitud Media (Zona Estricta)"],
        "water_prompt": "4. Información de Fuente de Agua y Ubicación",
        "country_input": "País / Región",
        "water_source_input": "Describa su fuente de agua más cercana:",
        "image_label": "5. Subir Fotos",
        "weather_label": "6. Análisis Climatológico y de Lluvias",
        "lat_label": "Latitud (o escriba NA para omitir)",
        "lon_label": "Longitud (o escriba NA para omitir)",
        "run_button": "Ejecutar Análisis de Forraje",
        "results_title": "Resultados de Análisis y Nutrición",
        "voice_title": "Resumen de Audio y Controles",
        "listen_btn": "Escuchar Resumen Completo",
        "stop_btn": "Detener Audio",
        "nutrition_header": "Identificación de Tipo de Pasto y Valor Nutricional",
        "grass_type_label": "Especie de Pasto Identificada",
        "protein_label": "Proteína Cruda Estimada",
        "digestibility_label": "Digestibilidad de Materia Seca",
        "capacity_header": "Capacidad de Carga y Presupuesto de Forraje",
        "usable_forage_text": "Forraje útil total disponible: {forage_lb:,.0f} libras (~{forage_kg:,.0f} kg) por año.",
        "daily_demand_text": "Demanda de consumo diario del rebaño: {demand_lb:,.1f} libras/día para {total_animals} animales ({cows} vacas, {sheep} ovejas, {goats} cabras).",
        "duration_text": "Duración estimada del forraje: {days:.1f} días de capacidad de pastoreo continuo.",
        "paddock_plan_text": "Plan de potreros rotacionales: Dividir {acres} acres en {paddocks} potreros da {paddock_size:.1f} acres por potrero.",
        "water_assessment": "Evaluación de Agua e Hidratación",
        "sustainable_methods": "10 Soluciones Prácticas de Pastizal y sus Beneficios",
        "solutions_list": [
            {
                "title": "1. Implementar Pastoreo Rotacional",
                "issue": "El pastoreo continuo provoca el sobreconsumo de especies deseadas y descuida las malezas.",
                "solution": "Divida el pastizal en potreros más pequeños y rote el ganado cada 3 a 5 días para dar 30 a 45 días de descanso.",
                "benefit": "Acelera la recuperación de las plantas e incrementa el rendimiento del forraje en un 20% a 30%."
            },
            {
                "title": "2. Establecer Alturas Mínimas de Rastrojo",
                "issue": "El sobrepastoreo debilita las raíces de las plantas.",
                "solution": "Retire los animales cuando el pasto alcance una altura mínima de 3 a 4 pulgadas.",
                "benefit": "Mantiene la capacidad fotosintética y acelera el rebrote."
            },
            {
                "title": "3. Desplegar Bebederos Móviles",
                "issue": "El ganado sobrepastorea cerca del agua permanente y descuida áreas lejanas.",
                "solution": "Mueva los bebederos periódicamente para distribuir el agua de manera uniforme.",
                "benefit": "Elimina el sobrepastoreo localizado y aprovecha el 100% del área."
            },
            {
                "title": "4. Ajustar la Carga Animal Dinámicamente",
                "issue": "La capacidad de carga varía drásticamente según las estaciones y sequías.",
                "solution": "Mantenga un rebaño base y animales secundarios flexibles para vender en sequía.",
                "benefit": "Evita pérdidas financieras catastróficas durante la sequía."
            },
            {
                "title": "5. Practicar Pastoreo Multiespecie",
                "issue": "El pastizal se llena de malezas que una sola especie no consume.",
                "solution": "Combine vacas (pastos altos) con ovejas o cabras (maleza y arbustos).",
                "benefit": "Aumenta la productividad en un 10% a 15% y controla malezas de forma natural."
            },
            {
                "title": "6. Proteger Suelos Saturados en Invierno",
                "issue": "El pisoteo en invierno destruye la estructura del suelo.",
                "solution": "Mueva los animales a plataformas de concreto o potreros de sacrificio durante lluvias intensas.",
                "benefit": "Preserva la estructura del suelo y previene la erosión."
            },
            {
                "title": "7. Intersembrar Leguminosas (Trébol)",
                "issue": "Disminución de fertilidad del suelo y bajo contenido proteico en el pasto.",
                "solution": "Siembre leguminosas fijadoras de nitrógeno como el trébol.",
                "benefit": "Fija nitrógeno en el suelo y mejora la ganancia de peso del ganado."
            },
            {
                "title": "8. Pastoreo Diferido para Semillación",
                "issue": "Degradación de pastos nativos por falta de reproducción.",
                "solution": "Descanse un potrero específico durante toda una temporada de crecimiento.",
                "benefit": "Restaura la densidad del pastizal nativo sin resembrar."
            },
            {
                "title": "9. Establecer Franjas de Protección en Ríos",
                "issue": "Erosión y contaminación de agua por el pisoteo en las orillas.",
                "solution": "Cercar ríos y estanques creando zonas de amortiguamiento.",
                "benefit": "Protege las fuentes de agua limpia y evita la erosión."
            },
            {
                "title": "10. Sembrar Especies de Raíz Profunda",
                "issue": "Sequías de verano que secan los pastos de raíz corta.",
                "solution": "Introduzca festuca alta o dáctilo con raíces profundas.",
                "benefit": "Extiende la temporada de pastoreo verde durante el verano."
            }
        ],
        "speech_template": "Resumen de pronóstico para {country}. El pasto identificado es {species}. El forraje utilizable total es de {forage} libras. La duración estimada es de {days} días.",
        "qa_livestock": "Desglose de ganado: Sus {cows} vacas requieren {cow_demand:.0f} lb/día, sus {sheep} ovejas requieren {sheep_demand:.0f} lb/día, y sus {goats} cabras requieren {goat_demand:.0f} lb/día. El pastoreo multiespecie optimiza el uso de sus {acres} acres.",
        "qa_duration": "Con sus datos ({acres} acres, {cows} vacas, {sheep} ovejas, {goats} cabras), el rebaño consume {daily_demand:.1f} lb/día. Su duración estimada de forraje es de {days:.1f} días.",
        "qa_paddock": "Dividiendo {acres} acres en {paddocks} potreros, cada potrero tiene {paddock_size:.1f} acres. Rotar cada 3 a 5 días permite períodos de descanso ideales de 30 a 45 días.",
        "qa_general": "Para su operación de {acres} acres en {country} con precipitación de {rainfall} mm, el pastoreo rotacional con bebederos móviles garantiza un uso uniforme del pastizal."
    },
    "German (Deutsch)": {
        "lang_code": "de-DE",
        "title": "Futterprognose 360: Weidekapazität",
        "subtitle": "Adaptives Weide- und Viehmanagement-Dashboard",
        "select_lang": "Sprache auswählen",
        "land_details": "1. Land- und Weideeingaben",
        "area_label": "Gesamte Nutzfläche (Acres)",
        "paddock_count": "Anzahl der Weidepaddocks",
        "livestock_label": "2. Viehbestand (Gesamt: 100)",
        "cows": "Kühe",
        "sheep": "Schafe",
        "goats": "Ziegen",
        "climate_label": "3. Klimazone",
        "climate_options": ["Gemäßigt / Milde Breiten"],
        "water_prompt": "4. Wasserquelle und Standortinfo",
        "country_input": "Land / Region",
        "water_source_input": "Beschreiben Sie Ihre nächste Wasserquelle:",
        "image_label": "5. Foto-Upload",
        "weather_label": "6. Wetter- und Niederschlagsanalyse",
        "lat_label": "Breitengrad (oder NA eingeben)",
        "lon_label": "Längengrad (oder NA eingeben)",
        "run_button": "Futterprognose und Nachhaltigkeitsanalyse starten",
        "results_title": "Weideanalyse und Nährstoffergebnisse",
        "voice_title": "Audio-Zusammenfassung und Steuerung",
        "listen_btn": "Vollständiges Audio anhören",
        "stop_btn": "Audio stoppen",
        "nutrition_header": "Grasart und Nährwertbestimmung",
        "grass_type_label": "Identifizierte Grasart",
        "protein_label": "Geschätztes Rohprotein",
        "digestibility_label": "Trockensubstanzverdaulichkeit",
        "capacity_header": "Tragfähigkeit und Futterbudget",
        "usable_forage_text": "Verfügbares Gesamtfutter: {forage_lb:,.0f} lbs (~{forage_kg:,.0f} kg) pro Jahr.",
        "daily_demand_text": "Täglicher Herdenbedarf: {demand_lb:,.1f} lbs/Tag für {total_animals} Tiere ({cows} Kühe, {sheep} Schafe, {goats} Ziegen).",
        "duration_text": "Geschätzte Futterdauer: {days:.1f} Tage kontinuierliche Weidekapazität.",
        "paddock_plan_text": "Rotations-Paddock-Plan: Aufteilung von {acres} Acres in {paddocks} Paddocks ergibt {paddock_size:.1f} Acres pro Paddock.",
        "water_assessment": "Wasser- und Hydratationsbewertung",
        "sustainable_methods": "10 Praktische Weidelösungen und ihre Vorteile",
        "solutions_list": [
            {
                "title": "1. Umtriebsweide einführen",
                "issue": "Dauerweide führt dazu, dass Tiere bevorzugte Pflanzen übernutzen.",
                "solution": "Teilen Sie die Weide in kleinere Paddocks auf und rotieren Sie das Vieh alle 3 bis 5 Tage.",
                "benefit": "Beschleunigt das Pflanzenwachstum und steigert den Futterertrag um 20% bis 30%."
            },
            {
                "title": "2. Strenge Stubbenporthöhen einhalten",
                "issue": "Überweidung schwächt die Pflanzenwurzeln.",
                "solution": "Treiben Sie Tiere aus, sobald das Gras eine Mindesthöhe von 3 bis 4 Zoll erreicht hat.",
                "benefit": "Schützt die Photosynthesekapazität für schnelleres Nachwachsen."
            },
            {
                "title": "3. Mobile Wassertränken einsetzen",
                "issue": "Vieh überweidet Bereiche nahe permanenter Wasserquellen.",
                "solution": "Verschieben Sie Wassertränken regelmäßig für gleichmäßige Verteilung.",
                "benefit": "Beseitigt lokale Überweidung und nutzt 100% der Weide."
            },
            {
                "title": "4. Bestandsdichte dynamisch anpassen",
                "issue": "Tragfähigkeit schwankt stark zwischen nassem Frühjahr und Dürre.",
                "solution": "Nutzen Sie eine Kernherde plus flexible Zusatztiere.",
                "benefit": "Verhindert finanzielle Verluste in Dürrezeiten."
            },
            {
                "title": "5. Mehrartenbeweidung praktizieren",
                "issue": "Weiden wachsen mit Unkräutern zu, die Rinder verschmähen.",
                "solution": "Kombinieren Sie Rinder mit Schafen oder Ziegen.",
                "benefit": "Erhöht die Landproduktivität um 10% bis 15%."
            },
            {
                "title": "6. Gesättigte Böden im Winter schützen",
                "issue": "Starker Viehtritt im Winter zerstört die Bodenstruktur.",
                "solution": "Tiere bei starkem Regen auf Futterpads oder Opferpaddocks halten.",
                "benefit": "Bewahrt die Bodenstruktur und verhindert Bodenerosion."
            },
            {
                "title": "7. Leguminosen einsäen (Klee)",
                "issue": "Sinkende Bodenfruchtbarkeit und geringer Proteingehalt.",
                "solution": "Säen Sie stickstofffixierenden Klee nach.",
                "benefit": "Erhöht den Proteingehalt und die Bodenfruchtbarkeit."
            },
            {
                "title": "8. Zeitweilige Weideruhe für Samengewinnung",
                "issue": "Degradation heimischer Gräser durch fehlende Reproduktion.",
                "solution": "Lassen Sie ein Paddock eine ganze Saison lang ruhen.",
                "benefit": "Stellt die biologische Vielfalt der Weide wieder her."
            },
            {
                "title": "9. Uferzonen und Pufferstreifen schützen",
                "issue": "Uferabbrüche und Wasserverschmutzung durch Viehtritt.",
                "solution": "Bäche und Teiche einzäunen und alternative Tränken bereitstellen.",
                "benefit": "Schützt saubere Wasserquellen und stoppt Erosion."
            },
            {
                "title": "10. Tiefwurzelnde Futterarten einsäen",
                "issue": "Sommerhitze lässt flachwurzelnde Weiden vertrocknen.",
                "solution": "Führen Sie tiefwurzelnde Gräser wie Wiesenschwingel ein.",
                "benefit": "Verlängert das grüne Weidefenster in Trockenperioden."
            }
        ],
        "speech_template": "Futterprognose für {country}. Identifiziertes Gras ist {species}. Gesamtes nutzbares Futter beträgt {forage} Pfund. Geschätzte Weidedauer ist {days} Tage.",
        "qa_livestock": "Viehbestand: Ihre {cows} Kühe benötigen {cow_demand:.0f} lbs/Tag, {sheep} Schafe {sheep_demand:.0f} lbs/Tag, {goats} Ziegen {goat_demand:.0f} lbs/Tag.",
        "qa_duration": "Bei Ihren Eingaben ({acres} Acres, {cows} Kühe, {sheep} Schafe, {goats} Ziegen) beträgt die Futterdauer {days:.1f} Tage.",
        "qa_paddock": "Aufteilung von {acres} Acres in {paddocks} Paddocks ergibt {paddock_size:.1f} Acres pro Paddock mit 30–45 Tagen Ruhezeit.",
        "qa_general": "Für Ihren Betrieb mit {acres} Acres in {country} und {rainfall} mm Niederschlag sichert die Umtriebsweide eine optimale Nutzung."
    },
    "French (Français)": {
        "lang_code": "fr-FR",
        "title": "Prévision Fourragère 360: Capacité de Charge",
        "subtitle": "Tableau de Bord de Pâturage Adaptatif",
        "select_lang": "Sélectionner la langue",
        "land_details": "1. Entrées de Terrains et Paddocks",
        "area_label": "Surface Utile Totale (Acres)",
        "paddock_count": "Nombre de Paddocks de Pâturage",
        "livestock_label": "2. Inventaire du Bétail (Total: 100)",
        "cows": "Vaches",
        "sheep": "Moutons",
        "goats": "Chèvres",
        "climate_label": "3. Zone Climatique",
        "climate_options": ["Tempéré / Moyennes Latitudes"],
        "water_prompt": "4. Source d'Eau et Emplacement",
        "country_input": "Pays / Région",
        "water_source_input": "Décrivez votre source d'eau la plus proche:",
        "image_label": "5. Téléchargement de Photos",
        "weather_label": "6. Analyse Météo et Pluviométrie",
        "lat_label": "Latitude (ou tapez NA pour ignorer)",
        "lon_label": "Longitude (ou tapez NA pour ignorer)",
        "run_button": "Lancer l'Analyse Fourragère",
        "results_title": "Résultats d'Analyse et Nutritionnels",
        "voice_title": "Résumé Audio et Commandes",
        "listen_btn": "Écouter le Résumé Audio",
        "stop_btn": "Arrêter l'Audio",
        "nutrition_header": "Identification du Type d'Herbe et Valeur Nutritive",
        "grass_type_label": "Espèce d'Herbe Identifiée",
        "protein_label": "Protéine Brute Estimée",
        "digestibility_label": "Digestibilité de la Matière Sèche",
        "capacity_header": "Capacité de Charge et Bilan Fourrager",
        "usable_forage_text": "Fourrage utile total disponible: {forage_lb:,.0f} lbs (~{forage_kg:,.0f} kg) par an.",
        "daily_demand_text": "Demande de consommation quotidienne: {demand_lb:,.1f} lbs/jour pour {total_animals} animaux ({cows} vaches, {sheep} moutons, {goats} chèvres).",
        "duration_text": "Durée estimée du fourrage: {days:.1f} jours de capacité de pâturage continu.",
        "paddock_plan_text": "Plan de paddocks tournants: La division de {acres} acres en {paddocks} paddocks donne {paddock_size:.1f} acres par paddock.",
        "water_assessment": "Évaluation de l'Eau et de l'Hydratation",
        "sustainable_methods": "10 Solutions Pratiques de Pâturage et Leurs Avantages",
        "solutions_list": [
            {
                "title": "1. Mettre en place le Pâturage Tournant",
                "issue": "Le pâturage continu entraîne la surconsommation des espèces préférées.",
                "solution": "Divisez le pâturage en petits paddocks et déplacez le bétail tous les 3 à 5 jours.",
                "benefit": "Accélère la repousse et augmente le rendement du fourrage de 20% à 30%."
            },
            {
                "title": "2. Respecter les Seuils de Hauteur de Stub",
                "issue": "Le surpâturage affaiblit les racines des plantes.",
                "solution": "Retirez le bétail dès que l'herbe atteint une hauteur minimale de 3 à 4 pouces.",
                "benefit": "Protège la capacité photosynthétique et accélère la repousse."
            },
            {
                "title": "3. Déployer des Abreuvoirs Mobiles",
                "issue": "Le bétail surpâture près des sources d'eau permanentes.",
                "solution": "Déplacez les abreuvoirs périodiquement pour répartir la pression.",
                "benefit": "Élimine le surpâturage localisé et utilise 100% de la zone."
            },
            {
                "title": "4. Ajuster Dynamiquement la Charge Animale",
                "issue": "La capacité de charge varie fortement entre saisons humides et sèches.",
                "solution": "Maintenez un troupeau de base et des animaux secondaires flexibles.",
                "benefit": "Prévient les pertes financières catastrophiques en cas de sécheresse."
            },
            {
                "title": "5. Pratiquer le Pâturage Multiespèces",
                "issue": "Les pâturages sont envahis par des mauvaises herbes refusées par une seule espèce.",
                "solution": "Associez des vaches (herbes hautes) à des ovins ou caprins.",
                "benefit": "Optimise la productivité des terres de 10% à 15% naturellement."
            },
            {
                "title": "6. Protéger les Sols Saturés en Hiver",
                "issue": "Le piétinement lourd en hiver détruit la structure du sol.",
                "solution": "Retirez les animaux des pâturages vulnérables lors de fortes pluies.",
                "benefit": "Préserve la structure du sol et prévient l'érosion."
            },
            {
                "title": "7. Introduire le Trèfle (Légumineuses)",
                "issue": "Baisse de fertilité du sol et faible teneur en protéines.",
                "solution": "Sursemez des légumineuses fixatrices d'azote comme le trèfle.",
                "benefit": "Améliore naturellement la fertilité du sol et la qualité protéique."
            },
            {
                "title": "8. Pratiquer le Pâturage Différé",
                "issue": "Dégradation des graminées indigènes par manque de reproduction.",
                "solution": "Reposez complètement un paddock pendant toute une saison.",
                "benefit": "Restaure la biodiversité et densifie la prairie naturellement."
            },
            {
                "title": "9. Établir des Zones Tampons Ripariennes",
                "issue": "Effondrement des berges par le piétinement du bétail.",
                "solution": "Clôturer les cours d'eau naturels et fournir des points d'eau alternatifs.",
                "benefit": "Protège l'eau propre et stabilise les berges."
            },
            {
                "title": "10. Semer des Variétés à Racines Profondes",
                "issue": "Les sécheresses estivales assèchent les pâturages superficiels.",
                "solution": "Introduisez des graminées vivaces à enracinement profond.",
                "benefit": "Prolonge la saison de pâturage vert en période sèche."
            }
        ],
        "speech_template": "Résumé des prévisions pour {country}. Herbe identifiée: {species}. Fourrage utilisable total: {forage} livres. Durée estimée: {days} jours.",
        "qa_livestock": "Détails du bétail: Vos {cows} vaches nécessitent {cow_demand:.0f} lbs/jour, vos {sheep} moutons {sheep_demand:.0f} lbs/jour, et vos {goats} chèvres {goat_demand:.0f} lbs/jour.",
        "qa_duration": "Selon vos données ({acres} acres, {cows} vaches, {sheep} moutons, {goats} chèvres), la durée estimée du fourrage est de {days:.1f} jours.",
        "qa_paddock": "La division de {acres} acres en {paddocks} paddocks donne {paddock_size:.1f} acres par paddock avec un repos de 30 à 45 jours.",
        "qa_general": "Pour votre exploitation de {acres} acres à {country} avec {rainfall} mm de pluie, le pâturage tournant assure une utilisation uniforme."
    },
    "Tamil (தமிழ்)": {
        "lang_code": "ta-IN",
        "title": "தீவன முன்னறிவிப்பு 360: மேய்ச்சல் நில கொள்ளளவு",
        "subtitle": "தகவமைப்பு மேய்ச்சல் மற்றும் கால்நடை மேலாண்மை பலகை",
        "select_lang": "மொழியைத் தேர்ந்தெடுக்கவும்",
        "land_details": "1. நில மற்றும் பாдок உள்ளீடுகள்",
        "area_label": "மொத்த பயன்படுத்தக்கூடிய நிலம் (ஏக்கர்)",
        "paddock_count": "மேய்ச்சல் பாட்டங்குகளின் எண்ணிக்கை",
        "livestock_label": "2. கால்நடைப் பட்டியல் (மொத்தம்: 100)",
        "cows": "பசுக்கள்",
        "sheep": "செம்மறி ஆடுகள்",
        "goats": "வெள்ளாடுகள்",
        "climate_label": "3. காலநிலை மண்டலம்",
        "climate_options": ["மிதशीतोष्ण / Temperate"],
        "water_prompt": "4. நீர் ஆதாரம் மற்றும் இருப்பிடத் தகவல்",
        "country_input": "நாடு / பிராந்தியம்",
        "water_source_input": "உங்கள் அருகிலுள்ள நீர் ஆதாரத்தை விவரிக்கவும்:",
        "image_label": "5. புகைப்பட பதிவேற்றம்",
        "weather_label": "6. வானிலை மற்றும் மழைப்பொழிவு பகுப்பாய்வு",
        "lat_label": "அட்சரேகை (தவிர்க்க NA என உள்ளிடவும்)",
        "lon_label": "தீர்க்கரேகை (தவிர்க்க NA என உள்ளிடவும்)",
        "run_button": "தீவன முன்னறிவிப்பு மற்றும் நிலைத்தன்மை பகுப்பாய்வை இயக்கு",
        "results_title": "நில பகுப்பாய்வு மற்றும் ஊட்டச்சத்து முடிவுகள்",
        "voice_title": "ஆடியோ சுருக்கம் மற்றும் கட்டுப்பாடுகள்",
        "listen_btn": "முழு ஆடியோ சுருக்கத்தைக் கேட்கவும்",
        "stop_btn": "ஆடியோவை நிறுத்து",
        "nutrition_header": "புல் வகை மற்றும் ஊட்டச்சத்து மதிப்பு அடையாளம்",
        "grass_type_label": "அடையாளம் காணப்பட்ட புல் இனம்",
        "protein_label": "மதிப்பிடப்பட்ட புரதம்",
        "digestibility_label": "உலர்ந்த பொருள் செரிமானம்",
        "capacity_header": "கொள்ளளவு மற்றும் தீவன பட்ஜெட் விவரம்",
        "usable_forage_text": "மொத்த பயன்பாட்டு தீவனம்: ஆண்டுக்கு {forage_lb:,.0f} பவுண்டுகள் (~{forage_kg:,.0f} கிலோ).",
        "daily_demand_text": "தினசரி நுகர்வு தேவை: {total_animals} விலங்குகளுக்கு ({cows} பசுக்கள், {sheep} ஆடுகள், {goats} வெள்ளாடுகள்) {demand_lb:,.1f} பவுண்டுகள்/நாள்.",
        "duration_text": "மதிப்பிடப்பட்ட தீவன காலம்: {days:.1f} நாட்கள் தொடர்ச்சியான மேய்ச்சல் திறன்.",
        "paddock_plan_text": "சுழற்சி பாட்டங்கு திட்டம்: {acres} ஏக்கரை {paddocks} பாட்டங்குகளாகப் பிரித்தால் பாட்டங்கிற்கு {paddock_size:.1f} ஏக்கர் கிடைக்கிறது.",
        "water_assessment": "நீர் மற்றும் நீரேற்றம் மதிப்பீடு",
        "sustainable_methods": "10 நடைமுறை மேய்ச்சல் நில தீர்வுகள்",
        "solutions_list": [
            {
                "title": "1. சுழற்சி மேய்ச்சல் முறையை செயல்படுத்துதல்",
                "issue": "தொடர்ந்து ஒரே இடத்தில் மேய்ப்பதால் தாவரங்கள் சேதமடைகின்றன.",
                "solution": "நிலத்தை சிறு பாட்டங்குகளாக பிரித்து ஒவ்வொரு 3 முதல் 5 நாட்களுக்கு ஒருமுறை கால்நடைகளை மாற்றவும்.",
                "benefit": "தாவர வளர்ச்சி துரிதப்படுத்தப்பட்டு தீவன உற்பத்தி 20% முதல் 30% அதிகரிக்கிறது."
            },
            {
                "title": "2. குறைந்தபட்ச புல் உயர வரம்பை பராமரித்தல்",
                "issue": "அதிகப்படியான மேய்ச்சல் தாவர வேர்களை பலவீனப்படுத்துகிறது.",
                "solution": "புல் 3 முதல் 4 அங்குல உயரத்திற்கு வந்ததும் கால்நடைகளை அப்புறப்படுத்தவும்.",
                "benefit": "வேகமாக மீண்டும் துளிர்க்க உதவுகிறது."
            },
            {
                "title": "3. நடமாடும் நீர் தொட்டிகளைப் பயன்படுத்துதல்",
                "issue": "கால்நடைகள் நீர் மூலங்களுக்கு அருகிலேயே அதிகளவில் மேய்கின்றன.",
                "solution": "நீர் தொட்டிகளை அவ்வப்போது நகர்த்தி சமமான மேய்ச்சலை உறுதிப்படுத்தவும்.",
                "benefit": "நிலம் முழுவதும் சமமாக மேய்ச்சல் பயன்படுத்தப்படுகிறது."
            },
            {
                "title": "4. கால்நடை எண்ணிக்கையை நெகிழ்வாக மாற்றுதல்",
                "issue": "மழைக்காலம் மற்றும் வறட்சி காலங்களுக்கு ஏற்ப கொள்ளளவு மாறும்.",
                "solution": "அடிப்படை மந்தையை வைத்துக் கொண்டு தேவையின்றி கூடுதல் விலங்குகளை விற்கவும்.",
                "benefit": "வறட்சி காலத்தில் நிதி இழப்பை தவிர்க்கலாம்."
            },
            {
                "title": "5. பல இன மேய்ச்சல் முறை",
                "issue": "களைகள் மற்றும் புதர்கள் அதிகமாக வளர்வது.",
                "solution": "பசுக்களுடன் ஆடுகள் மற்றும் வெள்ளாடுகளை சேர்த்து மேய்க்கவும்.",
                "benefit": "நில உற்பத்தித்திறன் அதிகரிக்கிறது."
            },
            {
                "title": "6. குளிர்காலத்தில் ஈரமான மண்ணைப் பாதுகாத்தல்",
                "issue": "கால்நடை நடமாட்டத்தால் மண் அமைப்பு சேதமடைகிறது.",
                "solution": "கனமழையின் போது விலங்குகளை பிரத்யேக கூடங்களில் வைக்கவும்.",
                "benefit": "மண் அரிப்பு தடுக்கப்படுகிறது."
            },
            {
                "title": "7. பயறு வகை தாவரங்களை விதைத்தல்",
                "issue": "மண் வளம் குறைதல் மற்றும் குறைந்த புரதச்சத்து.",
                "solution": "clover போன்ற பயறு வகைகளை விதைக்கவும்.",
                "benefit": "மண் வளம் மற்றும் புரதச்சத்து அதிகரிக்கிறது."
            },
            {
                "title": "8. விதை மீட்சியுக்காக மேய்ச்சலை நிறுத்துதல்",
                "issue": "இயற்கை இனப்பெருக்கம் இல்லாததால் தாவரங்கள் அழிவது.",
                "solution": "ஒரு குறிப்பிட்ட பாட்டங்கை ஒரு முழு பருவத்திற்கு ஓய்வு அளிக்கவும்.",
                "benefit": "இயற்கையான தாவர வளம் மீட்கப்படுகிறது."
            },
            {
                "title": "9. நீரோடை ஓரங்களை பாதுகாத்தல்",
                "issue": "கால்நடைகளால் நீர் நிலைகள் மாசுபடுவது.",
                "solution": "நீர்நிலைகளின் চারপাশে வேலி அமைக்கவும்.",
                "benefit": "சுத்தமான நீர் ஆதாரம் பாதுகாக்கப்படும்."
            },
            {
                "title": "10. ஆழமான வேர்களைக் கொண்ட புல் வகைகளை நடுதல்",
                "issue": "கோடை காலத்தில் மேய்ச்சல் காய்ந்துவிடுவது.",
                "solution": "ஆழமான வேர்களைக் கொண்ட புல் வகைகளை அறிமுகப்படுத்தவும்.",
                "benefit": "வறட்சி காலத்திலும் பசுமை நீடிக்கும்."
            }
        ],
        "speech_template": "{country} க்கான தீவன முன்னறிவிப்பு சுருக்கம். அடையாளம் காணப்பட்ட புல் {species} ஆகும். மொத்த தீவனம் {forage} பவுண்டுகள் ஆகும். மதிப்பிடப்பட்ட காலம் {days} நாட்கள்.",
        "qa_livestock": "கால்நடை விவரம்: உங்கள் {cows} பசுக்களுக்கு தினசரி {cow_demand:.0f} பவுண்டுகள், {sheep} ஆடுகளுக்கு {sheep_demand:.0f} பவுண்டுகள், மற்றும் {goats} வெள்ளாடுகளுக்கு {goat_demand:.0f} பவுண்டுகள் தேவைப்படுகிறது.",
        "qa_duration": "உங்கள் உள்ளீடுகளின் அடிப்படையில் ({acres} ஏக்கர், {cows} பசுக்கள், {sheep} ஆடுகள், {goats} வெள்ளாடுகள்), உங்கள் தீவன காலம் {days:.1f} நாட்கள் ஆகும்.",
        "qa_paddock": "{acres} ஏக்கரை {paddocks} பாட்டங்குகளாகப் பிரித்தால், பாட்டங்கிற்கு {paddock_size:.1f} ஏக்கர் கிடைக்கிறது.",
        "qa_general": "{country} இல் உங்கள் {acres} ஏக்கர் நிலத்திற்கு {rainfall} மிமீ மழையளவு உள்ளது. சுழற்சி மேய்ச்சல் முறை சிறந்த பயன்பாட்டை உறுதி செய்கிறது."
    },
    "Telugu (తెలుగు)": {
        "lang_code": "te-IN",
        "title": "మేత అంచనా 360: పశుక్షేత్ర సామర్థ్యం",
        "subtitle": "అనుకూల మేత మరియు పశువుల నిర్వహణ డాష్‌బోర్డ్",
        "select_lang": "భాషను ఎంచుకోండి",
        "land_details": "1. భూమి మరియు పాడాక్ ఇన్‌పుట్లు",
        "area_label": "మొత్తం ఉపయోగపడే భూమి (ఎకరాలు)",
        "paddock_count": "మేత పాడాక్‌ల సంఖ్య",
        "livestock_label": "2. పశువుల జాబితా (మొత్తం: 100)",
        "cows": "ఆవులు",
        "sheep": "గొర్రెలు",
        "goats": "మేకలు",
        "climate_label": "3. వాతావరణ మండలం",
        "climate_options": ["మితశీతోష్ణ / Temperate"],
        "water_prompt": "4. నీటి వనరు మరియు స్థాన సమాచారం",
        "country_input": "దేశం / ప్రాంతం",
        "water_source_input": "మీ సమీప నీటి వనరును వివరించండి:",
        "image_label": "5. ఫోటో అప్‌లోడ్",
        "weather_label": "6. వాతావరణం మరియు వర్షపాత విశ్లేషణ",
        "lat_label": "అక్షాంశం (దాటవేయడానికి NA అని టైప్ చేయండి)",
        "lon_label": "రేఖాంశం (దాటవేయడానికి NA అని టైప్ చేయండి)",
        "run_button": "మేత అంచనా మరియు స్థిరత్వ విశ్లేషణను అమలు చేయి",
        "results_title": "పశుక్షేత్ర విశ్లేషణ మరియు పోషకాహార ఫలితాలు",
        "voice_title": "ఆడియో సారాంశం మరియు నియంత్రణలు",
        "listen_btn": "పూర్తి ఆడియో సారాంశాన్ని వినండి",
        "stop_btn": "ఆడియోను ఆపు",
        "nutrition_header": "గడ్డి రకం మరియు పోషక విలువల గుర్తింపు",
        "grass_type_label": "గుర్తించబడిన గడ్డి జాతి",
        "protein_label": "అంచనా వేయబడిన ప్రొటీన్",
        "digestibility_label": "జీర్ణశక్తి సామర్థ్యం",
        "capacity_header": "సామర్థ్యం మరియు మేత బడ్జెట్ వివరణ",
        "usable_forage_text": "అందుబాటులో ఉన్న మొత్తం మేత: సంవత్సరానికి {forage_lb:,.0f} పౌండ్లు (~{forage_kg:,.0f} కిలోలు).",
        "daily_demand_text": "రోజువారీ మేత అవసరం: {total_animals} జంతువులకు ({cows} ఆవులు, {sheep} గొర్రెలు, {goats} మేకలు) రోజుకు {demand_lb:,.1f} పౌండ్లు.",
        "duration_text": "అంచనా వేయబడిన మేత వ్యవధి: {days:.1f} రోజుల నిరంతర మేత సామర్థ్యం.",
        "paddock_plan_text": "రొటేషనల్ పాడాక్ ప్రణాళిక: {acres} ఎకరాలను {paddocks} పాడాక్‌లుగా విభజిస్తే పాడాక్‌కు {paddock_size:.1f} ఎకరాలు వస్తుంది.",
        "water_assessment": "నీటి వనరుల అంచనా",
        "sustainable_methods": "10 ఆచరణాత్మక మేత క్షేత్ర పరిష్కారాలు",
        "solutions_list": [
            {
                "title": "1. రొటేషనల్ పాడాక్ మేతను అమలు చేయడం",
                "issue": "ఒకే చోట నిరంతరం మేపడం వల్ల మొక్కలు దెబ్బతింటాయి.",
                "solution": "భూమిని చిన్న పాడాక్‌లుగా విభజించి ప్రతి 3 నుండి 5 రోజులకు ఒకసారి పశువులను మార్చండి.",
                "benefit": "మొక్కల పునరుత్పత్తి వేగవంతమై మేత దిగుబడి 20% నుండి 30% పెరుగుతుంది."
            },
            {
                "title": "2. కనీస గడ్డి ఎత్తును నిర్వహించడం",
                "issue": "అతిగా మేపడం వల్ల మొక్కల వేర్లు బలహీనపడతాయి.",
                "solution": "గడ్డి ఎత్తు 3 నుండి 4 అంగుళాలకు రాగానే పశువులను వేరే పాడాక్‌కు మార్చండి.",
                "benefit": "త్వరితగతిన మళ్లీ పెరగడానికి సహాయపడుతుంది."
            },
            {
                "title": "3. మొబైల్ నీటి తొట్టెలను అమర్చడం",
                "issue": "శాశ్వత నీటి వనరుల దగ్గరే పశువులు ఎక్కువగా మేస్తాయి.",
                "solution": "నీటి తొట్టెలను కదిలించడం ద్వారా క్షేత్రం అంతటా సమానంగా మేతను వినియోగించండి.",
                "benefit": "స్థానిక అతిమేత తగ్గి 100% భూమి ఉపయోగపడుతుంది."
            },
            {
                "title": "4. పశువుల సంఖ్యను వాతావరణానికి అనుగుణంగా మార్చడం",
                "issue": "వర్షాకాలం మరియు కరువు కాలంలో మేత సామర్థ్యం మారుతుంది.",
                "solution": "ప్రధాన మందను ఉంచుకుని, కరువు సమయంలో అదనపు పశువులను తగ్గించండి.",
                "benefit": "కరువు కాలంలో భారీ ఆర్థిక నష్టాలను నివారించవచ్చు."
            },
            {
                "title": "5. బహుళ జాతుల మేత విధానం",
                "issue": "ఒకే రకమైన జంతువులు తినని కలుపు మొక్కలు పెరగడం.",
                "solution": "ఆవులను గొర్రెలు లేదా మేకలతో కలిపి మేపండి.",
                "benefit": "భూమి ఉత్పాదకత 10% నుండి 15% పెరుగుతుంది."
            },
            {
                "title": "6. శీతాకాలంలో తడి నేలలను రక్షించడం",
                "issue": "వర్షాకాలంలో పశువుల సంచారం వల్ల నేల నిర్మాణం దెబ్బతింటుంది.",
                "solution": "భారీ వర్షాల సమయంలో పశువులను ప్రత్యేక ఫీడింగ్ ప్యాడ్‌లపై ఉంచండి.",
                "benefit": "నేల కోత మరియు నిర్మాణం దెబ్బతినకుండా కాపాడుతుంది."
            },
            {
                "title": "7. పప్పుధాన్యాల గడ్డిని అంతర పంటగా వేయడం",
                "issue": "నేలసారం తగ్గడం మరియు ప్రొటీన్ లోపం.",
                "solution": "క్లోవర్ వంటి నైట్రోజన్ అందించే మొక్కలను నాటండి.",
                "benefit": "నేలసారాన్ని మరియు పశువుల బరువును పెంచుతుంది."
            },
            {
                "title": "8. విత్తనాల కొరకు మేతను నిలిపివేయడం",
                "issue": "సహజ పునరుత్పత్తి లేకపోవడం వల్ల దేశీయ గడ్డి నశించడం.",
                "solution": "ఒక నిర్దిష్ట పాడాక్‌ను ఒక పూర్తి కాలం పాటు మేతకు దూరంగా ఉంచండి.",
                "benefit": "సహజ పశుక్షేత్ర జీవవైవిధ్యాన్ని పునరుద్ధరిస్తుంది."
            },
            {
                "title": "9. నీటి వనరుల చుట్టూ రక్షణ ఏర్పాట్లు",
                "issue": "పశువుల తొక్కడం వల్ల నీటి వనరులు కలుషితం కావడం.",
                "solution": "సహజ నదులు మరియు కుంటల చుట్టూ కంచె వేయండి.",
                "benefit": "పరిశుభ్రమైన నీటిని రక్షించి నేల కోతను ఆపుతుంది."
            },
            {
                "title": "10. లోతుగా వేర్లు దిగే గడ్డి రకాలను పెంచడం",
                "issue": "వేసవిలో పైపూత గడ్డి ఎండిపోవడం.",
                "solution": "లోతైన వేర్లు ఉన్న గడ్డి రకాలను ఎంచుకోండి.",
                "benefit": "ఎండకాలంలో కూడా పచ్చని మేత అందుబాటులో ఉంటుంది."
            }
        ],
        "speech_template": "{country} కోసం మేత అంచనా సారాంశం. గుర్తించబడిన గడ్డి {species}. మొత్తం ఉపయోగపడే మేత {forage} పౌండ్లు. అంచనా వేయబడిన గ్రేజింగ్ వ్యవధి {days} రోజులు.",
        "qa_livestock": "పశువుల వివరాలు: మీ {cows} ఆవులకు రోజుకు {cow_demand:.0f} పౌండ్లు, {sheep} గొర్రెలకు {sheep_demand:.0f} పౌండ్లు, {goats} మేకలకు {goat_demand:.0f} పౌండ్లు అవసరం.",
        "qa_duration": "మీ వివరాల ప్రకారం ({acres} ఎకరాలు, {cows} ఆవులు, {sheep} గొర్రెలు, {goats} మేకలు), మీ మేత వ్యవధి {days:.1f} రోజులు.",
        "qa_paddock": "{acres} ఎకరాలను {paddocks} పాడాక్‌లుగా విభజిస్తే, పాడాక్‌కు {paddock_size:.1f} ఎకరాలు వస్తుంది.",
        "qa_general": "{country} లో మీ {acres} ఎకరాలకు వర్షపాతం {rainfall} మిమీ ఉంది. రొటేషనల్ మేత విధానం ఉత్తమ ఫలితాలను ఇస్తుంది."
    }
}

GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")